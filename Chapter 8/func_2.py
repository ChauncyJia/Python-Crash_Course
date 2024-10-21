#返回值
def get_formatted_name(first_name, last_name):
    """返回整洁的姓名"""
    full_name = f"{first_name} {last_name}"
    return full_name.title()

musician = get_formatted_name('jimi','hendrix')
print(musician)

def get_formatted_name(first_name,middle_name, last_name):
    """返回整洁的姓名"""
    full_name = f"{first_name} {middle_name} {last_name}"
    return full_name.title()

musician = get_formatted_name('jia','xiang','sheng')
print(musician)

#可选实参
def get_formatted_name(first_name, last_name,middle_name=''):
    """返回整洁的姓名"""
    if middle_name:
        full_name = f"{first_name} {middle_name} {last_name}"
    else:
        full_name = f"{first_name} {last_name}"
    return full_name.title()

musician = get_formatted_name('jia','Xiangsheng')
print(musician)

musician = get_formatted_name(first_name='jia',last_name='Xiangsheng')
print(musician)

#返回字典 
def build_person(first_name, lastname,age= None):
    """返回一个字典，其中包含有关一个人的信息"""
    person = {'first': first_name,'last':lastname}
    if age:
        person['age'] = age
    return person

name = build_person('jia','xiangsheng')
print(name)
name = build_person('jia','xiangsheng',30)
print(name)

#结合while

# def get_formatted_name(first_name, last_name):
#     """返回整洁的姓名"""
#     full_name = f"{first_name} {last_name}"
#     return full_name.title()

# while True:
#     print("\n Please tell me your name:")
#     print("enter'q' at any time too quit!")
#     f_name = input("Fist name: ")
#     l_name = input("Last name: ")
#     again = input("again?(yes/no) ")
#     if again == 'no':
#         break

# formatted_name = get_formatted_name(f_name,l_name)
# print(f"\nHello, {formatted_name}")

# 练习8-7：专辑 　编写一个名为make_album() 的函数，它创建一个描述音乐
# 专辑的字典。这个函数应接受歌手的名字和专辑名，并返回一个包含这两项信
# 息的字典。使用这个函数创建三个表示不同专辑的字典，并打印每个返回的
# 值，以核实字典正确地存储了专辑的信息。
# 给函数make_album() 添加一个默认值为None 的可选形参，以便存储专辑包
# 含的歌曲数。如果调用这个函数时指定了歌曲数，就将该值添加到表示专辑的
# 字典中。调用这个函数，并至少在一次调用中指定专辑包含的歌曲数。
def make_car(name,country,ver= None):
    """描述汽车名称和国家"""
    car_info = {name.title():country.title(),}
    if ver:
        car_info['ver'] = ver
    return car_info

your_car = make_car('subaru','japan')
print(your_car)
my_car = make_car('tesla','usa')
print(my_car)

my_car = make_car('changcheng','china',2024)
print(my_car)

# 练习8-8：用户的专辑 　在为完成练习8-7编写的程序中，编写一个while 循
# 环，让用户输入专辑的歌手和名称。获取这些信息后，使用它们来调用函数
# make_album() 并将创建的字典打印出来。在这个while 循环中，务必提供
# 退出途径。
while True:
    car_name = input("Please let me you car name:")
    car_source = input("Please let me you car source:")
    again = input("again? (yes/no)")
    if again == 'no':
        break
car = make_car(car_name,car_source)
print(car)