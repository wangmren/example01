from lxml import html

import requests


etree = html.etree

class Tieba(object):
    def __init__(self, name):
        self.url = "https://tieba.baidu.com/f?ie=utf-8&kw={}".format(name)
        self.headers = {
            "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36 Edg/106.0.1370.37"
        }

    def get_data(self, url):
        response = requests.get(url, headers=self.headers)
        with open("temp.html", "wb") as f:
            f.write(response.content)
        return response.content

    def parse_data(self, data):
        data = data.decode().replace("<!--", "").replace("-->", "")
        html = etree.HTML(data)
        el_list = html.xpath('//li[@class=" j_thread_list clearfix thread_item_box"]/div/div[2]/div[1]/div[1]/a')
        data_list = []
        for el in el_list:
            temp={}
            temp['title'] = el.xpath("./text()")[0]
            temp['link'] = 'http://tieba.baidu.com'+el.xpath("./@href")[0]
            data_list.append(temp)

        try:
            next_url = 'https:' + html.xpath('//a[contains(text(),"下一页>")]/@href')[0]
        except:
            next_url = None

        return data_list, next_url

    def save_data(self, data_list):
        for data in data_list:
            print(data)



    def run(self):
        next_url= self.url
        while True:
            data = self.get_data(next_url)
            data_list, next_url = self.parse_data(data)
            self.save_data(data_list)
            print(next_url)
            if next_url == None:
                break

if __name__ == '__main__':
    tieba = Tieba("轮回乐园")
    tieba.run()