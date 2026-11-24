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
incoming = {}
sitemap_urls = set()
noindex_urls = set()
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
        self.images = []
        self.h1_count = 0
        self.viewport = False
    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if tag == "img":
            self.images.append(a)
        if tag == "h1":
            self.h1_count += 1
        if tag == "meta" and a.get("name", "").lower() == "viewport":
            self.viewport = True
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
    inventory[-1].update({"html_bytes": f.stat().st_size, "images": len(p.images), "h1_count": p.h1_count, "viewport": p.viewport})
    if rel != "404.html":
        if not p.viewport:
            issues.append(f"{rel}: missing mobile viewport")
        if p.h1_count != 1:
            issues.append(f"{rel}: review H1 count {p.h1_count}")
        for image in p.images:
            if "alt" not in image:
                issues.append(f"{rel}: image without alt attribute: {image.get('src', '')}")
            if image.get("src") and not exists(urljoin(url, image["src"])):
                issues.append(f"{rel}: missing image: {image['src']}")
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
    if "noindex" in p.robots.lower():
        noindex_urls.add(url)
    for href in set(p.links):
        target = urlsplit(urljoin(url, href))
        if target.netloc == urlsplit(origin).netloc:
            path = target.path or "/"
            if path.endswith("/index.html"):
                path = path[:-10]
            elif not path.endswith("/") and (root / unquote(path).lstrip("/") / "index.html").is_file():
                path += "/"
            normalized = origin + path
            if normalized != url:
                incoming.setdefault(normalized, set()).add(url)
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
            if loc.text:
                if loc.text in sitemap_urls:
                    issues.append(f"Duplicate sitemap URL: {loc.text}")
                sitemap_urls.add(loc.text)
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
for entry in inventory:
    url = entry["url"]
    entry["incoming_pages"] = len(incoming.get(url, set()))
    entry["in_sitemap"] = url in sitemap_urls
    if url.endswith("/404.html"):
        continue
    if url in noindex_urls and url in sitemap_urls:
        issues.append(f"Noindex URL in sitemap: {url}")
    if url in sitemap_urls and url != origin + "/" and not incoming.get(url):
        issues.append(f"Sitemap URL without detected incoming links: {url}")
if not pages:
    issues.append("No generated HTML pages")
resources = []
for f in sorted(root.rglob("*")):
    if f.is_file() and f.suffix.lower() in {".jpg", ".jpeg", ".png", ".webp", ".avif", ".gif", ".svg", ".css", ".js", ".woff", ".woff2"}:
        size = f.stat().st_size
        resources.append({"path": f.relative_to(root).as_posix(), "bytes": size})
        if f.suffix.lower() in {".jpg", ".jpeg", ".png", ".webp", ".avif", ".gif"} and size > 500000:
            issues.append(f"Review image over 500 KB: {f.relative_to(root)} ({size} bytes)")
print(f"HTML pages: {len(pages)}; findings: {len(set(issues))}")
for issue in sorted(set(issues)):
    print(issue)
Path("seo-audit.json").write_text(json.dumps({"pages": inventory, "resources": resources, "findings": sorted(set(issues))}, ensure_ascii=False, indent=2), encoding="utf-8")
sys.exit(bool(issues))
