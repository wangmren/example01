html="""
<div class="wrapper">
<a href="/" id="channel">新浪社会</a>
<ul id="nav">
<li><a href="http://domestic.sina.com/" title="国内">国内</a></li>
<li><a href="http://world.sina.com/" title="国际">国际</a></li>
<li><a href="http://mil.sina.com/" title="军事">军事</a></li>
<li><a href="http://photo.sina.com/" title="图片">图片</a></li>
<li><a href="http://society.sina.com/" title="社会">社会</a></li>
<li><a href="http://ent.sina.com/" title="娱乐">娱乐</a></li>
<li><a href="http://tech.sina.com/" title="科技">科技</a></li>
<li><a href="http://sports.sina.com/" title="体育">体育</a></li>
<li><a href="http://finance.sina.com/" title="财经">财经</a></li>
<li><a href="http://auto.sina.com/" title="汽车">汽车</a></li>
</ul>
</div>
"""
from lxml import etree
#获取xpath对象
parse_html=etree.HTML(html)
# 1.获取所有栏目信息
xpath_dbs='//a/text()'
r_list=parse_html.xpath(xpath_dbs)
print(r_list)
# 2.获取所有a节点 href 的属性值
xpath_dbs='//a/@href'
r_list=parse_html.xpath(xpath_dbs)
print(r_list)
# 3.获取所有a节点 href 的属性值,但是不包含 /
xpath_dbs='//li/a/@href'
r_list=parse_html.xpath(xpath_dbs)
print(r_list)
# 4.获取 国际、国内、军事...,但是不包含 新浪社会
xpath_dbs='//li/a/text()'
r_list=parse_html.xpath(xpath_dbs)
print(r_list)
#用循环
xpath_dbs='//ul[@id="nav"]/li'
r_list=parse_html.xpath(xpath_dbs)
for item in r_list:
    name=item.xpath('./a/text()')
    print(name)


