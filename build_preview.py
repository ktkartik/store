from pathlib import Path
import re,base64,json
root=Path(__file__).parent
mods=['config/brand.js','data/catalog.js','components/ui.js','context/store.js','pages/storefront.js','main.js']
js='const modules = {};\n'
for m in mods:
 p=root/'src'/m;s=p.read_text();exports=[]
 def imp(match):
  spec,path=match.groups(); target=(p.parent/path).resolve().relative_to((root/'src').resolve()).as_posix()
  if spec.startswith('* as '): return 'const '+spec[5:]+' = modules['+json.dumps(target)+'];'
  return 'const '+spec+' = modules['+json.dumps(target)+'];'
 s=re.sub(r'^import\s+(.+?)\s+from\s+[\'\"]([^\'\"]+)[\'\"];?\s*$',imp,s,flags=re.M)
 def dec(match): exports.append(match.group(2));return match.group(1)+' '+match.group(2)
 s=re.sub(r'\bexport (const|function) (\w+)',dec,s)
 def ex(match):exports.extend(x.strip() for x in match.group(1).split(','));return ''
 s=re.sub(r'export\s*\{([^}]+)\};',ex,s)
 if m=='components/ui.js':
  assets={p.stem:'data:image/webp;base64,'+base64.b64encode(p.read_bytes()).decode() for p in (root/'public/images').glob('*.webp')}
  s='const ASSETS='+json.dumps(assets)+';\n'+s.replace('./images/${name}.webp','${ASSETS[name]||ASSETS.hero}')
 js+='modules['+json.dumps(m)+'] = (()=>{\n'+s+'\nreturn {'+','.join(exports)+'};\n})();\n'
js+='modules["main.js"].mountStorefront(document.getElementById("app"));'
css=(root/'src/styles/main.css').read_text();css=re.sub(r'^@import[^\n]*\n','',css)
html='<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1"><meta name="description" content="AUREVANA luxury botanical haircare concept store."><title>AUREVANA — Nature in Every Drop.</title><style>'+css+'</style></head><body><div id="app"></div><script>'+js.replace('</script','<\\/script')+'</script></body></html>'
(root/'AUREVANA-preview.html').write_text(html)
