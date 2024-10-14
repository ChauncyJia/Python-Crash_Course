#元组
dimensions = (200, 50)
print(dimensions[0])
print(dimensions[1])

#dimensions[0] = 100 无法修改元组的赋值

#可以修改
dimensions = (400, 100)
print(dimensions)

# 练习4-13：自助餐 　有一家自助式餐馆，只提供五种简单的食品。请想出五种
# 简单的食品，并将其存储在一个元组中。使用一个for 循环将该餐馆提供的五种食品都打印出来。
# 尝试修改其中的一个元素，核实Python确实会拒绝你这样做。
# 餐馆调整了菜单，替换了它提供的其中两种食品。请编写一个这样的代码块：给元组变量赋值，并使用一个for 循环将新元组的每个元素都打印出来。

cars = ('audi','bmw','benz','subaru','toyota')

for car in cars:
    print(car)

#cars[0]='tesla'
cars=('tesla','lixiang','benz','subaru','toyota')
print('\n')
for car in cars:
    print(car)
