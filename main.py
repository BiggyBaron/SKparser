# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.support.ui import Select
import os
import datetime
import sys
import telebot


base_url = ("https://backend.digital-summer.sk.kz/login")
second_url = "https://backend.digital-summer.sk.kz/member/index?year=2020&sort=case_total"
options2 = webdriver.ChromeOptions()
options2.add_argument('headless')
driver = webdriver.Chrome("chromedriver", options=options2)
bot = telebot.TeleBot("1272517220:AAGp0kXsJc7Ne7qhZudC0EuiF3z1qnUhj4Q")


@bot.message_handler(content_types=['text'])
def start_message(message):
    dojob(message.chat.id)


def dojob(chat_id):
    driver.get(base_url)
    driver.maximize_window()
    username = driver.find_element_by_id("login-form-login")
    password = driver.find_element_by_id("login-form-password")
    if username:
        username.send_keys("dr.cleverest@gmail.com")
        password.send_keys("NkGAfL")
        driver.find_element_by_id("login-form").submit()
        time.sleep(3)
    driver.get(second_url)
    time.sleep(3)
    data = driver.find_element_by_id("w0-container").get_attribute('innerHTML')
    values = driver.find_elements_by_xpath('//td[@data-col-seq="7"]')
    news = 0
    for el in values:
        if el.get_attribute('innerHTML') == "0.00":
            news++
    
    print(values)
    
    bot.send_message(chat_id, news)


if __name__=="__main__":
    dojob("536244426")
    bot.polling()