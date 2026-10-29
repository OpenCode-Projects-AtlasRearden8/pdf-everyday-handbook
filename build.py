#!/usr/bin/env python3
"""Build the PDF, Every Day handbook into a static HTML site.

Pure standard-library Python: no pandoc, no pip installs, no network.
Reads the Markdown files in docs/ (sorted by filename) and writes a
single combined page, site/index.html, with a table of contents.

Usage:
    python3 build.py              # build into site/
    python3 build.py --out /tmp/out   # build elsewhere

Supported Markdown (the subset this handbook uses):
    # - #### headings, paragraphs, blank lines
    **bold**, *italic*, `inline code`, [text](https://link)
    - bullet lists (one nesting level via 2-space indent)
    1. numbered lists, - [ ] / - [x] checkbox items
    | tables | with | a |---| separator row |
    > blockquotes, ``` fenced code, --- horizontal rules
All text is HTML-escaped, so stray < > & characters are safe.
"""

from __future__ import annotations

import argparse
import html
import re
import sys
from pathlib import Path

SITE_TITLE = "PDF, Every Day"
SITE_SUBTITLE = "A friendly handbook for living with PDFs"
FOOTER = (
    "PDF, Every Day &mdash; built by <strong>Asdale Dynamics, LLC</strong>. "
    "Released under the MIT License. Local-first: this page was generated "
    "from the Markdown files in docs/ with no network access."
)

CSS = """\
:root {
  --ink: #2b2620;
  --paper: #faf6ee;
  --card: #ffffff;
  --accent: #8a4b2d;
  --accent-soft: #f3e4d9;
  --line: #e4dacb;
  --code-bg: #f0e9dd;
}
* { box-sizing: border-box; }
body {
  margin: 0;
  background: var(--paper);
  color: var(--ink);
  font: 18px/1.7 Georgia, "Iowan Old Style", "Times New Roman", serif;
}
main { max-width: 50rem; margin: 0 auto; padding: 0 1.5rem 4rem; }
header.site {
  border-bottom: 3px double var(--accent);
  background: var(--card);
}
header.site .inner {
  max-width: 50rem; margin: 0 auto; padding: 2rem 1.5rem 1.2rem;
}
h1.site-title { font-size: 2rem; margin: 0; letter-spacing: 0.01em; }
p.site-sub { margin: 0.2rem 0 0; color: #6b5d4e; font-style: italic; }
nav.toc {
  background: var(--card);
  border-bottom: 1px solid var(--line);
}
nav.toc .inner {
  max-width: 50rem; margin: 0 auto; padding: 1rem 1.5rem 1.4rem;
}
nav.toc h2 { font-size: 0.95rem; text-transform: uppercase; letter-spacing: 0.12em; color: var(--accent); margin: 0 0 0.5rem; }
nav.toc ol { margin: 0; padding-left: 1.4rem; columns: 2; column-gap: 3rem; }
nav.toc li { margin: 0.15rem 0; break-inside: avoid; }
nav.toc a { text-decoration: none; color: var(--ink); border-bottom: 1px dotted var(--accent); }
nav.toc a:hover { color: var(--accent); }
section.chapter { border-top: 1px solid var(--line); margin-top: 3rem; padding-top: 1rem; }
h1 { font-size: 1.7rem; line-height: 1.25; margin: 1.4rem 0 0.4rem; }
h2 { font-size: 1.28rem; margin: 2rem 0 0.4rem; }
h3 { font-size: 1.08rem; margin: 1.6rem 0 0.3rem; }
h4 { font-size: 1rem; margin: 1.3rem 0 0.3rem; }
p, li { max-width: 46rem; }
a { color: var(--accent); }
code {
  font: 0.88em/1.5 "SF Mono", ui-monospace, Consolas, "DejaVu Sans Mono", monospace;
  background: var(--code-bg);
  padding: 0.08em 0.35em;
  border-radius: 4px;
}
pre {
  background: var(--code-bg);
  border: 1px solid var(--line);
  border-radius: 8px;
  padding: 0.8rem 1rem;
  overflow-x: auto;
}
pre code { background: none; padding: 0; font-size: 0.9rem; }
blockquote {
  margin: 1rem 0;
  padding: 0.5rem 1.1rem;
  border-left: 4px solid var(--accent);
  background: var(--accent-soft);
  border-radius: 0 8px 8px 0;
}
blockquote p { margin: 0.3rem 0; font-style: italic; }
table {
  border-collapse: collapse;
  width: 100%;
  margin: 1rem 0;
  font-size: 0.95rem;
  background: var(--card);
}
th, td { border: 1px solid var(--line); padding: 0.45rem 0.7rem; text-align: left; vertical-align: top; }
th { background: var(--accent-soft); }
tr:nth-child(even) td { background: #fdfbf6; }
hr { border: none; border-top: 1px solid var(--line); margin: 2rem 0; }
li.checkbox { list-style: none; margin-left: -1.4rem; }
.box { display: inline-block; width: 0.9em; height: 0.9em; border: 2px solid var(--accent); border-radius: 3px; margin-right: 0.45em; vertical-align: -2px; }
footer.site { border-top: 3px double var(--accent); background: var(--card); }
footer.site .inner { max-width: 50rem; margin: 0 auto; padding: 1.2rem 1.5rem 2rem; font-size: 0.9rem; color: #6b5d4e; }
@media (max-width: 640px) { nav.toc ol { columns: 1; } }
@media print { nav.toc, footer.site { display: none; } }
"""


def slugify(text: str) -> str:
    slug = re.sub(r"[^a-z0-9]+", "-", text.lower()).strip("-")
    return slug or "section"


def inline(text: str) -> str:
    """Inline Markdown -> HTML, after HTML-escaping the source text."""
    escaped = html.escape(text, quote=False)
    snippets: list[str] = []

    def stash(snippet: str) -> str:
        snippets.append(snippet)
        return f"\x00{len(snippets) - 1}\x01"

    # Inline code first, so its contents never get bold/italic markup applied.
    escaped = re.sub(r"`([^`]+)`", lambda m: stash(f"<code>{m.group(1)}</code>"), escaped)
    escaped = re.sub(r"\*\*([^*]+)\*\*", r"<strong>\1</strong>", escaped)
    escaped = re.sub(r"(?<!\*)\*([^*]+)\*(?!\*)", r"<em>\1</em>", escaped)
    # URL already HTML-escaped above; only neutralize quotes so the href stays valid.
    escaped = re.sub(r"\[([^\]]+)\]\(([^)\s]+)\)", lambda m: stash(f'<a href="{m.group(2).replace(chr(34), "%22")}">{m.group(1)}</a>'), escaped)

    def unstash(match: re.Match) -> str:
        return snippets[int(match.group(1))]

    return re.sub(r"\x00(\d+)\x01", unstash, escaped)


HEADING_TAG = {"#": "h1", "##": "h2", "###": "h3", "####": "h4"}


class Converter:
    """Converts one handbook chapter into (html_fragment, first_h1_title)."""

    def __init__(self, used_slugs: set[str]) -> None:
        self.used_slugs = used_slugs
        self.first_h1: str | None = None

    def _slug(self, text: str) -> str:
        base = slugify(text)
        slug, n = base, 2
        while slug in self.used_slugs:
            slug = f"{base}-{n}"
            n += 1
        self.used_slugs.add(slug)
        return slug

    def convert(self, source: str) -> str:
        raw = source.replace("\r\n", "\n").split("\n")
        out: list[str] = []
        para: list[str] = []
        i = 0

        def flush_para() -> None:
            nonlocal para
            if para:
                out.append(f"<p>{inline(' '.join(para))}</p>")
                para = []

        while i < len(raw):
            line = raw[i]
            stripped = line.strip()

            if not stripped:
                flush_para()
                i += 1
                continue

            if stripped.startswith("```"):
                flush_para()
                i += 1
                block: list[str] = []
                while i < len(raw) and not raw[i].strip().startswith("```"):
                    block.append(raw[i])
                    i += 1
                i += 1  # skip closing fence
                out.append(f"<pre><code>{html.escape(chr(10).join(block), quote=False)}</code></pre>")
                continue

            match = re.match(r"^(#{1,4})\s+(.*)$", line)
            if match:
                flush_para()
                level, text = match.group(1), match.group(2).strip()
                tag = HEADING_TAG[level]
                if tag == "h1" and self.first_h1 is None:
                    self.first_h1 = text
                slug = self._slug(text)
                out.append(f'<{tag} id="{slug}">{inline(text)}</{tag}>')
                i += 1
                continue

            if re.match(r"^(---+|\*\*\*+)$", stripped):
                flush_para()
                out.append("<hr>")
                i += 1
                continue

            if stripped.startswith(">"):
                flush_para()
                quote: list[str] = []
                while i < len(raw) and raw[i].strip().startswith(">"):
                    quote.append(raw[i].strip().lstrip(">").strip())
                    i += 1
                out.append(f"<blockquote><p>{inline(' '.join(quote))}</p></blockquote>")
                continue

            if stripped.startswith("|"):
                flush_para()
                rows: list[str] = []
                while i < len(raw) and raw[i].strip().startswith("|"):
                    rows.append(raw[i].strip())
                    i += 1
                # Drop the |---| separator row, then render the rest as a table.
                body_rows = [r for r in rows if not re.match(r"^\|[\s:|-]+\|?\s*$", r)]
                if body_rows:
                    cells = [
                        [c.strip() for c in r.strip().strip("|").split("|")]
                        for r in body_rows
                    ]
                    head = cells[0]
                    html_rows = []
                    html_rows.append(
                        "<thead><tr>"
                        + "".join(f"<th>{inline(c)}</th>" for c in head)
                        + "</tr></thead>"
                    )
                    for row in cells[1:]:
                        html_rows.append(
                            "<tr>" + "".join(f"<td>{inline(c)}</td>" for c in row) + "</tr>"
                        )
                    out.append("<table>" + "".join(html_rows) + "</table>")
                continue

            if re.match(r"^\s*[-*]\s+(.*)$", line):
                flush_para()
                list_html, i = self._render_list(raw, i, ordered=False, checkboxes=True)
                out.extend(list_html)
                continue

            if re.match(r"^\s*\d+\.\s+(.*)$", line):
                flush_para()
                list_html, i = self._render_list(raw, i, ordered=True, checkboxes=False)
                out.extend(list_html)
                continue

            para.append(stripped)
            i += 1

        flush_para()
        return "\n".join(out)

    ITEM_RE = re.compile(r"^(\s*)([-*]\s+|\d+\.\s+)(.*)$")

    def _render_list(
        self, raw: list[str], i: int, ordered: bool, checkboxes: bool
    ) -> tuple[list[str], int]:
        """Render the list starting at raw[i]; returns (HTML, next line index)."""
        base_indent = len(raw[i]) - len(raw[i].lstrip())
        items: list[tuple[int, str]] = []  # (nesting level, item text)
        j = i
        while j < len(raw):
            line = raw[j]
            stripped = line.strip()
            if not stripped:
                j += 1
                continue
            m = self.ITEM_RE.match(line)
            if not m:
                break
            is_ordered = m.group(2)[0].isdigit()
            if is_ordered != ordered:
                break
            indent = len(m.group(1))
            level = 0 if indent <= base_indent + 1 else 1
            items.append((level, m.group(3)))
            j += 1
        # Trailing blank lines were consumed as separators; that is fine.

        rendered: list[str] = []
        for level, text in items:
            if checkboxes:
                m = re.match(r"^\[([ xX])\]\s+(.*)$", text)
                if m and level == 0:
                    checked = m.group(1).lower() == "x"
                    box = '<span class="box">&#10003;</span>' if checked else '<span class="box"></span>'
                    rendered.append(f'<li class="checkbox">{box}{inline(m.group(2))}</li>')
                    continue
            if level == 0:
                rendered.append(f"<li>{inline(text)}</li>")
            else:
                # One nesting level: close the previous item inline as a sub-item.
                if rendered and rendered[-1].endswith("</li>"):
                    rendered[-1] = rendered[-1][:-5] + "<ul><li>" + inline(text) + "</li></ul></li>"
                else:
                    rendered.append(f"<li>{inline(text)}</li>")
        tag = "ol" if ordered else "ul"
        return [f"<{tag}>{''.join(rendered)}</{tag}>"], j


def convert_document(used_slugs: set[str], source: str) -> tuple[str, str | None]:
    conv = Converter(used_slugs)
    return conv.convert(source), conv.first_h1


def read_docs(docs_dir: Path) -> list[tuple[str, str, str]]:
    """Return sorted (slug-from-filename, filename, markdown text) tuples."""
    docs: list[tuple[str, str, str]] = []
    for path in sorted(docs_dir.glob("*.md")):
        text = path.read_text(encoding="utf-8")
        docs.append((path.stem, path.name, text))
    if not docs:
        raise SystemExit(f"No .md files found in {docs_dir}")
    return docs


def build_site(docs: list[tuple[str, str, str]], footer: str) -> str:
    used_slugs: set[str] = set()
    chapters: list[tuple[str, str]] = []  # (title, html)

    for stem, filename, text in docs:
        html_frag, first_h1 = convert_document(used_slugs, text)
        title = first_h1 or stem
        chapters.append((title, html_frag))

    toc_items = "".join(
        f'<li><a href="#{slugify(title)}">{inline(title)}</a></li>'
        for title, _ in chapters
    )

    body_sections: list[str] = []
    for title, frag in chapters:
        body_sections.append(f'<section class="chapter">{frag}</section>')

    toc_html = f'<nav class="toc"><div class="inner"><h2>Table of contents</h2><ol>{toc_items}</ol></div></nav>'
    header = (
        '<header class="site"><div class="inner">'
        f'<h1 class="site-title">{SITE_TITLE}</h1>'
        f'<p class="site-sub">{SITE_SUBTITLE}</p>'
        "</div></header>"
    )
    footer_html = f'<footer class="site"><div class="inner"><p>{footer}</p></div></footer>'
    head = (
        "<!DOCTYPE html>\n"
        '<html lang="en">\n<head>\n'
        '<meta charset="utf-8">\n'
        '<meta name="viewport" content="width=device-width, initial-scale=1">\n'
        f"<title>{html.escape(SITE_TITLE)} &mdash; {html.escape(SITE_SUBTITLE)}</title>\n"
        f"<style>\n{CSS}</style>\n"
        "</head>\n<body>\n"
    )
    return head + header + toc_html + "<main>" + "\n".join(body_sections) + "</main>\n" + footer_html + "</body>\n</html>\n"


def main(argv: list[str] | None = None) -> list[tuple[str, str]]:
    parser = argparse.ArgumentParser(description="Build the PDF, Every Day handbook site.")
    parser.add_argument("--docs", default="docs", help="directory of Markdown chapters")
    parser.add_argument("--out", default="site", help="output directory")
    args = parser.parse_args(argv)

    root = Path(__file__).resolve().parent
    docs_dir = Path(args.docs)
    if not docs_dir.is_absolute():
        docs_dir = root / docs_dir
    out_dir = Path(args.out)
    if not out_dir.is_absolute():
        out_dir = root / out_dir

    docs = read_docs(docs_dir)
    page = build_site(docs, FOOTER)
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "index.html").write_text(page, encoding="utf-8")
    print(f"Built {len(docs)} chapters -> {out_dir / 'index.html'}")
    return [(stem, name) for stem, name, _ in docs]


if __name__ == "__main__":
    main()
