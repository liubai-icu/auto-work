from urllib import request as rq

import sendEmail


def day_of_60s():
    api = 'https://api.vvhan.com/api/60s'
    response = rq.urlopen(api)  # img
    sendEmail.send_day_60s(response)
