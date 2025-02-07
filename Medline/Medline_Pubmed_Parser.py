from Bio import Medline
import pandas as pd
from tqdm import tqdm

alldata = []
with open('pubmed-activating-set.txt', encoding='ISO 8859-7') as data:
    pmids = Medline.parse(data)
    for pmid in tqdm(pmids):
        dic = {
            'PMID': pmid.get('PMID', ''),
            'abstract': pmid.get('AB', '')
        }
        alldata.append(dic)

df = pd.DataFrame(alldata)
df.to_csv('output.csv', index=False)
