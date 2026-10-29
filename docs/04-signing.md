# Sign It: Print-Sign-Scan vs. Careful Digital Signing

A signature is a claim: *I agreed to this.* Both of the approaches in this chapter can carry that claim honestly — but they carry it in different ways, and mixing them up causes real problems. Let's get the difference straight so you always pick on purpose.

## Print-sign-scan: the ink-and-paper classic

You print the PDF, sign with a real pen, scan (or photograph) the pages back into one PDF, and send it. Courts, employers, and landlords accept this daily. What a scrawled scan actually proves, though, is weaker than it feels: it proves *somebody's ink* was on the page at some point. It does not prove who, or when, or what happened to the file afterwards.

That weakness can be just fine — a signed lease between you and your landlord needs to be truthful and accepted, not cryptographically armored.

Steps that make print-sign-scan smooth (details for the hardware itself live in the companion printer-and-scanner-handbook):

1. Print **only the pages that expect your signature** if the rest is 40 pages of contract boilerplate; know exactly where your initials and date go before you hit print. Signature-required pages usually tell you, but circle each signature and date line with pencil before printing, so you do not mail back an unsigned page 14.
2. Sign every clearly-marked line, and *date it on the day you sign*.
3. Scan **straight-on, even page-by-page, black text mode or color as the original requires** — do not crop so tightly that a margin note disappears; the context around your scrawl is part of the proof.
4. Merge back into a single PDF in the original page order (chapter 05 covers this in detail).
5. Re-read it once, asking "would I be embarrassed if a stranger saw this?" before sending.

## Careful digital signing: ink, upgraded with math

When people say "digital signature" they may mean three genuinely different things. Know which one is happening:

1. **A typed or drawn signature image placed on the page.** This is the drag-and-draw-your-name stage in e-signature services, Adobe Fill & Sign, Mac Preview's Sign tool, or an image created from a photo of your cursive. It is the visual ritual, and it is no more technically tamper-proof than the scanned version. It is fine for most everyday agreements, especially when the counterparty uses the same service checkbox ("this is my signature") as part of their acceptance flow.
2. **A cryptographic digital signature with a certificate.** This is the real deal: your signing identity plus a certificate, so the file itself carries tamper-evidence. If so much as a comma changes after signing, the file announces it as invalid. Ordinary people meet this through government-issued electronic ID programs (several countries give every citizen one for free), employer-issued signing identities, or a certificate from a verification service. Tools that can apply such a signature include Adobe Acrobat (paid), LibreOffice (free), and various government ID apps.
3. **An e-signature service with legal-wrap agreements.** The signature itself is a drawn stack, but the *service* keeps an audit trail: who clicked, from which account, at what timestamp, with which IP address. Courts in many places treat this trail as the actual signature. You are trading some privacy and a little cash for a strong legal shield. Choose it when the deal is big enough to matter.

## Choosing on purpose: which one for which job?

- Everyday, low-stakes, inside-your-community agreements: print-sign-scan or a drawn signature image — whichever you have at hand. Truthfully said and mutually understood beats cryptographically perfect every time.
- Employment, housing, financial agreements: drawn signature image inside a reputable e-signature service both sides already use, or a real certificate-signed PDF if you have the cert.
- Anything where the *other side* could be tempted to alter the file later — contracts with a stranger, final records tied to money or property, medical consents — ask for a service that produces an audit trail, or a certificate-signed file, and keep the email thread that quotes the crucial paragraph back to you.
- Legal or high-stakes paperwork where you suspect fraud risk: certificate-signed. Full stop.

## The gotchas this corner of the book exists for

- **A "signed" PDF is only as protected as the tool that handled it after signing.** If someone re-saves a signed file through a converter or viewer that rewrites it, the drawn or scanned signature can survive visually while the protection underneath quietly breaks or disappears. Verify the final version before you rely on it or send it.
- **E-signature services sometimes legally do not cover** the type of document you have. Read the service's own one-pager about what is excluded (wills, some real property transfers, some medical consents in the US) before you rely on it.
- **Never re-sign somebody else's already-signed document.** If a counterparty must also add their signature, start from a copy of the unsigned file that both sides agreed on. With paper signing, everyone watches the same page; with audit-trail services, the service tracks the signing order for you.
- **If a portal demands a specific kind of signature** (some government and bidding portals insist on certificate-signed PDFs), ink will be rejected no matter how beautiful. Budget the time to get the real signing identity once, rather than fighting rejections forever.

## One privacy word

A scanned or drawn signature is a copy of *you* that you then share with every recipient and their servers. If you wouldn't want your handwritten signature public, use a service-side drawn signature rather than a scan of your actual cursive, or sign with a stylus rather than a phone photo of your hand. Real ink, real you, real risk.
