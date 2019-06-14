# -*- coding: utf-8 -*-
# @Time    : 2019/6/14 21:29
# @Author  : 魏芳萤
# 5.1if 语句每条测试语句的核心都是一个值为true or false的表达式，这种表达式被称为条件语句
cars = ['audi', 'bmw', 'subaru', 'toyota']

for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())
# 5.2检查值是否相等
# 大多数条件测试都将一个变量的当前值同特定值进行比较。
car = 'bmw'  # 将变量car的值设置为bmw
car == 'bmw'  # 变量car的值是"bmw",区分大小写
# 5.2.3 检查是否不相等
requested_topping = 'mushrooms'
if requested_topping != 'anchovies':
    print("hold the anchovies")

# 5.2.4 检查多个条件
# 1.使用and检查多个条件，检查是否两个条件都为true，可以使用关键字and将两个条件测试合二为一
# 例，检查是否两个人都不小于21岁
age_0 = 22
age_1 = 18
age_0 >= 21 and age_1 >= 21  # false

age_1 = 21
age_1 >= 21 and age_1 >= 21  # true

# 2.使用or检查多个条件，只要至少有一个条件满足，就能通过整个测试，只有两个条件都不满足，表达式才为false
age_0 = 22
age_1 = 18
age_0 >= 21 and age_1 >= 21  # true

age_0 = 18
age_1 >= 21 and age_1 >= 21  # false

# 5.2.6检查特定值是否包含在列表中，可使用关键字in
requested_toppings = ['mushrooms', 'onions', 'pineapple']
'mushrooms'in requested_toppings  # true
'pepperoin' in requested_toppings # false

# 5.2.7 检查特定值是否不包含在列表中，not in
banned_user = ['andrew', 'carolina', 'david']
user = 'marie'

if user not in banned_user:
    print(user.title() + " sorry,you can post a response if you wish.")
# 5.2.8 布尔表达式，布尔值通常记录条件，如游戏是否运行
# 在跟踪程序状态或程序中重要的条件方面，布尔值提供了一种高效的方式

# 5.3 if语句
'''
简单的if语句
if conditional_test:
    do something
'''
age = 19
if age >= 18:
    print("you are old enough to vote")

# 5.3.2.if_else语句
age = 17
if age >= 18:
    print("you are old enough to vote")
else:
    print("sorry, you are too young to vote")

# 5.3.3 if-elif-else结构，elif语句可以多次使用，else不一定必须使用
# 4岁以下免费
# 4-18岁收费5美元
# 18岁（含）以上收费10美元
age = 12
if age < 4:
    print("you admission cost is $0")
elif age < 18:
    print("your admission cost is $5")
else:
    print("your admission cost is $10")

# 简洁方法
if age < 4:
    price = 0
elif age < 18:
    price = 5
else:
    price = 10
print("your admission cost is $" + str(price) + ".")

# 5.3.6 测试多个条件，在多个测试条件都为true的情况下
requested_toppings = ['mushrooms', 'extra cheese']

if 'mushrooms' in requested_toppings:
    print("\nadding mushrooms.")
if 'pepperoni' in requested_toppings:
    print("adding pepperoni.")
if 'extra cheese' in requested_toppings:
    print("adding extra cheese.")
print("\nFinished making your pizza!")

# 总之，你想要只执行一个代码块，就用if-elif-else结构，如果要运行多个代码块，就使用一系列独立的if语句
# 5.4使用if语句处理列表
# 5.4.1检查特殊元素
requested_toppings = ['mushrooms', 'green peppers', 'extra cheese']

for requested_topping in requested_toppings:
    if requested_topping == "green peppers":
        print("\nsorry, we are out of green peppers right now.")
    else:
        print("\nadding" + requested_topping + ".")
print("\nfinished making your pizza")

# 5.4.2确定列表不为空
# 在制作披萨前检查顾客点的配料列表是否为空，如果列表为空，就像顾客确认他是否是点普通披萨；如果不为空
# 就像前面示例那样输出披萨
requested_toppings = []
if requested_toppings:
    for requested_topping in requested_toppings:
        print("\n5.4.2adding" + requested_topping + ".")
    print("\n5.4.2finished making your pizza")
print("are you sure you want a plain pizza?")

# 使用多个列表
# 定义两个列表，其中第一个列表包含披萨店供应的配料而第二个列表包含顾客点的配料。这次对于requested_toppings中的每个元素，都检查
# 是否它是披萨店供应的配料，在决定是否满足在披萨中添加它
available_toppings = ["mushrooms", "olives", "green peppers","pepperoni", "pineapple", "extra cheese"]
requested_toppings = ["mushrooms", "french fries", "extra cheese"]
for requested_topping in requested_toppings:
    if requested_topping in available_toppings:
        print("adding" + requested_topping + ".")
    else:
        print("sorry, we don't have " + requested_topping + ".")
