#异常
try:
    print(5/0)
except ZeroDivisionError:
    print("You can't divide by zero!")

# try-except-else
""" while True:
    first_number = input("\nFirst Number:")
    if first_number == "q":
        break
    second_number = input("Second number:")
    if second_number == 'q':
        break
    try:
        answer = int(first_number)/int(second_number)
    except ZeroDivisionError:
        print("You can't divide by 0.")
    else:
        print(answer) """

#
file_path = 'Chapter 10\\alice.txt'
try:
    with open(file_path,encoding='utf-8') as f:
        contents = f.readlines()
except FileNotFoundError:
    print(f"Sorry, the file{file_path} does not exist.")

#split()
title = 'Alice in Wonderland'
print(title.split())
print(len(title.split()))