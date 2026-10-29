# Gotchas: Learn From My Scars

Every row here is a real trap people hit, roughly in the order you will meet them. When a PDF misbehaves, check this table *first* — chances are the behavior and the fix are here before you reach for a search engine.

## The gotcha table

| Gotcha | What happens | What to do instead |
| --- | --- | --- |
| Trusting the filename | `contract_signed.pdf` is still unsigned; `statement.pdf` is a screenshot. | Chapter 08's 60-second inspection. The file's content is the truth; its name is a nickname. |
| Drag-select finds no text on a "PDF" | It is a scanned (image-only) PDF — photos, not text. | No software can "fill" a photo; use OCR (chapter 07) or annotate/print-and-write (chapter 02). |
| Typed form answers vanish on the receiver's end | Fields weren't saved with data, or the receiver's tool ignores fields. | The **flatten trick**: fill, then Print, Save as PDF. Send the rebaked copy (chapter 02). |
| Calling print-sign-scan "tamper-proof" | A scan of ink proves *ink*, not *who, when, or what changed later*. | Choose the honest level of proof on purpose (chapter 04): drawn/placed image, service with an audit trail, or real certificate signing. |
| Re-saving a "signed" PDF through the wrong viewer | Visible ink survives; the tamper-evidence underneath quietly breaks or disappears. | Never re-save a signed file unless you accept losing the protection; verify signature validity before relying on it (chapters 04, 08). |
| Asking someone to sign a PDF you already "locked" | Fields refuse, pages refuse to flip, the signing flow fights back. | Agree on the unsigned file, everyone's signature added on *their* copy; the last signer merges or the service tracks it (chapter 04). |
| Compressing until it is unreadable | Portal accepts the upload; the clerk can't read your ID. | Compress to *readable* — `/ebook` for portals, `/prepress` when detail matters — and post-check every page (chapter 03). |
| Deleting the original after compressing | No way to fix, recheck, or re-submit; the compressed copy is now your only copy. | **Always keep originals.** Compressed copies work downward from originals; originals are re-workable (chapter 03). |
| Re-scanning to fix a size cap | Another 20 MB of photos where 2 MB of PDF would do, now with two versions of each page. | Compress or re-export, not re-scan; page tools exist precisely for this (chapters 03, 05). |
| Merging without a manifest | Packet contains two insurance cards, no paystubs, and a fax-cover sheet from 2011 on page 7. | The **packet-packing worksheet** (chapter 09): manifest first, then merge. |
| Page-order or orientation slips in a merged packet | Reviewer opens page sideways, calls it "illegible," and requests everything again. | **Final flip-through at reading speed** before sending — a printed 2-minute ritual worth doing. |
| Feeding a scanned PDF straight into AI for analysis | The model sees nothing (the text was never in the file) and answers from imagination. | Drag test *first*; OCR image-only PDFs (chapter 07), then extract (chapter 06), then ask. |
| Extracting text from an ornately-typeset PDF | Words arrive in the wrong order; the AI reads them wrong. | In such PDFs, extract with `-layout`, tidy small, or extract page-by-page (chapter 06). |
| Uploading a private form to a web "free PDF filler" | Your information now lives on someone else's server, forever-ish. | Local tools first: Firefox, Reader, Preview, LibreOffice all fill forms offline (chapter 02). Local-first is a boundary, not a slogan. |
| Trusting PDF metadata as authentication | Metadata is user-editable before sending; "Author: Bank" proves nothing. | Read it as a *hint*, not truth; corroborate with the channel that carried the file (chapter 08). |
| Streamlining "just print the middle page" without looking | You mail back an unsigned page 14 or exclude the signature page. | Circle every signature and date line before printing; know where the ink should land (chapter 04). |
| Assuming one PDF viewer = truth | The same file renders "perfectly" in one tool and misprints in another. | If the stakes are real, open it in two viewers before trusting it (chapter 08). |
| Believing page thumbnails = proof of completeness | Thumbnails show *images*, omit *content*; a blank page can hide in a full thumbnail strip. | Page-through at reading speed; read what you send (chapter 08). |

## How to use this table

- **Hit a snag scrolling?** Find the behavior-then-cause row above; go to the chapter named in the third column for the calm fix.
- **Doing something new?** Scan the rows that mention what you are about to do; the pre-merge, pre-compress, pre-send trade-offs live here in one place.
- **Reading for the future?** This is the fifteenth chapter you will eventually need. Every row is shorter than the mistake it prevents.
