from requests_html import HTMLSession
from tqdm import tqdm

s = HTMLSession()

url = 'https://pubmed.ncbi.nlm.nih.gov/'
file = open('input.txt', 'r')
pmids = file.readlines()
for pmid in tqdm(pmids):
    r = s.get(url + pmid.strip())
    con = r.html.find('#full-view-heading')
    for item in con:
        author = item.find('.authors-list', first=True).text.replace('\xa0', '')
        Affiliation = item.find('ul.item-list', first=True).text.replace('.\n', '|')
        file = open('out.tsv', 'a', encoding = 'utf-8')
        file.write(pmid.strip() + '\t'+ author + '\t'+ Affiliation + '\n')
        file.close()
