#!/usr/bin/env python3
"""Check static Observatory facts and navigation against repository evidence.

Standard library only; no network, scientific inference, or runtime Skill rules.
"""
import argparse
from html.parser import HTMLParser
import json
from pathlib import Path
import re
from urllib.parse import unquote, urlsplit

GITHUB = "https://github.com/ZWY-research/physics-to-math-research"
REPORT = "literature-audits/physics/statistical-mechanics/1997-jarzynski-nonequilibrium-free-energy.md"
DOI = "https://doi.org/10.1103/PhysRevLett.78.2690"


class Page(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.nodes = []
        self.stack = []

    def handle_starttag(self, tag, attrs):
        node = {"tag": tag, "attrs": dict(attrs), "text": ""}
        self.nodes.append(node)
        if tag not in {"meta", "link", "br", "hr", "img", "input", "source", "wbr"}:
            self.stack.append(node)

    def handle_endtag(self, tag):
        if not self.stack or self.stack[-1]["tag"] != tag:
            raise ValueError(f"Unbalanced HTML closing tag: {tag}")
        self.stack.pop()

    def handle_data(self, data):
        for node in self.stack:
            node["text"] += data


def check(repo):
    repo = repo.resolve()
    docs = repo / "docs"
    for filename in ["index.html", "observatory.css", ".nojekyll"]:
        if not (docs / filename).is_file():
            raise ValueError(f"Missing website file: docs/{filename}")
    if (docs / ".nojekyll").read_bytes():
        raise ValueError("docs/.nojekyll must be empty")
    css = (docs / "observatory.css").read_text(encoding="utf-8")
    if "@import" in css or re.search(r'url\(\s*[\x22\x27]?(?:https?:)?//', css):
        raise ValueError("External CSS/font resources are prohibited")
    page = Page()
    page.feed((docs / "index.html").read_text(encoding="utf-8"))
    page.close()
    if page.stack:
        raise ValueError("Unclosed HTML elements")
    ids = [n["attrs"]["id"] for n in page.nodes if "id" in n["attrs"]]
    if len(set(ids)) != len(ids):
        raise ValueError("Duplicate HTML anchor IDs")
    links = []
    for node in page.nodes:
        if node["tag"] in {"script", "iframe", "object", "embed"}:
            raise ValueError(f"External/runtime content prohibited: {node['tag']}")
        for attribute in ["href", "src"]:
            target = node["attrs"].get(attribute)
            if not target:
                continue
            if target.startswith("#"):
                if target[1:] not in ids:
                    raise ValueError(f"Missing anchor: {target}")
            elif not urlsplit(target).scheme:
                resource = (docs / unquote(urlsplit(target).path)).resolve()
                if resource.is_dir():
                    resource = resource / "index.html"
                if not resource.is_relative_to(docs) or not resource.is_file():
                    raise ValueError(f"Missing/unsafe relative resource: {target}")
            elif target.startswith(GITHUB + "/blob/main/"):
                path = unquote(target[len(GITHUB + "/blob/main/"):])
                resource = (repo / path).resolve()
                if not resource.is_relative_to(repo) or not resource.is_file():
                    raise ValueError(f"GitHub evidence target absent: {path}")
            elif node["tag"] != "a":
                raise ValueError(f"External resource forbidden: {target}")
            links.append(target)
    required = {DOI, GITHUB, GITHUB + "/issues", GITHUB + "/discussions",
                GITHUB + "/blob/main/" + REPORT,
                GITHUB + "/blob/main/literature-audits/README.md",
                GITHUB + "/blob/main/evaluation-reports/README.md",
                GITHUB + "/blob/main/docs/literature-audit-protocol.md"}
    if required - set(links):
        raise ValueError(f"Required link targets missing: {sorted(required - set(links))}")
    if not any(n["tag"] == "link" and n["attrs"].get("href") == "./observatory.css" for n in page.nodes):
        raise ValueError("Stylesheet must use ./observatory.css")

    def marked(attribute):
        nodes = [n for n in page.nodes if attribute in n["attrs"]]
        if len(nodes) != 1:
            raise ValueError(f"Expected one {attribute} marker, found {len(nodes)}")
        return nodes[0]

    skill = (repo / "SKILL.md").read_text(encoding="utf-8")
    version = re.search(r'^\s+version:\s*"([^"]+)"\s*$', skill, re.MULTILINE)[1]
    v = marked("data-project-version")
    if v["attrs"]["data-project-version"] != version or v["text"].strip() != "v" + version:
        raise ValueError(f"Page version differs from SKILL metadata.version {version}")
    core_count = len(re.findall(r'^### Core \d+ ', skill, re.MULTILINE))
    c = marked("data-core-count")
    if core_count != 4 or c["attrs"]["data-core-count"] != str(core_count) or c["text"].strip() != "4 Rules":
        raise ValueError(f"Core count mismatch: source {core_count}, page {c['text']}")
    oac = skill.split("## Observable Audit Requirements", 1)[1].split("## Stop & escalation", 1)[0]
    if len(re.findall(r'^\d+\. ', oac, re.MULTILINE)) != int(marked("data-oac-count")["attrs"]["data-oac-count"]):
        raise ValueError("OAC requirement count mismatch")
    registry = (repo / "literature-audits/README.md").read_text(encoding="utf-8")
    registered = set()
    for path in re.findall(r'\[[^\]]*\]\(([^)]+)\)', registry):
        if path.startswith(("http", "..", "#")) or not path.endswith(".md") or Path(path).name in {"README.md", "execution-record.md"}:
            continue
        if not (repo / "literature-audits" / path).is_file():
            raise ValueError(f"Registered report absent: {path}")
        registered.add("literature-audits/" + path)
    index_count = int(re.search(r'Reviewed papers:\s*\*\*(\d+)\*\*', registry)[1])
    shown = marked("data-reviewed-count")
    cards = {n["attrs"]["data-report-path"] for n in page.nodes if "data-report-path" in n["attrs"]}
    if index_count != len(registered) or cards != registered or shown["attrs"]["data-reviewed-count"] != str(index_count) or shown["text"].strip() != str(index_count):
        raise ValueError(f"Paper count/card drift: registry {index_count}/{len(registered)}, page {shown['text']}/{sorted(cards)}")
    evaluations = (repo / "evaluation-reports/README.md").read_text(encoding="utf-8")
    records = set(re.findall(r'\]\((\d{4}-\d{2}-\d{2}-[^)]+\.md)\)', evaluations))
    if int(marked("data-evaluation-records")["attrs"]["data-evaluation-records"]) != len(records):
        raise ValueError(f"Historical evaluation index changed ({len(records)} reports); synchronize the page")
    for attribute, expected, visible in [
        ("data-validation-status", "not-established", "Incremental Gain Not Established"),
        ("data-comparison-status", "not-established", "Reliable incremental benefit not established"),
        ("data-adapter-status", "experimental", "Experimental"),
    ]:
        node = marked(attribute)
        if node["attrs"][attribute] != expected or visible not in node["text"]:
            raise ValueError(f"Evidence-status mismatch: {attribute}")
    body = next(n["text"] for n in page.nodes if n["tag"] == "body")
    if re.search(r'\d+(?:\.\d+)?\s*[%％]', body):
        raise ValueError("Undefined percentage/performance indicator in page text")
    for sentence in ["not evidence that the Skill independently solved an unguided research problem",
                     "not a mandatory reasoning pipeline or a guarantee of success",
                     "Historical controlled evaluations are documented"]:
        if sentence not in body:
            raise ValueError(f"Required evidence qualification missing: {sentence}")
    return {"status": "PASS", "version": version, "reviewed_papers": index_count,
            "core_rules": core_count, "historical_evaluation_records": len(records),
            "anchors": len(ids), "links_checked": len(links),
            "scope": "Static facts/navigation checks; not semantic scientific validation or network checks"}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo", type=Path, default=Path(__file__).resolve().parents[1])
    args = parser.parse_args()
    try:
        print(json.dumps(check(args.repo), ensure_ascii=False, indent=2))
    except (OSError, ValueError, IndexError, KeyError, AttributeError) as error:
        parser.exit(1, f"Observatory check FAILED: {error}\n")


if __name__ == "__main__":
    main()
