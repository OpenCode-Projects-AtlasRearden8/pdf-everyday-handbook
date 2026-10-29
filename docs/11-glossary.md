# Glossary

Every term this handbook leans on, translated into human. Terms link back to what matters, but the table is designed to be read on its own — 2 minutes, and jargon stops being a wall.

| Term | Plain-English meaning |
| --- | --- |
| PDF | Portable Document Format — a file that describes where every page of "ink" sits on fixed pages, so the same pages show up the same way everywhere. A print job saved as a file. |
| Born-digital PDF | A PDF whose words are real text (made by an export button or PDF-maker). You can select its text, the file is light, and your AI can read it straight away. |
| Scanned (image-only) PDF | A photograph of pages, wrapped together in a PDF jacket. No actual text inside — just pixels — until OCR is applied. |
| Page | One fixed "sheet" inside a PDF. A file has a page count; nothing re-flows it. |
| Field | A pre-drawn placeholder box in a form PDF where an answer goes. Some PDFs have real fields; others only look like they do. |
| Flatten | To bake a filled form's typed answers (or field boxes) permanently into the page as plain ink, so they show up the same everywhere. |
| Annotation | A drawn or typed mark placed on top of a PDF page (a text box, highlight, checkmark). Annotations usually stay a separate layer. |
| Metadata | A PDF's small inventory card: title, author, creation date, which program made it. Readable, useful as a hint, and easy for a sender to edit before they send. |
| Compression | Making a file smaller by storing its pictures more economically. Text is nearly weightless; compression mostly means treating images. |
| Lossy compression | Compression that throws detail away on purpose (standard for photos and page scans). Fine while pages stay readable; see chapter 03's checklists. |
| Ghostscript | The free, open-source command-line tool used for real PDF compression in this handbook (`gs`, or `gswin64c` on Windows). |
| DPI (dots per inch) | Image density. Lower on scans = smaller file and coarser look. 150 dpi is usually "fine for screens"; higher is for print shops. |
| Signature (ink-style) | Your physical or drawn signature as an image on the page. Proves agreement to humans; adds no tamper-protection at all. |
| Certificate | A file proving "this digital identity was verified by somebody" — the credential you need for real, math-protected digital signatures. |
| Digital signature (cryptographic) | A signature protecting the *file* itself with a certificate: any change after signing breaks the seal and is announced as invalid. |
| Audit trail | An e-sign service's diary of who signed, which account and timestamp, IP address. Courts often treat the trail, not the ink smudge, as the signature. |
| Tamper-evidence | The property that says "if any part of this PDF was changed after signing, somebody can detect it." |
| Merge | Combining two or more PDFs into one, in a chosen page order — your packet (chapter 05). |
| Split | Cutting a PDF into pieces — by page count or, better, by logical document. |
| Cross-reference table | The internal index inside a PDF that tells a viewer where each object lives in the file. If this index is damaged, some viewers open the file anyway while others refuse — a PDF can be technically readable and technically broken at once. |
| pdftotext | The free, offline tool for pulling the text back out of born-digital PDFs (Poppler suite). |
| OCR (optical character recognition) | The trick that turns a photograph of text back into actual text, by asking the computer "is this shape an e?" a few million times per page. |
| Tesseract | The free, open-source OCR engine this handbook recommends. |
| OCRmyPDF | The friendly wrapper around Tesseract that adds a searchable text layer *into* a scanned PDF without changing its pages or size much. |
| Searchable PDF | A scanned PDF that has quietly gained an invisible text layer: photo on top, select- and search-able text underneath. |
| Local AI | A language model running entirely on your own computer (Ollama, LM Studio, llamafile). Your documents stay home. |
| Extraction | Chapter 06's whole job: getting the words back out of a PDF so tools and AI can read them. |
| Portal | The website that says "please upload a PDF under 2 MB," then stores whatever actually arrives. Now you know how to feed it right. |

## Where each chapter picks up a term

Chapter 01 hands out the vocabulary frame (born-digital vs. scanned; metadata; embedded fonts). Chapters 02 to 04 use the vocabulary in practice. Chapters 05 to 08 are where the **technical** workhorse terms live: merge/split, compression, tamper-evidence, extraction, OCR. The worksheet and gotcha tables chapter 09/10 are where the vocabulary is applied — and this glossary is the page you flip back to whenever any of those terms blur.
