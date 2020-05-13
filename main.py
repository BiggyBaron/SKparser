import urllib.request
import telebot
import ssl


context = ssl._create_unverified_context()

with urllib.request.urlopen('https://backend.digital-summer.sk.kz/member/index?year=2020&sort=case_total', context=context) as response:
   html = response.read()
   print(html)