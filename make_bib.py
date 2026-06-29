#!/usr/bin/env python3
"""Generate _data/papers.yml from a BibTeX file (e.g. exported from Zotero).

Usage:
    python make_bib.py                      # reads publications.bib -> _data/papers.yml
    python make_bib.py my.bib _data/papers.yml

Notes
-----
* Author names are rendered Scholar-style: initials + last name, e.g.
  "Roger Philip Levy" -> "RP Levy", "Matthias Hofer" -> "M Hofer".
  (The site bolds "M Hofer" via JS, so keep that exact spelling for yourself.)
* The PDF/landing link is taken from `url`, else built from `doi`, else from
  an `eprint`/arXiv id. Direct-PDF vs. landing-page icons are chosen in the
  template based on the URL, so no extra fields are needed here.
* Research-area markers: put space-separated area keys in the BibTeX
  `keywords` field (matching the `key`s in _data/areas.yml), e.g.
      keywords = {evolution, communication}
  and they become the paper's `tags:` list.
* Entries with `year = {unpublished}` or no year sort to the top.
"""

import re
import sys

import bibtexparser
import yaml


def parse_bibtex(path):
    with open(path) as f:
        parser = bibtexparser.bparser.BibTexParser(common_strings=True)
        return bibtexparser.load(f, parser=parser).entries


def clean(text):
    """Strip BibTeX braces and collapse whitespace."""
    text = text.replace("{", "").replace("}", "")
    return re.sub(r"\s+", " ", text).strip()


def format_authors(raw):
    """'Last, First and Last, First' -> 'FI Last, FI Last' (initials + last)."""
    names = []
    for person in raw.split(" and "):
        person = person.strip()
        if not person:
            continue
        if "," in person:
            last, given = [p.strip() for p in person.split(",", 1)]
        else:
            parts = person.split()
            last, given = parts[-1], " ".join(parts[:-1])
        initials = "".join(w[0].upper() for w in given.split() if w)
        names.append(f"{initials} {last}".strip())
    return ", ".join(names)


def pick_link(entry):
    if entry.get("url"):
        return clean(entry["url"])
    if entry.get("doi"):
        return "https://doi.org/" + clean(entry["doi"])
    eprint = entry.get("eprint") or entry.get("arxiv")
    if eprint:
        return "https://arxiv.org/pdf/" + clean(eprint)
    return None


def build_venue(entry):
    venue = entry.get("journal") or entry.get("booktitle") or entry.get("publisher")
    if not venue and entry.get("eprint"):
        return f"arXiv preprint arXiv:{clean(entry['eprint'])}"
    venue = clean(venue) if venue else "Publication unknown"
    if entry.get("volume"):
        venue += f", {clean(entry['volume'])}"
    if entry.get("pages"):
        venue += f", {clean(entry['pages'])}"
    return venue


def to_paper(entry):
    paper = {
        "title": clean(entry.get("title", "No title")),
        "authors": format_authors(entry.get("author", "")),
        "year": clean(entry.get("year", "")),
        "details": build_venue(entry),
    }
    link = pick_link(entry)
    if link:
        paper["link"] = link
    if entry.get("keywords"):
        tags = [t.strip() for t in re.split(r"[;,]", entry["keywords"]) if t.strip()]
        if tags:
            paper["tags"] = tags
    return paper


def year_key(paper):
    try:
        return int(paper["year"])
    except (ValueError, KeyError):
        return 9999  # unpublished / undated sort to the top


def main():
    src = sys.argv[1] if len(sys.argv) > 1 else "publications.bib"
    dst = sys.argv[2] if len(sys.argv) > 2 else "_data/papers.yml"

    papers = [to_paper(e) for e in parse_bibtex(src)]
    papers.sort(key=year_key, reverse=True)

    with open(dst, "w") as f:
        yaml.dump(papers, f, sort_keys=False, allow_unicode=True, width=1000)
    print(f"Wrote {len(papers)} papers to {dst}")


if __name__ == "__main__":
    main()
