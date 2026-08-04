# Human Trust Experience — full snapshot (explorer + research)

> **Snapshot date: 4 August 2026 at 17:51**
> Live version: <https://platform.validant.ai/trust-experience>

A **self-contained, static snapshot of the whole validant Human Trust Experience**, ready to drop into a GitHub
repository and serve with GitHub Pages. No server, no build step.

## Pages
- **`index.html`** — the **explorer**: a gallery of all 74 best-practice screens, screenshots
  bundled. Client-side search and filter by trust moment and origin; click any screen for its detail.
- **`research.html`** — the **research findings**: the thirteen-moment journey model, calibration, best
  practices, exemplars, prescriptive rules and evidence.
- The two pages share a top navigation bar.

## What is inside
| Path | Purpose |
|------|---------|
| `index.html` | Explorer (gallery). The main page. |
| `research.html` | Research findings. |
| `images/` | All 74 bundled screenshots. |
| `data/patterns.json` | Screen metadata (title, origin, moment, licence, attribution, image path). |
| `data/research.json` | The structured research data. |
| `snapshot.json` | Machine-readable metadata. |
| `.nojekyll` | Tells GitHub Pages to serve every file as-is. |

## View it as a web page (GitHub Pages)
1. Commit this folder to a GitHub repository and push it.
2. In the repo, open **Settings → Pages**.
3. Under **Build and deployment → Source**, choose **Deploy from a branch**.
4. Pick your branch and folder **/ (root)**, then **Save**.
5. After ~1 minute the URL appears; `index.html` (the explorer) is the home page:
   `https://<your-org>.github.io/<your-repo>/trust-experience-snapshot-2026-08-04/` — or the repo root if you put the contents there.

Locally, just open `index.html` in a browser — it works offline.

## Live-only
Community **ratings**, **contributing** a screen and **removing** screens happen on the live platform; in this
snapshot those controls open a notice linking back to <https://platform.validant.ai/trust-experience>.

---
Prepared for Glinz & Company / validant / iceberg.digital. Screenshots are reproduced under each item's stated
licence with attribution; content may have changed since 2026-08-04.
