# print("Hello world")
# 2.2变量
message = "Hello Python world!"
print(message)
# 程序中可随时修改变量的值，而Python将始终记录变量的最新值
message = "Hello Python Crash Course world!"
print(message)
'''
2.2.1变量的命名和使用
1.变量只能包含字母，数字，下划线，可以以字母和下划线开头，但是不能以数字开头
2.不要将Python关键字和函数名用作变量名，既不要使用Python保留用于特殊用途的单词
3，变量名应该简短又具有描述性
4.据目前而言应使用小写字母作为变量名，单词间用_分隔，如student_name
'''
# 2.3字符串，字符串用双引号或者单引号括起来
# 2.3.1使用方法修改字符串的大小写title()
name = "ada lovelace"
print(name.title())
# 将字符串全部改为大写upper()
print(name.upper())
# 将字符串全部改为小写lower()
# 存储数据时，方法lower很有用，可以先将字符串全部转化为小写然后再进行转化成想要的方式
print(name.lower())

# 2.3.2合并（拼接）字符串
first_name = 'ada'
last_name = 'lovelace'
full_name = first_name + " " + last_name
message = "hello, " + full_name.title() + "!"
print(message)

# 2.3.3使用制表符（\t)或换行符(\n)来添加空白
print("language:\n\tpython\n\tC\n\tJavaScript")

# 2.3.4删除空白,常用于存储用户输入前对其进行处理
# Python能够找出字符串开头和末尾多余的空白。要确保字符串末尾没有空白，可使用rtrip()
# 删除字符串末尾空白rstrip()
# 删除字符串开头空白lstrip()
# 删除字符串两端空白strip()
favorite_language = 'python '
favorite_language = favorite_language.rstrip()

# 2.4数字
# 2.4.1 整数，可以对整数进行加（+）减（-)乘(*)除(/)乘方（**）操作
# 2.4.2 浮点数带小数点的数字都称为浮点数，注意学习处理多于小数位的方法
# 2.4.3使用str()避免类型错误，将非字符串转化为字符串类型
age = 23
message = "Happy " + str(age) + "rd Birthday"
print(message)