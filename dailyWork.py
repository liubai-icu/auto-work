import json
from urllib import request as rq

import sendEmail
from lxml import etree


def day_of_60s():
    api = 'https://www.zhihu.com/api/v4/columns/c_1261258401923026944/items'    #json
    html = etree.HTML(json.load(rq.urlopen(api))['data'][0]['content'])
    top_img = rq.urlopen(html.xpath('/html/body/figure[1]/img/@src')[0])
    content = [etree.tostring(x, encoding='utf-8').decode('utf-8')
               for x in html.xpath('/html/body/p')]
    sendEmail.send_day_60s(top_img, content)

if __name__ == "__main__":
    day_of_60s()
