# -*- coding: utf-8 -*-
# @Time    : 2019/7/20 22:19
# @Author  : 魏芳萤
import random
import time
from selenium import webdriver
from xpathConf import xpath_info


driver = webdriver.Chrome()  # 打开浏览器
driver.get("http://b2b.blibao.com/AppService/mybank/unionpayStep.htm")  # 访问url
driver.set_window_size(480, 900)  # 设置浏览器大小
shop_name_input, shop_type_div, shop_type1, shop_type2, shop_type3, sure_button = xpath_info()


def select_shop_type():
    shop_type = driver.find_element_by_xpath(shop_type_div)
    shop_type.click()  # 选择商户类型
    time.sleep(3)
    type_value = random.randint(1, 4)
    if type_value == 1:
        shop_type_list = driver.find_element_by_xpath(shop_type1)
    elif type_value == 2:
        shop_type_list = driver.find_element_by_xpath(shop_type2)
    else:
        shop_type_list = driver.find_element_by_xpath(shop_type3)
    shop_type_list.click()
    time.sleep(2)
    sure = driver.find_element_by_xpath(sure_button).click()
    print(type_value)
    return type_value
