#字典
alien_0 = {'color':'green', 'point': 5}
print(alien_0['color'])
print(alien_0['point'])
new_point = alien_0['point']
print(f"You just earned {new_point} points.")

#字典添加键值对
alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0)

#空字典使用
alien_0 = {}
alien_0['color'] = 'red'
alien_0['point'] = 10
print(alien_0)

#修改字典的值
alien_0['color'] = 'yellow'
alien_0['point'] = 5
print(alien_0)

alien_0 = {'x_position': 0, 'y_position': 25, 'speed':'fast'}
print(f"Original position: {alien_0['x_position']}")

if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] =='medium':
    x_increment = 2
else:
    x_increment = 3

alien_0['x_position'] += x_increment

print(f"New position: {alien_0['x_position']}")

#删除键值对
alien_0 = {'color':'green', 'point': 5}
print(alien_0)
del alien_0['color']
print(alien_0)

#类似对象组成的字典
favorite_languages ={
    'jen':'python',
    'sarah':'C',
    'edward':'ruby',
    'phil': 'python',
    }
language = favorite_languages['sarah'].title()
print(f"Sarah's favorite language is {language}")

#使用get()来访问值
alien_0 = {'color':'green','speed':'slow'}
#print(alien_0['point']) 获取的键值在字典不存在时会报错
point_value = alien_0.get('points','No point value assigned.')
print(point_value)

# 练习6-1：人 　使用一个字典来存储一个熟人的信息，包括名、姓、年龄和居
# 住的城市。该字典应包含键first_name 、last_name 、age 和city 。将
# 存储在该字典中的每项信息都打印出来。

jia = {
    'first_name':'jia',
    'last_name':'xiangsheng',
    'age':30,
    'city':'Dalian',
    }
print(jia['first_name'].title())
print(jia['last_name'].title())
print(jia['age'])
print(jia['city'])

# 练习6-2：喜欢的数 　使用一个字典来存储一些人喜欢的数。请想出5个人的名
# 字，并将这些名字用作字典中的键；找出每个人喜欢的一个数，并将这些数作
# 为值存储在字典中。打印每个人的名字和喜欢的数。为了让这个程序更有趣，
# 通过询问朋友确保数据是真实的。
number ={
    'zhangsan': 123,
    'lisi': 234,
    'wangwu': 345,
}
print(f"Zhangsan like number is :{number['zhangsan']}")
print(f"Lisi like number is :{number['lisi']}")
print(f"Wangwu like number is :{number['wangwu']}")