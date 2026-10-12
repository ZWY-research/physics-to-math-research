#!/usr/bin/env python3
"""Build a deterministic Markdown-only ZIP from a clean, published Git commit.

Requires an existing Git executable for publication checks; installs nothing.
Only package README license links are adjusted. Repository files stay unchanged.
"""

import argparse
import hashlib
import io
import json
from pathlib import Path, PurePosixPath
import re
import subprocess
import zipfile


def git(repo, *args):
    return subprocess.check_output(["git", *args], cwd=repo, stderr=subprocess.PIPE)


def safe_name(name):
    path = PurePosixPath(name)
    return (not path.is_absolute() and ".." not in path.parts and "\\" not in name
            and ":" not in name and path.as_posix() == name and name.endswith(".md"))


def package_readme(data):
    """Adjust exact local LICENSE link destinations outside fenced/inline code."""
    text = data.decode("utf-8")
    parts = re.split(r"(```[^\n]*\n[\s\S]*?```|~~~[^\n]*\n[\s\S]*?~~~|`[^`\n]*`)", text)
    for index in range(0, len(parts), 2):
        parts[index] = re.sub(
            r"(\[[^\]\n]*\]\()(?:(?:\./)?LICENSE)(#[^\s)]*)?(\))",
            lambda match: match[1] + "LICENSE.md" + (match[2] or "") + match[3],
            parts[index],
        )
    return "".join(parts).encode("utf-8")


def build(repo, output):
    repo = repo.resolve(strict=True)
    output = output.resolve()
    if output.is_relative_to(repo):
        raise ValueError("Output ZIP must be outside the repository")
    if output.exists():
        raise FileExistsError(f"Refusing to overwrite {output}")
    if output.suffix.lower() != ".zip":
        raise ValueError("Output must have a .zip extension")
    if git(repo, "rev-parse", "--show-toplevel").decode().strip().replace("\\", "/") != repo.as_posix():
        raise ValueError("--repo must be the repository root")
    if git(repo, "status", "--porcelain=v1", "--untracked-files=all"):
        raise ValueError("Repository has uncommitted or untracked changes")
    commit = git(repo, "rev-parse", "HEAD").decode().strip()
    local_main = git(repo, "rev-parse", "origin/main").decode().strip()
    remote = git(repo, "ls-remote", "origin", "refs/heads/main").decode().splitlines()
    if len(remote) != 1 or remote[0].split()[0] != commit or local_main != commit:
        raise ValueError("HEAD, fetched origin/main and actual remote main must match")

    tree = {}
    for row in git(repo, "ls-tree", "-r", "-z", commit).split(b"\0"):
        if not row:
            continue
        attributes, path = row.split(b"\t", 1)
        tree[path.decode("utf-8")] = attributes.split()[0].decode()
    required = {"SKILL.md", "README.md", "README.zh-CN.md", "LICENSE"}
    if not required.issubset(tree):
        raise ValueError("Required root source files missing")
    sources = sorted(required | {name for name in tree if name.startswith("references/") and name.endswith(".md")})
    entries = {}
    for name in sources:
        if tree[name] not in ("100644", "100755"):
            raise ValueError(f"Not a regular tracked file: {name}")
        data = git(repo, "show", f"{commit}:{name}")
        if (repo / name).read_bytes() != data:
            raise ValueError(f"Working bytes differ from published commit: {name}")
        archive_name = "LICENSE.md" if name == "LICENSE" else name
        if not safe_name(archive_name) or archive_name in entries:
            raise ValueError(f"Unsafe or duplicate entry: {archive_name}")
        entries[archive_name] = package_readme(data) if name in ("README.md", "README.zh-CN.md") else data
    skill = entries["SKILL.md"].decode("utf-8")
    match = re.search(r'^metadata:\r?\n[ \t]+version:[ \t]+"([^"]+)"[ \t]*\r?$', skill, re.MULTILINE)
    if not match:
        raise ValueError("Cannot read canonical metadata.version")
    version = match[1]
    if f"# physics-to-math-research — v{version}" not in skill:
        raise ValueError("SKILL version/title disagree")
    for name in ("README.md", "README.zh-CN.md"):
        if f"`{version}`" not in entries[name].decode().splitlines()[2]:
            raise ValueError(f"Current README version differs: {name}")
    if version not in output.name:
        raise ValueError("Output filename must include canonical version")

    buffer = io.BytesIO()
    with zipfile.ZipFile(buffer, "w", compression=zipfile.ZIP_DEFLATED, compresslevel=9) as archive:
        for name, data in sorted(entries.items()):
            item = zipfile.ZipInfo(name, date_time=(1980, 1, 1, 0, 0, 0))
            item.create_system = 3
            item.external_attr = 0o100644 << 16
            item.compress_type = zipfile.ZIP_DEFLATED
            archive.writestr(item, data, compresslevel=9)
    packed = buffer.getvalue()
    with zipfile.ZipFile(io.BytesIO(packed)) as archive:
        names = archive.namelist()
        if names != sorted(entries) or len(set(names)) != len(names):
            raise ValueError("ZIP entry listing does not match whitelist")
        if not all(safe_name(name) for name in names) or "LICENSE" in names:
            raise ValueError("ZIP contains forbidden paths/files")
        if archive.testzip() is not None:
            raise ValueError("ZIP CRC validation failed")
        for name, data in entries.items():
            if archive.read(name) != data:
                raise ValueError(f"ZIP bytes differ: {name}")
        if archive.read("LICENSE.md") != git(repo, "show", f"{commit}:LICENSE"):
            raise ValueError("LICENSE.md differs from original LICENSE")
    # Recheck publication and local state immediately before writing the artifact.
    if git(repo, "status", "--porcelain=v1", "--untracked-files=all") or git(repo, "rev-parse", "HEAD").decode().strip() != commit:
        raise ValueError("Repository changed during package construction")
    if git(repo, "ls-remote", "origin", "refs/heads/main").decode().split()[0] != commit:
        raise ValueError("Remote main changed during package construction")
    output.parent.mkdir(parents=True, exist_ok=True)
    with output.open("xb") as stream:
        stream.write(packed)
    with zipfile.ZipFile(output) as archive:
        if archive.testzip() is not None or any(archive.read(name) != data for name, data in entries.items()):
            raise ValueError("Written ZIP failed reread validation")
    return {"version": version, "commit": commit, "zip": str(output), "files": len(entries),
            "bytes": output.stat().st_size, "sha256": hashlib.sha256(output.read_bytes()).hexdigest(),
            "validation": "PASS", "entry_sha256": {name: hashlib.sha256(data).hexdigest() for name, data in sorted(entries.items())}}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo", type=Path, default=Path(__file__).resolve().parents[1])
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    try:
        print(json.dumps(build(args.repo, args.output), ensure_ascii=False, indent=2))
    except (ValueError, OSError, subprocess.SubprocessError, zipfile.BadZipFile) as error:
        parser.exit(1, f"Package build stopped: {error}\n")


if __name__ == "__main__":
    main()
