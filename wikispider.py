#wikispider

import requests
from bs4 import BeautifulSoup as soup

class wikispider:
    urls=['https://en.wikipedia.org/wiki/Artificial_intelligence#cite_note-AI_in_2000s-16','https://en.wikipedia.org/wiki/Big_data','https://en.wikipedia.org/wiki/Data_analysis']

    def download(self,url):
        print("Start downloading page")
        return requests.get(url).text

    def parse_paragraph(self,content,parser='html.parser'):
        html=soup(content,parser)
        results=html.find_all('p')
        return [result.text for result in results]

    def savefile(self,data):
        with open('wikiscrape.txt','a+') as file:
            for d in data:
                file.write(d)

    def main(self,url):
        content=wikispider.download(self,url)
        para=self.parse_paragraph(content)
        self.savefile(para)
        print("FILE SAVED")


if __name__=="__main__":
    spider=wikispider()
    if isinstance(spider.urls, list):
        for url in spider.urls:
            spider.main(url)
    elif isinstance(spider.urls, str):
        spider.main(url)
