# OCR in Plain English

OCR — "optical character recognition" — is the trick that turns a *photograph of text* back into *text*. If that explanation lands, you already know what it does; the rest of this chapter teaches you the two things everyone actually needs: when you need it, and how to run it free, offline.

## When a PDF needs OCR, and when it does not

- **Born-digital PDF** (you can drag-select a sentence; the file was made by an export button) — **no OCR. Ever.** The text is already text. Running OCR on it would be a suspiciously expensive way to degrade something that was free and perfect.
- **Scanned PDF** (nothing draggable; each page is one flat picture) — **this is OCR's home.** The pixels go in, words come out.

Chapter 01's drag test, again, in a sentence: you cannot work with what you cannot see, and OCR is how the machine gets to see.

## What OCR actually does (plain English, thirty seconds)

The computer looks at each page-image and asks, over and over: *is this shape an e? an f? a comma?* Then it stitches the letters into words, the words into lines, and lays them down as real text positioned to match the picture. That's it. It is pattern-matching done at industrial scale and speed.

What follows from that simple description:

- **It can be wrong.** Blurry scans, weird fonts, handwriting, coffee stains — every imperfection of the originals is a chance to guess a wrong letter. Check the output against the picture when the stakes are high.
- **It works best on clean, straight, typed text.** Low-contrast, skew-jewed, smudgy photos reduce accuracy. Rescanning gently beats OCR-ing desperately; the printer-and-scanner-handbook has the scan settings.

## The free, local, mature stack: Tesseract and OCRmyPDF

1. **Tesseract** is the free, open-source OCR engine: the actual shape-reader. Install it once via your package manager (the hub guide's setup section covers your operating system; Mac users typically install via Homebrew).
2. **OCRmyPDF** is the friendly wrapper built *around* Tesseract, specialized for our main job — it adds the text layer *into the same PDF* (an invisible layer of selectable text sitting under each page photo), so the PDF stays a PDF and becomes *both* things at once: photo on top, text underneath.

```
ocrmypdf --language eng scanned.pdf searchable.pdf
```

Plain-English translation: "read scanned.pdf assuming English words, and write searchable.pdf, same pages, but now with searched-from text." Add `--language eng+fra` if the document mixes in a second language — a hint that genuinely improves accuracy.

Then the magic moment: open `searchable.pdf`, and **drag-select a paragraph. It highlights now.** You have converted a member of the scanned family into a hybrid — and once the text is in there, chapter 06's `pdftotext` works on this PDF, and your local AI can read it.

## Practical prices and trade-offs

- **Time.** Tesseract processes a typed page in a second or two on ordinary hardware. A 300-page lease takes some minutes — let it run, check your email instead, come back.
- **Accuracy.** Fine scans of typed text: usually excellent, 99-ish percent. Phone-photos at an angle: noticeably worse; straighten (OCRmyPDF has `--deskew` for a light auto-straighten) and re-shoot if the whole document matters.
- **Language and handwriting:** English typed is the sweet spot; other languages work when you tell OCRmyPDF which ones to expect. Neat handwriting produces tolerable results with patience; truly terrible pens beat OCR outright, and a human reading it is faster than a machine guessing.
- **File size:** the text layer adds a whisper of data; the page photos stay the same weight. This is not be confused with compression (chapter 03) — you can do both in sequence on the same file.

## A homesick note on trust

OCR output is a *best guess with proof*, not a certification. If the extracted text says "$1,850 per month" and your eyes look at the page photo and see "$1,350 per month," believe the page photo, not the OCR. This same principle extends to feeding local AI documents: scan-then-OCR text feeding an AI should come with a "verify the numbers" disclaimer — worth remembering even for summaries and deadlines.

And that is all of OCR you need for ordinary life: test the PDF first; OCR only when it is actually a photo-of-text; use free local tools, not someone else's upload server; check the output with your own eyes.
