import bibtexparser
import yaml

def parse_bibtex(file_path):
    with open(file_path) as bibtex_file:
        parser = bibtexparser.bparser.BibTexParser(common_strings=True)
        bib_database = bibtexparser.load(bibtex_file, parser=parser)
    return bib_database.entries

def format_as_yaml(entries):
    papers = []
    for entry in entries:
        # Remove {{ and }} from the title
        title = entry.get('title', 'No Title Available').replace('{{', '').replace('}}', '')

        paper = {
            'title': title,
            'authors': entry.get('author', 'Authors Unknown').replace(" and ", ", "),
            'year': entry.get('year', 'Year Unknown'),
            'details': entry.get('journal', entry.get('booktitle', 'Publication Unknown'))
        }
        if 'pages' in entry:
            paper['details'] += f", pp. {entry['pages']}"
        papers.append(paper)
    return papers


# Path to your BibTeX file
bibtex_file_path = 'publications.bib'

# Parse the BibTeX file
entries = parse_bibtex(bibtex_file_path)

# Format entries as YAML
yaml_content = format_as_yaml(entries)

# Save to a YAML file
with open('_data/papers.yml', 'w') as file:
    yaml.dump(yaml_content, file, sort_keys=False)
