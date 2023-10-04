import sys
import os

if not os.path.exists('/home/runner/.config/'):
    os.makedirs('/home/runner/.config/')

if not os.path.isfile('/home/runner/.config/pybliometrics.cfg'):
  file = open('/home/runner/.config/pybliometrics.cfg', 'w') 
  file.write(f'''[Directories]
AbstractRetrieval = /home/runner/.cache/pybliometrics/Scopus/abstract_retrieval
AffiliationRetrieval = /home/runner/.cache/pybliometrics/Scopus/affiliation_retrieval
AffiliationSearch = /home/runner/.cache/pybliometrics/Scopus/affiliation_search
AuthorRetrieval = /home/runner/.cache/pybliometrics/Scopus/author_retrieval
AuthorSearch = /home/runner/.cache/pybliometrics/Scopus/author_search
CitationOverview = /home/runner/.cache/pybliometrics/Scopus/citation_overview
ScopusSearch = /home/runner/.cache/pybliometrics/Scopus/scopus_search
SerialSearch = /home/runner/.cache/pybliometrics/Scopus/serial_search
SerialTitle = /home/runner/.cache/pybliometrics/Scopus/serial_title
PlumXMetrics = /home/runner/.cache/pybliometrics/Scopus/plumx
SubjectClassifications = /home/runner/.cache/pybliometrics/Scopus/subject_classification

[Authentication]
APIKey = 52a3dd44114b12b72933c41192a060d3

[Requests]
Timeout = 20
Retries = 5''')
  file.close()

with open('/home/runner/.config/pybliometrics.cfg', 'r') as f:
    print(f.read())

print('DONE PREPARE')