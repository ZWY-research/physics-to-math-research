#!/usr/bin/env python3
"""Check full source coverage, formula fidelity and local resources; no models."""
import argparse
from collections import Counter
import hashlib
from html.parser import HTMLParser
import json
from pathlib import Path
import re
from urllib.parse import unquote, urlsplit


class Page(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.stack = []
        self.text = []
        self.codes = []
        self.formulas = []
        self.links = []
        self.resources = []
        self.ids = set()
        self.in_article = False
        self.math_depth = 0
        self.pre = None

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        assert tag not in ['script', 'iframe', 'object', 'embed'], tag
        if 'id' in a:
            assert a['id'] not in self.ids
            self.ids.add(a['id'])
        if tag == 'article':
            self.in_article = True
        if 'data-tex' in a:
            self.formulas.append(a['data-tex'])
            self.math_depth += 1
        if tag == 'pre':
            self.pre = []
        if 'href' in a:
            self.links.append(a['href'])
            if tag == 'link':
                self.resources.append(a['href'])
        if 'src' in a:
            self.resources.append(a['src'])
        if tag not in ['meta', 'link', 'br', 'hr', 'img', 'input', 'source', 'wbr']:
            self.stack.append((tag, 'data-tex' in a))

    def handle_startendtag(self, tag, attrs):
        pass

    def handle_endtag(self, tag):
        assert self.stack and self.stack[-1][0] == tag, (tag, self.stack[-3:])
        _, math = self.stack.pop()
        if math:
            self.math_depth -= 1
        if tag == 'pre':
            self.codes.append(''.join(self.pre))
            self.pre = None
        if tag == 'article':
            self.in_article = False

    def handle_data(self, data):
        if self.in_article and not self.math_depth:
            self.text.append(data)
        if self.pre is not None:
            self.pre.append(data)


def words(s):
    result = Counter(re.findall(r'[A-Za-z]{4,}', s))
    for phrase in re.findall(r'[\u4e00-\u9fff]{2,}', s):
        result.update(phrase[i:i+2] for i in range(len(phrase)-1))
    return result


def check(repo):
    docs = repo / 'docs'
    manifest = json.loads((docs / 'report-pages-manifest.json').read_text(encoding='utf-8'))
    assert manifest['version'] == '0.2.11'
    expected = set(manifest['output_hashes'])
    expected.add('report-pages-manifest.json')
    for name, digest in manifest['output_hashes'].items():
        assert hashlib.sha256((docs / name).read_bytes()).hexdigest() == digest, name
    sources = []
    for entry in manifest['documents']:
        source = (repo / entry['source']).read_text(encoding='utf-8')
        assert hashlib.sha256(source.encode()).hexdigest() == entry['source_sha256']
        page = Page()
        html = (docs / entry['output']).read_text(encoding='utf-8')
        page.feed(html)
        assert not page.stack
        assert page.formulas == [f['tex'] for f in entry['formulas']], entry['source']
        assert len(page.formulas) == entry['formula_count']
        assert 'katex-error' not in html and '\ue000' not in html
        render_source = source
        if entry['source'].endswith('can-itg-gradient-scans-distinguish-turbulent-states.md'):
            render_source, repairs = re.subn(r'([^\n`])```(?=\n|$)', r'\1\n```', source)
            assert repairs == 3 == entry['in_memory_inline_fence_repairs']
        code = re.findall(r'^```[^\n]*\n(.*?)^```[^\n]*$', render_source, re.M | re.S)
        assert len(page.codes) == len(code), entry['source']
        assert all(a.rstrip('\n') == b.rstrip('\n') for a, b in zip(page.codes, code)), entry['source']
        # Compare source lexical content independently of the HTML renderer.
        # TeX is checked above; full fenced-code bodies are checked separately.
        plain = re.sub(r'^```[^\n]*\n.*?^```[^\n]*$', '', render_source, flags=re.M | re.S)
        for formula in entry['formulas']:
            for left, right in [('$$', '$$'), ('$', '$'), (r'\[', r'\]'), (r'\(', r'\)')]:
                plain = plain.replace(left + formula['tex'] + right, '')
        plain = re.sub(r'!?\[([^\]]+)\]\([^)]*\)', r'\1', plain)
        plain = re.sub(r'<[^>]+>', '', plain)
        wanted = words(plain)
        actual = words(''.join(page.text))
        missing = wanted - actual
        assert not missing, (entry['source'], missing)
        sources.append({'source': entry['source'], 'formulas': len(page.formulas), 'code_blocks': len(code), 'full_text_coverage': 'PASS'})
    generated = set()
    for group in ['research-audits', 'skill-evaluations', 'methods-sources', 'releases']:
        generated.update(p.relative_to(docs).as_posix() for p in (docs / group).rglob('*.html'))
    assert generated == {n for n in expected if n.endswith('.html') and not n.startswith('assets/')}, 'Unindexed/stale report page'
    pages = {}
    for p in docs.rglob('*.html'):
        page = Page()
        page.feed(p.read_text(encoding='utf-8'))
        assert not page.stack, p
        pages[p.resolve()] = page
    link_count = 0
    for p, page in pages.items():
        for target in page.resources:
            assert not urlsplit(target).scheme and not target.startswith('//'), (p, target)
        for href in page.links + page.resources:
            parsed = urlsplit(href)
            if parsed.scheme:
                assert parsed.scheme in ['http', 'https', 'mailto'], href
                continue
            target = (p.parent / unquote(parsed.path)).resolve() if parsed.path else p
            assert target.is_relative_to(docs.resolve()), (p, href)
            if target.is_dir():
                target /= 'index.html'
            assert target.is_file(), (p, href)
            if parsed.fragment and target in pages:
                assert unquote(parsed.fragment) in pages[target].ids, (p, href)
            link_count += 1
    for p in docs.rglob('*.css'):
        css = p.read_text(encoding='utf-8')
        assert '@import' not in css
        for url in re.findall(r'url\([\x22\x27]?([^\x22\x27)]+)', css):
            assert not urlsplit(url).scheme and not url.startswith('//'), (p, url)
            assert (p.parent / url).is_file(), (p, url)
    jarzynski = next(e for e in manifest['documents'] if e['group'] == 'research-audits')
    formula_text = '\n'.join(f['tex'] for f in jarzynski['formulas'])
    for feature in ['_', '^', r'\frac', r'\int', r'\beta', r'\begin{aligned}']:
        assert feature in formula_text, feature
    regression = next(e for e in manifest['documents'] if 'v0.2.5-research' in e['source'])
    html = (docs / regression['output']).read_text(encoding='utf-8')
    for branch in [g + str(n) for g in 'ABCDE' for n in (1, 2)]:
        assert f'<td>{branch}</td>' in html
    for keyword in ['PASS', 'FAIL', 'INCONCLUSIVE', 'NOT RUN', '工程', 'OFF / Short Prompt']:
        assert keyword in html
    source_html = (docs / 'methods-sources/index.html').read_text(encoding='utf-8')
    for keyword in ['OpenAI Math', 'Mathlib4', 'Physlib', 'Apache-2.0', 'Under evaluation', '未采用']:
        assert keyword in source_html
    return {'status': 'PASS', 'source_coverage': sources, 'html_pages': len(pages), 'local_links': link_count,
            'formula_count': sum(s['formulas'] for s in sources), 'third_party_runtime_requests': 0,
            'scope': 'Static full-content, exact code/TeX, evidence-state, HTML and local-resource checks; browser visual QA is separate.'}


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--repo', type=Path, default=Path(__file__).resolve().parents[1])
    args = parser.parse_args()
    print(json.dumps(check(args.repo.resolve()), ensure_ascii=False, indent=2))
