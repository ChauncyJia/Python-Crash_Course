class Dog:
    """一次模拟小狗的简单尝试"""
    def __init__(self, name, age):
        """初始化属性name和age"""
        self.name = name
        self.age = age
    def sit(self):
        """模拟小狗收到命令时蹲下"""
        print(f"{self.name} is now sitting.")

    def roll_over(self):
        """模拟小狗收到命令时打滚"""
        print(f"{self.name} rolled over.")

my_dog= Dog('Willie',6)

print(my_dog.name)
print(my_dog.age)
my_dog.sit()
my_dog.roll_over()

my_dog = Dog('Dada',6)
your_dog = Dog('Xiaoxiao',3)

my_dog.sit()
your_dog.roll_over()

# 练习9-1：餐馆 　创建一个名为Restaurant 的类，为其方法__init__()
# 设置属性restaurant_name 和cuisine_type 。创建一个名为
# describe_restaurant() 的方法和一个名为open_restaurant() 的方
# 法，前者打印前述两项信息，而后者打印一条消息，指出餐馆正在营业。

class Restaurant:
    """模拟餐馆的类"""
    def __init__(self,restaurant_name,cuisine_type):
        """初始化餐馆名称和类型"""
        self.name = restaurant_name
        self.type = cuisine_type
    def describe_restaurant(self):
        """描述餐馆"""
        print(f"Retaurant name: {self.name}")
        print(f"Cuisine type: {self.type}")
    def open_restaurant(self):
        """餐厅正在营业"""
        print(f'The {self.name} is open. ')

# 练习9-2：三家餐馆 　根据为完成练习9-1而编写的类创建三个实例，并对每个
# 实例调用方法describe_restaurant() 。

my_res = Restaurant('大大拉面','快餐')
your_res = Restaurant('北京大饭店','酒店')
my_res.describe_restaurant()
your_res.describe_restaurant()

your_res.open_restaurant()
    
# 练习9-3：用户 　创建一个名为User 的类，其中包含属性first_name 和
# last_name ，以及用户简介通常会存储的其他几个属性。在类User 中定义一个名为
# describe_user() 的方法，用于打印用户信息摘要。再定义一个名为
# greet_user() 的方法，用于向用户发出个性化的问候。
# 创建多个表示不同用户的实例，并对每个实例调用上述两个方法。

class User:
    """用户属性的类"""
    def __init__(self,first_name,last_name):
        """参数初始化"""
        self.first_name = first_name
        self.last_name = last_name
    
    def describe_user(self):
        """描述用户信息"""
        full_name =f"{self.first_name} {self.last_name}"
        print(full_name.title())
    def greet_user(self):
        """欢迎用户"""
        print(f"hello {self.first_name} {self.last_name},welcome!")

jia = User('jia','xiangsheng')
zheng = User('zheng','qiulei')
jia.describe_user()
zheng.describe_user()
jia.greet_user()
zheng.greet_user()
      
