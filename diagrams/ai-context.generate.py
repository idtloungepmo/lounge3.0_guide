from pathlib import Path
import re, html

root=Path(__file__).resolve().parents[1]
md=(root/'project/ai-context.md').read_text(encoding='utf-8')
path=root/'project/ai-context.html'
page=path.read_text(encoding='utf-8')
blocks=re.findall(r'```mermaid\n(.*?)```',md,re.S)
matches=list(re.finditer(r'<div class="mermaid">\s*(.*?)</div>',page,re.S))
assert blocks and len(blocks)==len(matches), 'Markdown and HTML diagram counts must match'
for match,block in reversed(list(zip(matches,blocks))):
    page=page[:match.start(1)]+html.escape(block,quote=False)+page[match.end(1):]
path.write_text(page,encoding='utf-8')
print(f'Synced {len(blocks)} Mermaid diagrams from Markdown')
