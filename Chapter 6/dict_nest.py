#嵌套
#字典列表
from calendar import firstweekday


alien_0 = {'color':'green','points':5}
alien_1 = {'color':'yellow','points': 10}
alien_2 = {'color':'red','points': 15}

aliens=[alien_0, alien_1, alien_2]

for alien in aliens:
    print(alien)
#创建多个字典列表
aliens =[]
for i in range(30):
    new_alien = {'color':'green', 'points':5,'speed':'slow'}
    aliens.append(new_alien)

for alien in aliens[:5]:
    print(alien)

print(len(aliens))

for alien in aliens[:3]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['speed'] = 'medium'
        alien['points'] = 15
    elif alien['color'] =='yellow':
        alien['color'] = 'red'
        alien['speed'] = 'fast'
        alien['points'] = 20

for alien in aliens[:5]:
    print(alien)

#在字典中存储列表
pizza = {
    'crust': 'thick',
    'toppings': ['mushrooms','extra cheese'],
}
print(pizza)

fav_language = {
    'jen': ['python','ruby'],
    'sarah': ['c'],
    'edward':['ruby','go'],
    'phil':['python','haskell']
}

for name, languages in fav_language.items():
    print(f"\n{name.title()}'s favorite languages are:")
    for language in languages:
        print(f'\t{language.title()}')

#字典中的字典
users= {
    'aginstein':{
        'first':'albert',
        'last':'einstein',
        'city':'princeton'
    },
    'mcurie':{
        'first':'marie',
        'last':'curie',
        'city':'paris'
    },
}
for username,user_info in users.items():
    print(f"\nUsername: {username}")
    full_name = f"{user_info['first']} {user_info['last']}"
    city = user_info['city']
    print(f"\tFull name: {full_name.title()}")
    print(f"\tCity: {city.title()}")

# 练习6-7：人们 　在为完成练习6-1而编写的程序中，再创建两个表示人的字
# 典，然后将这三个字典都存储在一个名为people 的列表中。遍历这个列表，
# 将其中每个人的所有信息都打印出来。

name_1 = {
    'first_name':'jia',
    'last_name':'xiangsheng',
    'age':30,
    'city':'Dalian',
    }
name_2 = {
    'first_name':'jia',
    'last_name':'zhengheng',
    'age':3,
    'city':'Dalian',
    }
name_3 = {
    'first_name':'zheng',
    'last_name':'qiulei',
    'age':30,
    'city':'Dalian',
    }
lists = [name_1, name_2,name_3]

for list in lists:
    full_name = f"{list['first_name']} {list['last_name']} "
    print(full_name)
    print(f'\t age :{list['age']}')
    print(f'\t city :{list['city']}')
    
# 练习6-8：宠物 　创建多个表示宠物的字典，每个字典都包含宠物的类型及其
# 主人的名字。将这些字典存储在一个名为pets 的列表中，再遍历该列表，并
# 将有关每个宠物的所有信息都打印出来。

cat_1 ={
    'name':'dada',
    'age': 2,
    'owner':'jia'
}
cat_2 ={
    'name':'xiaoxiao',
    'age': 3,
    'owner':'cheng'
}
pets =[cat_1, cat_2]

for pet in pets:
    print(f"{pet['owner'].title()} have a cat:")
    print(f'\tName is: {pet['name'].title()} ')
    print(f'\tAge is: {pet['age']} ')

# 练习6-9：喜欢的地方 　创建一个名为favorite_places 的字典。在这个字
# 典中，将三个人的名字用作键，并存储每个人喜欢的1～3个地方。为了让这个
# 练习更有趣些，可以让一些朋友说出他们喜欢的几个地方。遍历这个字典，并
# 将其中每个人的名字及其喜欢的地方打印出来。
fav_places={
    'zhangsan':['Dalian','Beijing'],
    'lisi':['shanghai','chengdu'],
    'wangwu':['aohan'],
}

for name, places in fav_places.items():
    print(f"{name.title()} favorite places:")
    for place in places:
        print(f'\t{place.title()}')

# 练习6-10：喜欢的数2 　修改为完成练习6-2而编写的程序，让每个人都可以有
# 多个喜欢的数，然后将每个人的名字及其喜欢的数打印出来。
number ={
    'zhangsan': [123,345],
    'lisi': [234,567],
    'wangwu': [135,790],
}
for name, nums in number.items():
    print(f'{name} favorite numberr:')
    for num in nums:
        print(f"\t{num}")

# 练习6-11：城市 　创建一个名为cities 的字典，将三个城市名用作键。对于
# 每座城市，都创建一个字典，并在其中包含该城市所属的国家、人口约数以及
# 一个有关该城市的事实。在表示每座城市的字典中，应包含country 、
# population 和fact 等键。将每座城市的名字以及有关信息都打印出来。
cities = {
    'Dalian': {
            'country':'china',
            'pop':'500万',
            'name': 'jia',
    },
    'shanghai':{
            'country':'china',
            'pop':'1000万',
            'name': 'cheng',
    },
    'beijing':{
            'country':'china',
            'pop':'2000万',
            'name': 'zheng',
    },
}
for city, content, in cities.items():
    print(f'I love {city.title()}:')
    for key, value in content.items():
        print(f"\t {key.title()}: {value}")