# 使用while 循环处理列表和字典
from ctypes import cast


unconfirmed_users = ['alice','brian','candace']
confirmed_user = []
while unconfirmed_users:
    current_user = unconfirmed_users.pop()
    print(f"Verifying suer:{current_user}")
    confirmed_user.append(current_user)
confirmed_user.reverse()
print(confirmed_user)

#删除为特定值的所有列表元素
pets = ['dog','cat','dog','goldfish','cat','rabbit','cat']
print(pets)
while 'cat' in pets:
    pets.remove('cat')
print(pets)

#使用用户输入来填充字典
""" responses = {}

polling_active = True

while polling_active:
    name = input(f"\nWhat is your name?")
    response = input('Which mountain whould you like to climb someday?')

    responses[name] = response
    repeat = input("Whoud you like to like wo let another person respond? (yes/no) ")
    if repeat == 'no':
        polling_active = False

print("\n--- Poll Results ---")
for name, response in responses.items():
    print(f"{name} would like to climb {response}.")
 """

# 练习7-8：熟食店 　创建一个名为sandwich_orders 的列表，在其中包含各
# 种三明治的名字，再创建一个名为finished_sandwiches 的空列表。遍历
# 列表sandwich_orders ，对于其中的每种三明治，都打印一条消息，如I
# made your tuna sandwich ，并将其移到列表finished_sandwiches
# 中。所有三明治都制作好后，打印一条消息，将这些三明治列出来。

my_cars = ['audi','subaru','tesla']
your_cars = []

while my_cars:
    car = my_cars.pop()
    print(f"{car} is good car.")
    your_cars.append(car)
your_cars.reverse()

print(your_cars)

# 练习7-9：五香烟熏牛肉卖完了 　使用为完成练习7-8而创建的列表
# sandwich_orders ，并确保'pastrami' 在其中至少出现了三次。在程序
# 开头附近添加这样的代码：打印一条消息，指出熟食店的五香烟熏牛肉
# （pastrami）卖完了；再使用一个while 循环将列表sandwich_orders 中
# 的'pastrami' 都删除。确认最终的列表finished_sandwiches 未包
# 含'pastrami' 。
my_cars = ['audi','subaru','tesla','subaru','suzuki','subaru','benz']

while 'subaru' in my_cars:
    my_cars.remove('subaru')
print(my_cars)

# 练习7-10：梦想的度假胜地 　编写一个程序，调查用户梦想的度假胜地。使用
# 类似于下面的提示，并编写一个打印调查结果的代码块。
# If you could visit one place in the world, where would you go?


dream_cars ={}
while True:
    name = input('Please input your name:')
    dream_car = input('Please ask me you dream car:')
    dream_cars [name] = dream_car
    print(f"Yes, it's {dream_car}")
    flag = input("Connect? (yes or no)")
    if flag == 'no':
        break

print(dream_cars)