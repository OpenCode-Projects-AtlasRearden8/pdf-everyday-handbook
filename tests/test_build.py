#!/usr/bin/env python3
"""Tests for the PDF, Every Day handbook build.

Run from the repository root:
    python3 -m unittest discover -s tests -v

Uses only the standard library. Builds are done into temporary
directories so the working tree is untouched.
"""

from __future__ import annotations

import re
import shutil
import sys
import tempfile
import unittest
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO_ROOT))

import build as buildmod  # noqa: E402  (imported after sys.path fix on purpose)


def _conv(markdown: str) -> tuple[Converter, str]:
    conv = buildmod.Converter(set())
    return conv, conv.convert(markdown)


class TestInlineMarkup(unittest.TestCase):
    def test_bold(self):
        _, html = _conv("**strong** tea")
        self.assertIn("<strong>strong</strong>", html)

    def test_italic(self):
        _, html = _conv("a *soft* voice")
        self.assertIn("<em>soft</em>", html)

    def test_bold_and_italic_together(self):
        _, html = _conv("**bold** and *ital*")
        self.assertIn("<strong>bold</strong>", html)
        self.assertIn("<em>ital</em>", html)

    def test_inline_code_is_literal_and_escaped(self):
        _, html = _conv("use `a<b && c>d` here")
        self.assertIn("<code>a&lt;b &amp;&amp; c&gt;d</code>", html)

    def test_markup_inside_code_not_transformed(self):
        _, html = _conv("type `**not bold**`")
        self.assertIn("<code>**not bold**</code>", html)
        self.assertNotIn("<strong>", html)

    def test_link(self):
        _, html = _conv("see [the chapter](https://example.com/x?a=1&b=2)")
        self.assertIn('<a href="https://example.com/x?a=1&amp;b=2">the chapter</a>', html)

    def test_link_text_with_markup(self):
        _, html = _conv("[**bold link**](https://example.com)")
        self.assertIn("<strong>bold link</strong>", html)
        self.assertIn('<a href="https://example.com">', html)

    def test_html_is_escaped(self):
        _, html = _conv("falls <script>alert(1)</script> & done")
        self.assertNotIn("<script>", html)
        self.assertIn("&lt;script&gt;", html)
        self.assertIn("&amp; done", html)


class TestBlocks(unittest.TestCase):
    def test_paragraphs_join_following_lines(self):
        _, html = _conv("one two\nthree")
        self.assertEqual("<p>one two three</p>", html.strip())

    def test_heading_levels_and_ids(self):
        conv = buildmod.Converter(set())
        html = conv.convert("# Big\n## Medium\n### Small")
        self.assertIn('<h1 id="big">Big</h1>', html)
        self.assertIn('<h2 id="medium">Medium</h1>'.replace("/h1", "/h2"), html)
        self.assertIn('<h3 id="small">Small</h3>', html)
        self.assertEqual("Big", conv.first_h1)

    def test_duplicate_heading_gets_unique_id(self):
        conv = buildmod.Converter(set())
        conv.convert("# Same")
        html = conv.convert("# Same #")
        self.assertIn('id="same-2"', html)

    def test_bullet_list(self):
        _, html = _conv("- alpha\n- beta")
        self.assertEqual("<ul><li>alpha</li><li>beta</li></ul>", html.strip())

    def test_nested_bullet(self):
        _, html = _conv("- alpha\n  - nested")
        self.assertIn("<li>alpha<ul><li>nested</li></ul></li>", html)

    def test_ordered_list(self):
        _, html = _conv("1. wake\n2. pack")
        self.assertEqual("<ol><li>wake</li><li>pack</li></ol>", html.strip())

    def test_unordered_and_ordered_lists_stay_separate(self):
        _, html = _conv("- bullet one\n1. step one")
        self.assertIn("<ul><li>bullet one</li></ul>", html)
        self.assertIn("<ol><li>step one</li></ol>", html)

    def test_checkboxes(self):
        _, html = _conv("- [ ] todo\n- [x] done")
        self.assertIn('<li class="checkbox"><span class="box"></span>todo</li>', html)
        self.assertIn('<span class="box">&#10003;</span>done</li>', html)

    def test_table(self):
        _, html = _conv("| A | B |\n| --- | --- |\n| one | two |")
        self.assertIn("<table><thead><tr><th>A</th>", html)
        self.assertIn("<tr><td>one</td><td>two</td></tr>", html)

    def test_table_row_with_inline_markup(self):
        _, html = _conv("| Term | Meaning |\n| --- | --- |\n| **PDF** | a file |")
        self.assertIn("<td><strong>PDF</strong></td>", html)

    def test_blockquote(self):
        _, html = _conv("> one calm line")
        self.assertEqual("<blockquote><p>one calm line</p></blockquote>", html.strip())

    def test_code_fence_escapes_content(self):
        md = "```\n1 < 2 && 3 > 2\n```"
        _, html = _conv(md)
        self.assertIn("<pre><code>1 &lt; 2 &amp;&amp; 3 &gt; 2</code></pre>", html)

    def test_horizontal_rule(self):
        _, html = _conv("before\n---\nafter")
        self.assertIn("<hr>", html)

    def test_list_followed_by_paragraph_terminates(self):
        _, html = _conv("- one\n- two\n\nA paragraph after.")
        self.assertIn("<ul><li>one</li><li>two</li></ul>", html)
        self.assertIn("<p>A paragraph after.</p>", html)


class TestFullSite(unittest.TestCase):
    """End-to-end: build the real docs/ and check the result."""

    @classmethod
    def setUpClass(cls):
        cls.tmp = Path(tempfile.mkdtemp(prefix="handbook-test-"))
        cls.docs = buildmod.read_docs(REPO_ROOT / "docs")
        cls.page = buildmod.build_site(cls.docs, buildmod.FOOTER)
        buildmod.main(["--docs", str(REPO_ROOT / "docs"), "--out", str(cls.tmp / "site")])
        cls.built = (cls.tmp / "site" / "index.html").read_text(encoding="utf-8")

    @classmethod
    def tearDownClass(cls):
        shutil.rmtree(cls.tmp, ignore_errors=True)

    def test_every_chapter_has_a_title_heading(self):
        _, titles = _docs_titles()
        for title in titles:
            self.assertIn(f">{title}<", self.page)

    def test_toc_links_match_heading_ids(self):
        self.assertIn('<h2>Table of contents</h2>', self.built)
        _, titles = _docs_titles()
        for title in titles:
            slug = buildmod.slugify(title)
            self.assertIn(f'href="#{slug}"', self.built)
            self.assertIn(f'id="{slug}"', self.built)

    def test_expected_services_rendered(self):
        # gotcha table and glossary
        self.assertGreaterEqual(self.built.count("<table>"), 2)
        # worksheet checkboxes
        self.assertIn('class="checkbox"', self.built)
        # command examples survive as code
        self.assertIn("<pre><code>", self.built)

    def test_site_is_valid_enough_html(self):
        self.assertTrue(self.built.startswith("<!DOCTYPE html>"))
        self.assertIn('<html lang="en">', self.built)
        self.assertIn("</html>", self.built)
        self.assertEqual(self.built.count("<main>"), 1)
        self.assertEqual(self.built.count("</main>"), 1)
        self.assertEqual(self.built.count("<section"), len(self.docs))
        self.assertEqual(self.built.count("</section>"), len(self.docs))

    def test_no_unconverted_markdown_artifacts(self):
        # headings never leak raw into paragraphs
        self.assertNotIn("<p>#", self.built)
        # list markers never leak raw into paragraphs
        self.assertNotIn("<p>- ", self.built)
        self.assertNotIn("<p>1. ", self.built)

    def test_build_is_deterministic(self):
        second_page = buildmod.build_site(self.docs, buildmod.FOOTER)
        self.assertEqual(self.page, second_page)

    def test_main_writes_one_index_html(self):
        self.assertTrue((self.tmp / "site" / "index.html").exists())
        others = [p.name for p in (self.tmp / "site").iterdir()]
        self.assertEqual(["index.html"], others)


def _docs_titles():
    docs = buildmod.read_docs(REPO_ROOT / "docs")
    titles = []
    for stem, filename, text in docs:
        m = re.match(r"^#\s+(.+)$", text.splitlines()[0])
        if m:
            titles.append(m.group(1).strip())
    return docs, titles


class TestContent(unittest.TestCase):
    """Content quality gates for the Markdown itself."""

    @classmethod
    def setUpClass(cls):
        cls.all, cls.titles = _docs_titles()
        cls.by_name = {name: text for _, name, text in cls.all}

    def test_every_doc_starts_with_h1(self):
        for name, text in self.by_name.items():
            self.assertTrue(
                text.startswith("# "),
                f"{name} must start with a '# ' title",
            )

    def test_expected_chapter_files_exist(self):
        stems = [stem for stem, _, _ in self.all]
        expected_prefixes = [
            "00-read-me-first",
            "01-what-a-pdf-really-is",
            "02-filling-forms",
            "03-compressing",
            "04-signing",
            "05-merge-split",
            "06-extracting-text",
            "07-ocr",
            "08-check-your-pdf",
            "09-worksheet-packet-packing",
            "10-gotchas",
            "11-glossary",
        ]
        for prefix in expected_prefixes:
            matches = [s for s in stems if s == prefix]
            self.assertEqual(1, len(matches), f"missing doc {prefix}")

    def test_gotcha_table_is_substantive(self):
        text = self.by_name["10-gotchas.md"]
        rows = [ln for ln in text.splitlines() if ln.startswith("|") and not re.match(r"^\|[\s:|-]+\|?\s*$", ln)]
        # header row + at least 15 gotcha rows
        self.assertGreaterEqual(len(rows), 16)
        self.assertIn("| Gotcha |", rows[0])

    def test_glossary_is_substantive(self):
        text = self.by_name["11-glossary.md"]
        rows = [ln for ln in text.splitlines() if ln.startswith("|") and not re.match(r"^\|[\s:|-]+\|?\s*$", ln)]
        self.assertGreaterEqual(len(rows), 26)  # header + 25 terms

    def test_worksheet_has_checklists(self):
        text = self.by_name["09-worksheet-packet-packing.md"]
        self.assertIn("manifest", text.lower())
        self.assertIn("post-merge", text.lower())
        boxes = re.findall(r"^- \[[ x]\]", text, flags=re.M)
        self.assertGreaterEqual(len(boxes), 10)

    def test_all_chapter_cross_references_resolve(self):
        for name, text in self.by_name.items():
            refs = re.findall(r"chapter (\d\d)", text)
            for ref in refs:
                self.assertTrue(
                    any(stem.startswith(ref) for stem, _, _ in self.all),
                    f"{name} references chapter {ref}, which has no file",
                )

    def test_no_secret_shaped_strings(self):
        patterns = {"sk-", "ghp_", "AKIA", "-----BEGIN", "api_key=", "API_KEY"}
        for name, text in self.by_name.items():
            for pattern in patterns:
                self.assertNotIn(pattern, text, f"{name} contains {pattern!r}")

    def test_sister_handbook_is_mentioned(self):
        readme = (REPO_ROOT / "README.md").read_text(encoding="utf-8")
        self.assertIn("printer-and-scanner-handbook", readme)

    def test_license_line_exact(self):
        lic = (REPO_ROOT / "LICENSE").read_text(encoding="utf-8")
        self.assertIn("Copyright (c) 2026 Asdale Dynamics, LLC", lic)

    def test_readme_credits_and_explains_build(self):
        readme = (REPO_ROOT / "README.md").read_text(encoding="utf-8")
        self.assertIn("Asdale Dynamics, LLC", readme)
        self.assertIn("python3 build.py", readme)
        self.assertIn("unittest", readme)


if __name__ == "__main__":
    unittest.main()
