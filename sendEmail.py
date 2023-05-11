import os
import smtplib
import time
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

sender = '3504448058@qq.com'
receiver = '3504448058@qq.com'
pwd = os.getenv('email_token')


def send_novel(message, subject):
    content = """
        <html>
        <style type="text/css">
            div{font-size:14px;font-family: Arial,serif}
            p{ text-indent: 2em}
        </style>
        <body>
            <div>
    """
    for x in message:
        content += x
    content += '</div></body></html>'
    msg = MIMEText(content, 'html', 'utf-8')
    print(content)
    send(subject, msg)


def send_day_60s(response):
    subject = '每天60s读懂世界'
    content = """
        <html>
            <body>
                <img src="cid:img"/>
            </body>
        </html>
    """
    msg = MIMEText(content, 'html', 'utf-8')  # 构建消息
    img = MIMEImage(response.read())
    img.add_header('Content-ID', 'img')
    send(subject, msg, img)


def send(subject, *args):
    multipart = MIMEMultipart()
    multipart['From'] = sender
    multipart['To'] = receiver
    multipart['Subject'] = subject

    for x in args:
        print(type(x))
        multipart.attach(x)

    flag = ''
    try:
        server = smtplib.SMTP_SSL('smtp.qq.com', 465)
        server.login(sender, pwd)
        server.sendmail(sender, receiver, multipart.as_bytes())
        server.quit()
        print('yes')
        flag = '发送成功'
    except:
        flag = '发送失败'

    with open('./log.txt', 'a+', encoding='utf-8') as file:
        date = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
        file.write(date + '(UTC)\t' + subject + '\t' + flag + '\n')
