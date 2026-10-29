# Merging and Splitting for Packet Uploads

Most portals do not want *a* PDF. They want one tidy PDF that contains your whole packet in the right order — cover sheet first, form second, proof third, extra evidence last — under the size cap, with no fax-cover-sheet ghosts from 2011 lurking on page 7. This chapter is how you build such a packet calmly, and the worksheet in chapter 09 gives it to you as a print-and-pencil checklist.

## The tools, all local and free

- **PDF Arranger** (Linux/Windows; free) — drag, drop, rotate, delete, reorder pages; save as a new PDF. The friendliest tool for this job, full stop.
- **Mac Preview** — the sidebar shows page thumbnails; drag to reorder, drag pages between two open PDFs, File, Export as PDF to save the merged result.
- **Command line, when it becomes a weekly chore** — `qpdf` (free, everywhere) merges and splits in one line:

```
qpdf --empty --pages doc1.pdf 1-3 doc2.pdf -- packet.pdf
```

That line says: start with nothing, take pages 1 to 3 of doc1, then all of doc2, save as packet.pdf. Swap tool for `pdftk` (also free) in `pdftk A=doc1.pdf B=doc2.pdf cat A B output packet.pdf` — same idea, slightly different grammar. One of these will be installed already or is a one-minute install away.

## Merging: the six-step calm ritual

1. **Gather the parts.** Every document gets its own properly named file in one folder before merging: `01-application-form.pdf`, `02-insurance-card.pdf`, `03-payslips-sept.pdf`. (Numbers in the names are a gift to your future self; they make the final order obvious to any human and any tool that lists files alphabetically.)
2. **Check the page shape.** Everything landscape or everything portrait? Mixed orientation is fine, but viewer-side flip-flopping isn't. Rotate the odd ones first, inside the page tool rather than re-scanning (the printer-and-scanner-handbook explains why re-scanning costs quality).
3. **De-duplicate.** If your insurance card is in two documents, decide which one is the good copy and delete the other from the working set.
4. **Put no cover sheet inside another document.** The cover sheet becomes page 1 of the packet PDF, not page 1 of an inner file, or the portal's packet-preview will look like a stack of brochures.
5. **Merge in order using a page tool** (see PDF Arranger / Preview / qpdf above) into one file: `packet-final.pdf`.
6. **Do the final flip-through.** Open the packet, page through at reading pace — not skimming, *reading* — and confirm order and orientation. Only then send it.

## Splitting: one-thing-per-upload, the clean way

Portals that accept one file per field need each document split back out. Both directions of the same knowledge:

- **Split by page range.** In PDF Arranger, export selected pages as a new file (right-click, Export). In `qpdf`:

```
qpdf --split-pages big.pdf out-%d.pdf
```

(Makes several files, each with the maximum page count the portal usually allows; to hand-split a range, `qpdf --empty --pages big.pdf 4-9 -- form-part.pdf`.)

- **Split by logical document, not by page count.** If `big.pdf` has 40 pages but the real documents inside it are "form (pages 1-8), insurance (9-10), paystubs (11-20)," extract each range into its own file. A page-count-max split does not fool a human clerk who needs the insurance card to be its own upload.
- **After splitting, always page through what you are about to upload.** It takes 30 seconds and catches the flipped or missing page that got you told "incomplete submission" two times already this year.

## The size cap collides with merging: the escape hatches

Merging usually *increases* total size — photos pile up. When your packet busts the upload limit:

1. Compress **before** merging, not after, so you compress once, knowingly, at the page level. Chapter 03's Ghostscript one-liner is your friend.
2. Or, if the portal allows only *some* merged size, split into packet-one (the required docs, compressed `/ebook`) and packet-two (extras), and upload packets separately per field.
3. Never re-scan to fix a size problem — re-scan always makes things bigger. Compress or re-export, and consult chapter 03.

## Page-order and packet sanity habits worth building

- **Alphabetical-but-numbered filenames** numbered pages 01, 02, 03 stay in the order you intend.
- **Names that a stranger (or the clerk, or you in six months) can visually classify without opening** the file: `03-payslips-oct2026.pdf` beats `scan0147.pdf`. Labels outside the packet make the inside of the packet findable.
- **Keep a copy of the sent packet, with the day's date on it** (`2026-10-29-coop-insurance-packet.pdf`), even when the portal returns a receipt. In disputes, this copy is your receipt.

Take the worksheet in chapter 09 with you on your next packet job. It is designed to be printed once and used, pencil-style, table-side; the first time you build a big packet with it, you will wonder how you ever shipped one unpaginated.
