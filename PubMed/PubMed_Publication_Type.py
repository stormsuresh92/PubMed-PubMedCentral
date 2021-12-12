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
        try:
            pubtype = item.find('.publication-type', first=True).text
        except:
            pubtype = ''
        file = open('Pubtypes.tsv', 'a', encoding = 'utf-8')
        file.write(pmid.strip() + '\t'+ pubtype + '\n')
        file.close()
