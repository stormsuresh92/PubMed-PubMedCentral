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
            details = {
            'PMID' : list.find('a', {'class' :'docsum-title'})['data-article-id'],
            'Title' : list.find('a', {'class' :'docsum-title'}).text.strip(),
            'Author' : list.find('span', {'class' :'docsum-authors full-authors'}).text,
            'Citation' : list.find('span', {'class' :'docsum-journal-citation full-journal-citation'}).text,
            'Journal' : list.find('span', {'class' :'docsum-journal-citation short-journal-citation'}).text,
            'Pub Type' : list.find('span', {'class' :'publication-type spaced-citation-item citation-part'}).text}
            pubmedlist.append(details) 
        except:
            pass
 
for x in range(1, 3):
    PubmedPages(x)
    
output = pd.DataFrame(pubmedlist)
output.to_excel('Pubmedresults.xlsx', index=False)
print('file downloaded.')
 