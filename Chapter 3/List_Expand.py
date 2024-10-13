#列表排序
from http.client import CannotSendRequest


cars = ['bmw','audi','toyota','subaru']
cars.sort()
print(cars)

#倒序
cars = ['bmw','audi','toyota','subaru']
cars.sort(reverse=True)
print(cars)

#sorted()临时排序
cars = ['bmw','audi','toyota','subaru']
print("Here is original list:")
print(cars)
print("\nHere is sorted list:")
print(sorted(cars)) #临时正序
print("\nHere is original list again:")
print(cars)

print(sorted(cars,reverse=True))  #临时倒序

#反转列表
cars = ['bmw','audi','toyota','subaru']
cars.reverse()
print(cars)

#列表长度
print(len(cars))


#练习3-8：放眼世界 　想出至少5个你渴望去旅游的地方。
# 将这些地方存储在一个列表中，并确保其中的元素不是按字母顺序排列的。
# 按原始排列顺序打印该列表。不要考虑输出是否整洁的问题，只管打印原始Python列表。
places = ['Dalian','Shanhai','Beijing','Tianjin','Chifeng']
#使用sorted() 按字母顺序打印这个列表，同时不要修改它。
print(sorted(places))
#再次打印该列表，核实排列顺序未变。
print(places)
#使用sorted() 按与字母顺序相反的顺序打印这个列表，同时不要修改它。
print(sorted(places,reverse=True))
# 再次打印该列表，核实排列顺序未变。
print(places)
# 使用reverse() 修改列表元素的排列顺序。打印该列表，核实排列顺序确实变了。
places.reverse()
print(places)
# 使用reverse() 再次修改列表元素的排列顺序。打印该列表，核实已恢复到原来的排列顺序。
places.reverse()
print(places)
# 使用sort() 修改该列表，使其元素按字母顺序排列。打印该列表，核实排列顺序确实变了。
places.sort()
print(places)
# 使用sort() 修改该列表，使其元素按与字母顺序相反的顺序排列。打印该列表，核实排列顺序确实变了。
places.sort(reverse=True)
print(places)

#练习3-9：晚餐嘉宾 　在完成练习3-4~练习3-7时编写的程序之一中，使用
#len() 打印一条消息，指出你邀请了多少位嘉宾来共进晚餐。

print(f"My fav citys have {len(places)}.")

# 练习3-10：尝试使用各个函数 　想想可存储到列表中的东西，如山川、河流、
# 国家、城市、语言或你喜欢的任何东西。编写一个程序，在其中创建一个包含
# 这些元素的列表，然后，对于本章介绍的每个函数，都至少使用一次来处理这
# 个列表。

#使用方法sort()
num = [1,3,8,9,8,4,1,7,4,2,5]
num.sort()
print(num)
num.sort(reverse=True)
print(num)

#使用方法reverse 反转
num = [1,3,8,9,8,4,1,7,4,2,5]
num.reverse()
print(num)

#临时排序
num = [1,3,8,9,8,4,1,7,4,2,5]
print(sorted(num))
print(sorted(num,reverse=True))
print(num)