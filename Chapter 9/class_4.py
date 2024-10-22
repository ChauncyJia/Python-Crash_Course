from random import randint,choice
print(randint(1, 6))

players = ['charles', 'martin', 'michael' ,'florence']
first_up =choice(players)
print(first_up)

# 练习9-13：骰子 　创建一个Die 类，它包含一个名为sides 的属性，该属性
# 的默认值为6。编写一个名为roll_die() 的方法，它打印位于1和骰子面数之
# 间的随机数。创建一个6面的骰子再掷10次。
# 创建一个10面的骰子和一个20面的骰子，再分别掷10次。

class Die:
    """创建一个骰子类"""
    def __init__(self):
        self.sides = 6
    def roll_die(self,num):
        self.sides = randint(1, num)
        return self.sides

num = Die()
for i in range(1,11):
    print(num.roll_die(6))
print("----------------------")
for i in range(1,11):
    print(num.roll_die(10))
print("----------------------")
for i in range(1,11):
    print(num.roll_die(20))

# 练习9-14：彩票 　创建一个列表或元组，其中包含10个数和5个字母。从这个
# 列表或元组中随机选择4个数或字母，并打印一条消息，指出只要彩票上是这4
# 个数或字母，就中大奖了。

list_1 =[111,222,333,444,555,666,777,888,999,000,'a','b','c','d','e']
list_2 =[666,888,'a','c']
your_num =choice(list_1)
print(your_num)