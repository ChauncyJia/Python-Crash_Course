#函数
def greet_user():
    """显示简单的问候语"""
    print('Hello')

greet_user()

#传递参数
def greet_user(username):
    """显示简单的问候语"""
    print(f"Hello ,{username.title()}")


greet_user('jia xiangsheng')
greet_user("jia zhenheng")

#形参和实参
# username → 形参
# jiaxiangsheng → 实参

# 练习8-1：消息 　编写一个名为display_message() 的函数，它打印一个句
# 子，指出你在本章学的是什么。调用这个函数，确认显示的消息正确无误。
def display_message():
    """显示描述的信息"""
    print("I want to go home.")

# 练习8-2：喜欢的图书 　编写一个名为favorite_book() 的函数，其中包含
# 一个名为title 的形参。这个函数打印一条消息，下面是一个例子。
# One of my favorite books is Alice in Wonderland.
# 调用这个函数，并将一本图书的名称作为实参传递给它。
def favorite_book(title):
    """描述喜欢的图书"""
    print(f"I favorite book is {title}.")

favorite_book('<HARD WAY LEAREN PYTHON3>')

#位置实参
def describe_pet(animal_type, pet_name):
    """显示宠物信息"""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")

describe_pet('hamster','harry')
describe_pet('dog','willie')

#关键字实参
describe_pet(animal_type='hamster',pet_name='harry')
describe_pet(pet_name='willie',animal_type='dog')

#默认值
def describe_pet(pet_name,animal_type ='dog'):
    """显示宠物信息"""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")

describe_pet(pet_name='willie')
describe_pet('harry','hamster')
describe_pet(pet_name='dada',animal_type='cat')

# 练习8-3：T恤 　编写一个名为make_shirt() 的函数，它接受一个尺码以及
# 要印到T恤上的字样。这个函数应打印一个句子，概要地说明T恤的尺码和字样。
def make_shirt(shirt_size,shirt_text):
    print(f"The shirt size is {shirt_size},band text: {shirt_text}")

make_shirt(170,'China')
make_shirt(shirt_size=180,shirt_text='Dalian')
# 练习8-4：大号T恤 　修改函数make_shirt() ，使其在默认情况下制作一件
# 印有“I love Python”字样的大号T恤。调用这个函数来制作：一件印有默认
# 字样的大号T恤，一件印有默认字样的中号T恤，以及一件印有其他字样的T恤
# （尺码无关紧要）。

def make_shirt(shirt_size=180,shirt_text='I love Python'):
    print(f"The shirt size is {shirt_size},band text: {shirt_text}")

make_shirt(180)
make_shirt(shirt_size=170)
make_shirt(shirt_size=160,shirt_text='I love you')

# 练习8-5：城市 　编写一个名为describe_city() 的函数，它接受一座城市
# 的名字以及该城市所属的国家。这个函数应打印一个简单的句子。

def describe_city(city,country='China'):
    print(f"The {city} is in {country}.")

describe_city('Dalian')
describe_city('Aohan')
describe_city(city='japan',country='Aohan')