# -*- coding: utf-8 -*-
# @Time    : 2019/6/24 19:45
# @Author  : 魏芳萤
# 遍历字典，有多种方式，可遍历字典的所有键值对，值或者键
# 6.3.1遍历所有的键-值对
user_0 = {
    'username': 'efermi',
    'first': 'enrico',
    'last': 'fermi',
}

for key, value in user_0.items():  # 声明两个变量存储键-值对中的键和值，item()用于返回键值对
    print('\nkey: ' + key)
    print('value: ' + value)  # 键值对的返回顺序不一定就是键值对的存储顺序，python不关心键值对的存储顺序，
    # 只关心键和值之间的关联关系

favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}
for name, language in favorite_languages.items():
    print('\nname: ' + name)
    print('language: ' + language)
    print(name.title() + "'s favorite language is " + language.title() + '.\n')

# 6.3.2 遍历字典中的所有键
friends = ['phil', 'sarah']
for name in favorite_languages.keys():
    print(name.title())
    if name in friends:
        print("Hi " + name.title() + ", I see your favorite language is " + favorite_languages[name].title() + "!")

# 6.3.3 按顺序遍历字典中的所有值sorted()
# 要以特定的顺序返回元素，一种办法就是在for循环中对返回的键进行排序，可使用函数sorted()来获得按特定顺序排列的键列表的副本
for name in sorted(favorite_languages.keys()):
    print(name.title() + ", thank you for taking the poll.")

# 6.3.3 遍历字典中的所有键
for language in set(favorite_languages.values()):  # set()去重
    print(language.title())

# 6.4 嵌套，将字典存储在列表中，将列表存储在字典中
alien_0 = {'color': 'green', 'points': 5}
alien_1 = {'color': 'yellow', 'points': 10}
alien_2 = {'color': 'red', 'points': 15}

# aliens = [alien_0, alien_1, alien_2]
#
# for alien in aliens:
#     print(alien)

# 创建一个存储外星人的空列表
aliens = []

# 创建30个绿色的外星人
for alien_number in range(30):
    new_alien = {'color': 'green', 'point': 5, 'speed': 'slow'}
    aliens.append(new_alien)

# 显示创建了多少个外星人
print('Total number of aliens: ' + str(len(aliens)))

# 批量处理数据
# 将前三个外星人的颜色变为黄色，速度为中等且值为10个点
for alien in aliens[:3]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['speed'] = 'medium'
        alien['point'] = 10
    elif alien['color'] == 'yellow':
        alien['color'] = 'red'
        alien['speed'] = 'fast'
        alien['point'] = 15

# 显示前五个外星人
for alien in aliens[:5]:
    print(alien)
print('.....')

# 将列表存储在字典中
# 存储所点pizza的所有信息
pizza = {
    'crust': 'thick',
    'toppings': ["mushroom", "extra cheese"],
}

# 概述所点的披萨
print("you order a " + pizza['crust'] + "-crust pizza" +
      "with the following toppings:")

for topping in pizza['toppings']:
    print("\t" + topping)
