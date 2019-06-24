# -*- coding: utf-8 -*-
# @Time    : 2019/6/17 22:00
# @Author  : 魏芳萤
# 6.1.一个简单的字典
alien_0 = {'color': 'green', 'points': 5}  # 字典是一系列键-对

print(alien_0['color'])  # 访问字典中的值，要获取与键相关的值。可依次指定字典名和方括号内的键
print(alien_0['points'])

new_points = alien_0['points']
print("you just earned " + str(new_points) + " points!")

# 6.2.2 添加键-值对，字典是一种动态结构，可随时添加键值对，可依次指定字典名，用方括号括起的键和相关联的值
print(alien_0)
alien_0["x_ppsition"] = 0
alien_0['y_position'] = 25
print(alien_0)

# 6.2.3 先创建一个空字典
alien_0 = dict()
alien_0['color'] = 'green'
print("the alien is now " + alien_0['color'] + ".")

alien_0['color'] = 'yellow'
print("the alien is now " + alien_0['color'] + ".")

# 例子：对一个能够以不同速度移动的外星人的位置进行跟踪。为此我们将存储该外星人的当前速度，并据此确定该外星人将向右移动多远
alien_0 = {"color": "green", "points": 5}
print(alien_0)

del alien_0["points"]
print(alien_0)

# 6.2.6 由类似对象组成的字典，字典存储的是一个对象的多种信息
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}

print("Sarah's favorite language is " +
      favorite_languages['sarah'].title() + ".")
