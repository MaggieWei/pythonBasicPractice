# -*- coding: utf-8 -*-
# @Time    : 2019/7/20 21:08
# @Author  : 魏芳萤
import random
import time


def xpath_info():
    shop_name_input = '//*[@id="app"]/div[2]/div/div[1]/div/div/div[1]/a[1]/div[2]/div[2]/input'
    merchant_type_div = '//*[@id="app"]/div[2]/div/div[1]/div/div/div[1]/a[2]/div[2]/div[2]/div[1]'
    sure_button = '//*[@id="app"]/div[2]/div/div[1]/div/div/div[1]/a[2]/div[2]/div[2]/div[2]/div[1]/div[2]/button'
    business_license_code = '//*[@id="app"]/div[2]/div/div[1]/div/div/div[1]/a[3]/div[2]/div[2]/input'
    business_license_expired = '//*[@id="app"]/div[2]/div/div[1]/div/div/div[1]/a[4]/div[2]/div[2]/input'
    business_license_name = '//*[@id="app"]/div[2]/div/div[1]/div/div/div[1]/a[5]/div[2]/div[2]/input'
    industry_category_id_div = '//*[@id="app"]/div[2]/div/div[1]/div/div/div[1]/a[6]/div[2]/div[2]/div[1]'
    sure_button01 = '//*[@id="app"]/div[2]/div/div[1]/div/div/div[1]/a[6]/div[2]/div[2]/div[2]/div[1]/div[2]/button'
    industry_category_id = '//*[@id="app"]/div[2]/div/div[1]/div/div/div[1]/a[6]/div[2]/div[2]' \
                           '/div[2]/div[2]/div/div[1]/div/div[106]'
    # logger.info('成功读取菜品分类&菜品xpath！')
    return shop_name_input, merchant_type_div, sure_button, \
        business_license_code, business_license_expired, business_license_name, industry_category_id_div,\
        sure_button01, industry_category_id


def select_merchant_type():
    key = random.randint(1, 4)
    merchant_type = '//*[@id="app"]/div[2]/div/div[1]/div/div/div[1]/a[2]/div[2]/div[2]/div[2]/div[2]/div/div[1]/div/'\
                    'div[' + str(key) + ']'
    return key, merchant_type

# xpath_industry_category_id()


def xpath_position():
    business_address_div = '//*[@id="app"]/div[2]/div/div[1]/div/div/div[2]/a[1]/div[2]/div[2]/div[1]'
    return business_address_div
