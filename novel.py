from urllib import request as req
from lxml import etree
import smtplib
from email.mime.text import MIMEText
import time

root = r'http://www.jianlaixiaoshuo.com'


def get_latest_chapter():
    response = req.urlopen(root)
    html = etree.HTML(response.read().decode('utf-8'))
    a = html.xpath('/html/body/div[1]/div/dl/dd/a')[-1]
    return a


def get_latest_content(latest_a):
    response = req.urlopen(root + latest_a.xpath('@href')[0])
    html = etree.HTML(response.read().decode('utf-8'))
    content_list = html.xpath('/html/body/div[2]/div[3]/div/div[3]/p/text()')
    content = ''
    for x in content_list:
        content += x + '\n\n'

    return content


def send_message(message, subject):
    flag = ''
    sender = '3504448058@qq.com'
    receiver = '3504448058@qq.com'
    psw = 'fqrubkoiihsgcihi'

    msg = MIMEText(message)
    msg['From'] = '3504448058@qq.com'
    msg['To'] = '3504448058@qq.com'
    msg['Subject'] = subject
    try:
        server = smtplib.SMTP_SSL('smtp.qq.com', 465)
        server.login(sender, psw)
        server.sendmail(sender, receiver, msg.as_string())
        server.quit()
        flag = '发送成功'
    except:
        flag = '发送失败'

    with open('./log.txt', 'a+', encoding='utf-8') as file:
        date = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
        file.write(date + '\t' + subject + '\t' + flag + '\n')
    pass


def is_latest():
    latest_a = get_latest_chapter()
    with open('./chapter.txt', 'r+', encoding='utf-8') as file:
        next_chapter = file.read()
        new_chapter = latest_a.xpath('text()')[0]
        if new_chapter == next_chapter:
            pass
        else:
            file.seek(0)
            file.truncate(0)
            file.write(new_chapter)
            message = get_latest_content(latest_a)
            send_message(message, new_chapter)
    pass


if __name__ == '__main__':
    is_latest()
