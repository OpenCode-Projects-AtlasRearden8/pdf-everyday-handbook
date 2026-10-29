# STATUS.md — PDF, Every Day

Last updated: 2026-10-29

## What was built

**PDF, Every Day** — a friendly, local-first handbook for living with PDFs from Asdale Dynamics, LLC. Twelve Markdown chapters in `docs/`, compiled into a single static HTML page (`site/index.html`) by a pure-standard-library Python build script (`build.py`), with a 39-test suite in `tests/`.

Contents, mapped to the original goal:

| Goal item | Where |
| --- | --- |
| What a PDF really is | `docs/01-what-a-pdf-really-is.md` |
| Filling forms without paid software | `docs/02-filling-forms.md` (interactive vs. flat forms, free local tools, the flatten trick) |
| Compressing files to meet upload limits | `docs/03-compressing.md` (print-to-PDF fast path, Ghostscript `/ebook`/`/screen`, when to email a human instead) |
| Print-sign-scan vs. careful digital signing | `docs/04-signing.md` (three meanings of "digital signature," choosing on purpose, signature gotchas) |
| Merging and splitting for packet uploads | `docs/05-merge-split.md` (PDF Arranger / Preview / qpdf recipes, size-cap escape hatches) |
| Extracting text to feed local AI | `docs/06-extracting-text.md` (`pdftotext`, privacy-first feeding into Ollama/LM Studio-style local models) |
| OCR in plain English | `docs/07-ocr.md` (drag test, Tesseract + OCRmyPDF, accuracy trade-offs) |
| Checking a PDF is what it claims | `docs/08-check-your-pdf.md` (60-second inspection routine, incoming and outgoing) |
| Packet-packing worksheet | `docs/09-worksheet-packet-packing.md` (manifest table + checkbox checklists) |
| Gotcha table | `docs/10-gotchas.md` (17-row gotcha / consequence / fix table) |
| Glossary | `docs/11-glossary.md` (25 terms in plain English) |
| Complements printer-and-scanner-handbook | cross-referenced in README, chapters 00, 05 (`ls docs` source), 04, and 07 |
| Local-first, tested build | `build.py` uses only the Python standard library (no pip, no network); `tests/test_build.py` covers it |

Other project files: `README.md` (what/how/run/verify, credits Asdale Dynamics, LLC), `LICENSE` (MIT, exact line `Copyright (c) 2026 Asdale Dynamics, LLC`), `.gitignore`. No secrets, API keys, or personal data anywhere in the repo.

## How to run it

```sh
python3 build.py                          # build docs/ -> site/index.html
python3 build.py --out /tmp/elsewhere     # build to a different directory
python3 -m unittest discover -s tests -v  # run the 39-test suite
```

Then open `site/index.html` in any browser. Requirements: Python 3 only — no pandoc, no markdown package, no network.

## Verification results (2026-10-29)

- `python3 build.py` — builds 12 chapters -> `site/index.html`. PASS.
- `python3 -m unittest discover -s tests` — 39 tests, all PASS:
  - converter unit tests (inline markup, escaping, headings/ids/unique slugs, lists incl. nesting + checkboxes, tables, blockquotes, code fences, hr, list/paragraph boundaries);
  - built-site tests (every chapter title present, TOC anchors match heading ids, `<table>` count, checkbox rendering, `<pre><code>` rendering, balanced `<main>`/`<section>` tags, no raw markdown leaking into paragraphs, byte-identical deterministic rebuild, exactly one `index.html`);
  - content gates (all 12 expected chapter files, chapter cross-references resolve, gotcha table has 15+ rows, glossary 25+ terms, worksheet has 10+ checkboxes, no secret-shaped strings, exact LICENSE line, README credits + build/test instructions, sister handbook mentioned).
- Fixed during verification: bullet lists in the in-repo build hung (list-item regex only matched ordered items); ordered items were being swallowed into adjacent bullet lists; link URLs were double-HTML-escaped; two flaky test helpers cleaned up.

## Known gaps

- `site/index.html` is a single combined page; per-chapter HTML pages were skipped to keep the build minimal (each chapter is still reachable via TOC anchors, and the page prints reasonably).
- The converter handles the Markdown subset this handbook actually uses (headings, paragraphs, lists, one nesting level, checkboxes, tables, blockquotes, fenced code, hr, inline bold/italic/code/links). Deeper nesting, reference-style links, and images are intentionally unsupported — unsupported syntax passes through as plain text.
- Command names (`qpdf`, `pdftk`, `pdftotext`, `ocrmypdf`, `ghostscript`) are documented but not invoked anywhere in the pipeline, so tool version drift is not detected by tests.
- The sister handbook `printer-and-scanner-handbook` is referenced but not part of this repository.
- Signing chapter mentions certificate authorities/services in generic terms only, deliberately — no service names are endorsed and no URLs beyond the author hub are cited.
