# Shrink a PDF to Meet an Upload Limit

"File exceeds maximum size" is the enroll-your-kid-blocker of our age. Here is the calm, mostly-local way to make any PDF smaller — plus the wisdom to know when *smaller is worse* and it is time to call the human on the other end of the portal.

## Why your PDF is big (usually the pictures)

Chapter 01's rule: text is nearly weightless; images are heavy. A 20 MB PDF of typed pages contains almost no text at all by weight — it contains photographs of pages (scans) while each photograph is stored at full quality, or it contains a handful of embedded photos snapped on a phone camera.

So shrinking a PDF is mostly about *treating the pictures*, in three honest ways:

- **Downsample** — store the picture at a lower dots-per-inch than you need.
- **Recompress** — store the same picture with stronger compression.
- **Remove** — delete pages (e.g., scans of blank backs) or unused extras.

## The two-minute path (works on any computer, no install)

1. Open the PDF and choose **Print**.
2. Choose the built-in **Save as PDF** (Mac) or **Microsoft Print to PDF** (Windows) printer.
3. If your print dialog has a "quality" or "images" setting, drop it to medium / 150 dpi.
4. Print to a new PDF. Keep the original! Check the new one still matches (chapter 08's checklist).

This re-prints the whole document at the print engine's pace, which quietly does some downscaling. It is not the strongest compression in the world, but it is free, offline, and often drops a bloated scan-PDF by half or more. On Linux, the "Print to PDF" printer plus CUPS options does the same job.

## The strong, still-free, still-local path: Ghostscript

Ghostscript is a free, open-source PDF post-processor with real compression muscle. One command:

```
gs -sDEVICE=pdfwrite -dCompatibilityLevel=1.4 -dPDFSETTINGS=/ebook -dNOPAUSE -dQUIET -dBATCH -sOutputFile=small.pdf input.pdf
```

What the important parts mean, in plain English:

- `-dPDFSETTINGS=/ebook` = "target 150 dpi images, fine for screens" (the sweet spot for upload portals).
- Use `/screen` for the most aggressive squeeze (72 dpi — fine for reference copies, risky for signatures; test readability after).
- Use `/prepress` if you need print-shop quality and are fighting the limit anyway (rare).
- On Windows the command is the same with `gswin64c` instead of `gs` (part of the free Ghostscript installer).
- On macOS and Linux, install Ghostscript from your package manager; the command runs in Terminal.

Then compare file sizes, and — important — open `small.pdf` and check it is still readable and complete. Compression is not magic; it is a controlled loss. You control how much loss is acceptable; the checklist in chapter 08 tells you what to verify.

## Trim the fat before you compress

- **Delete blank or duplicate pages.** Scans with a blank back-of-page, or "same doc saved twice," shrink instantly when you use a page rearranger (chapter 05 covers free page tools).
- **Split and send the biggest, then the rest.** If a portal accepts one file per field, you may not need to compress at all — the size limit is usually per file.
- **Not the file's fault? Then it is the photo's fault.** Retape, reshoot or rescan the *original* at a sanely lower resolution (phone scanning apps often ask for quality level; medium is plenty for text) and you win before compressing.

## Reading the winner's numbers like a pro

For most portals, here are the rough size targets, translated into real life:

- Under **1 MB** — almost always fine; this is a screen-readable scan of typed pages.
- **1 to 5 MB** — fine for most portals; page images around 150 to 200 dpi.
- **Over 10 MB** — usually means full-resolution photos are inside. There is nearly always room to shrink *without* anyone noticing, unless the PDF contains real photographs needed as evidence (property photos, ID documents, medical scans).

## When to stop squeezing and email a human instead

Sometimes the right move is a different door, not more compression:

- The PDF is irreplaceable artwork or a signed medical image where quality loss matters.
- You have squeezed with `/ebook` and `/screen` and it is still over the cap. The cap may be the wrong axis (the portal may also have a page limit or a count-of-files limit you have missed).
- The portal says "must be under 2 MB" and your file is 2.1 MB after honest compression — email or call; portals get adjusted by humans all the time.

> The most important line in this chapter: **always keep the original file.** Compressed copies work *down* from originals. Delete the original and you have deleted your ability to fix, re-check, or re-submit anything.
