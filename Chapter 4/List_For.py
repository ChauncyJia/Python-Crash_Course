#遍历整个列表

magicians = ['alice','david','carolina']
for magician in magicians:
    print(magician)

magicians = ['alice','david','carolina']
for magician in magicians:
    print(f"{magician.title()}, that was a great trick!")
    print(f"I can't wait to see your next trick,{magician.title()}.\n")
print("Thank you everyone. That was a great magic show!")

# 练习4-1：比萨 　想出至少三种你喜欢的比萨，将其名称存储在一个列表中，
# 再使用for 循环将每种比萨的名称打印出来。
cars = ['audi','bmw','benz']
for car in cars:
    print(f"I like {car}.")
print("I really love car!")

# 练习4-2：动物 　想出至少三种有共同特征的动物，将其名称存储在一个列表
# 中，再使用for 循环将每种动物的名称打印出来。

persons = ['zhang san','li si','wang wu']
for person in persons:
    print(f"{person.title()}, would make a great pet.")
print("Any of therse persons would make a great pet.")