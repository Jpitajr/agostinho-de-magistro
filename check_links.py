import urllib.request
import re

req = urllib.request.Request('https://jpitajr.github.io/agostinho-de-magistro/index.html', headers={'User-Agent': 'Mozilla/5.0'})
with urllib.request.urlopen(req) as resp:
    html = resp.read().decode('utf-8', errors='ignore')

links = re.findall(r'href=["\']([^"\']+\.html)["\']', html)
for l in sorted(set(links)):
    print('Link in index.html:', l)
