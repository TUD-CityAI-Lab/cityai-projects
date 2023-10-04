import os.path
import sys

if os.path.isfile('~/.config/pybliometics.cfg') == False:
  file = open('~/.config/pybliometics.cfg', 'w') 
  file.write(f'''[Directories]
  AbstractRetrieval = PPP/.pybliometrics/Scopus/abstract_retrieval
  AffiliationSearch = PPP/.pybliometrics/Scopus/affiliation_search
  AuthorRetrieval = PPP/.pybliometrics/Scopus/author_retrieval
  AuthorSearch = PPP/.pybliometrics/Scopus/author_search
  CitationOverview = PPP/.pybliometrics/Scopus/citation_overview
  AffiliationRetrieval = PPP/.pybliometrics/Scopus/affiliation_retrieval
  ScopusSearch = PPP/.pybliometrics/Scopus/scopus_search
  SerialTitle = PPP/.pybliometrics/Scopus/serial_title

  [Authentication]
  APIKey = {sys.argv[1]}

  [Requests]
  Timeout = 20
  Retries = 5''')
  file.close()

from pybliometrics.scopus import AuthorRetrieval
import shutil

authors = [
  55342333800, # Sander
  24344046200, # Maarten
  36695851100, # Simeon
  35751118200, # Oded
  57568162000, # Francisco
  58288387600, # Lucas
  57196345277, # Yiru
  57694437300, # Nicholas
]

documents = []

for author_id in authors:
  author = AuthorRetrieval(author_id)
  author_docs = author.get_documents()
  documents.extend(author_docs)

# remove duplicates
documents = list(set(documents))
len(documents)

# filter and sort by date
documents = list(filter(lambda x: x.coverDate > '2020-01-01', documents))
documents = sorted(documents, key=lambda x: x.coverDate, reverse=True)

html = '<!-- AUTO GENERATED FILE, DO NOT EDIT MANUALLY -->\n\n<ul class="publications">'

for doc in documents:
  html += f'''
  <li class="publication-list-item">
    <div class="publication-title"><a href="https://doi.org/{doc.doi}">{doc.title}</a></div>
    <div>{doc.author_names.replace(';', ', ')}</div>
    <div><b class="journal-name">{doc.publicationName}</b>, {doc.coverDate[:4]}</div>
  </li>'''

html += '</ul>'

shutil.copy('_automation/_publications.html', 'publications.html')

file = open('publications.html', 'a') 
file.write(html)
file.close()