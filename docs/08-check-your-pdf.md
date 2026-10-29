# Is This PDF What It Claims to Be?

Every so often, a PDF arrives wearing a costume. It says `final_contract_signed.pdf` and contains an unsigned draft. It claims to be a bank statement and is a random document renamed. It looks fine in the email preview and falls apart in the portal. This chapter is the short, calm inspection routine — a pre-flight check before you *trust* a PDF someone else sent, and before you *send* a PDF of your own.

## The 60-second inspection (do this every time before you trust or send)

1. **Read the file, not the filename.** What is this *really*? Open it. Filenames are labels, not guarantees — chapter 01's first rule. `statement.pdf` might be a photo of a prompt in a web browser; `receipts_scan_2026.pdf` might contain one receipt and nine pages of blank backs.
2. **The drag test.** Select some text. Highlights mean born-digital; empty cursor means scanned family. Now you know whether the text is real and extractable — remember, this decides what you can do with the document later.
3. **Count the pages, glance at every page.** Is the expected page order there? Missing last page? Page 2 and page 3 swapped? Page rotation sideways for two pages in the middle? Every mis-matched page is a re-do request waiting to happen. Page through at reading speed, not skim speed; the portal's thumbnail strip counts page *images* but not page *content*.
4. **Check every page's readability.** Text legible? Photos dim but usable? Scan slanted? Signatures *visible* and *on the correct lines*? A compressed-but-unreadable page costs you another email round-trip, same as a missing page.
5. **Look at the metadata (the "inventory card" of chapter 01).** Right-click the file: Properties (Windows), Get Info (Mac). Viewer menus show PDF metadata on documents too (in Firefox: File, Properties or in Adobe Reader: Document Properties). What usually matters: which program made it, when, is the title or author something unexpected, and did a *different* page get appended by a different program at a different time. This is a *hint*, not truth — the fields are user-editable before upload, so they can be misleading, but a suspicious mismatch ("Author: DMV Forms System" on a personal letter) is worth a raised eyebrow.
6. **If the document carries a claimed digital signature, verify it, don't admire it.** A file can show a realistic-looking signature image while having no valid cryptographic signature underneath at all. Where it matters, check what the *viewer* reports about the signature's validity, not just the ink on the page (chapter 04 explains the difference).

## Sending: the same 60-second check, backwards

Before you send a PDF of your own, use the same checklist as the receiver's first impression:

1. **Rename honestly.** `2026-10-29-coop-insurance-packet.pdf` — dates and content, not `final_v7_REAL.pdf`. The reader finds it in six months, thanks you.
2. **Re-check page order, rotation, completeness** in one steady pass.
3. **Strip anything that was not meant to travel.** Click File, Properties; if the metadata lists tracked-page notes or a stranger's sign-off, decide on purpose whether it should travel. Metadata edits are legal; some privacy-strict portals blanch at freighting.
4. **Confirm form fields really saved.** Chapter 02's flatten trick, if needed.
5. **Check size against the portal's cap** (chapter 03) — and confirm visually that the *compressed copy* still matches the original page-for-page.

## Signs of a PDF worth being suspicious about

In your life, the facts will probably never be interesting enough to use this section. That is fine; it is your seatbelt for the day they are:

- A document where page order files DO NOT simply continue: e.g., page 5 of "Appendix" comes after page 9 of "Exhibit B."
- File contents inconsistent with the email that carries them: statement attachment where the stated date is wrong.
- A document where the file was a *photograph* of a computer screen — the resolution and horizon lines tell you. Good question: why *was* it a photograph?
- Multiple CreationDate fields, or metadata claiming two entirely different producer programs with no story for the gap.
- The signature's visible ink and the tamper-evidence stamp *disagree* about what was signed.

Any of these deserve a plain-language question to the sender: *"I want to double-check this PDF's history before I rely on it."* Most honest senders simply re-send. A good-faith question in email is the cheapest fraud filter in the world — and it costs zero megabytes.

## Why this routine matters more than any single tool

Chapter upon chapter, every operation in this handbook — filling, compressing, signing, merging, extracting — can go quietly wrong, and every failure mode produces the same verdict: *a PDF that looks okay and isn't.* The inspection routine above is your handrail over all of it. Two minutes of looking, before you send and before you trust, beats two weeks of un-winding anything else.
