#字符串灵活使用单引号和双引号
"This is a string"
'This is also a string'
'I told my friend, "Python is my favorite language!"'
"The language 'python' is named after Monty Pyhon, not ths snake."
"One of Python's strengths is its diverse and supportive community."

#使用方法修改字符串大小写
name = "add lovelace"
print(name.title()) #单词首字母大写，其他小写
name = name.title()

print(name.upper()) # 单词大写
print(name.lower()) # 单词小写

#f字符串
first_name = 'add'
last_name = 'lovelace'

full_name = f"{first_name} {last_name}"
print(full_name)

print("Hello,",full_name.title()+"!") # 方式1
print(f"Hello, {full_name.title()}!") # f字符串方式

message= f"Hello, {full_name.title()}!" # f字符串赋值变量
print(message)

#python 3.5以前 使用format
full_name = "{} {}".format(first_name,last_name)
print(full_name)

#使用制表符或换行来添加空白
print('python')
print("\tPython")
print("Languages:\nPython\nC\nC++")
print("Language:\n\tPython\n\tC\n\tC++")

#删除空白

favorite_language = " Python "
favorite_language.rstrip() #删除末尾空白
favorite_language.lstrip() #删除开头空白
favorite_language.strip()  #删除开头和末尾空白


#练习2-3：用变量表示一个人的名字，并向其显示一条消息。显示的消息应非常简单
# Hello Eric, would you like to learn some Python today?

name_1 = "Jia Xiangsheng"
print(f"Hello {name_1}, would you likt to learn some Python touday?")

#练习2-4：调整名字的大小写 　用变量表示一个人的名字，再以小写、大写和首字母大写的方式显示这个人名。

name_2 = 'jia xiangsheng'
print(name_2.title())
print(name_2.upper())
print(name_2.lower())

#练习2-5：名言 　找一句你钦佩的名人说的名言，将其姓名和名言打印出来。

var_1 = f'Albert Einstein once said,"A person who never made a mistake never tried anything new."'
print(var_1)

#练习2-6：名言2 　重复练习2-5，但用变量famous_person 表示名人的姓名，再创建要显示的消息并将其赋给变量message ，然后打印这条消息。

famous_person = "Albert Einstein"
var_2 = f'{famous_person} once said,"A person who never made a mistake never tried anything new."'
print(var_2)

#练习2-7：剔除人名中的空白 　用变量表示一个人的名字，并在其开头和末尾都包含一些空白字符。
#务必至少使用字符组合"\t" 和"\n" 各一次。
#打印这个人名，显示其开头和末尾的空白。然后，分别使用剔除函数lstrip() 、
#rstrip() 和strip() 对人名进行处理，并将结果打印出来。


name_3 = "\nmask"
name_4 = "mask\t"
name_5 = "\nmask\t"

print(name_3.lstrip())
print(name_4.rstrip())
print(name_5.strip())
