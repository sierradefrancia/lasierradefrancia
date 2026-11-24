"""Read-only audit of Jekyll output; report findings without changing content."""
import json
import sys
from pathlib import Path
from html.parser import HTMLParser
from urllib.parse import urlsplit, urljoin, unquote
import xml.etree.ElementTree as ET

root = Path(sys.argv[1] if len(sys.argv) > 1 else "_site")
origin = "https://lasierradefrancia.es"
issues = []
titles = {}
descriptions = {}
canonicals = {}
inventory = []
class Page(HTMLParser):
    def __init__(self):
        super().__init__()
        self.canonicals = []
        self.links = []
        self.scripts = []
        self.capture = False
        self.buf = ""
        self.title = ""
        self.in_title = False
        self.description = ""
        self.robots = ""
        self.lang = ""
    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if tag == "title":
            self.in_title = True
        if tag == "html":
            self.lang = a.get("lang", "")
        if tag == "meta" and a.get("name", "").lower() == "description":
            self.description = a.get("content", "")
        if tag == "meta" and a.get("name", "").lower() == "robots":
            self.robots = a.get("content", "")
        if tag == "link" and a.get("rel") == "canonical":
            self.canonicals.append(a.get("href"))
        if tag == "a" and a.get("href"):
            self.links.append(a["href"])
        if tag == "script" and a.get("type") == "application/ld+json":
            self.capture = True
            self.buf = ""
    def handle_data(self, data):
        if self.in_title:
            self.title += data
        if self.capture:
            self.buf += data
    def handle_endtag(self, tag):
        if tag == "title":
            self.in_title = False
        if tag == "script" and self.capture:
            self.scripts.append(self.buf)
            self.capture = False

def exists(url):
    u = urlsplit(url)
    if u.netloc and u.netloc != urlsplit(origin).netloc:
        return True
    if u.scheme not in ("", "https", "http"):
        return True
    p = root / unquote(u.path).lstrip("/")
    return p.is_file() or (p / "index.html").is_file()

pages = sorted(root.rglob("*.html"))
for f in pages:
    rel = f.relative_to(root).as_posix()
    url = origin + "/" + (rel[:-10] if rel.endswith("index.html") else rel)
    p = Page()
    p.feed(f.read_text(encoding="utf-8"))
    if rel != "404.html" and len(p.canonicals) != 1:
        issues.append(f"{rel}: canonical count {len(p.canonicals)}")
    inventory.append({"url": url, "title": p.title.strip(), "description": p.description, "canonical": p.canonicals, "robots": p.robots, "lang": p.lang})
    if rel != "404.html":
        for label, value, registry in (("title", p.title.strip(), titles), ("description", p.description.strip(), descriptions)):
            if not value:
                issues.append(f"{rel}: missing {label}")
            else:
                registry.setdefault(value, []).append(rel)
        if not p.lang.lower().startswith("es"):
            issues.append(f"{rel}: unexpected language {p.lang}")
        for canonical in p.canonicals:
            canonicals.setdefault(canonical, []).append(rel)
            if canonical != url:
                issues.append(f"{rel}: canonical differs from generated URL: {canonical}")
    for s in p.scripts:
        try:
            json.loads(s)
        except ValueError as e:
            issues.append(f"{rel}: invalid JSON-LD: {e}")
    for href in set(p.links):
        if not exists(urljoin(url, href)):
            issues.append(f"{rel}: missing internal link {href}")
for label, registry in (("title", titles), ("description", descriptions), ("canonical", canonicals)):
    for value, paths in registry.items():
        if len(paths) > 1:
            issues.append(f"Duplicate {label}: {value}: {', '.join(paths)}")
for name in ("sitemap.xml", "robots.txt", "llms.txt"):
    if not (root / name).is_file():
        issues.append(f"Missing {name}")
if (root / "sitemap.xml").is_file():
    try:
        tree = ET.parse(root / "sitemap.xml")
        for entry in tree.findall(".//{*}url"):
            loc = entry.find("{*}loc")
            if loc is None:
                issues.append("Sitemap entry without loc")
                continue
            if entry.find("{*}lastmod") is None:
                issues.append(f"Sitemap lastmod absent: {loc.text}")
            if not loc.text or not exists(loc.text):
                issues.append(f"Sitemap target missing: {loc.text}")
    except ET.ParseError as e:
        issues.append(f"Invalid sitemap: {e}")
if (root / "llms.txt").is_file():
    t = (root / "llms.txt").read_text(encoding="utf-8")
    if "{%" in t or "{{" in t or t.startswith("---"):
        issues.append("llms.txt contains unrendered template")
    if origin + "/ai-canon/" not in t:
        issues.append("llms.txt missing Canon link")
if not pages:
    issues.append("No generated HTML pages")
print(f"HTML pages: {len(pages)}; findings: {len(issues)}")
for issue in sorted(set(issues)):
    print(issue)
Path("seo-audit.json").write_text(json.dumps({"pages": inventory, "findings": sorted(set(issues))}, ensure_ascii=False, indent=2), encoding="utf-8")
sys.exit(bool(issues))
