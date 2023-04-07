import requests
from bs4 import BeautifulSoup
import lxml

headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:78.0) Gecko/20100101 Firefox/78.0"}

urls=['https://search.open.canada.ca/en/ct/?sort=contract_date_s%20desc&page=1&search_text=&ct-search-agreement=Aboriginal%20Business%20Set%20Aside%20%E2%80%93%20Procurement%20Strategy%20for%20Aboriginal%20Business%20(ABSA%20(PSAB))','https://search.open.canada.ca/en/ct/?sort=contract_date_s%20desc&page=2&search_text=&ct-search-agreement=Aboriginal%20Business%20Set%20Aside%20%E2%80%93%20Procurement%20Strategy%20for%20Aboriginal%20Business%20(ABSA%20(PSAB))']

def f():
    myFile=open('contracts.txt',"w")
    for url in urls:
        r=requests.get(url, headers=headers)
        try:
            soup=BeautifulSoup(r.text,'lxml')
            myFile.write(soup.text)
        except UnicodeEncodeError:
            print("unable to encode")
    myFile.close()


if __name__=="__main__":
	f()
