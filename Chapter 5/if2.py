#if
age = 19
if age >= 18:
    print("You are old enough to vote!")
    print("Have you reqistered to vote yet?")

#if else
age = 17
if age >= 18:
    print("You are old enough to vote!")
    print("Have you reqistered to vote yet?")
else:
    print("Sorry, you are too young to vote.")
    print("Please register to vote as soon as you trun 18.")

#if elif else
age = 12
if age < 4:
    print("You admission cost is $0.")
elif age < 18:
    print("Your admission cost is $25.")
else:
    print("You admission coat is $40.")

age = 12
if age < 4:
    price = 0
elif age < 18:
    price = 25
else:
    price = 40
print(f"Your admission cost is ${price}.")

#多个elif
age = 120
if age < 4:
    price = 0
elif age < 18:
    price = 25
elif age > 65:
    price = 20
else:
    price = 40
print(f"Your admission cost is ${price}.")

age = 120
if age < 4:
    price = 0
elif age < 18:
    price = 25
elif age < 65:
    price = 40
elif age>= 65:
    price = 20
print(f"Your admission cost is ${price}.")

#多个条件

cars = ['subaru','audi','toyota']

if 'audi' in cars:
    print("Adding audi")
if 'bmw' in cars:
    print("Adding bmw")
if 'toyota' in cars:
    print("Adding toyota")

# 练习5-3：外星人颜色 　假设在游戏中刚射杀了一个外星人，请创建一个名为
# alien_color 的变量，并将其赋值为'green' 、'yellow' 或'red' 。
# 编写一条if 语句，检查外星人是否是绿色的。如果是，就打印一条消息，
# 指出玩家获得了5分。
# 编写这个程序的两个版本，在一个版本中上述测试通过了，而在另一个版
# 本中未通过（未通过测试时没有输出）。
alien_color = 'green'
if alien_color == 'green':
    print("得到5分")
alien_color = 'yellow'
if alien_color == 'green':
    print("得到5分")

# 练习5-4：外星人颜色2 　像练习5-3那样设置外星人的颜色，并编写一个if else 结构。
# 如果外星人是绿色的，就打印一条消息，指出玩家因射杀该外星人获得了5
# 分。
# 如果外星人不是绿色的，就打印一条消息，指出玩家获得了10分。
alien_color = 'yello'
if alien_color == 'green':
    print("得到5分")
else:
    print("得到10分")

# 练习5-5：如果外星人是绿色的，就打印一条消息，指出玩家获得了5分。
# 如果外星人是黄色的，就打印一条消息，指出玩家获得了10分。
# 如果外星人是红色的，就打印一条消息，指出玩家获得了15分。
# 编写这个程序的三个版本，分别在外星人为绿色、黄色和红色时打印一条
# 消息。
alien_color = 'red'
if alien_color == 'green':
    print("得到5分")
elif alien_color =='yello':
    print("得到10分")
elif alien_color == 'red':
    print("得到15分")

# 练习5-6：人生的不同阶段 　设置变量age 的值，再编写一个if-elif-else
# 结构，根据age 的值判断一个人处于人生的哪个阶段。
# 如果年龄小于2岁，就打印一条消息，指出这个人是婴儿。
# 如果年龄为2（含）～4岁，就打印一条消息，指出这个人是幼儿。
# 如果年龄为4（含）～13岁，就打印一条消息，指出这个人是儿童。
# 如果年龄为13（含）～20岁，就打印一条消息，指出这个人是青少年。
# 如果年龄为20（含）～65岁，就打印一条消息，指出这个人是成年人。
# 如果年龄超过65岁（含），就打印一条消息，指出这个人是老年人。

age = 100000
if age < 2:
    print("婴儿")
elif age >= 2 and age < 4:
    print("幼儿")
elif age >= 4 and age < 13:
    print("儿童")
elif age >= 13 and age < 20:
    print("少年")
elif age >= 20 and age < 65:
    print("成年")
elif age >= 65 and age <150:
    print("老年人")
else:
    print("Error")

# 练习5-7：喜欢的水果 　创建一个列表，其中包含你喜欢的水果，再编写一系
# 列独立的if 语句，检查列表中是否包含特定的水果。
# 将该列表命名为favorite_fruits ，并在其中包含三种水果。
# 编写5条if 语句，每条都检查某种水果是否包含在列表中。如果是，就打
# 印一条消息，下面是一个例子。
# You really like bananas!
cars = ['audi','bmw','benz']

if 'bmw' in cars:
    print("in")
if 'audi' in cars:
    print("in")
if "toyota" not in cars:
    print("yes ,it't not in")