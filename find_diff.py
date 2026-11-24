
import re
f1 = open('relatorio_burnyeat_de_magistro.html', encoding='utf-8').read()
f2 = open('relatorio_agostinho_de_magistro.html', encoding='utf-8').read()
print('Burnyeat length:', len(f1))
print('Agostinho length:', len(f2))
# Check if there are JS errors or console errors
