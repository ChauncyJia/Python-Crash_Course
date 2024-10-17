#遍历字典
user_0 ={
    'username':'efermi',
    "first":'enrico',
    'last':'fermi',
}
for key, value in user_0.items():
    print(f"\nKey: {key}")
    print(f'Value: {value}')
#字典的方法
print(user_0.items())
print(user_0.keys())
print(user_0.values())

fav_languages = {
    'jen':'python',
    'sarah':'C',
    'edward':'ruby',
    'phil':'python',
}
for name, lanuage in fav_languages.items():
    print(f"{name.title()}'s favorite language is {lanuage.title()}")

#遍历字典键
friends =['phil','sarah']
for name in fav_languages.keys():
    print(f"Hello, {name.title()}")
    if name in friends:
        lanuage = fav_languages[name].title()
        print(f"\t{name.title()}, I see you love {lanuage}")

if 'erin' not in fav_languages.keys():
    print('Erin Please take our poll.')

#按特定顺序遍历字典键
for name in sorted(fav_languages.keys()):
    print(name.title())

#遍历字典值
print('The following lanuages have been mentioned:')
for language in fav_languages.values():
    print(language.title())
#不重复
for lanuage in set(fav_languages.values()):
    print(language.title())


# 练习6-4：词汇表2 　现在你知道了如何遍历字典，可以整理为完成练习6-3而
# 编写的代码，将其中的一系列函数调用print() 替换为一个遍历字典中键和值
# 的循环。确定该循环正确无误后，再在词汇表中添加5个Python术语。当你再次
# 运行这个程序时，这些新术语及其含义将自动包含在输出中。



# 练习6-5：河流 　创建一个字典，在其中存储三条重要河流及其流经的国家。
# 例如，一个键值对可能是'nile': 'egypt' 。
# 使用循环为每条河流打印一条消息，下面是一个例子。
# The Nile runs through Egypt.
# 使用循环将该字典中每条河流的名字打印出来。
# 使用循环将该字典包含的每个国家的名字打印出来。


fav_cars ={
    'subaru':'japan',
    'tesla':'USA',
    'Changcheng':'China',
}
for key, value in fav_cars.items():
    print(f"{key.title()} from {value}")
for car in fav_cars:
    print(car)
for country in fav_cars.values():
    print(country)

# 练习6-6：调查 　在6.3.1节编写的程序favorite_languages.py中执行以下操作。
# 创建一个应该会接受调查的人员名单，其中有些人已包含在字典中，而其
# 他人未包含在字典中。
# 遍历这个人员名单。对于已参与调查的人，打印一条消息表示感谢；对于
# 还未参与调查的人，打印一条消息邀请他参加。
fav_languages = {
    'jen':'python',
    'sarah':'C',
    'edward':'ruby',
    'phil':'python',
}
name_lists =['zhansan','lisi','phil','jen']

for name in name_lists:
    if name in fav_languages:
        print(f'{name}, Welcome.')
    else:
        print(f'{name}, Please let me know you fav lanuage.')
