# if 处理列表
requested_toppings = ['mushrooms','green poppers','extra cheese']
for requested_topping in requested_toppings:
    print(f"Adding {requested_topping}.")
print("\nFinished making your pizza!")

requested_toppings = ['mushrooms','green poppers','extra cheese']
for requested_topping in requested_toppings:
    if requested_topping == 'green poppers':
        print("Sorry,we are out of green poppers right now.")
    else:
        print(f"Adding {requested_topping}.")
print("\nFinished making your pizza!")

#确定列表不是空的
requested_toppings = []

if requested_toppings:
    for requested_topping in requested_toppings:
        print(f"Adding {requested_topping}.")
    print("\nFinished making your pizza!")
else:
    print("\nAre you sure you want a lanin pizza?") 

#两个列表匹配
ava_lists = [1,3,5,7,9,11]
req_lists = [1,2,3,4,5,6,7]

for req_list in req_lists:
    if req_list in ava_lists:
        print(f"Adding {req_list}")
    else:
        print(f"Sorry, we don't have {req_list}.")
print("finished")

# 练习5-8：以特殊方式跟管理员打招呼 　创建一个至少包含5个用户名的列表，
# 且其中一个用户名为'admin' 。想象你要编写代码，在每位用户登录网站后都
# 打印一条问候消息。遍历用户名列表，并向每位用户打印一条问候消息。
# 如果用户名为'admin' ，就打印一条特殊的问候消息，如下所示。
# Hello admin, would you like to see a status report?
# 否则，打印一条普通的问候消息，如下所示。
# Hello Jaden, thank you for logging in again.

user_names = ['zhangsan', 'lisi', 'wangwu', 'zhaoliu', 'admin']
for user_name in user_names:
    if user_name == 'admin':
        print("Hello admin,would you like to see a status report?")
    else:
        print(f"{user_name}, thank you for logging in again.")

# 练习5-9：处理没有用户的情形 　在为完成练习5-8编写的程序中，添加一条
# if 语句，检查用户名列表是否为空。
user_names = []
if user_names:
    for user_name in user_names:
        if user_name == 'admin':
            print("Hello admin,would you like to see a status report?")
        else:
            print(f"{user_name}, thank you for logging in again.")
else:
    print("\nwe need to find some users.")

# 练习5-10：检查用户名 　按下面的说明编写一个程序，模拟网站如何确保每位
# 用户的用户名都独一无二。
# 创建一个至少包含5个用户名的列表，并将其命名为current_users 。
# 再创建一个包含5个用户名的列表，将其命名为new_users ，并确保其中
# 有一两个用户名也包含在列表current_users 中。
# 遍历列表new_users ，对于其中的每个用户名，都检查它是否已被使
# 用。如果是，就打印一条消息，指出需要输入别的用户名；否则，打印一
# 条消息，指出这个用户名未被使用。
# 确保比较时不区分大小写。换句话说，如果用户名'John' 已被使用，应
# 拒绝用户名'JOHN' 。（为此，需要创建列表current_users 的副本，
# 其中包含当前所有用户名的小写版本。）

current_users = ['1','2','3','4','5']
new_users =['1','3','5','7','9']

for new_user in new_users:
    if new_user.lower() in current_users:
        print(f"User {new_user},please use other.")
    else:
        print(f"You can use {new_user}")

# 练习5-11：序数 　序数表示位置，如1st和2nd。序数大多以th结尾，只有1、2
# 和3例外。
# 在一个列表中存储数字1～9。
# 遍历这个列表。
# 在循环中使用一个if-elif-else 结构，以打印每个数字对应的序数。输
# 出内容应为"1st 2nd 3rd 4th 5th 6th 7th 8th 9th" ，但每个序
# 数都独占一行。

nums = [value for value in range(1,10)]

for num in nums:
    if num == 1:
        print(f"{num}st")
    elif num == 2:
        print(f"{num}nd")
    elif num == 3:
        print(f"{num}rd")
    else:
        print(f"{num}th")
