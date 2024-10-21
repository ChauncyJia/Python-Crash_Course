#传递任意数量的实参（元组）
from pyexpat import model


def make_pizza(*toppings):
    """打印顾客点的所有配料"""
    print('\nMaking a pizza with the following toppings: ')
    for topping in toppings:
        print(f"-{topping}")
make_pizza('pepperoni')
make_pizza('mushrooms','green peppers','extra cheese')

#结合使用位置实参和任意数量实参
def make_pizza(size, *toppings):
    """概述要制作的披萨"""
    print(f"\nMaking a {size}-inch pizza with the fllowing toppings: ")
    for topping in toppings:
        print(f"-{topping}")

make_pizza(6,'pepperoni')
make_pizza(9,'mushrooms','green peppers','extra cheese')

#使用任意数量的关键字实参（字典）
def build_profile(first, last, **user_info):
    """创建一个字典，其中包含我们知道的用户一切。"""
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info
user_profile = build_profile('jia','xiangsheng',location='Dalian',field='physics')

print(user_profile)

def test_func(**user_info):
    """创建字典"""
    return user_info

user = test_func(first='jia',last='xiangsheng',age=30,city='dalian')
print(user)

# 练习8-12：三明治 　编写一个函数，它接受顾客要在三明治中添加的一系列食
# 材。这个函数只有一个形参（它收集函数调用中提供的所有食材），并打印一
# 条消息，对顾客点的三明治进行概述。调用这个函数三次，每次都提供不同数
# 量的实参。

def user_car(*name):
    """收集用户车辆名字"""
    for car in name:
        print(f"-{car}.")
    return name

user_car('audi','subaru','toyota')
user_car('tesla','changcheng','lixiang')

# 练习8-13：用户简介 　复制前面的程序user_profile.py，在其中调用
# build_profile() 来创建有关你的简介。调用这个函数时，指定你的名和
# 姓，以及三个描述你的键值对。

def build_profile(**user_info):
    """手机用户信息并打印"""
    print(user_info)
    return user_info

build_profile(first='jia',last='xiangsheng',age=30)
build_profile(first='zheneg',last='qiulei',age= 30)

# 练习8-14：汽车 　编写一个函数，将一辆汽车的信息存储在字典中。这个函数
# 总是接受制造商和型号，还接受任意数量的关键字实参。这样调用该函数：提
# 供必不可少的信息，以及两个名称值对，如颜色和选装配件。
def make_car(name,model,**car_info):
    """车辆信息描述"""
    car_info['name'] = name
    car_info['model'] = model
    return car_info

my_car = make_car('tesla','modle Y',color='black',year =2024)
print(my_car)
your_car = make_car('toyota','RAV4',color='red',year=2019)
print(your_car)