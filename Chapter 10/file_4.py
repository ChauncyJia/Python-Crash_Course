import json
#写入
numbers = [2, 3, 5, 7, 11, 13]
file_path='Chapter 10\\number.json'
with open(file_path,'w') as f:
    json.dump(numbers,f)

#读取
with open(file_path) as f:
    numbers = json.load(f)

print(numbers)

#保存和读取用户生成的数据

#username = input('What is your name? ')
username = 'jia xiangsheng'
file_path ='Chapter 10\\username.json'
with open(file_path, 'w') as f:
    json.dump(username, f)
    print(f"We'll remember you when you come back, {username}")

with open(file_path) as f:
    username = json.load(f)
    print(f"Welcome back {username}.")

try:
    with open(file_path) as f:
        username = json.load(f)
except FileNotFoundError:
    username = input("Please input your name:")
    with open(file_path,'w') as f:
        json.dump(username,f)
        print("We'll remember you when you come back, {username}")
else:
    print(f"Welcome back {username}.")


#重构
username = None
def get_stored_username():
    """获取存储用户"""
    file_path ='Chapter 10\\username2.json'
    try:
        with open(file_path,) as f:
            username = json.load(f)
    except FileNotFoundError:
        return None
    else:
        return username


def get_new_username():
    """提示用户输入用户名"""
    username = input("Please input your name:")
    file_path ='Chapter 10\\username2.json'
    with open(file_path, 'w') as f:
       json.dump(username,f)
       return username

def greet_user():
    """问候用户，并指出其名字"""
    username = get_stored_username()
    if username:
        print(f"Welcomcome back, {username}")
    else:
        username =get_new_username()
        print(f"We'll remember you when you back, {username}")

greet_user()

# 练习10-11：喜欢的数 　编写一个程序，提示用户输入喜欢的数，并使用
# json.dump() 将这个数存储到文件中。再编写一个程序，从文件中读取这个
# 值，并打印如下所示的消息。
# I know your favorite number! It's _____.

""" fav_number = input('Please enter you fav number:')
file_path = 'Chapter 10\\usernumber.json'
with open(file_path,'w') as f:
    json.dump(fav_number,f)

with open(file_path) as f:
    fav_number = json.load(f)

print(fav_number) """

# 练习10-12：记住喜欢的数 　将练习10-11中的程序合二为一。如果存储了用户
# 喜欢的数，就向用户显示它，否则提示用户输入喜欢的数并将其存储到文件
# 中。运行这个程序两次，看看它能否像预期的那样工作。
file_path = 'Chapter 10\\usernumber.json'
try:
    with open(file_path) as f:
        fav_number = json.load(f)
except FileNotFoundError:
    fav_number = input("Please input your fav number:")
    with open(file_path,'w') as f:
        json.dump(fav_number,f)
else:
    print(f"You fav number: {fav_number}")