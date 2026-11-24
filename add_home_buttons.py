import glob, os, re

files = glob.glob(r'c:\Users\Admin\Desktop\FILOSOFIA\Agostinho - De Magistro\*.html')

home_btn_html = '''
<!-- BOTÃO HOME FLUTUANTE / VOLTAR AO ÍNDICE -->
<div id="home-floating-btn" style="position: fixed; bottom: 24px; right: 24px; z-index: 99999;">
  <a href="index.html" style="
    display: inline-flex;
    align-items: center;
    gap: 8px;
    background-color: #e0522b;
    color: #ffffff;
    padding: 10px 18px;
    border-radius: 999px;
    text-decoration: none;
    font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
    font-size: 14px;
    font-weight: 600;
    box-shadow: 0 4px 16px rgba(0,0,0,0.45);
    border: 1px solid rgba(255,255,255,0.2);
    transition: all 0.2s ease;
    backdrop-filter: blur(8px);
  " onmouseover="this.style.transform='translateY(-2px)';this.style.boxShadow='0 6px 20px rgba(224,82,43,0.45)';" onmouseout="this.style.transform='translateY(0)';this.style.boxShadow='0 4px 16px rgba(0,0,0,0.45)';">
    <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round">
      <path d="M3 9l9-7 9 7v11a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z"></path>
      <polyline points="9 22 9 12 15 12 15 22"></polyline>
    </svg>
    <span>Home</span>
  </a>
</div>
'''

top_bar_html = '''
<div class="portal-nav-bar" style="margin-bottom: 2rem; padding: 0.75rem 0; border-bottom: 1px solid rgba(255,255,255,0.1); font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif; font-size: 0.85rem;">
  <a href="index.html" style="color: #e0522b; text-decoration: none; font-weight: 600; display: inline-flex; align-items: center; gap: 6px;">
    <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round">
      <line x1="19" y1="12" x2="5" y2="12"></line>
      <polyline points="12 19 5 12 12 5"></polyline>
    </svg>
    Voltar para o Portal Home (De Magistro)
  </a>
</div>
'''

for filepath in files:
    filename = os.path.basename(filepath)
    if filename == 'index.html':
        continue

    with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()

    # Remove floating button if already added previously
    content = re.sub(r'<!-- BOTÃO HOME FLUTUANTE.*?</div>\s*', '', content, flags=re.DOTALL)
    
    # 1. Adicionar o Top Bar no início do corpo/main se não houver portal-nav-bar
    if 'portal-nav-bar' not in content:
        if '<main' in content:
            content = re.sub(r'(<main[^>]*>)', r'\1\n' + top_bar_html, content, count=1)
        elif '<body' in content:
            content = re.sub(r'(<body[^>]*>)', r'\1\n' + top_bar_html, content, count=1)

    # 2. Adicionar o Botão Flutuante antes de </body>
    if '</body>' in content:
        content = content.replace('</body>', home_btn_html + '\n</body>')
    else:
        content += home_btn_html

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f'Atualizado com botão HOME: {filename}')
