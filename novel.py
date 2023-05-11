from urllib import request as req

from lxml import etree

import sendEmail

import json


def is_latest(name, chapter):
    flag = False
    with open('./novel.json', 'r+', encoding='utf-8') as file:
        data = json.load(file)
        if data[name] != chapter:
            data[name] = chapter
            file.seek(0)
            file.truncate(0)
            json.dump(data, file, ensure_ascii=False)
            flag = True
    return flag


def get_JianLai():
    url = 'http://www.jianlaixiaoshuo.com'
    name = '剑来'
    response = req.urlopen(url)
    html = etree.HTML(response.read().decode('utf-8'))
    label_a = html.xpath('/html/body/div[1]/div/dl/dd/a/@href')[-1]  # 获取章节链接
    chapter = html.xpath('/html/body/div[1]/div/dl/dd/a/text()')[-1]  # 获取章节名称
    if is_latest(name, chapter):
        subject = name + '\t' + chapter
        content_html = etree.HTML(req.urlopen(url + label_a).read().decode('utf-8'))
        print(url + label_a)
        p_list = content_html.xpath('/html/body/div[2]/div[3]/div/div[3]/p')
        message = [etree.tostring(x, encoding='utf-8').decode('utf-8') for x in p_list]
        sendEmail.send_novel(message, subject)


if __name__ == "__main__":
    get_JianLai()
