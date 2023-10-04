import sys
import os

if not os.path.exists('~/.config/'):
    os.makedirs('~/.config/')

if not os.path.isfile('~/.config/pybliometics.cfg'):
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