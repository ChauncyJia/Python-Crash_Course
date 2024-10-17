#input()

""" message = input("Tell me somthing, and I will repeat it back to you: ")
print(message)  """


""" name = input("Please enter your name:")
print(f"\nHello, {name}")  """


""" prompt = "If you tell us who you are, we can presonalize the messages you see."
prompt += '\nWhat is your first name?'

name = input(prompt)
print(f"Hello ,{name}") """

#获取数字

""" age = input("How old ase you?")
age = int(age)
print(age >= 18) """

""" height = input("How tall are you. in inches?")
height = int(height)
if height >= 48:
    print(f"\n You're tall enough to ride.")
else:
    print("\nYou'll be able to ride when you're a little older.") """

#余数
print(4 % 3)
print(5 % 3)
print(6 % 3)

""" number = input("Enter a number, and I'll tell you if it's even or odd:")
number = int(number)
if number % 2 == 0:
    print(f"\nThe number {number} is even.")
else:
    print(f"\nThe number {number} is odd.") """

# 练习7-1：汽车租赁 　编写一个程序，询问用户要租赁什么样的汽车，并打印
# 一条消息，下面是一个例子。

""" car = input("Please input if I can your car:")
print(f"I can find you a {car}") """

# 练习7-2：餐馆订位 　编写一个程序，询问用户有多少人用餐。如果超过8位，
# 就打印一条消息，指出没有空桌；否则指出有空桌。

""" num = input("Please input number:")
num = int(num)
if num > 8:
    print("go out")
else:
    print("come in") """

#练习7-3：10的整数倍 　让用户输入一个数，并指出该数是否是10的整数倍。
num = input("Please input number:")
num = int(num)
if num % 10 == 0:
    print("yes")
else:
    print("no")