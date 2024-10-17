#while
current_number = 1
while current_number <= 5:
    print(current_number)
    current_number += 1

# 用户选择退出
""" prompt = '\nTell me something, and I will repeat it back to you:'
prompt += "\nEnter'quit' to end the program."
message = ''
while message != "quit":
    message = input(prompt)
    if message != 'quit':
        print(message) """

#使用标志
""" prompt = '\nTell me something, and I will repeat it back to you:'
prompt += "\nEnter'quit' to end the program."
active = True
while active:
    message = input(prompt)
    if message == 'quit':
        active = False
    else:
        print(message) """

#break退出

""" prompt = '\nTell me something, and I will repeat it back to you:'
prompt += "\nEnter'quit' to end the program."

while True:
    message = input(prompt)
    if message == 'quit':
        break
    else:
        print(message)  """

#continue
current_number = 0
while current_number < 10:
    current_number += 1
    if current_number % 2 == 0:
        continue

    print(current_number)

# 练习7-4：比萨配料 　编写一个循环，提示用户输入一系列比萨配料，并在用
# 户输入'quit' 时结束循环。每当用户输入一种配料后，都打印一条消息，指
# 出我们会在比萨中添加这种配料。
""" cars = []
while True:
    car = input("Please input you car:(enter 'q' quit.)")
    if car =='q':
        break
    cars.append(car)
    print(f"{car} add finished.")
print(cars) """

# 练习7-5：电影票 　有家电影院根据观众的年龄收取不同的票价：不到3岁的观
# 众免费；3～12岁的观众收费10美元；超过12岁的观众收费15美元。请编写一个
# 循环，在其中询问用户的年龄，并指出其票价
""" while True:
    age = input("Please input you age:(enter 'q' quit.)")
    if age =='q':
        break
    age = int(age)
    if age < 3 and age >= 0:
        print('need $0')
    elif age >= 3 and age < 12:
        print('need $10')
    elif age >= 12 and age < 149:
        print('need $20')
    else:
        continue """
