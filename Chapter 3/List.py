#列表 由一系列按特定顺序排列的元素组成。你可以创建包含字母表中所有字母、数字0～9或所有家庭成员姓名的列表
bicycles = ['trek','cannondale','redline','specialized']
print(bicycles)

#访问元素
print(bicycles[0])
print(bicycles[0].title())
print(bicycles[3],bicycles[2])
print(bicycles[-1])

msg_1 = f"My first bicycle was a {bicycles[0].title()}"
print(msg_1)

#练习3-1：姓名 　将一些朋友的姓名存储在一个列表中，并将其命名为names 。
# 依次访问该列表中的每个元素，从而将每个朋友的姓名打印出来。
names = ['zhangsan','lisi','wangwu','zhaoliu']

print(names[0])
print(names[1])
print(names[-1])

#练习3-2：问候语 　继续使用练习3-1中的列表 为每人打印一条消息。
# 每条消息都包含相同的问候语，但抬头为相应朋友的姓名。

msg_2 = f"{names[0].title()},welcome to china."
msg_3 = f"{names[1].title()},welcome to china."
print(msg_2)
print(msg_3)

#练习3-3：自己的列表 　想想你喜欢的通勤方式，如骑摩托车或开汽车，并创建一
#个包含多种通勤方式的列表。根据该列表打印一系列有关这些通勤方式

ways = ['car','bicyle','walk','motorcycle']

print(f"I woudl like to own a Toyta {ways[0]}")

