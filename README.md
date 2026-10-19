# Human Trust Experience Task Force

Research, onboarding resources and proposed guidance for human experience design in digital trust.


📖 [Website and existing resources](https://trustoverip.github.io/dtgwg-htx-tf/)

🧑‍💻 [How to contribute](docs/contributing.md)

The new documentation contains the taxonomy analysis, 13 trust moments, 18 proposed pattern families, an authoring template and the completed P18.01 independent-confirmation example. Publication, implementation and evaluation status are separate; this is proposed guidance.

## Editing

Edit Markdown under `docs/`, or use **Edit this page on GitHub** on the website. Submit a pull request and review **Check documentation** before merging. The first lines of each Markdown file control its title, navigation and URL.

## Publishing

Keep the existing GitHub Pages source: **Deploy from a branch → main → / (root)**. Merging into `main` triggers the normal Pages build. The root `_config.yml` loads a pinned Just the Docs theme. Its default layout applies only to the new documentation; the existing standalone HTML files and research snapshot stay at their original paths.

The pull-request workflow only builds and validates. It has no Pages deployment permissions and does not change publishing settings. Existing static files are compared against the pull request's base revision. After a merge, check the Pages deployment and both the new and existing links.

## Sources and scope

The initial documentation adapts *Digital Trust Taxonomy Analysis* and *HDX Pattern Catalogue*, edition 1, 14 October 2026, contributed by Daniel Glinz / validant.ai. See [Sources](docs/references.md) for the research references and their draft status. Existing research and onboarding material is retained.

Repository license: [Apache License 2.0](LICENSE). The remotely loaded [Just the Docs](https://github.com/just-the-docs/just-the-docs) theme retains its own MIT license.
