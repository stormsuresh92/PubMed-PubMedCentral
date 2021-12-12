import requests
from bs4 import BeautifulSoup
import pandas as pd


headers = {'user-agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36'}

pubmedlist = []

def PubmedPages(pages):
    url = f'https://pubmed.ncbi.nlm.nih.gov/?term=egfr%5Bti%5D&page={x}'
    r = requests.get(url, headers=headers)
    soup = BeautifulSoup(r.text, 'html.parser')
    articles = soup.find_all('article', {'class': 'full-docsum'})
    for list in articles:
        try:
            PMID = list.find('a', {'class' :'docsum-title'})['data-article-id']
        except:
            pass
        try:
            Title = list.find('a', {'class' :'docsum-title'}).text.strip()
        except:
            pass
        try:
            Author = list.find('span', {'class' :'docsum-authors full-authors'}).text
        except:
            pass
        try:
            Citation = list.find('span', {'class' :'docsum-journal-citation full-journal-citation'}).text
        except:
            pass
        try:
            Journal = list.find('span', {'class' :'docsum-journal-citation short-journal-citation'}).text
        except:
            pass
        

            details = {
            'PMID' : PMID,
            'Title' : Title,
            'Author' : Authors,
            'Citation' : Citations,
            'Journal' : Journal
            }
            pubmedlist.append(details)
 
for x in range(1, 3):
    PubmedPages(x)
    
output = pd.DataFrame(pubmedlist)
output.to_excel('Pubmedresults.xlsx', index=False)
print('file downloaded.')
 
