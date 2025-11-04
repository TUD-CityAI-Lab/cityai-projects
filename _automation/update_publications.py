from crossref.restful import Works
from pybliometrics.scopus import ScopusSearch
import pybliometrics
import shutil
import os

if os.path.exists("/home/runner"):
  pybliometrics.scopus.init(config_dir="/home/runner/.config/pybliometrics.cfg")
else:
  print("Skipping pybliometrics.scopus.init() as not in CI environment")

print('query scopus...')

publications = ScopusSearch('''
PUBYEAR > 2019 
AND (
  AU-ID("van Cranenburgh, Sander" 55342333800)OR
  AU-ID("Kroesen, Maarten" 24344046200) OR
  AU-ID("Calvert, Simeon C." 36695851100) OR
  AU-ID("Cats, Oded" 35751118200) OR
  AU-ID("Garrido-Valenzuela, Francisco" 57568162000) OR
  AU-ID("Spierenburg, Lucas" 58288387600) OR
  AU-ID("Jiao, Yiru" 57196345277) OR
  AU-ID("Smeele, Nicholas V.R." 57694437300)
) 
AND (
  FIRSTAUTH("van Cranenburgh") OR
  FIRSTAUTH("Kroesen") OR
  FIRSTAUTH("Calvert") OR
  FIRSTAUTH("Cats") OR
  FIRSTAUTH("Garrido-Valenzuela") OR
  FIRSTAUTH("Spierenburg") OR
  FIRSTAUTH("Jiao") OR
  FIRSTAUTH("Smeele") OR
  FIRSTAUTH("Cassens") OR
  FIRSTAUTH("Nova")
)
''', subscriber=False, refresh=True).results

print(f'{len(publications)} publications received from scopus')

# sort publications by date
documents = sorted(publications, key=lambda x: x.coverDate, reverse=True)

# generate HTML and query author names from crossref
html = '<!-- AUTO GENERATED FILE, DO NOT EDIT MANUALLY -->\n\n<ul class="publications">'
for publication in publications:
  print(f'processing: {publication.title} \n({publication.doi})')
  
  if publication.doi is None:
    print('Skipping entry as DOI is None')
    continue

  works = Works()
  ref = works.doi(publication.doi)

  authors = ''
  if ref is None:
    print('Error: authors could not be retrieved from crossref (skip)!')
    continue

  for author in ref['author']:
    authors += author['family'] + ', ' + author['given'][:1] + '.' + ', '
  authors = authors[:-2]

  html += f'''
  <li class="publication-list-item">
    <div class="publication-title"><a href="https://doi.org/{publication.doi}">{publication.title}</a></div>
    <div>{authors}</div>
    <div><b class="journal-name">{publication.publicationName}</b>, {publication.coverDate[:4]}</div>
  </li>'''

html += '</ul>'

shutil.copy('_automation/_publications.html', 'publications/index.html')

file = open('publications/index.html', 'a') 
file.write(html)
file.close()

print("Done!")