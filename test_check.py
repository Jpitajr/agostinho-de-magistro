
import html.parser
class MyParser(html.parser.HTMLParser):
    def __init__(self):
        super().__init__()
        self.tags = []
        self.errors = []
    def handle_starttag(self, tag, attrs):
        if tag not in ['meta', 'link', 'br', 'hr', 'img', 'input']:
            self.tags.append(tag)
    def handle_endtag(self, tag):
        if tag not in ['meta', 'link', 'br', 'hr', 'img', 'input']:
            if not self.tags:
                self.errors.append(f'Unexpected end tag: {tag}')
            else:
                last = self.tags.pop()
                if last != tag:
                    self.errors.append(f'Mismatched tag: expected {last}, got {tag}')

for filename in ['relatorio_agostinho_de_magistro.html', 'relatorio_burnyeat_de_magistro.html']:
    p = MyParser()
    p.feed(open(filename, encoding='utf-8').read())
    print(filename, 'Errors:', len(p.errors), 'Unclosed:', len(p.tags))
    if p.errors:
        print('Sample errors:', p.errors[:5])
    if p.tags:
        print('Unclosed tags:', p.tags[-5:])
