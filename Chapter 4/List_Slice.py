players = ['charles','martina','michael','floroence','eli']
print(players[0:3])

print(players[1:4])

print(players[:5])

print(players[3:])

print(players[-2:])

#遍历切片

print("\nHere are the first three players on my team:")
for player in players[:3]:
    print(player.title())

#复制

my_foods = ['pizza','falafel','cake']
friend_foods = my_foods[:]
print(my_foods)
print(friend_foods)

my_foods.append("ice cream")
friend_foods.append("cannoli")

print(my_foods)
print(friend_foods)

# 练习4-10：切片 　选择你在本章编写的一个程序，在末尾添加几行代码，以完成如下任务。
# 打印消息“The first three items in the list are:”，再使用切片来打印列表的前三个元素。
# 打印消息“Three items from the middle of the list are:”，再使用切片来打印列表的中间三个元素。
# 打印消息“The last three items in the list are:”，再使用切片来打印列表的末尾三个元素。

cars = ['audi','benz','subaru','toyota','bmw']
print("\nThe first three item in the list are:")
print(cars[:3])
print("\nThree items from the middle of the list are: ")
print(cars[1:4])
print("\n The last three items in the list are:")
print(cars[-3:])

# 练习4-11：你的比萨，我的比萨 　在你为完成练习4-1而编写的程序中，创建比萨列表的副本，并将其赋给变量friend_pizzas ，再完成如下任务。
# 在原来的比萨列表中添加一种比萨。
# 在列表friend_pizzas 中添加另一种比萨。
# 核实有两个不同的列表。为此，打印消息“My favorite pizzas are:”，
# 再使用一个for 循环来打印第一个列表；打印消息“My friend's
# favorite pizzas are:”，再使用一个for 循环来打印第二个列表。核实
# 新增的比萨被添加到了正确的列表中。

my_cars =['audi','benz','subaru']
friend_cars = my_cars[:]
my_cars.append("sukuzi")
friend_cars.append("toyota")
print("\nMy cars:")
for car in my_cars:
    print(car)

print("\nFriend cars:")
for car in friend_cars:
    print(car)

# 练习4-12：使用多个循环 　在本节中，为节省篇幅，程序foods.py的每个版本
# 都没有使用for 循环来打印列表。请选择一个版本的foods.py，在其中编写两
# 个for 循环，将各个食品列表打印出来。
my_foods = ['pizza','falafel','cake']
for my_food in my_foods:
    print(my_food)