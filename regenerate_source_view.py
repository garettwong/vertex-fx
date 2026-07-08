from pathlib import Path
import html
import re
import subprocess

ROOT = Path(__file__).resolve().parent
PUBLIC = ROOT / "index.html"
SOURCES = ROOT / "FX_SOURCES.md"
VAULT = ROOT / "g-fx-source-vault-79f87fe9a255b6f590cc"
OUT = VAULT / "index.html"
VAULT_REL = "g-fx-source-vault-79f87fe9a255b6f590cc/index.html"

public = PUBLIC.read_text(encoding="utf-8")
sources = SOURCES.read_text(encoding="utf-8")
try:
    old_hidden = subprocess.check_output(["git", "show", f"HEAD:{VAULT_REL}"], cwd=ROOT, text=True, encoding="utf-8", errors="replace")
except Exception:
    old_hidden = ""

# Map demo filename -> exact X status URL from FX_SOURCES.md lines like:
# - **Title** (`file.html`) — from [@handle](https://x.com/handle/status/123).
source_map = {}
for card in re.findall(r'<a class="card" href="([^"]+)"[^>]*>(.*?)</a>', old_hidden, re.S):
    href, inner = card
    m = re.search(r'class="srcgo exact" data-source="([^"]+)"', inner)
    if m:
        source_map[href] = html.unescape(m.group(1))
for line in sources.splitlines():
    m = re.search(r"`([^`]+\.html)`[^\n]*?from \[@[^\]]+\]\((https://x\.com/[^)]+/status/\d+)\)", line)
    if m:
        source_map[m.group(1)] = m.group(2)

# Pull current public cards.
card_re = re.compile(r'<a class="card" href="([^"]+)"([^>]*)>(.*?)</a>', re.S)
field_re = {
    "title": re.compile(r'<div class="ct">(.*?)</div>', re.S),
    "desc": re.compile(r'<div class="cd">(.*?)</div>', re.S),
    "tag": re.compile(r'<span class="tag">(.*?)</span>', re.S),
    "date": re.compile(r'<span class="date">(.*?)</span>', re.S),
}

def first(pattern, text, default=""):
    m = pattern.search(text)
    return m.group(1).strip() if m else default

cards = []
for href, attrs, inner in card_re.findall(public):
    if href.startswith("#"):
        continue
    qa = ""
    mqa = re.search(r'data-mobile-qa="([^"]+)"', attrs)
    if mqa:
        qa = mqa.group(1)
    title = first(field_re["title"], inner)
    desc = first(field_re["desc"], inner)
    tag = first(field_re["tag"], inner)
    date = first(field_re["date"], inner)
    if not title or not href.endswith(".html"):
        continue
    source = source_map.get(href)
    cards.append({"href": href, "qa": qa, "title": title, "desc": desc, "tag": tag, "date": date, "source": source})

if not cards:
    raise SystemExit("No cards parsed from public index")

css = r'''
:root{--red:#E2231A;--black:#000;--muted:#9a9a9a;--line:rgba(255,255,255,.12);--font:'Archivo',system-ui,-apple-system,sans-serif}
*{margin:0;padding:0;box-sizing:border-box}
html{scroll-behavior:smooth}
body{font-family:var(--font);background:#050505;color:#fff;-webkit-font-smoothing:antialiased;line-height:1.6;overflow-x:hidden}
img{display:block;max-width:100%}
a{color:inherit;text-decoration:none}
.fx-badge{position:fixed;top:18px;left:18px;z-index:550;background:rgba(17,17,17,.92);border:1px solid var(--line);border-radius:50px;padding:9px 16px;font-size:.7rem;font-weight:700;letter-spacing:.14em;text-transform:uppercase;display:flex;align-items:center;gap:9px}
.fx-badge .dot{width:7px;height:7px;border-radius:50%;background:var(--red)}
.fx-hub{display:none}
.fx-hint{display:none}
.hub{max-width:1120px;margin:0 auto;padding:120px clamp(20px,5vw,60px) 100px}
.hub .lead{text-align:center;margin-bottom:50px}
.hub .lead h1{font-size:clamp(2.2rem,6vw,4rem);font-weight:800;letter-spacing:-.02em}
.hub .lead p{color:var(--muted);margin-top:14px;letter-spacing:.04em}
.cards{display:grid;grid-template-columns:repeat(auto-fit,minmax(260px,1fr));gap:18px}
.card{background:#101010;border:1px solid var(--line);border-radius:12px;padding:26px;transition:.4s;display:flex;flex-direction:column;gap:8px}
.card:hover{transform:translateY(-6px);border-color:var(--red);background:#141414}
.card .ct{font-size:1.25rem;font-weight:800}
.card .cd{color:var(--muted);font-size:.92rem;flex:1}
.crow{display:flex;align-items:center;justify-content:space-between;margin-top:14px;gap:10px;flex-wrap:wrap}
.tag{font-size:.6rem;font-weight:700;letter-spacing:.12em;text-transform:uppercase;color:#ffb4a8;background:rgba(226,35,26,.14);border:1px solid rgba(226,35,26,.4);padding:3px 9px;border-radius:50px}
.cgo{color:var(--red);font-weight:700;font-size:.85rem;letter-spacing:.06em;text-transform:uppercase}
.date{font-size:.58rem;font-weight:800;letter-spacing:.12em;text-transform:uppercase;color:#d5d5d5;background:rgba(255,255,255,.08);border:1px solid rgba(255,255,255,.14);padding:3px 9px;border-radius:50px;white-space:nowrap}
.srcgo{color:#ffd1cb;font-weight:800;font-size:.72rem;letter-spacing:.06em;text-transform:uppercase;border:1px solid rgba(255,120,105,.42);background:rgba(226,35,26,.12);border-radius:999px;padding:5px 9px;cursor:pointer;transition:.25s;user-select:none}
.srcgo:hover{color:#fff;border-color:#fff;background:rgba(226,35,26,.25)}
.srcgo.note{color:#cfcfcf;border-color:rgba(255,255,255,.22);background:rgba(255,255,255,.06)}
.private-note{margin:0 auto 22px;max-width:820px;color:rgba(255,255,255,.62);font-size:.78rem;line-height:1.55;text-align:center;border:1px solid rgba(255,255,255,.11);background:rgba(255,255,255,.045);border-radius:16px;padding:12px 16px}
.quick{margin:0 auto 28px;max-width:820px;display:flex;gap:10px;justify-content:center;flex-wrap:wrap}
.quick a{font-size:.72rem;font-weight:800;letter-spacing:.08em;text-transform:uppercase;border:1px solid rgba(255,255,255,.16);border-radius:999px;padding:8px 12px;color:#d9d9d9;background:rgba(255,255,255,.05)}
.quick a:hover{color:#fff;border-color:rgba(226,35,26,.7)}
@media (max-width:640px){.fx-badge{position:static;margin:18px 18px 0;display:inline-flex}.hub{padding:58px 18px 80px}.cards{grid-template-columns:1fr}.card{padding:22px}.crow{align-items:flex-start}.srcgo,.cgo{font-size:.78rem}.date{font-size:.62rem}.hub .lead{margin-bottom:26px}}
'''

card_html = []
for c in cards:
    qa_attr = f' data-mobile-qa="{html.escape(c["qa"], quote=True)}"' if c["qa"] else ""
    if c["source"]:
        src = f'<span class="srcgo exact" data-source="{html.escape(c["source"], quote=True)}">Source X ↗</span>'
    else:
        # Link the general source note page instead of inventing missing X status links.
        src = '<span class="srcgo note" data-source="FX_SOURCES.md">Source note ↗</span>'
    href = c["href"]
    source_href = href + ("&" if "?" in href else "?") + "source=1"
    card_html.append(
        f'<a class="card" href="{html.escape(source_href, quote=True)}"{qa_attr}>'
        f'<div class="ct">{c["title"]}</div>'
        f'<div class="cd">{c["desc"]}</div>'
        f'<div class="crow"><span class="tag">{c["tag"]}</span><span class="date">{c["date"]}</span>{src}<span class="cgo">Open →</span></div>'
        f'</a>'
    )

exact_count = sum(1 for c in cards if c["source"])
html_out = f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<meta name="robots" content="noindex,nofollow,noarchive">
<base href="../">
<title>VERTEX — Source View</title>
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Archivo:wght@300;400;500;600;700;800;900&display=swap" rel="stylesheet">
<style>{css}</style>
</head>
<body>
<div class="fx-badge"><span class="dot"></span>Interactive FX</div>
<div class="hub"><div class="lead"><h1>Interactive FX</h1><p>Unlisted source-view copy. Same FX library, with source X links for your review.</p></div>
<div class="private-note">This is the second version: an unlisted source view with X-source buttons. It is not linked from the public hub. GitHub Pages is still public-by-URL, so treat this as a review URL, not true password protection. Current build: {len(cards)} demo cards, {exact_count} exact X links.</div>
<div class="quick"><a href="index.html">Public clean hub ↗</a><a href="FX_SOURCES.md">Source notes file ↗</a></div>
<div class="cards">{''.join(card_html)}</div></div>
<script>
(function(){{var K='vtxSourceScroll',lock=true;try{{if('scrollRestoration' in history)history.scrollRestoration='manual';}}catch(e){{}}function cur(){{return Math.round(window.scrollY||document.documentElement.scrollTop||0);}}function save(){{try{{sessionStorage.setItem(K,String(cur()));}}catch(e){{}}}}function restore(){{try{{var y=parseInt(sessionStorage.getItem(K)||'0',10)||0;if(y>0)window.scrollTo(0,y);}}catch(e){{}}}}var rt;addEventListener('scroll',function(){{if(lock)return;clearTimeout(rt);rt=setTimeout(save,150);}},{{passive:true}});document.addEventListener('click',function(e){{var a=e.target.closest&&e.target.closest('a.card');if(a)save();}},true);addEventListener('load',function(){{restore();requestAnimationFrame(restore);setTimeout(function(){{restore();lock=false;}},140);}});}})();
document.addEventListener('click',function(e){{var s=e.target.closest&&e.target.closest('.srcgo');if(!s)return;e.preventDefault();e.stopPropagation();var url=s.getAttribute('data-source');if(url) window.open(url,'_blank','noopener');}},true);
</script>
</body>
</html>
'''
VAULT.mkdir(exist_ok=True)
OUT.write_text(html_out, encoding="utf-8")
print(f"generated {OUT}")
print(f"cards {len(cards)} exact_x {exact_count}")
for wanted in ["molten-city-particle-hero.html", "system-book-landing.html"]:
    print(wanted, source_map.get(wanted), wanted in html_out)
