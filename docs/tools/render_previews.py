"""Render the BookVerse screens straight from the FXML views and style.css, with sample data.

This is a layout preview, not a JavaFX screenshot: it positions the FXML nodes in HTML and maps
the -fx-* style rules to CSS, so fonts and some details differ from the real app.

Usage (needs Python 3 and Playwright with Chromium):
    python docs/tools/render_previews.py
Writes PNGs to docs/tools/out/.
"""
import re, sys, html, pathlib, xml.etree.ElementTree as ET
ROOT = pathlib.Path(__file__).resolve().parents[2]
RES = ROOT / 'src/main/resources/com/example/librarymanager'
NS = '{http://javafx.com/javafx/25}'
FX = '{http://javafx.com/fxml/1}'
def tag(e): return e.tag.split('}')[-1]
# ---- CSS translation
css = (RES/'style.css').read_text(encoding='utf-8'); css = re.sub(r'/\*.*?\*/', '', css, flags=re.S)
rules = {}
for sel, body in re.findall(r'([^{}]+)\{([^{}]*)\}', css):
    for s in sel.split(','):
        s = s.strip()
        if ':' in s or not s.startswith('.'): continue
        rules.setdefault(s[1:], '')
        rules[s[1:]] += body
def tr(body):
    out = []
    for k, v in re.findall(r'(-fx-[a-z\-]+)\s*:\s*([^;]+);', body):
        v = v.strip()
        if k == '-fx-background-color': out.append(f'background:{v}')
        elif k == '-fx-text-fill': out.append(f'color:{v}')
        elif k == '-fx-font-size': out.append(f'font-size:{v}')
        elif k == '-fx-font-weight': out.append(f'font-weight:{v}')
        elif k == '-fx-background-radius': out.append(f'border-radius:{v}')
        elif k == '-fx-border-radius': out.append(f'border-radius:{v}')
        elif k == '-fx-border-color': out.append(f'border-color:{v}')
        elif k == '-fx-border-width': out.append(f'border-width:{v};border-style:solid')
        elif k == '-fx-border-style': out.append(f'border-style:{v}')
        elif k == '-fx-padding': out.append(f'padding:{v}')
        elif k == '-fx-effect': out.append('box-shadow:0 2px 8px rgba(0,0,0,.25)')
    return ';'.join(out)
def num(e, k):
    v = e.attrib.get(k)
    try:
        f = float(v); return f if f > 0 else None
    except: return None
def font(e):
    for f in e.iter('Font'):
        return f.attrib.get('name', ''), f.attrib.get('size', '14')
    return None
def classes(e):
    c = e.attrib.get('styleClass', '').split()
    sc = e.find('styleClass')
    if sc is not None: c += [s.attrib.get(FX+'value') for s in sc]
    return [x for x in c if x]
ROWS = {}
OVR = {}
def style_of(e, parent):
    st = []
    for c in classes(e): st.append(tr(rules.get(c, '')))
    inline = []
    x, y = e.attrib.get('layoutX'), e.attrib.get('layoutY')
    pw, ph = num(e, 'prefWidth'), num(e, 'prefHeight')
    if tag(e) in ('Label','Button','TextField','PasswordField','Text'):
        pass
    if parent is not None and tag(parent) in ('Pane','AnchorPane','StackPane','ScrollPane','TableView') or parent is None:
        if x is not None or y is not None:
            inline.append(f'position:absolute;left:{x or 0}px;top:{y or 0}px')
    elif parent is not None: inline.append('position:relative;flex:none')
    if pw: inline.append(f'width:{pw}px')
    if ph: inline.append(f'height:{ph}px')
    inline.append('box-sizing:border-box')
    return ';'.join(s for s in st if s) + ';' + ';'.join(inline)
def render(e, parent=None):
    t = tag(e)
    if t in ('font','Font','image','Image','styleClass','stylesheets','URL','color','Color','LinearGradient','stops','Stop','textFill','effect','padding','Insets','columns','cursor','Cursor','Rotate','DropShadow','Glow'): return ''
    kids = e.find('children')
    inner = ''.join(render(c, e) for c in kids) if kids is not None else ''
    s = style_of(e, parent)
    text = html.escape(OVR.get(e.attrib.get(FX+'id',''), e.attrib.get('text', '')))
    f = font(e) if t != 'TableView' else None
    fs = ''
    if f:
        n, sz = f
        fam = "'DejaVu Serif',serif;text-transform:uppercase;font-weight:700" if n in ('Algerian','Cooper Black') else "Inter,'DejaVu Sans',sans-serif"
        fs = f'font-family:{fam};font-size:{float(sz)*(0.74 if n in ('Algerian','Cooper Black') else 0.95):.1f}px;letter-spacing:.01em'
    fill = e.attrib.get('textFill')
    if fill: fs += f';color:{fill}'
    if e.find('textFill') is not None:
        c = e.find('textFill').find('Color')
        if c is not None:
            r,g,b = [int(float(c.attrib.get(k,0))*255) for k in ('red','green','blue')]; fs += f';color:rgb({r},{g},{b})'
    al = e.attrib.get('alignment','')
    if t == 'Label':
        return f'<div style="{s};{fs};white-space:pre-wrap;overflow:hidden;line-height:1.15">{text}{inner}</div>'
    if t == 'Text':
        return f'<div style="{s};{fs};white-space:pre-wrap">{text}</div>'
    if t == 'Button':
        base = 'background:linear-gradient(#f4f4f4,#d8d8d8);border:1px solid #9a9a9a;border-radius:4px;display:flex;align-items:center;justify-content:center;'
        return f'<div style="{base}{s};{fs};white-space:nowrap">{text}</div>'
    if t in ('TextField','PasswordField','TextArea','DatePicker'):
        pt = html.escape(e.attrib.get('promptText', ''))
        shown = '••••••' if False else ''
        return f'<div style="background:#fff;border:1px solid #c4c4c4;border-radius:3px;display:flex;align-items:center;padding:0 8px;color:#8a8a8a;font:13px Inter,sans-serif;{s}">{pt}</div>'
    if t == 'ImageView':
        im = e.find('image/Image')
        src = im.attrib.get('url','').lstrip('@') if im is not None else ''
        w, h = num(e,'fitWidth'), num(e,'fitHeight')
        st = s.replace('width:','x:')  # ignore pref sizes
        pos = ''
        x, y = e.attrib.get('layoutX'), e.attrib.get('layoutY')
        if (parent is None or tag(parent) in ('Pane','AnchorPane','StackPane')) and (x or y): pos = f'position:absolute;left:{x or 0}px;top:{y or 0}px;'
        elif parent is not None: pos = 'position:relative;flex:none;'
        sz = (f'width:{w}px;' if w else '') + (f'height:{h}px;' if h else '')
        return f'<img src="file://{RES}/{src}" style="{pos}{sz}object-fit:contain;display:block"/>'
    if t == 'ProgressBar':
        p = float(e.attrib.get('progress', '0.4') or 0.4)
        if p < 0: p = .4
        return f'<div style="background:#dcdcdc;border-radius:4px;{s}"><div style="width:{p*100}%;height:100%;background:#0096c9;border-radius:4px"></div></div>'
    if t == 'TableView':
        cols = [c for c in e.iter('TableColumn')]
        hdr = ''.join(f'<th style="width:{num(c,"prefWidth") or 120}px;text-align:left;padding:6px 8px;background:#f4f4f4;border-bottom:1px solid #c4c4c4;font:600 12px Inter,sans-serif;color:#333">{html.escape(c.attrib.get("text",""))}</th>' for c in cols)
        rows = ROWS.get(e.attrib.get(FX+'id',''), [])
        body = ''.join('<tr>'+''.join(f'<td style="padding:5px 8px;font:12px Inter,sans-serif;color:#222;border-bottom:1px solid #eee;background:{"#fff" if i%2==0 else "#f6f6f6"}">{html.escape(str(v))}</td>' for v in r)+'</tr>' for i, r in enumerate(rows))
        return f'<div style="background:#fff;border:1px solid #c4c4c4;overflow:hidden;{s}"><table style="border-collapse:collapse;table-layout:fixed;width:100%"><thead><tr>{hdr}</tr></thead><tbody>{body}</tbody></table></div>'
    if t == 'HBox': disp = 'display:flex;flex-direction:row;'
    elif t == 'VBox': disp = 'display:flex;flex-direction:column;'
    else: disp = ''
    if t in ('Pane','AnchorPane','StackPane','ScrollPane') or True:
        if not disp: disp = 'position:relative;' if 'position:absolute' not in s else ''
    return f'<div style="{disp}{s};overflow:hidden">{inner}</div>'
def page(fxml, rows=None, ovr=None, scale=2):
    global ROWS, OVR; ROWS = rows or {}; OVR = ovr or {}
    t = (RES/fxml).read_text(encoding='utf-8'); t = re.sub(r'<\?import[^>]*\?>', '', t)
    root = ET.fromstring(t)
    # normalise namespaced tag/attr names
    for e in root.iter():
        e.tag = e.tag.split('}')[-1]
    body = render(root)
    w, h = num(root,'prefWidth'), num(root,'prefHeight')
    return f'<!doctype html><meta charset=utf-8><body style="margin:0;background:transparent"><div id=app style="position:relative;width:{w}px;height:{h}px;overflow:hidden">{body}</div>', w, h

OUT = ROOT / 'docs/tools/out'
OUT.mkdir(parents=True, exist_ok=True)
from playwright.sync_api import sync_playwright
BOOKS=[('B101','Dune','Frank Herbert','Available'),('B102','Emma','Jane Austen','Issued'),('B103','Pride and Prejudice','Jane Austen','Available'),('B104','Inferno','Dan Brown','Issued'),('B105','The Alchemist','Paulo Coelho','Available'),('B106','To Kill a Mockingbird','Harper Lee','Available'),('B107','1984','George Orwell','Issued'),('B108','Frankenstein','Mary Shelley','Available'),('B109','The Hobbit','J. R. R. Tolkien','Available')]
MEM=[('Nadia Rahman','Student','2','01700000001','nadia@example.com'),('Imran Hasan','Teacher','1','01700000002','imran@example.com'),('Sadia Karim','Engineer','3','01700000003','sadia@example.com'),('Tanvir Alam','Student','0','01700000004','tanvir@example.com'),('Maliha Chowdhury','Writer','1','01700000005','maliha@example.com')]
ISS=[('B102','Emma','Issued','Jane Austen'),('B104','Inferno','Issued','Dan Brown'),('B107','1984','Issued','George Orwell')]
DUE=[('B104','Inferno','Dan Brown','6','360.0'),('B107','1984','George Orwell','2','120.0')]
DASH={'total_issues':'3','my_issues':'3','total_returns':'1','my_returns':'1','total_fines':'480','my_fines':'480','total_dues':'360','my_dues':'360'}
JOBS=[('bookverse-welcome','log_out.fxml',None,None),
('bookverse-dashboard','hello-view.fxml',None,DASH),
('bookverse-inventory','inventory.fxml',{'inventoryTable':[b for b in BOOKS]},None),
('bookverse-issue','issue.fxml',{'issueTable':[b for b in BOOKS]},None),
('bookverse-return','return.fxml',{'returnTable':ISS,'table1':DUE},None),
('bookverse-members','members.fxml',{'memberTable':MEM},None),
]
with sync_playwright() as p:
    b=p.chromium.launch(args=['--allow-file-access-from-files'])
    for name,fx,rows,ovr in JOBS:
        h,w,hh=page(fx,rows,ovr); open(OUT/f'{name}.html','w').write(h)
        pg=b.new_page(viewport={'width':int(w),'height':int(hh)},device_scale_factor=2)
        pg.goto((OUT/f'{name}.html').as_uri()); pg.wait_for_timeout(400); pg.screenshot(path=str(OUT/f'{name}.png')); pg.close(); print(name,int(w),int(hh))
    b.close()
