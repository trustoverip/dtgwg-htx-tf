# Human Trust Experience — Research findings (static snapshot)

> **Snapshot date: 4 August 2026 at 13:04**
> Live, interactive version: <https://platform.validant.ai/trust-experience#research>

This folder is a **self-contained, static snapshot** of the validant *Human Trust Experience* research
page. It is designed to be dropped, unchanged, into a GitHub repository so that anyone with the repo can
open the page and get an experience close to the live one, without a server, a build step, or a network
connection.

## What is inside

| File | Purpose |
|------|---------|
| `index.html` | The whole research page as one self-contained document (all styling, text and the iceberg diagram are embedded). Open it in any browser. |
| `README.md` | This file. |
| `snapshot.json` | Machine-readable metadata: extraction date, source URL, and the counts captured at snapshot time. |
| `data/research.json` | The structured research data behind the page (moments, calibration, best practices, exemplars, prescriptive rules, findings, evidence), for reuse and citation. |
| `.nojekyll` | Tells GitHub Pages to serve every file as-is (no Jekyll processing). |

## How to use it

**Read it locally.** Just open `index.html` in a browser. Everything is embedded, so it works offline
and over `file://` — no download of anything else, no server.

## View it as a rendered web page (GitHub Pages)

Opening `index.html` **on github.com shows its source, not the rendered page** — GitHub does not render
arbitrary HTML files inline. To serve it as a real, shareable web page, turn on **GitHub Pages** (free, no
build step, one-time setup):

1. Commit this folder to a GitHub repository and push it.
2. In the repository, open **Settings → Pages**.
3. Under **Build and deployment → Source**, choose **Deploy from a branch**.
4. Pick the branch you pushed to and the folder **/ (root)**, then **Save**.
5. After a minute the published URL appears at the top of the same page. This snapshot then lives at:
   `https://<your-org>.github.io/<your-repo>/trust-experience-research-snapshot-2026-08-04/` — open it and the page renders directly,
   with nothing to download.

Notes:
- No workflow or GitHub Actions setup is needed for the "Deploy from a branch" option above.
- Want the cleanest possible URL? Put the **contents** of this folder at the repository root instead of the
  dated subfolder; Pages then serves it at `https://<your-org>.github.io/<your-repo>/`.
- The `.nojekyll` file (included) ensures every asset is served untouched.

## What is and is not interactive

This is a **frozen snapshot**, so the live-only features are disabled here and instead point you back to
the platform:

- Browsing and filtering the **gallery of example screens** — live only.
- **Community ratings** and **contributing** patterns — live only.

Selecting any of those in this snapshot opens a small notice with a link to the live page. Everything
else (the thirteen moments, the calibration model, the best practices, the exemplar interfaces, the
prescriptive rules, the findings and the evidence base) is fully present as read-only content, with the
collapsible sections working natively.

To explore the interactive version, or to change anything, open the live page:

- **Research page:** <https://platform.validant.ai/trust-experience#research>
- **Example-screen gallery:** <https://platform.validant.ai/trust-experience>
- **Platform:** <https://validant.ai>

## Snapshot facts (as of 2026-08-04)

- Trust moments: **13** (in five phases)
- Best practices: **20**
- Exemplar interfaces: **29**
- Prescriptive rules: **54**
- Example screens then tagged across moments: **74** (browse them live)

---

Prepared for Glinz & Company / validant / iceberg.digital. The example screenshots shown on the live
gallery are reproduced there under each item's stated licence with attribution; this snapshot carries the
research text and data only. Content may have changed since 2026-08-04; the live page is the source of truth.
