# Pull Text Out of a PDF (and Feed It to Local AI)

There comes a day when you want a machine to do something useful with your paperwork: "summarize this lease," "find every deadline in these fourteen pages," "compare the two quotes side by side." All of it starts with one step: turn the PDF into text the AI can actually read. This chapter is that step — done safely, locally, and for free.

## Remember the two families (this is the chapter where it matters)

Chapter 01 taught the test; here is why it decides everything:

- **Born-digital PDF** — the letters are real text. Extracting is a free lunch, done in seconds.
- **Scanned PDF** — a photo of paper wrapped in a PDF jacket. There is *no text in the file to extract*; the machine sees only shapes. This family needs OCR first (chapter 07).

Nothing else in this chapter works until you know which family you are in. Drag-select a paragraph. Highlights? Born-digital, continue. Nothing? Scanned — jump to chapter 07 and come back.

## The free-and-local extraction menu

1. **Copy-paste.** Honestly: select, copy, paste into your text editor. Fine for a paragraph or two. Watch out for weird characters when you paste ("fi" and "fl" sometimes arrive fused, quotation marks arrive in strange guises, line breaks land mid-sentence) — for a paragraph, clean-up is a ten-second relief.
2. **`pdftotext` (from the free Poppler tools).** The old, reliable, offline standard, built for this exact job. Installed on most Linux; one homebrew or installer away on Mac and Windows.

```
pdftotext -layout lease.pdf lease.txt
```

The plain-English part: `-layout` means "keep the two-column and table arrangement the way a human laid it out," which usually makes AI summaries better because tables stop being a jumble of identical rows.

3. **That's it, honestly.** For text extraction, `pdftotext` *is* the graceful unsung hero. Commercial extractors mostly re-wrap the same capability, and web-based "free PDF to text" services just move the same job onto a stranger's server — see the privacy note.

## Feeding extracted text to a local AI, safely

Once you have clean `.txt` (or markdown copies of the text), local-first AI is genuinely local: your document never leaves your machine. Tools like **Ollama**, **LM Studio**, or llamafile run language models entirely on your own computer.

1. **Have the text ready in a file you can point to** (`lease.txt` from `pdftotext`, or a copy-paste from one chapter's worth of text).
2. **Load a decent model in your local AI app.** For reading leases, paystubs, contracts, insurance PDFs, casual small docs — a mid-sized model you can run comfortably on your machine is fine. Ask the app or hub guide for its current recommendation; the model menu changes by the season.
3. **Paste or attach the text, then ask human-shaped questions**: "What dates in this document matter?", "What am I promising?", "What is the riskiest sentence here you'd want a lawyer to check?" — plain language, in, out.
4. **Extract only what you need.** Whole-30-page-PDFs as context can waste the model's attention (some models can't "see" all of a long paste at once). Give it the pages that actually matter: chapter 05's splitting knowledge (`qpdf --empty --pages big.pdf 9-14 -- just-the-relevant-part.pdf`, then `pdftotext` that) pays off again here.

> With a local model, the classic privacy fear is solved structurally: nothing was uploaded anywhere. Do keep normal computer hygiene — anyone with access to this computer can still read what you asked it.

## The small print of extracted text

- **Formatting isn't just decoration — tables collapse or misalign, footnotes run underneath, page numbers go stray.** Skim the `.txt` before feeding it to the AI; five seconds of tidying often upgrades the answers.
- **Some born-digital PDFs still extract badly** — ornate layout programs can save each *word* as individually positioned shapes, which extraction tools then get in the wrong order.
- **A scanned PDF will extract to an *empty* or near-empty `.txt` file.** That's the family-mix-up check, not a bug: no text was in the file. OCR first, then extract.
- **Private but not secret:** a local model processes within your machine, but keep your own habits tidy — the extracted `.txt` files linger in your folder. Delete or archive them like any other copy of your documents.

## One chapter, one promise

Do this right, and AI reads your paperwork *like a friend would* — carefully, locally, and without anyone's cloud getting a copy. That is the whole idea this handbook's AI chapters stand on.
