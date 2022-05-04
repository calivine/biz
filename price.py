from sms import Sms
from price_feed import Price
from analyze import Analyzer

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from urllib.request import urlopen, Request
import queue
import threading
import os
import json
import time
import atexit





email = "caloggero.a@gmail.com"
password = "exroybjchilipmub"

sms_gateway = '3394401732@txt.att.net'
smtp = "smtp.gmail.com"
port = 587

url = "https://api.coingecko.com/api/v3/simple/token_price/polygon-pos?contract_addresses=0xE5417Af564e4bFDA1c483642db72007871397896&vs_currencies=usd"

price_feed = Price(url)
messenger = Sms(email, password)

messenger.connect()


def exit_handler():
    messenger.disconnect()
    print("Sms server terminated")


atexit.register(exit_handler)

price = price_feed.get_price()
print(price)
analyzer = Analyzer(price)
analyzer.alert_setting('big_move')
while True:
    # current_price = price_feed.get_price()
    analyzer.update_price(price_feed.get_price())
    print(analyzer.new_price)
    ''' 
    if current_price != price:
        body = str(current_price)
        messenger.sendSms("GNS Price\n", body)
        '''
    if analyzer.analyze():
        body = str(analyzer.new_price)
        messenger.sendSms("GNS Price\n", body)
    time.sleep(60)





