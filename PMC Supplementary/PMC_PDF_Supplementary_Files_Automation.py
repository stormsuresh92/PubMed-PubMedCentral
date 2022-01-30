from requests_html import HTMLSession
import os
import time
import logging
from tqdm import tqdm
import requests
from requests.exceptions import ConnectionError


s = HTMLSession()


headers = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.71 Safari/537.36',
    'referer': 'https://pubmed.ncbi.nlm.nih.gov/',
    'connection':'keep-alive',
    'Keep-Alive':'timeout=60'
}

logging.basicConfig(filename='logfile.log', level=logging.DEBUG, 
                    format='%(asctime)s-%(message)s', datefmt='%d-%b-%y %H-%M-%S')

print('Supplementary files downloading...')    
file = open('Input.txt', 'r')
urls = file.readlines()

for url in tqdm(urls):
    fname = url.strip()
    cur_dir = os.getcwd()
    out = cur_dir + f'/{fname}'
    if not os.path.exists(out):
        os.mkdir(out)

    baseurl = 'https://www.ncbi.nlm.nih.gov/labs/pmc/articles/'
    r = s.get(baseurl+url.strip(), headers=headers, timeout=10)
    try:
        suppls = r.html.find('#data-suppmats')
        for item in suppls:
            atag = item.find('div.half_rhythm a')
            for tag in atag:
                try:
                    files = 'https://www.ncbi.nlm.nih.gov' + tag.attrs['href']
                    r = s.get(files.strip(), timeout=10, stream=True)
                    if r.status_code == 200:
                        name = os.path.basename(files)
                        with open(out + '/' + name, 'wb') as f:
                            for chunk in r.iter_content(chunk_size=1024):
                                if chunk:
                                    f.write(chunk)

                    output = open('Supplementary files.tsv', 'a')
                    output.write(url.strip()+'\t'+files+'\n')
                except:
                    output = open('No Supplementary files.tsv', 'a')
                    output.write(url.strip()+'\n')
  
                    
    except requests.exceptions.RequestException as e:  
        output = open('Connection_Error_IDS.txt', 'a')
        output.write(url.strip() + '\n')
    except:
        pass

    time.sleep(30)

print('Files Completed')
input()

