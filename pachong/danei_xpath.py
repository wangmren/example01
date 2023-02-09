import requests
from lxml import etree
from fake_useragent import UserAgent
user_name='tarenacode'
user_password='code_2013'

class CodeSpider(object):
    def __init__(self):
        self.url=' http://code.tarena.com.cn'
        #web 客户端验证传参
        self.auth=(user_name,user_password)
    def save_file(self):
        ua=UserAgent()
        headers={'User-Agent':ua.random}
        html=requests.get(url=self.url,auth=self.auth,headers=headers).text
        print(html)
        p=etree.HTML(html)
        href_list=p.xpath('//a/@href')
        for href in href_list:
            if href.endswith('.zip') or href.endswith('.rar'):
                self.dowload(href)

    def dowload(self,href):
        file_url=self.url+href
        html=requests.get(url=file_url,auth=self.auth).content
        with open(href,'wb') as f:
            f.write(html)
        print(href,'下载成功!')
if __name__ == '__main__':
    spider=CodeSpider()
    spider.save_file()