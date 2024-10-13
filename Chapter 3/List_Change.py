#修改列表元素
from os import name


motorcycles = ['honda','yamaha','suzuki']
print(motorcycles)

motorcycles[0] = 'ducati'
print(motorcycles)

#添加元素
motorcycles = ['honda','yamaha','suzuki']

motorcycles.append('ducati')
print(motorcycles)

motorcycles = []
motorcycles.append('honda')
motorcycles.append('yamaha')
motorcycles.append('suzuki')
print(motorcycles)

#插入元素
motorcycles = ['honda','yamaha','suzuki']
motorcycles.insert(0,'ducati')
print(motorcycles)

#删除元素
del motorcycles[0]
print(motorcycles)
del motorcycles[1]
print(motorcycles)

#pop()删除元素
motorcycles = ['honda','yamaha','suzuki']
pop_motorcycles = motorcycles.pop()
print(motorcycles)
print(pop_motorcycles)

motorcycles = ['honda','yamaha','suzuki']
last_owned = motorcycles.pop()
print(f"The last motorcycle I owned was a {last_owned}")

#pop(index)
motorcycles = ['honda','yamaha','suzuki']
first_owned = motorcycles.pop(0)

print(f"The first motorcycle I owned was a {first_owned}")
print(motorcycles)

#根据值删除元素remove()
motorcycles = ['honda','yamaha','suzuki','ducati']
motorcycles.remove('ducati')
print(motorcycles)

#使用删除元素
motorcycles = ['honda','yamaha','suzuki','ducati']
too_expensive = 'ducati'
motorcycles.remove(too_expensive)
print(motorcycles)
print(f"\nA {too_expensive.title()} is too expensive for me.")


#练习3-4：嘉宾名单 　
#如果你可以邀请任何人一起共进晚餐，你会邀请哪些人？请创建一个列表，其中包含至少三个你想邀请
#的人，然后使用这个列表打印消息，邀请这些人来与你共进晚餐。

name_list = ['zhangsan','lisi','wangwu','zhaoliu']

print(f"Hello,{name_list[0]} welcom. ")
print(f"Hello,{name_list[1]} welcom. ")
print(f"Hello,{name_list[2]} welcom. ")
print(f"Hello,{name_list[3]} welcom. ")

#练习3-5：修改嘉宾名单 　你刚得知有位嘉宾无法赴约，因此需要另外邀请一位嘉宾。

pop_name = name_list.pop(0)
name_list.append('wangba')
print(name_list)
print(f"{pop_name} couldn't come and welcome {name_list[-1]}")

#练习3-6：添加嘉宾 　
#你刚找到了一个更大的餐桌，可容纳更多的嘉宾。请想想你还想邀请哪三位嘉宾。
#以完成练习3-4或练习3-5时编写的程序为基础，在程序末尾添加一条print 语句，指出你找到了一个更大的餐桌
#使用insert() 将一位新嘉宾添加到名单开头。
#使用insert() 将另一位新嘉宾添加到名单中间。
#使用append() 将最后一位新嘉宾添加到名单末尾。
#打印一系列消息，向名单中的每位嘉宾发出邀请。

print("Whoops, we found a bigger table and I'll be inviting three friends again.")
name_list.insert(0,'zhaoqi')
name_list.insert(3,'jiajia')
name_list.append("wushi")
print(name_list)

# 练习3-7：缩减名单 　你刚得知新购买的餐桌无法及时送达，因此只能邀请两 位嘉宾。
# 以完成练习3-6时编写的程序为基础，在程序末尾添加一行代码，打印一条
# 你只能邀请两位嘉宾共进晚餐的消息。
# 使用pop() 不断地删除名单中的嘉宾，直到只有两位嘉宾为止。每次从名
# 单中弹出一位嘉宾时，都打印一条消息，让该嘉宾知悉你很抱歉，无法邀
# 请他来共进晚餐。
# 对于余下两位嘉宾中的每一位，都打印一条消息，指出他依然在受邀人之列。
# 使用del 将最后两位嘉宾从名单中删除，让名单变成空的。打印该名单，
# 核实程序结束时名单确实是空的。

print("Damn, I can only invite two people now.")
pop_name = name_list.pop()
print(f"{pop_name},byebye.")
pop_name = name_list.pop()
print(f"{pop_name},byebye.")
pop_name = name_list.pop()
print(f"{pop_name},byebye.")
pop_name = name_list.pop()
print(f"{pop_name},byebye.")
pop_name = name_list.pop()
print(f"{pop_name},byebye.")

print(f"{name_list[0]}, welcome")
print(f"{name_list[1]}, welcome")

del name_list[0]
del name_list[0]
print(name_list)