
with open('relatorio_burnyeat_de_magistro.html', encoding='utf-8') as f:
    lines = f.readlines()
for i, line in enumerate(lines[-35:]):
    print(f'{len(lines)-35+i+1}: {line}', end='')
