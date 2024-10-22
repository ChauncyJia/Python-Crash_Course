file_path = 'Chapter 10\\programming.txt'
with open(file_path,'w') as file_object:
    file_object.write("I love programming.")

with open(file_path,'w') as file_object:
    file_object.write("I love programming.\n")
    file_object.write("I love creating new games.\n")

with open(file_path,'a') as file_object:
    file_object.write("I also love finding meaning in large datasets.\n")
    file_object.write("I love creating apps that can run in a browser.\n")

# 练习10-3：访客 　编写一个程序，提示用户输入名字。用户做出响应后，将其
# 名字写入文件guest.txt中。
""" name = input("Please input your name:")
file_path = 'Chapter 10\guest.txt'

with open(file_path,'w') as file_object:
    file_object.write(name) """

# 练习10-4：访客名单 　编写一个while 循环，提示用户输入名字。用户输入
# 名字后，在屏幕上打印一句问候语，并将一条到访记录添加到文件
# guest_book.txt中。确保这个文件中的每条记录都独占一行。
file_path ="Chapter 10\guest_book.txt"
while True:
    name = input("Please input your name:(enter 'q' quit.)")
    if name == "q":
        break
    else:
        print(f"Hello, {name}")
        with open(file_path,'a') as file_object:
            file_object.write(f"{name}\n")