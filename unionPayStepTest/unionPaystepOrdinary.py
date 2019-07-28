# -*- coding: utf-8 -*-
# @Time    : 2019/7/20 21:07
# @Author  : 魏芳萤
import random
import time
from selenium import webdriver
from xpathConf import xpath_info
from xpathConf import select_merchant_type
from xpathConf import xpath_position
# from selectShopType import select_shop_type

driver = webdriver.Chrome()  # 打开浏览器
driver.get("http://b2b.blibao.com/AppService/meituan/index.htm?shopId=1060800")  # 访问url
driver.set_window_size(480, 900)  # 设置浏览器大小
shop_name_input, merchant_type_div, sure_button, business_license_code, business_license_expired, \
    business_license_name, industry_category_id_div, sure_button01, industry_category_id = xpath_info()

business_address_div = xpath_position()
print(business_address_div)
key, merchant_type = select_merchant_type()

# 定位,点击在线申请输入框
driver.find_element_by_xpath('//*[@id="polymerization"]/div[2]/div/a').click()
time.sleep(2)

# 基础信息填写
driver.find_element_by_xpath(shop_name_input).send_keys('阳光中的青时雨')  # 填写商户全称
time.sleep(2)
# 选择商户类型
driver.find_element_by_xpath(merchant_type_div).click()
time.sleep(2)
driver.find_element_by_xpath(merchant_type).click()
driver.find_element_by_xpath(sure_button).click()
# 填写营业执照号码
shop_num = random.randint(1e08, 1e21)
driver.find_element_by_xpath(business_license_code).send_keys(shop_num)
# 经营有效期
driver.find_element_by_xpath(business_license_expired).send_keys("20200221")
# 营业执照名称
driver.find_element_by_xpath(business_license_name).send_keys("Awin的奶茶店")
# 选择行业类目
driver.find_element_by_xpath(industry_category_id_div).click()
time.sleep(2)
driver.find_element_by_xpath(industry_category_id).click()
time.sleep(2)
driver.find_element_by_xpath(sure_button01).click()

# 位置及环境信息
driver.find_element_by_xpath(business_address_div).click()




