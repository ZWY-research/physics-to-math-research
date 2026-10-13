#!/usr/bin/env node
// Static, allowlisted Markdown -> HTML. No client-side fetching or scripts.
'use strict';
const fs = require('node:fs');
const path = require('node:path');
const crypto = require('node:crypto');
const {createRequire} = require('node:module');
const args = process.argv.slice(2);
const repo = path.resolve(__dirname, '..');
const depsIndex = args.indexOf('--deps');
const load = depsIndex >= 0 ? createRequire(path.resolve(args[depsIndex + 1], 'package.json')) : require;
const MarkdownIt = load('markdown-it');
const katex = load('katex');
const actualVersions = {'markdown-it':load('markdown-it/package.json').version, katex:load('katex/package.json').version};
if (actualVersions['markdown-it'] !== '14.1.0' || actualVersions.katex !== '0.16.22') throw new Error('Use pinned build dependencies from package-lock.json');
const check = args.includes('--check');
const docs = path.join(repo, 'docs');
const github = 'https://github.com/ZWY-research/physics-to-math-research/blob/main/';
const version = fs.readFileSync(path.join(repo, 'SKILL.md'), 'utf8').match(/version:\s*"([^"]+)"/)[1];
const PUBLIC = [
  {source:'literature-audits/physics/statistical-mechanics/1997-jarzynski-nonequilibrium-free-energy.md', route:'research-audits/1997-jarzynski-nonequilibrium-free-energy/', group:'research-audits', title:'Jarzynski (1997): Exponential work equality / 指数功恒等式', status:'Reviewed — Limited-scope mathematical audit; not full-paper validation', context:'Canonical preparation, Hamiltonian volume preservation and conditional measure-space formulation. / 正则初态、保体积演化及其数学条件。'},
  {source:'evaluation-reports/v0.2.5-research-delivery-smoke.md', route:'skill-evaluations/v0.2.5-research-delivery-smoke/', group:'skill-evaluations', title:'v0.2.5 Research-delivery Regression / 科研交付行为回归', status:'v0.2.5 · gpt-6.1-sol / medium · PASS 10, FAIL 0, INCONCLUSIVE 0, NOT RUN 0; engineering assessment, no independent human adjudication', context:'Five near-pairs A1–E2: task purpose, installation boundaries, style and actual file delivery. No OFF / Short Prompt gain test.'},
  {source:'evaluation-reports/2026-10-09-can-calibration-evidence-identify-material-response.md', route:'skill-evaluations/can-calibration-evidence-identify-material-response/', group:'skill-evaluations', title:'Can calibration evidence identify material response? / 材料响应可识别性', status:'v0.1-alpha.2 · GPT-6.1 Sol / High · internal comparison; no substantive ON/OFF advantage established', context:'Four-cell local affine constitutive response and calibration identifiability. / 本构响应与标定信息。'},
  {source:'evaluation-reports/2026-10-09-can-linear-stability-rule-out-sustained-tokamak-turbulence.md', route:'skill-evaluations/can-linear-stability-rule-out-sustained-tokamak-turbulence/', group:'skill-evaluations', title:'Can linear stability rule out sustained tokamak turbulence? / 线性稳定性与持续湍流', status:'v0.1-alpha.2 · GPT-6.1 Sol / High · internal comparison tied; incremental advantage not established', context:'Distinguishing linear decay, transient growth and finite-amplitude long-time behavior. / 线性衰减与非线性长期状态。'},
  {source:'evaluation-reports/2026-10-09-can-itg-gradient-scans-distinguish-turbulent-states.md', route:'skill-evaluations/can-itg-gradient-scans-distinguish-turbulent-states/', group:'skill-evaluations', title:'Can ITG gradient scans distinguish turbulent states? / ITG 湍流态判别', status:'v0.1-alpha.2 · GPT-6.1 Sol / High · narrow positive signal; reliable incremental value not established', context:'Coexisting attractors versus intermittency, transients and numerical selection. / 吸引态、间歇性与数值选择。'},
  {source:'docs/research-method-sources.md', route:'methods-sources/', group:'methods-sources', title:'Methods & Sources / 方法与来源', status:'Reviewed public materials; method adoption under evaluation; none Adopted', context:'OpenAI Math, Mathlib4 and Physlib: attribution, reviewed materials, licenses and untested limits. No mathematical-method integration.'},
  {source:'docs/releases/v0.2.6-evidence-publication.md', route:'releases/v0.2.6/', group:'releases', title:'v0.2.6 Evidence Publication / 证据发布记录', status:'Released on main; original results remain preliminary engineering assessment', context:'Release identity, checks, evidence boundaries and pending independent human review.'}
];
const escape = s => String(s).replace(/[&<>"']/g, c => ({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]));
const hash = s => crypto.createHash('sha256').update(s).digest('hex');
const normalized = s => s.replace(/\r\n/g, '\n');
const outputs = new Map();
function output(name, value) { outputs.set(name, Buffer.isBuffer(value) ? value : Buffer.from(value)); }
function relative(from, to) {
  const result = path.posix.relative(from, to);
  if (!result) return './';
  return (!to || to.endsWith('/')) ? result + '/' : result;
}

// Extract TeX without changing its bytes; placeholders protect pipes in tables.
// Fenced/inline code remains code, including archived original model answers.
function extractMath(source) {
  const formulas = []; let text = ''; let i = 0;
  while (i < source.length) {
    const startLine = i === 0 || source[i - 1] === '\n';
    const fence = startLine && source.slice(i).match(/^ {0,3}(`{3,}|~{3,})[^\n]*\n/);
    if (fence) {
      const endRE = new RegExp('^ {0,3}' + fence[1][0] + '{' + fence[1].length + ',}[^\\S\\n]*(?:\\n|$)', 'gm');
      endRE.lastIndex = i + fence[0].length;
      const end = endRE.exec(source); const j = end ? endRE.lastIndex : source.length;
      text += source.slice(i, j); i = j; continue;
    }
    if (source[i] === '`') {
      const ticks = source.slice(i).match(/^`+/)[0]; const end = source.indexOf(ticks, i + ticks.length);
      if (end >= 0) { text += source.slice(i, end + ticks.length); i = end + ticks.length; continue; }
    }
    let open, close, display;
    if (source.startsWith('$$', i)) { open = '$$'; close = '$$'; display = true; }
    else if (source.startsWith('\\[', i)) { open = '\\['; close = '\\]'; display = true; }
    else if (source.startsWith('\\(', i)) { open = '\\('; close = '\\)'; display = false; }
    else if (source[i] === '$' && source[i - 1] !== '\\') { open = '$'; close = '$'; display = false; }
    if (open) {
      let end = source.indexOf(close, i + open.length);
      while (end >= 0 && close === '$' && source[end - 1] === '\\') end = source.indexOf(close, end + 1);
      if (end < 0) throw new Error('Unclosed math delimiter at ' + i);
      const tex = source.slice(i + open.length, end);
      const id = formulas.length; formulas.push({tex, display});
      text += '\uE000M' + id + '\uE001'; i = end + close.length; continue;
    }
    text += source[i++];
  }
  return {text, formulas};
}
function render(source, entry) {
  let inlineFenceRepairs = 0;
  if (entry.source.endsWith('can-itg-gradient-scans-distinguish-turbulent-states.md')) {
    // This frozen report has closing fences appended to three final prose lines.
    // Move only those delimiters in memory; never rewrite the Markdown artifact.
    source = source.replace(/([^\n`])```(?=\n|$)/g, (_,last) => { inlineFenceRepairs++; return last + '\n```'; });
    if (inlineFenceRepairs !== 3) throw new Error('Historical ITG fence layout changed; review required');
  }
  const {text, formulas} = extractMath(source);
  const md = new MarkdownIt({html:true, linkify:false, typographer:false});
  const fenceRenderer = md.renderer.rules.fence;
  md.renderer.rules.fence = (...parameters) => fenceRenderer(...parameters).replace(/[ \t]+(?=\n)/g,
    whitespace => [...whitespace].map(c => '&#' + c.charCodeAt(0) + ';').join(''));
  const formula = id => {
    const f = formulas[id];
    const html = katex.renderToString(f.tex, {displayMode:f.display, throwOnError:true, trust:false, strict:'warn', output:'htmlAndMathml'});
    return `<${f.display ? 'div' : 'span'} class="formula${f.display ? ' formula-block' : ''}" data-tex="${escape(f.tex)}">${html}</${f.display ? 'div' : 'span'}>`;
  };
  md.inline.ruler.before('text', 'formula', (state, silent) => {
    const match = state.src.slice(state.pos).match(/^\uE000M(\d+)\uE001/);
    if (!match) return false;
    if (!silent) { const token = state.push('formula', '', 0); token.content = match[1]; }
    state.pos += match[0].length; return true;
  });
  md.block.ruler.before('paragraph', 'formula_block', (state, start, end, silent) => {
    const line = state.src.slice(state.bMarks[start] + state.tShift[start], state.eMarks[start]).trim();
    const match = line.match(/^\uE000M(\d+)\uE001$/);
    if (!match || !formulas[Number(match[1])].display) return false;
    if (!silent) { const token = state.push('formula', '', 0); token.content = match[1]; }
    state.line = start + 1; return true;
  });
  md.renderer.rules.formula = (tokens, i) => formula(Number(tokens[i].content));
  md.renderer.rules.text = (tokens, i) => md.utils.escapeHtml(tokens[i].content).replace(/\uE000M(\d+)\uE001/g, (_,n) => formula(Number(n)));
  md.renderer.rules.table_open = () => '<div class="table-scroll"><table>\n';
  md.renderer.rules.table_close = () => '</table></div>\n';
  for (const rule of ['html_block','html_inline']) md.renderer.rules[rule] = (tokens, i) => {
    const s = tokens[i].content;
    if (!/^(?:\s*<\/?(?:details|summary|br|sub|sup)>\s*|[^<>]+)*$/.test(s)) throw new Error('Non-allowlisted source HTML: ' + s);
    return s;
  };
  md.renderer.rules.link_open = (tokens, i, options, env, self) => {
    const token = tokens[i]; const href = token.attrGet('href');
    if (href && !/^(?:[a-z]+:|#)/i.test(href)) {
      const [file, fragment] = href.split('#');
      const destination = path.posix.normalize(path.posix.join(path.posix.dirname(entry.source), decodeURI(file)));
      if (destination.startsWith('../')) throw new Error('Unsafe link');
      const target = PUBLIC.find(x => x.source === destination);
      token.attrSet('href', target ? relative(entry.route, target.route) + (fragment ? '#' + fragment : '') : github + destination + (fragment ? '#' + fragment : ''));
    }
    return self.renderToken(tokens, i, options);
  };
  const tokens = md.parse(text, {}); const toc = []; const ids = new Set();
  tokens.forEach((t, i) => {
    if (t.type !== 'heading_open') return;
    const label = tokens[i + 1].content.replace(/\uE000M(\d+)\uE001/g, (_,n) => formulas[n].tex);
    let id = label.toLowerCase().replace(/[^\p{L}\p{N}\s-]/gu,'').trim().replace(/\s+/g,'-') || 'section';
    const original = id; let n = 1; while(ids.has(id)) id = original + '-' + n++;
    ids.add(id); t.attrSet('id',id);
    if (Number(t.tag.slice(1)) <= 3) toc.push(`<li><a href="#${escape(id)}">${escape(label)}</a></li>`);
  });
  const html = md.renderer.render(tokens, md.options, {});
  if (/\uE000M\d+\uE001/.test(html)) throw new Error('Unrendered math placeholder');
  return {html, toc:toc.join(''), formulas, inlineFenceRepairs};
}
function shell(entry, body, digest, toc = '') {
  const home = relative(entry.route, ''); const index = relative(entry.route, entry.group + '/');
  const assets = relative(entry.route,'assets/');
  return `<!doctype html>\n<html lang="zh-CN"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1"><title>${escape(entry.title)} · Research Observatory</title><link rel="stylesheet" href="${home}observatory.css"><link rel="stylesheet" href="${assets}report-reading.css"><link rel="stylesheet" href="${assets}vendor/katex/katex.min.css"></head><body><a class="skip-link" href="#report">跳至正文 / Skip to content</a><header class="site-header"><div class="container header-inner"><a class="brand" href="${home}index.html">Research Observatory<span lang="zh-CN">科研进展与证据看板</span></a><nav><a href="${home}research-audits/">Research Audits / 研究审查</a><a href="${home}skill-evaluations/">Skill Evaluations / 评估</a><a href="${home}methods-sources/">Methods &amp; Sources / 方法与来源</a></nav></div></header><main class="container reading" id="report"><header class="report-header"><p class="eyebrow">${escape(entry.group)}</p><h1>${escape(entry.title)}</h1><p class="review-badge">${escape(entry.status)}</p><p>${escape(entry.context)}</p>${entry.source ? `<p><a href="${github + entry.source}">Original Markdown / GitHub 原文 ↗</a> · <a href="${index}">返回分类目录 / Back to index</a></p>` : ''}</header>${toc ? `<details class="contents"><summary>目录 / Contents</summary><ul>${toc}</ul></details>` : ''}<article data-source="${escape(entry.source || '')}" data-source-sha256="${digest || ''}">${body}</article><p class="source-note">正文来自白名单公开 Markdown；公式静态渲染。本站阅读无需打开 GitHub，原始证据链接仍可指向外部。 / Full allowlisted source, statically rendered; no runtime document fetching.</p></main><footer class="site-footer"><div class="container footer-inner"><a href="${home}index.html">返回 Observatory</a><span>v${escape(version)} · <a href="${assets}third-party-notices.html">Third-party licenses / 依赖许可证</a></span></div></footer></body></html>\n`;
}
const manifest = {generator:'scripts/build-report-pages.cjs', version, source_hash_normalization:'UTF-8 Markdown with CRLF normalized to LF; original Git artifacts remain unchanged', dependencies:{'markdown-it':'14.1.0', katex:'0.16.22'}, documents:[], resources:[]};
for (const entry of PUBLIC) {
  const source = normalized(fs.readFileSync(path.join(repo,entry.source),'utf8'));
  const rendered = render(source, entry); const destination = entry.route + 'index.html';
  output(destination,shell(entry,rendered.html,hash(source),rendered.toc));
  manifest.documents.push({...entry, output:destination, source_sha256:hash(source), formula_count:rendered.formulas.length, formulas:rendered.formulas, in_memory_inline_fence_repairs:rendered.inlineFenceRepairs});
}
for (const group of ['research-audits','skill-evaluations','releases']) {
  const title = {'research-audits':'Research Audits / 研究审查','skill-evaluations':'Skill Evaluations / Skill 评估','releases':'Release Records / 发布记录'}[group];
  const note = {'research-audits':'1 distinct reviewed paper; limited scope. / 1 篇已审查论文，范围受限。','skill-evaluations':'行为 Regression 与历史 ON/OFF 比较属于不同证据；稳定科研增量收益尚未建立。 / Behavior regression is separate from capability comparisons; reliable research gain not established.','releases':'Publishing engineering evidence does not establish independent human adjudication or research gains. / 工程证据发布不改变科学审查身份或证明科研增量。'}[group];
  const body = `<p>${note}</p><ul class="report-list">` + PUBLIC.filter(x=>x.group===group).map(x=>`<li><h2><a href="${relative(group+'/',x.route)}">${escape(x.title)}</a></h2><p>${escape(x.status)}</p><p>${escape(x.context)}</p></li>`).join('') + '</ul>';
  output(group+'/index.html',shell({route:group+'/',group,title,status:'Public full reports / 公开完整报告',context:'Original scope, verification status and limitations preserved.'},body));
}
const katexRoot = path.dirname(load.resolve('katex/package.json'));
output('assets/vendor/katex/katex.min.css',fs.readFileSync(path.join(katexRoot,'dist/katex.min.css')));
for (const file of fs.readdirSync(path.join(katexRoot,'dist/fonts')).sort()) output('assets/vendor/katex/fonts/'+file,fs.readFileSync(path.join(katexRoot,'dist/fonts',file)));
output('assets/vendor/katex/LICENSE.txt',fs.readFileSync(path.join(katexRoot,'LICENSE')));
output('assets/vendor/markdown-it-LICENSE.txt',fs.readFileSync(path.join(path.dirname(load.resolve('markdown-it/package.json')),'LICENSE')));
output('assets/third-party-notices.html',`<!doctype html><html lang="en"><head><meta charset="utf-8"><title>Third-party notices</title></head><body><h1>Third-party notices</h1><p>KaTeX 0.16.22, MIT, Khan Academy and contributors: statically generated mathematical markup, local CSS and fonts. <a href="vendor/katex/LICENSE.txt">Full license</a>. <a href="https://github.com/KaTeX/KaTeX/tree/v0.16.22">Source</a>.</p><p>markdown-it 14.1.0, MIT, Vitaly Puzrin, Alex Kocharin and contributors: build-time Markdown parser. <a href="vendor/markdown-it-LICENSE.txt">Full license</a>. <a href="https://github.com/markdown-it/markdown-it/tree/14.1.0">Source</a>.</p><p>No third-party mathematical library or paper text is redistributed. Dependency versions and transitive integrity are pinned in package-lock.json.</p><a href="../index.html">Observatory</a></body></html>\n`);
manifest.resources = [...outputs.keys()].filter(x=>x.startsWith('assets/')).sort();
manifest.output_hashes = Object.fromEntries([...outputs].map(([name,buf])=>[name,hash(buf)]));
output('report-pages-manifest.json',JSON.stringify(manifest,null,2)+'\n');
const stale = [];
for (const [name,buf] of outputs) {
  const destination = path.join(docs,name);
  if (check) { if (!fs.existsSync(destination) || !fs.readFileSync(destination).equals(buf)) stale.push(name); }
  else { fs.mkdirSync(path.dirname(destination),{recursive:true});fs.writeFileSync(destination,buf); }
}
if (stale.length) throw new Error('Generated pages stale: '+stale.join(', '));
console.log(JSON.stringify({status:'PASS', mode:check?'check':'build',documents:PUBLIC.length,outputs:outputs.size,formulas:manifest.documents.reduce((s,x)=>s+x.formula_count,0),version}));
