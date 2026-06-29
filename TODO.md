# Website TODO & ideas

Working list for rmhofer.github.io. Check things off as we go.

## Open — needs Matthias
- [ ] **Pick site fonts** — see https://rmhofer.github.io/fonts-preview.html (dropdowns for display + body font). Tell Claude the combo to apply.
- [ ] **Full dissertation PDF** — drop it at `assets/papers/dissertation.pdf`; the "book" icon in the News item 404s until then.
- [ ] **Review the new Research section** "Computational and Bayesian models of cognition" — draft text, edit to taste (or rename, e.g. "hierarchical models").
- [ ] **Check category dots** — eyeball the colored markers against the legend; correct any in `_data/papers.yml` (`tags:`).
- [ ] **Domain decision** — buy `matthiashofer.net` (or alternative)? If yes, Claude adds `CNAME` + gives DNS records.

## Open — Claude can do
- [ ] Apply chosen fonts site-wide; then **delete `fonts-preview.html`**.
- [ ] When a full Zotero `.bib` is exported (with area keys in each entry's `keywords`), switch publications to the `make_bib.py` workflow and retire hand-edited `papers.yml`.

## Ideas / future
- Academic ↔ artistic **landing split**: one domain, a minimal root page branching to `/academic` and `/art`, each with its own look.
- CV link or dedicated CV page.
- Talks / teaching section.
- Extra per-paper links (code, slides, video, BibTeX) as additional little glyphs.
- More social links if wanted (Semantic Scholar, Bluesky).
- Optional dark mode.

## Recently done
- New 2026 profile photo (downscaled 360×360, full-res not published).
- Real social links (Scholar, ORCID, GitHub, obfuscated email); fixed icon stylesheet.
- SEO/Open Graph meta, favicon, page title.
- Added four 2025 papers; per-link PDF/external glyphs.
- Research-area color markers + legend; research sections tinted to match.
- Responsive layout fix (flex + sticky sidebar; max width 880px).
- News updates (CogSci 2025, Cosyne 2026) + dissertation/précis icons.
- Repo cleanup: removed leftover scaffold & tracked build output; added `.gitignore`.
- Modernized `make_bib.py` (BibTeX → `papers.yml`).
