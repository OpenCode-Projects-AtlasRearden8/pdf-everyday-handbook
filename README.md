# PDF, Every Day

A friendly handbook for living with PDFs — what a PDF really is, filling forms without paid software, shrinking files to meet upload limits, signing safely, building multi-document packets, pulling out text for local AI, OCR in plain English, and checking that a PDF is what it claims to be.

Written by **Asdale Dynamics, LLC** in the house style: plain English, step by step, never condescending. Local-first throughout — every path we recommend can be done on your own computer, and whenever a task tempts you to upload your personal paperwork to a stranger's server, we say so plainly and give you the offline route first.

## What's inside

Twelve short chapters in `docs/`:

0. **Read me first** — who this is for and how to use the book
1. **What a PDF really is** — the "print job on paper" idea that unlocks everything else
2. **Fill in any form** — free, local ways to fill interactive and flat forms (plus the flatten trick)
3. **Shrink a PDF** — meet upload limits without making pages unreadable
4. **Sign it** — print-sign-scan vs. careful digital signing, and when each is the honest choice
5. **Merge and split** — building multi-document packet uploads that portals accept the first time
6. **Pull text out** — extraction, plus feeding text to a *local* AI without anything leaving your machine
7. **OCR in plain English** — turning photographs of text back into text, free and offline
8. **Is this PDF what it claims to be?** — a 60-second inspection routine, both directions
9. **The packet-packing worksheet** — a print-and-pencil checklist for building packets
10. **Gotchas** — a table of traps, consequences, and fixes
11. **Glossary** — every term, translated into human

Plus `README.md` (this file), `LICENSE` (MIT), and one built page: `site/index.html`.

## Build the site

No dependencies, no network, no pip installs — just Python 3:

```sh
python3 build.py
```

That reads every `docs/*.md` chapter (sorted by filename) and writes a single static page to `site/index.html` with a table of contents, styled for screens and reasonable for printing. Open it in any browser.

To build somewhere else:

```sh
python3 build.py --out /tmp/my-build
```

The build is pure standard library (the Markdown-to-HTML converter lives in `build.py`), so it runs anywhere Python 3 runs — deliberately, so you can keep this handbook alive on an offline laptop.

## Run the tests

```sh
python3 -m unittest discover -s tests -v
```

The test suite covers the converter (every block type it handles checks it), the built site (all chapters present, TOC links resolve, tables/checkboxes/code blocks rendered, byte-for-byte deterministic builds), and contents gates (chapter ids resolve, gotcha table and glossary size, no secret-shaped strings, LICENSE/README checks).

## Repository layout

```
build.py                      # stdlib-only Markdown -> static HTML site builder
docs/                         # the handbook chapters (Markdown, numbered for order)
site/index.html               # the built handbook page (open in any browser)
tests/test_build.py           # build + content test suite (stdlib unittest)
LICENSE                       # MIT, Copyright (c) 2026 Asdale Dynamics, LLC
README.md                     # this file
STATUS.md                     # what's done, how to run, verification results, gaps
```

## Sister handbook

This handbook pairs with the **printer-and-scanner-handbook**, which covers the hardware side of the same story: setting up printers and scanners, getting clean readable scans, and troubleshooting all-in-ones. This handbook is the document lifecycle (filling, compressing, signing, merging, checking); that one is the hardware that feeds it. If a step here says "scan it" and your scanner has opinions, look there.

Both handbooks come from Dylan Asdale's [Asdale Dynamics, LLC](https://dylanasdale.github.io) — plain-English AI education, books and guides, and practical tools that respect your privacy and your budget.

## License

MIT. See `LICENSE`. The handbook text and the build script are free to use, adapt, and republish, including commercially, as long as the license travels with them.

Copyright (c) 2026 Asdale Dynamics, LLC
