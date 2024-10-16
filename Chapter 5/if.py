# 条件测试
cars = ['audi', 'bmw', 'subaru', 'toyota']
for car in cars:
    if car == "bmw":
        print(car.upper())
    else:
        print(car.title())

#相等
car = 'bmw'
print(car == "bmw")
print(car == "audi")

#大小写
car = "Audi"
print(car =="audi")
print(car.lower() == "audi")

#不相等
requestend_topping = "mushrooms"
if requestend_topping != "anchovies":
    print("Hold the anchovies!")

#数值比较
age = 18
print(age == 18)
answer = 17
if answer != 42:
    print("That is not the correct answer.Please try again!")

#比较符
age = 19
print(age < 21)
print(age <= 21)
print(age > 21)
print(age >= 21)

#检查多个条件
age_0 = 22
age_1 = 18
print(age_0 >= 21 and age_1 >= 21)
age_1 = 22
print(age_0 >= 21 and age_1 >= 21)

age_0 = 22
age_1 = 18
print(age_0 >= 21 or age_1 >= 21)
print(age_0 <= 21 or age_1 >= 21)

#包含，不包含
requestend_toppings =['mushrooms', 'onions', 'pineapple']
print("mushrooms" in requestend_toppings)
print("car" in requestend_toppings)
banned_users = ['andrew', 'carolina', 'david']
user = 'marie'
if user not in banned_users:
    print(f"{user.title()}, You can post a response if you wish.")

#布尔
game_active = True
can_edit = False
print(game_active)
print(can_edit)

# 练习5-1：条件测试 　编写一系列条件测试，将每个测试以及对其结果的预测
# 和实际结果打印出来。
cat_name = 'xiaoxiao'
print(f"Is cat =='xiaoxiao',I think True.\n{cat_name == 'xiaoxiao'}")
print(f"Is cat =='dada',I think False.\n{cat_name == 'dada'}")

# 练习5-2：更多条件测试 　你并非只能创建10个测试。如果想尝试做更多比
# 较，可再编写一些测试，并将它们加入conditional_tests.py中。对于下面列
# 出的各种情况，至少编写两个结果分别为True 和False 的测试。
# 检查两个字符串相等和不等。
# 使用方法lower() 的测试。
# 涉及相等、不等、大于、小于、大于等于和小于等于的数值测试
# 使用关键字and 和or 的测试。
# 测试特定的值是否包含在列表中。
# 测试特定的值是否未包含在列表中。

str_1 = 'test'
if str_1 == 'test':
    print(str_1 == 'test')

car = 'Subaru'
if car.lower() == 'subaru':
    print("yes")

arg_1 = 18
arg_2 = 20

print(arg_1 >= 20)
print(arg_2 >= 20)

print(arg_1 > 15 and arg_2 < 20)
print(arg_1 > 15 or arg_2 < 20)

cars =['audi','bmw','toyota']

print('tesla' in cars)
print('audi' not in cars)

    
