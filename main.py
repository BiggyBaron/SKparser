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
driver = webdriver.Chrome("chromedriver")
bot = telebot.TeleBot("1272517220:AAGp0kXsJc7Ne7qhZudC0EuiF3z1qnUhj4Q")


driver.get(base_url)
driver.maximize_window()
username = driver.find_element_by_id("login-form-login")
password = driver.find_element_by_id("login-form-password")
username.send_keys("dr.cleverest@gmail.com")
password.send_keys("NkGAfL")
driver.find_element_by_id("login-form").submit()
driver.save_screenshot("/home/ubuntu/SKparser/landing_page.png")
photo = open('/home/ubuntu/SKparser/landing_page.png', 'rb')
chat_id = "536244426"
bot.send_photo(chat_id, photo)


driver.quit()