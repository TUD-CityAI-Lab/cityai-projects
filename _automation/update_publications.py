from crossref.restful import Works
from pybliometrics.scopus import ScopusSearch
import pybliometrics
import shutil
import os
import sys

# load from csv file instead
import pandas as pd
from datetime import datetime

# USAGE: python update_publications.py <path_to_scopus_csv>
# Example: python update_publications.py /Users/lion/Downloads/scopus.csv

if len(sys.argv) < 2:
  print('Error: Please provide the path to an exported Scopus CSV file (requires a DOI column).')
  print('Usage: python update_publications.py <path_to_scopus.csv>')
  sys.exit(1)

csv_path = sys.argv[1]
if not os.path.exists(csv_path):
  print(f'Error: CSV file not found at {csv_path}')
  sys.exit(1)

publications_csv = pd.read_csv(csv_path)

# query crossref and collect publication data
publications_data = []
works = Works()

for idx, row in publications_csv.iterrows():
  doi = row['DOI']
  
  if pd.isna(doi):
    print(f'Skipping entry {idx} as DOI is None')
    continue

  print(f'processing: {row["Title"]} \n({doi})')
  
  ref = works.doi(doi)

  if ref is None:
    print('Error: publication could not be retrieved from crossref (skip)!')
    continue

  # extract authors from crossref
  authors = ''
  if 'author' in ref and ref['author']:
    for author in ref['author']:
      authors += author['family'] + ', ' + author['given'][:1] + '.' + ', '
    authors = authors[:-2]
  else:
    authors = 'Author information not available'

  # extract publication date from crossref (prefer published-date)
  pub_date = None
  if 'published-date' in ref and ref['published-date']:
    date_parts = ref['published-date'].get('date-parts', [[]])
    if date_parts and date_parts[0]:
      pub_date = date_parts[0]  # [year, month, day]
  elif 'issued' in ref and ref['issued']:
    date_parts = ref['issued'].get('date-parts', [[]])
    if date_parts and date_parts[0]:
      pub_date = date_parts[0]

  # use year from Scopus or Crossref
  year = str(row['Year']) if pd.notna(row['Year']) else (pub_date[0] if pub_date else 'Unknown')
  
  publications_data.append({
    'doi': doi,
    'title': row['Title'],
    'authors': authors,
    'journal': row['Source title'] if pd.notna(row['Source title']) else 'Unknown',
    'year': year,
    'pub_date': pub_date,
    'date_key': tuple(pub_date) if pub_date else (int(year) if isinstance(year, (int, str)) and str(year).isdigit() else 9999,)
  })

# sort by publication date (year, month, day) in descending order
publications_data.sort(key=lambda x: x['date_key'], reverse=True)

# generate HTML
html = '<!-- AUTO GENERATED FILE, DO NOT EDIT MANUALLY -->\n\n<ul class="publications">'
for pub in publications_data:
  html += f'''
  <li class="publication-list-item">
    <div class="publication-title"><a href="https://doi.org/{pub['doi']}">{pub['title']}</a></div>
    <div>{pub['authors']}</div>
    <div><b class="journal-name">{pub['journal']}</b>, {pub['year']}</div>
  </li>'''

html += '</ul>'

shutil.copy('_automation/_publications.html', 'publications/index.html')

with open('publications/index.html', 'a') as file:
  file.write(html)

print("Done!")