file_path = 'Chapter 10\\pi_digits.txt'
with open(file_path) as file_object:
    contents = file_object.read()
print(contents.rstrip())

with open(file_path) as file_object:
    for line in file_object:
        print(line)
#删除空白
with open(file_path) as file_object:
    for line in file_object:
        print(line.rstrip())

with open(file_path) as file_object:
    lines = file_object.readlines()

for line in lines:
    print(line.rstrip())

#使用文件内容
pi_string =''
for line in lines:
    pi_string += line.rstrip()

print(pi_string)
print(len(pi_string))

pi_string =''
for line in lines:
    pi_string += line.strip()

print(pi_string)
print(len(pi_string))

# 练习10-1：Python学习笔记 　在文本编辑器中新建一个文件，写几句话来总结
# 一下你至此学到的Python知识，其中每一行都以“In Python you can”打头。
# 将这个文件命名为learning_python.txt，并存储到为完成本章练习而编写的程
# 序所在的目录中。编写一个程序，它读取这个文件，并将你所写的内容打印三
# 次：第一次打印时读取整个文件；第二次打印时遍历文件对象；第三次打印时
# 将各行存储在一个列表中，再在with 代码块外打印它们


file_path = 'Chapter 10\\learning_python.txt'
with open(file_path) as file_object:
    contents = file_object.read()
print(contents.rstrip())

with open(file_path) as file_object:
    for line in file_object:
        print(line.rstrip())

with open(file_path) as file_object:
    lines = file_object.readlines()

print(lines)
for line in lines:
    print(line.rstrip())

# 练习10-2：C语言学习笔记 　可使用方法replace() 将字符串中的特定单词
# 都替换为另一个单词。
message = 'I really like dogs.'
print(message.replace('dog','cat'))

for line in lines:
    print(line.rstrip().replace('Python', 'cursor'))