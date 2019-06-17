# -*- coding: utf-8 -*-
# @Time    : 2019/6/14 23:44
# @Author  : 魏芳萤
# 练习题外星人
# alien_color = "green"
# alien_color = "red"
# # alien_color = "yellow"
# if alien_color == "green":
#     print("you get 5 points")
# elif alien_color == "yellow":
#     print("you get 15 points")
# else:
#     print("you get 10 points")

# 5-8以特殊的方式跟管理员打招呼
# managements = ["admin", "maggie", "eric", "mac", "apple"]
managements = []
if managements:
    for management in managements:
        if management == "admin":
            print("Hello, " + management + " would you like you to see a status report")
        else:
            print("Hello, " + management + " thank you for login in again")
else:
    print("we need find some users")

# 检查用户名，模拟网站确保每个用户的昵称独一无二
# current_users = ["a", "s", "d", "f", "e"]
# new_users = ["A", "s", "w", "e", "r"]
# for new_user in new_users:
#     if new_user.lower() in current_users:
#         print(new_user + "不好意思，该昵称已被占用")
#     else:
#         print(new_user + "该昵称未被占用")

# 序数
numbers = list(range(1, 10))
for number in numbers:
    if number == 1:
        print(str(number) + "st")
    elif number == 2:
        print(str(number) + "nd")
    elif number == 3:
        print(str(number) + "rd")
    else:
        print(str(number) + "th")



