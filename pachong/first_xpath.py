import requests,time,random,csv
from lxml import etree
from fake_useragent import UserAgent

class LianJiaSpider(object):
    def __init__(self):
        self.url= 'https://bj.lianjia.com/ershoufang/pg{}/'
        self.flag=1


    def get_html(self,url):
        ua=UserAgent()
        headers={'User-Agent':ua.random}

        if self.flag <= 3:
            try:
                res = requests.get(url=url,headers=headers,timeout=5)
                res.encoding='utf-8'
                html=res.text
                self.parse_page(html)
            except Exception as e:
                print(e,self.flag)
                self.flag+=1
                self.get_html(url)

    def parse_page(self,html):

        parse_html=etree.HTML(html)
        xpath_dbs='//ul[@class="sellListContent"]/li[@class="clear LOGVIEWDATA LOGCLICKDATA"]'
        li_list=parse_html.xpath(xpath_dbs)
        item={}
        L=[]
        for li in li_list:
            #名字
            name_list=li.xpath('.//div[@class="positionInfo"]/a[1]/text()')
            #if推导式
            item['name']=name_list[0].strip() if name_list else None
            address_list = li.xpath('.//div[@class="positionInfo"]/a[2]/text()')
            #位置
            item['address']=address_list[0].strip() if address_list else None
            # 房屋信息
            houseInfo_list = li.xpath('.//div[@class="houseInfo"]/text()')
            info_str=houseInfo_list[0].strip() if houseInfo_list else None
            if info_str:
                info_arr=info_str.split('|')
                print(info_arr)
                if len(info_arr)==7:
                    item['model']=info_arr[0].strip()#户型
                    item['area']=info_arr[1].strip()#面积
                    item['direction']=info_arr[2].strip()#朝向
                    item['zhuangxiu']=info_arr[3].strip()#装修
                    item['floor']=info_arr[4].strip()#楼层
                    item['createtime']=info_arr[5].strip()#时间
                    item['floor_type']=info_arr[6].strip()#楼的
                else:
                    item['model'] = item['area'] = item['direction'] = item['zhuangxiu'] = item['floor'] = item[
                        'createtime'] = item['floor_type'] = None
                    # 总价
                total_pice_list = li.xpath('.//div[@class="totalPrice totalPrice2"]/span/text()')
                item['total_pice'] = total_pice_list[0].strip() if total_pice_list else None
                # 单价
                unitPrice_list = li.xpath('.//div[@class="unitPrice"]/span/text()')[0][0:-3]
                item['unitPrice'] = unitPrice_list[0].strip()[0:-3] if unitPrice_list else None
            L.append((item['name'], item['address'], item['model'], item['area'], item['direction'], item['zhuangxiu'],
                      item['floor'], item['createtime'], item['floor_type'], item['total_pice'], item['unitPrice']))
            self.save_data(L)

    def save_data(self,L):
        with open('lianjia.csv','a',newline='',encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerows(L)

    def run(self):
        for pg in range(1,101):
            url=self.url.format(pg)
            self.flag=1
            self.get_html(url)
            time.sleep(random.randint(1,3))

if __name__ == '__main__':
    start=time.time()
    spider=LianJiaSpider()
    spider.run()
    end=time.time()
    print('耗时:%.2f'%(end-start))




