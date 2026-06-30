# Website TODO & ideas

Working list for matthiashofer.net (repo: rmhofer/rmhofer.github.io).

## Open — needs Matthias
- [ ] **Full dissertation PDF** — drop it at `assets/papers/dissertation.pdf`; the "book" icon in the News item 404s until then.
- [ ] **Review the Research section** "Computational and Bayesian models of cognition" — draft text in Claude's words; edit/rename to taste.
- [ ] **Check category dots** — eyeball the colored markers against the legend; correct any in `_data/papers.yml` (`tags:`).
- [ ] **Ping Claude to enable "Enforce HTTPS"** once GitHub finishes provisioning the cert (~15–60 min after DNS went live).
- [ ] **Dark palette feedback** — toggle the moon icon and tell Claude if you want it warmer/cooler/higher-contrast.
- [ ] **Code / Demos menu item?** — decide name (Code, Demos, or "Code & Demos") and gather links to share.

## Open — Claude can do
- [ ] Enable "Enforce HTTPS" for matthiashofer.net (after cert is issued).
- [ ] Scaffold a "Code & Demos" section/nav item (data-driven, like Papers) once content is decided.
- [ ] When a full Zotero `.bib` is exported (area keys in each entry's `keywords`), switch publications to the `make_bib.py` workflow and retire hand-edited `papers.yml`.

## Ideas / future
- Academic ↔ artistic **landing split**: one domain, a minimal root page branching to academic vs. art, each with its own look.
- CV link or dedicated CV page.
- Talks / teaching section.
- Extra per-paper links (code, slides, video, BibTeX) as additional little glyphs.
- More social links if wanted (Semantic Scholar, Bluesky).
- Custom email forwarding (you@matthiashofer.net → inbox) — Porkbun MX/SPF already in place.

## Recently done
- Custom domain **matthiashofer.net** (CNAME + DNS A/CNAME records); rmhofer.github.io kept (auto-redirects).
- **Dark mode + font-set toggle** in the footer; default is **light**, fonts default to **Space Grotesk + Source Sans 3** (toggle → Montserrat + Lato).
- Subtle "updated <month year>" in footer.
- Removed email from bio (kept obfuscated email in sidebar).
- New 2026 profile photo (360×360, full-res not published).
- Real social links (Scholar, ORCID, GitHub, obfuscated email); fixed icon stylesheet.
- SEO/Open Graph meta, favicon, page title.
- Four 2025 papers added; per-link PDF/external glyphs.
- Research-area color markers + legend; research sections tinted to match (3px border); 3rd research section added.
- Responsive layout fix (flex + sticky sidebar).
- News updates (CogSci 2025, Cosyne 2026) + dissertation/précis icons.
- Repo cleanup: removed leftover scaffold & tracked build output; added `.gitignore`.
- Modernized `make_bib.py` (BibTeX → `papers.yml`).
- `fonts-preview.html` kept in repo but unpublished.
