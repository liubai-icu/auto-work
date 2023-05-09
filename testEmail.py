import smtplib
from email.mime.text import MIMEText

sender = '3504448058@qq.com'
receiver = '3504448058@qq.com'
psw = 'fqrubkoiihsgcihi'  # 授权码

content = 'test'
msg = MIMEText(content)  # 构建消息

msg['From'] = sender  # 发送方
msg['Subject'] = 'test'  # 发送主题
msg['To'] = receiver  # 接受者

try:
    server = smtplib.SMTP_SSL('smtp.qq.com', 465)
    server.login(sender, psw)
    server.sendmail(sender, receiver, msg.as_string())
    server.quit()
    print('发送成功')
except:
    print('发送失败')
