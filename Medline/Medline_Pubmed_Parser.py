from Bio import Medline
import pandas as pd
from tqdm import tqdm


alldata = []
with open('pubmed-activating-set.txt', encoding='ISO 8859-7') as data:
    pmids = Medline.parse(data)
    for pmid in tqdm(pmids):
        try:
            pi = pmid['PMID']
        except:
            pi = ''
        try:
            ab = pmid['AB']
        except:
            ab = ''
        dic = {
            'PMID':pi,
            'abstract':ab
        }
        alldata.append(dic)

df = pd.DataFrame(alldata)
df.to_csv('output.csv', index=False)
print('fin')


input()
