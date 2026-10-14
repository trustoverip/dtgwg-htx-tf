---
layout: default
title: Contribute
nav_order: 6
permalink: /docs/contributing/
---

# Contribute

Help improve the wording, evidence or interaction guidance. A GitHub account is needed to propose an edit.

## Edit an existing page

1. Select **Edit this page on GitHub** at the bottom of the page.
2. Edit the Markdown text. Keep the settings between the first two `---` lines unless you intend to change the title or navigation.
3. Use **Preview** to check headings, tables and links.
4. Choose **Commit changes**, create a branch for your proposal and open a pull request. If you do not have write access, GitHub guides you through a fork.
5. Explain what changed and why. A maintainer reviews the proposal and merges it when ready. The published website then updates automatically.

For a question or suggestion without an edit, [open an issue](https://github.com/trustoverip/dtgwg-htx-tf/issues).

## Add a pattern

Start with the [pattern template]({{ '/docs/pattern-template/' | relative_url }}) and [blank Markdown starter]({{ '/docs/pattern-starter.txt' | relative_url }}). Create a file in `docs/patterns/`, choose an unused child ID such as `P06.01`, and add a link from the catalogue. Use `parent: HDX pattern catalogue` to place the page in navigation.

Each entry needs one coherent problem and solution, material states, evidence requirements, accessible alternatives and an evaluation plan. Keep **publication**, **implementation** and **evaluation** status separate. A merged contribution remains proposed unless a documented endorsement decision says otherwise.

## Review an entry

- Is its context and reusable solution distinct from existing entries?
- Do wording, visual indicators and available actions match the evidence and service capabilities?
- Can people refuse, pause and recover? Are accessible alternatives defined?
- Are source versions, ownership, open decisions and evaluation findings explicit?

See [Develop the catalogue]({{ '/docs/patterns/development/' | relative_url }}) for the work queue and review process.

## For maintainers

Keep **Settings → Pages → Deploy from a branch → main → / (root)**. The root `_config.yml` loads the documentation theme; `docs/` contains the maintained content. Existing HTML resources retain their original filenames and locations.

The **Check documentation** workflow builds pull requests and checks internal documentation links and preservation of existing static files. It does not deploy. Inspect its result before merging. After merging, check the normal **pages build and deployment** run, the documentation homepage, and the existing onboarding and research pages.

Use the browser editor for routine content changes. A theme or build change needs a build check and a review of existing resource links. Keep the theme pinned to a reviewed version. If a rollout fails, revert the introducing merge and let the existing Pages build run again.

## Provenance

The initial Markdown pages adapt *Digital Trust Taxonomy Analysis* and *HDX Pattern Catalogue*, edition 1, 14 October 2026, prepared for validant.ai. The split improves navigation; the definitions, 13 moment IDs, 18 family IDs and worked pattern retain their original status. Source notes are collected on the [Sources]({{ '/docs/references/' | relative_url }}) page.
