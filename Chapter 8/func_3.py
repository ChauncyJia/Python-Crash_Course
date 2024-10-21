# 传递列表
def greet_users(names):
    """向列表中的每位用户发出简单问候"""
    for name in names:
        msg = f"Hello,{name.title()}"
        print(msg)

usernames = ['zhangsan','lisi','wangwu']
greet_users(usernames)

#在函数中修改列表
def print_models(unprinted_designs,completed_models):
    """
    模拟打印每个设计，知道没有未打印的设计为止。
    打印每个设计后都将其移动到completed_models."""
    while unprinted_designs:
        current_design = unprinted_designs.pop()
        print(f"Printing model: {current_design}.")
        completed_models.append(current_design)

def show_completed_models(completed_models):
    """显示打印好的所有模型"""
    print("\nThe following models have been printed:")
    for completed_model in completed_models:
        print(completed_model)

unprinted_designs = ['phone case','robot pendant','dodecahedron']
completed_models = []

print_models(unprinted_designs,completed_models)
show_completed_models(completed_models)

print(unprinted_designs)
print(completed_models)

#传递列表副本可不修改原列表
print_models(unprinted_designs,completed_models)
show_completed_models(completed_models)

print(unprinted_designs)
print(completed_models)

# 练习8-9：消息 　创建一个列表，其中包含一系列简短的文本消息。将该列表
# 传递给一个名为show_messages() 的函数，这个函数会打印列表中的每条文本消息。
def show_messages(lists):
    """打印列表消息"""
    for list in lists:
        print(list)

msg_lists = ['hello','nihao','goodbye']
show_messages(msg_lists)

# 练习8-10：发送消息 　在你为完成练习8-9而编写的程序中，编写一个名为
# send_messages() 的函数，将每条消息都打印出来并移到一个名为
# sent_messages 的列表中。调用函数send_messages() ，再将两个列表都
# 打印出来，确认正确地移动了消息。
def send_messages(lists,sent_messages):
    """打印消息并移动到sent_messages"""
    while lists:
        msg = lists.pop()
        print(msg)
        sent_messages.append(msg)
copy_list = []
msg_lists = ['hello','nihao','goodbye']
send_messages(msg_lists,copy_list)

print(msg_lists)
print(copy_list)

# 练习8-11：消息归档 　修改你为完成练习8-10而编写的程序，在调用函数
# send_messages() 时，向它传递消息列表的副本。调用函数
# send_messages() 后，将两个列表都打印出来，确认保留了原始列表中的消
# 息。
copy_list = []
msg_lists = ['hello','nihao','goodbye']
send_messages(msg_lists[:],copy_list)

print(msg_lists)
print(copy_list)