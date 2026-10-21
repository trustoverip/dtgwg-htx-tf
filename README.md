<p align="center">
  <a href="https://trustoverip.github.io/dtgwg-htx-tf/">
    <img src="images/HTX_v0.1.svg" alt="HTX Human Trust Experience Task Force logo" width="360">
  </a>
</p>

<h1 align="center">Human Trust Experience Task Force</h1>

<p align="center">
  Research, onboarding resources and proposed guidance for human experience design in digital trust.
</p>

<p align="center">
  <a href="https://trustoverip.github.io/dtgwg-htx-tf/"><strong>Website</strong></a> ·
  <a href="https://trustoverip.github.io/dtgwg-htx-tf/docs/">Taxonomy</a> ·
  <a href="https://trustoverip.github.io/dtgwg-htx-tf/docs/patterns/">Pattern Catalog</a> ·
  <a href="docs/contributing.md">Contributing</a> ·
  <a href="docs/references.md">Sources</a>
</p>

---

## Mission

Digital trust systems such as wallets, credentials and verifiable trust agents are usually designed from the protocol up. The people who use them experience something different: a series of moments in which they decide whether to share, accept, confirm or walk away.

The Human Trust Experience (HTX) Task Force works on that human side. Our mission is to give designers, engineers, researchers and standards bodies a **shared language**, **evidence-based patterns** and **practical guidance**, so that digital trust systems are understandable, respect people's agency and earn trust rather than assume it.

## What the task force does

- **Defines a shared vocabulary.** Teams use *trust moments*, *trust tasks*, *trust ceremonies* and *trust patterns* in overlapping ways. We define these terms and how they relate.
- **Catalogs trust patterns.** We map the interactions where trust is tested, established or restored, and describe proven ways to design them.
- **Collects real-world evidence.** We gather and annotate examples of good trust UX, so the patterns are concrete and can be cited.
- **Turns patterns into guidance.** We translate the patterns into reusable designs and requirements, including the human-facing side of disclosure decisions.
- **Explains the work.** We produce short learning material that makes trust concepts accessible beyond the task force.

## Deliverables

| ID | Deliverable | Status |
|----|-------------|--------|
| D1 | [Shared HTX Taxonomy](https://trustoverip.github.io/dtgwg-htx-tf/docs/): glossary and conceptual hierarchy | Published, proposed guidance |
| D2 | [HTX Pattern Catalog](https://trustoverip.github.io/dtgwg-htx-tf/docs/patterns/): visual library and pattern inventory | Published, proposed guidance |
| D2.1 | HTX Best Practices Repository: open gallery of annotated real-world UX screens | Live; content validation in progress |
| D3 | HTX Design Blueprints: UX designs per trust pattern | Output format to be defined |
| D4 | TADAL (Trust-Aware Disclosure and Agency Layer): decision layer of the Verifiable Trust Agent | Concept paper |
| D5 | [Trustlets](https://platform.validant.ai/trust-experience#trustlets): short videos, one trust concept each | Sample scripts |
| D6 | Values Assessment & Benefits Promotion Toolkit, with the Risks/Harms Task Force | Proposed |

## What's in this repository

The documentation under [`docs/`](docs/) currently contains:

- the **taxonomy analysis**
- the **13 trust moments**
- **18 proposed pattern families**
- a **pattern authoring template**
- a completed example: **P18.01 Independent confirmation**

> [!NOTE]
> All content is **proposed guidance**. Publication, implementation and evaluation status are tracked separately. Publishing a pattern does not mean it has been implemented or evaluated.

Existing research and onboarding material is kept at its original location.

## Contributing

Contributions are welcome. Please read the [contribution guide](docs/contributing.md) first.

1. Edit the Markdown files under `docs/`, or use **Edit this page on GitHub** on the website.
2. Open a pull request.
3. Wait for the **Check documentation** workflow to pass, and review its results before merging.

The first lines of each Markdown file set its page title, its place in the navigation and its URL.

## Publishing

The site is published with GitHub Pages.

| Setting | Value |
|---------|-------|
| Source | Deploy from a branch |
| Branch | `main` |
| Folder | `/ (root)` |
| Theme | [Just the Docs](https://github.com/just-the-docs/just-the-docs), pinned in the root `_config.yml` |

- **Merging into `main`** triggers the normal Pages build.
- **The theme layout** applies only to the new documentation. Existing standalone HTML files and the research snapshot stay at their original paths.
- **The pull-request workflow** only builds and validates. It has no Pages deployment permissions and does not change publishing settings. It compares existing static files against the pull request's base revision.

After each merge, check that the Pages deployment succeeded and that both the new and the existing links still work.

## Sources

The initial documentation adapts *Digital Trust Taxonomy Analysis* and *HDX Pattern Catalogue*, edition 1 (14 October 2026), contributed by Daniel Glinz / validant.ai. See [Sources](docs/references.md) for all research references and their draft status.

## License

This repository is licensed under the [Apache License 2.0](LICENSE). The remotely loaded [Just the Docs](https://github.com/just-the-docs/just-the-docs) theme keeps its own MIT license.
