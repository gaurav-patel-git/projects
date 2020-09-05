from kiteconnect import KiteTicker
import logging
from py_csv import *
logging.basicConfig(level=logging.DEBUG)

api_key= "" # your api kei
access_token= ""  # your access_token
tokens=[53703431]  # for now only one instruemnts token

kws=KiteTicker(api_key,access_token)


def on_ticks(ws,ticks):
    insert_tick=insert_ticks("stock.csv", ticks)  # file name only, converted to csv format and response ticks
    print(ticks)

def on_connect(ws,response):
    ws.subscribe(tokens)
    ws.set_mode(ws.MODE_FULL,tokens)


kws.on_ticks=on_ticks
kws.on_connect=on_connect
kws.connect()