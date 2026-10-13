# Static full-report reader / 静态全文阅读构建

Only the explicit PUBLIC list in scripts/build-report-pages.cjs is published. Original archived Markdown is the single content source; no models, paper downloads or database are involved.

Dependencies: Node >=20; markdown-it 14.1.0 and KaTeX 0.16.22, MIT. Install from package-lock.json with `npm ci --ignore-scripts`. To keep dependency/cache files outside the repo, copy package.json/package-lock.json into a dedicated build-tools directory under the authorized run root and use `npm ci --prefix <build-tools> --ignore-scripts` there.

```sh
node scripts/build-report-pages.cjs --deps <build-tools>
node scripts/build-report-pages.cjs --deps <build-tools> --check
python scripts/check-report-pages.py
python scripts/check-observatory.py
```

Without --deps, Node resolves dependencies from the project's node_modules. Build outputs are deterministic checked-in docs/ HTML, a source/formula/hash manifest and local KaTeX assets. --check compares exact output bytes and fails on stale content/resources. The content checker verifies source text coverage, headings, formulas, evidence states, local URLs and runtime-resource independence. Browser QA additionally checks loaded local math fonts, blocked external resources, mobile layout and live deployment.

KaTeX uses build-time HTML+MathML with original TeX in data-tex. No client JS/CDN is needed. Code fences (including original archived answers) remain code; they are not silently turned into newly rendered answers. Local source/evidence Markdown links outside the reader allowlist lead to their original GitHub source. Original reports and evidence are never rewritten by the generator.

Pages source remains main/docs. Generated output changes do not change the scientific review or model-evaluation status. China-mainland connectivity remains unverified unless tested explicitly from that network.

Historical ITG source has three closing code fences appended to the last prose line. The generator recognizes exactly these three boundaries in memory (fails if the layout changes); original source bytes stay unchanged. Full code bodies and source SHA-256 are checked independently. This is layout compatibility, not editing or rescoring original answers.

.gitattributes fixes generated output to LF so Windows core.autocrlf does not create false stale-output failures; font files remain binary.

source_sha256 and data-source-sha256 identify LF-normalized UTF-8 Markdown content for deterministic builds; they are not advertised as raw Git blob digests. Frozen evaluation manifest hashes retain their original identities. The generator rejects dependency versions other than the pinned versions.
