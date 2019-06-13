# 4.1遍历整个列表
"""
这行代码让python从列表magicians中取出一个名字，并将其存储在变量magician中
for magician in magicians:这行代码让python获取magician中的第一个值（’alice')，并将其存储到变量magician中
对于列表中的每一个元素，都将执行指定步骤，不管列表中包含多少元素
"""
magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    # 4.2避免缩进错误:python根据缩进来判断代码行与前一个代码行的关系
    print(magician.title() + ",that was a great trick" + "\n")
# for循环后面没有缩进的语句都只执行一次，而不会重复执行
# 使用for循环对数据进行整体操作是一种不错的选择
print("Thank you, everyone. that was a great magic show!")

# 4.2 创建数值列表
for value in range(1, 5):  # 使用函数range()范围[1, 5)
    print(value)
# 创建数字列表，可使用函数list()将range()的结果直接转换为列表
# numbers = list(range(1, 5))
numbers = list(range(2, 11, 2))  # 打印1,10内的偶数
print(numbers)

# 列表操作
squares = []
for value in range(1, 11):
    square = value ** 2
    squares.append(square)
print(squares)

# 对数字列表执行简单的统计计算
digits = list(range(0, 10))
# print(digits)
min_digit = min(digits)  # 获取列表最小值
# print(min_digit)
max_digit = max(digits)  # 获取列表最大值
# print(max_digit)
sum_digit = sum(digits)  # 获取列表总和
# print(sum_digit)

# 列表解析，将for循环和创建新元素的代码合并成一行，并且自动附加新元素
"""要使用这种语法，首先指定一个描述性的列表名，如squares;
然后，指定一个左方括号，用于生成你要存储到列表中的值
如下列示例中，表达式为value**2，他计算平方值。接下来，编写一个for循环，用于给表达式提供值，再加上右方括号"""
squares = [value**2 for value in range(1, 11)]
print(squares)

# 4.4 使用列表的一部分
# 切片
# 要创建切片可指定要使用的第一个元素以及最后一个元素的索引，同range()一样，python在到达你指定的第二个索引前面的元素就停止
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[0:3])  # 打印前三名队员
print(players[1:4])  # 输出第二名到第四名队员
print(players[:4])  # 没有指定一个索引，python自动从列表开头开始
print(players[2:])  # 从索引为2的元素到最后一个元素
# 负数索引返回里列表末尾相应距离的元素，因此你可以输出列表末尾的任何片段
print(players[-3:])  # 打印列表最后3位
print("Here are the first three player on my team:")
for player in players[:3]:
    print("\t" + player)

# 复制列表，可创建一个包含整个列表的切片，即复制整个列表
# 例，假设有一个列表，其中包含你最喜欢的的四种食物，而你还想创建一个列表，在其中包含一位朋友喜欢的所有食物不过你喜欢的
# 食品你这位朋友都喜欢
my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]  # 使用切片复制列表，生成是两个列表
friend_foods = my_foods  # 这样实际上就是只有一个列表，不能得到两个列表

my_foods.append('cannoli')
friend_foods.append('ice cream')
print("My favorite foods are:")
print(my_foods)
print("\nmy friend's favorite foods are:")
print(friend_foods)

# 4.5元组
# 列表非常适合用于存储在程序运行期间可能要变化的数据集，列表是可以修改的。
# 创建一系列不可修改的元素，元组可以满足这种需求，不可变的列表成为元组
dimensions = (200, 50)
# dimensions[1] = 100 # 会报错，元组的值是不可修改的
print(dimensions[0])
print(dimensions[1])
# 遍历元组的值
print("Original dimensions:")
for dimension in dimensions:
    print(dimension)
dimensions = (100,400) # 给元组变量赋值是合法的
print("\nmodified dimensions:")
for dimension in dimensions:
    print(dimension)

