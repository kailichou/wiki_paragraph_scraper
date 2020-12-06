#wikispider

import requests
from bs4 import BeautifulSoup as soup

class wikispider:
    url='https://en.wikipedia.org/wiki/Data_analysis'

    def download(self):
        if isinstance(self,str):
            print("Start downloading page")
            return requests.get(self).text
        
        else:
            pass

    def parse_paragraph(self,content,parser='html.parser'):
        html=soup(content,parser)
        results=html.find_all('p')
        return [result.text for result in results]

    def savefile(self,data):
        with open('wikiscrape.txt','w') as file:
            for d in data:
                file.write(d)

    def main(self):
        content=wikispider.download(self.url)
        para=self.parse_paragraph(content)
        self.savefile(para)
        print("FILE SAVED")



if __name__=="__main__":
    spider=wikispider()
    spider.main()
