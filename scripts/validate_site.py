"""Validate the small public Pages artifact without third-party dependencies."""
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[1] / "docs"
BASE = "/hackeat/"


class Document(HTMLParser):
    def __init__(self):
        super().__init__()
        self.ids = set()
        self.refs = []
        self.h1 = 0
        self.language = False
        self.viewport = False
        self.title = False

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        assert tag not in {"script", "iframe", "form", "input", "object", "embed"}, tag
        assert not any(key.startswith("on") for key in attrs), "inline event handler"
        if "id" in attrs:
            assert attrs["id"] not in self.ids, "duplicate id"
            self.ids.add(attrs["id"])
        self.h1 += tag == "h1"
        self.language |= tag == "html" and attrs.get("lang") == "es"
        self.viewport |= tag == "meta" and attrs.get("name") == "viewport"
        self.title |= tag == "title"
        if tag == "img":
            assert "alt" in attrs, "image needs alt"
            assert "width" in attrs and "height" in attrs, "image dimensions missing"
        for key in ("href", "src"):
            if key in attrs:
                self.refs.append(attrs[key])


documents = {}
for path in ROOT.glob("*.html"):
    document = Document()
    document.feed(path.read_text(encoding="utf-8"))
    assert document.h1 == 1 and document.language and document.viewport and document.title, path
    documents[path.resolve()] = document

assert (ROOT / "index.html").resolve() in documents
assert (ROOT / "404.html").resolve() in documents
for path, document in documents.items():
    for ref in document.refs:
        url = urlsplit(ref)
        if url.scheme or url.netloc:
            assert url.scheme == "https" and url.hostname == "docs.github.com", ref
            continue
        relative = unquote(url.path)
        if relative.startswith(BASE):
            target = ROOT / relative[len(BASE):]
        else:
            assert not relative.startswith("/"), ref
            target = path.parent / relative if relative else path
        if target.is_dir():
            target /= "index.html"
        target = target.resolve()
        assert target.is_relative_to(ROOT.resolve()) and target.is_file(), ref
        if url.fragment:
            assert target in documents and unquote(url.fragment) in documents[target].ids, ref

for asset in ROOT.rglob("*"):
    if asset.is_file():
        assert asset.suffix in {".html", ".css", ".png"} or asset.name == ".nojekyll", asset
        assert asset.stat().st_size < 500_000, asset
print(f"Public site validated: {len(documents)} HTML pages, local references and bounded static assets.")
