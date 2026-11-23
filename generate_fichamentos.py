import os, re, html

css_template = """<!DOCTYPE html>
<html lang="pt-BR">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=5.0, user-scalable=yes">
  <title>{title}</title>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=IBM+Plex+Mono:ital,wght@0,400;0,500;1,400&family=Inter:wght@400;500;600;700;800&display=swap" rel="stylesheet">
  <style>
    :root {{
      --bg: #141413;
      --bg-subtle: #1a1918;
      --bg-code: #1d1c1a;
      --border: #2a2926;
      --border-soft: #22211f;
      --text-title: #e6e2da;
      --text-body: #c7c4bc;
      --text-strong: #ece8e0;
      --text-muted: #8e8b84;
      --text-dim: #66635d;
      --accent: #e0522b;
      --accent-soft: rgba(224, 82, 43, 0.12);
      --font-sans: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
      --font-mono: 'IBM Plex Mono', monospace;
    }}
    * {{ box-sizing: border-box; margin: 0; padding: 0; }}
    html {{
      background-color: var(--bg);
      color: var(--text-body);
      font-family: var(--font-sans);
      font-size: 16px;
      line-height: 1.72;
      -webkit-font-smoothing: antialiased;
      -webkit-text-size-adjust: 100%;
      scroll-behavior: smooth;
    }}
    body {{
      background-color: var(--bg);
      color: var(--text-body);
      min-height: 100vh;
      padding: 4rem 3cm 6rem;
      position: relative;
    }}
    .sheet {{
      width: calc(100% - 6cm);
      max-width: 1140px;
      margin: 0 auto;
    }}
    @media (max-width: 900px) {{
      body {{ padding: 3rem 1.5rem 5rem; }}
      .sheet {{ width: 100%; max-width: 100%; }}
    }}
    .meta-kicker {{
      font-family: var(--font-mono);
      font-size: 0.78rem;
      letter-spacing: 0.12em;
      text-transform: uppercase;
      color: var(--text-muted);
      margin-bottom: 1.1rem;
    }}
    h1.doc-title {{
      font-size: clamp(2.2rem, 5vw, 3.8rem);
      font-weight: 800;
      letter-spacing: -0.04em;
      line-height: 1.08;
      color: var(--text-title);
      margin-bottom: 2rem;
    }}
    h1.doc-title .accent {{ color: var(--accent); }}
    .back-nav {{
      margin-bottom: 2.5rem;
      font-family: var(--font-mono);
      font-size: 0.8rem;
    }}
    .back-nav a {{
      color: var(--accent);
      text-decoration: none;
      border: 1px solid rgba(224, 82, 43, 0.3);
      padding: 0.35rem 0.75rem;
      border-radius: 4px;
      background: var(--accent-soft);
    }}
    .back-nav a:hover {{ background: var(--accent); color: #fff; }}
    blockquote {{
      font-family: var(--font-mono);
      font-size: 0.92rem;
      line-height: 1.7;
      color: var(--text-muted);
      border-left: 2px solid var(--accent);
      padding-left: 1.25rem;
      margin: 1.5rem 0 2.5rem;
      text-align: justify;
      text-justify: inter-word;
    }}
    h2 {{
      font-size: clamp(1.35rem, 2.2vw, 1.85rem);
      font-weight: 700;
      color: var(--accent);
      margin-top: 3.5rem;
      margin-bottom: 1.25rem;
      letter-spacing: -0.02em;
    }}
    h3 {{
      font-size: clamp(1.1rem, 1.4vw, 1.35rem);
      font-weight: 700;
      color: var(--text-title);
      margin-top: 2.25rem;
      margin-bottom: 0.95rem;
    }}
    h4 {{
      font-family: var(--font-mono);
      font-size: 0.92rem;
      color: var(--accent);
      margin-top: 1.75rem;
      margin-bottom: 0.65rem;
    }}
    p {{
      margin-bottom: 1.25rem;
      color: var(--text-body);
      text-align: justify;
      text-justify: inter-word;
      hyphens: auto;
    }}
    strong {{ color: var(--text-strong); font-weight: 600; }}
    em {{ color: #dad6ce; font-style: italic; }}
    code {{
      font-family: var(--font-mono);
      font-size: 0.86em;
      background: var(--bg-code);
      color: #dedad0;
      padding: 0.15em 0.4em;
      border-radius: 3px;
      border: 1px solid var(--border-soft);
    }}
    pre {{
      background: var(--bg-subtle);
      border: 1px solid var(--border);
      border-radius: 4px;
      padding: 1.2rem;
      overflow-x: auto;
      margin: 1.5rem 0;
      font-family: var(--font-mono);
      font-size: 0.86rem;
      color: var(--text-body);
      line-height: 1.6;
    }}
    ul, ol {{
      margin: 1rem 0 1.5rem;
      padding-left: 1.75rem;
      color: var(--text-body);
    }}
    li {{
      margin-bottom: 0.75rem;
      text-align: justify;
      text-justify: inter-word;
      hyphens: auto;
    }}
    li::marker {{ color: var(--accent); }}
    hr {{
      border: none;
      border-top: 1px solid var(--border);
      margin: 3rem 0;
    }}
    .table-wrap {{
      overflow-x: auto;
      margin: 1.75rem 0;
      border: 1px solid var(--border);
      border-radius: 4px;
      background: var(--bg-subtle);
    }}
    table {{
      width: 100%;
      border-collapse: collapse;
      font-size: 0.88rem;
      line-height: 1.6;
      text-align: left;
    }}
    th {{
      font-family: var(--font-mono);
      font-size: 0.76rem;
      text-transform: uppercase;
      letter-spacing: 0.08em;
      color: var(--accent);
      background: var(--bg-code);
      padding: 0.85rem 1rem;
      border-bottom: 1px solid var(--border);
    }}
    td {{
      padding: 0.95rem 1rem;
      border-bottom: 1px solid var(--border-soft);
      vertical-align: top;
      color: var(--text-body);
    }}
    tr:last-child td {{ border-bottom: none; }}
    footer.doc-footer {{
      margin-top: 5rem;
      padding-top: 2rem;
      border-top: 1px solid var(--border);
      font-family: var(--font-mono);
      font-size: 0.78rem;
      color: var(--text-dim);
      display: flex;
      justify-content: space-between;
      flex-wrap: wrap;
      gap: 1rem;
    }}
    footer.doc-footer a {{ color: var(--text-muted); text-decoration: none; }}
    footer.doc-footer a:hover {{ color: var(--accent); }}
  </style>
</head>
<body>
  <main class="sheet" id="top">
    <div class="back-nav">
      <a href="index.html">← Voltar ao Portal Geral</a>
    </div>
    <div class="meta-kicker">{kicker}</div>
    <h1 class="doc-title">{heading}</h1>
    {body_content}
    <footer class="doc-footer">
      <span>{footer_tag}</span>
      <a href="#top">↑ Topo do Fichamento</a>
    </footer>
  </main>
</body>
</html>"""

def md_to_html_simple(md_text):
    lines = md_text.splitlines()
    html_lines = []
    in_code = False
    code_block = []
    in_table = False
    table_rows = []
    in_list = False
    list_type = None
    in_blockquote = False
    bq_lines = []

    def flush_list():
        nonlocal in_list, list_type
        if in_list:
            html_lines.append(f'</{list_type}>')
            in_list = False
            list_type = None

    def flush_bq():
        nonlocal in_blockquote, bq_lines
        if in_blockquote:
            content = '<br>'.join(bq_lines)
            html_lines.append(f'<blockquote>{content}</blockquote>')
            in_blockquote = False
            bq_lines = []

    def flush_table():
        nonlocal in_table, table_rows
        if in_table:
            html_lines.append('<div class="table-wrap"><table>')
            is_header = True
            for r in table_rows:
                if re.match(r'^\s*\|?\s*:?-+:?\s*\|', r):
                    continue
                cells = [c.strip() for c in r.strip('|').split('|')]
                tag = 'th' if is_header else 'td'
                row_html = '<tr>' + ''.join(f'<{tag}>{format_inline(c)}</{tag}>' for c in cells) + '</tr>'
                html_lines.append(row_html)
                is_header = False
            html_lines.append('</table></div>')
            in_table = False
            table_rows = []

    def format_inline(text):
        text = re.sub(r'\*\*(.+?)\*\*', r'<strong>\1</strong>', text)
        text = re.sub(r'\*(.+?)\*', r'<em>\1</em>', text)
        text = re.sub(r'`(.+?)`', r'<code>\1</code>', text)
        return text

    i = 0
    while i < len(lines):
        line = lines[i]

        if line.strip().startswith('```'):
            if in_code:
                in_code = False
                html_lines.append('<pre><code>' + html.escape('\n'.join(code_block)) + '</code></pre>')
                code_block = []
            else:
                flush_list()
                flush_bq()
                flush_table()
                in_code = True
            i += 1
            continue

        if in_code:
            code_block.append(line)
            i += 1
            continue

        if line.strip().startswith('|'):
            flush_list()
            flush_bq()
            in_table = True
            table_rows.append(line)
            i += 1
            continue
        elif in_table:
            flush_table()

        if line.strip().startswith('>'):
            flush_list()
            in_blockquote = True
            bq_lines.append(format_inline(line.strip()[1:].strip()))
            i += 1
            continue
        elif in_blockquote:
            flush_bq()

        if line.strip() == '---':
            flush_list()
            html_lines.append('<hr>')
            i += 1
            continue

        # Headers
        if line.startswith('# '):
            flush_list()
            i += 1
            continue
        elif line.startswith('## '):
            flush_list()
            html_lines.append(f'<h2>{format_inline(line[3:])}</h2>')
            i += 1
            continue
        elif line.startswith('### '):
            flush_list()
            html_lines.append(f'<h3>{format_inline(line[4:])}</h3>')
            i += 1
            continue
        elif line.startswith('#### '):
            flush_list()
            html_lines.append(f'<h4>{format_inline(line[5:])}</h4>')
            i += 1
            continue

        # Lists
        ul_match = re.match(r'^\s*[-*]\s+(.*)', line)
        ol_match = re.match(r'^\s*\d+\.\s+(.*)', line)
        if ul_match:
            if not in_list or list_type != 'ul':
                flush_list()
                in_list = True
                list_type = 'ul'
                html_lines.append('<ul>')
            html_lines.append(f'<li>{format_inline(ul_match.group(1))}</li>')
            i += 1
            continue
        elif ol_match:
            if not in_list or list_type != 'ol':
                flush_list()
                in_list = True
                list_type = 'ol'
                html_lines.append('<ol>')
            html_lines.append(f'<li>{format_inline(ol_match.group(1))}</li>')
            i += 1
            continue
        else:
            flush_list()

        stripped = line.strip()
        if stripped:
            html_lines.append(f'<p>{format_inline(stripped)}</p>')
        i += 1

    flush_list()
    flush_bq()
    flush_table()
    return '\n'.join(html_lines)

# Artigo 1 - Gisela Lermen
art1_path = r'c:\Users\Admin\Desktop\FILOSOFIA\Agostinho - De Magistro\[ARTIGO] Agostinho_De Magistro_Uma análise sob o aspecto da Filosofia da Linguagem.md'
with open(art1_path, 'r', encoding='utf-8') as f:
    art1_md = f.read()

art1_body = md_to_html_simple(art1_md)
art1_html = css_template.format(
    title='Fichamento: De Magistro e Filosofia da Linguagem (Gisela Lermen)',
    kicker='GISELA ANNA BÜTTNER LERMEN · EUGENIO COSERIU (1975) · UNICAP',
    heading='Fichamento: De Magistro <span class="accent">&amp; Filosofia da Linguagem</span>',
    body_content=art1_body,
    footer_tag='fichamento_artigo_filosofia_da_linguagem.html · Síntese Exaustiva'
)

out1 = r'c:\Users\Admin\Desktop\FILOSOFIA\Agostinho - De Magistro\fichamento_artigo_filosofia_da_linguagem.html'
with open(out1, 'w', encoding='utf-8') as f:
    f.write(art1_html)
print('Generated:', out1, len(art1_html))

# Artigo 2 - Christoph Horn
art2_path = r'c:\Users\Admin\Desktop\FILOSOFIA\Agostinho - De Magistro\[ARTIGO] Agostinho_Teoria Linguística dos Sinais.md'
with open(art2_path, 'r', encoding='utf-8') as f:
    art2_md = f.read()

art2_body = md_to_html_simple(art2_md)
art2_html = css_template.format(
    title='Fichamento: Teoria Linguística dos Sinais (Christoph Horn)',
    kicker='CHRISTOPH HORN · VERITAS (2006) · UNIVERSITÄT BONN',
    heading='Fichamento: Teoria Linguística <span class="accent">dos Sinais</span>',
    body_content=art2_body,
    footer_tag='fichamento_artigo_teoria_linguistica_sinais.html · Síntese Exaustiva'
)

out2 = r'c:\Users\Admin\Desktop\FILOSOFIA\Agostinho - De Magistro\fichamento_artigo_teoria_linguistica_sinais.html'
with open(out2, 'w', encoding='utf-8') as f:
    f.write(art2_html)
print('Generated:', out2, len(art2_html))
