class Car:
    """一次模拟汽车的简单尝试"""
    def __init__(self,make, model, year):
        """初始化描述汽车的属性"""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0
    
    def get_descriptive_name(self):
        """返回整洁的描述信息"""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()
    
    def read_odometer(self):
        """打印汽车里程信息"""
        print(f"This car has {self.odometer_reading} miles on it.")
    
    def update_odometer(self,mileage):
        """将里程表读书设定为指定的值
        禁止里程回调"""
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")
    def increment_odometer(self, miles):
        """将里程数增肌指定值"""
        if miles >= 0:
            self.odometer_reading += miles
        else:
            self.odometer_reading

my_new_car = Car('audi','A4', 2020)
print(my_new_car.get_descriptive_name())
my_new_car.read_odometer()

my_new_car.odometer_reading = 23
my_new_car.read_odometer()

my_new_car.update_odometer(100)
my_new_car.read_odometer()

my_new_car.update_odometer(10)
my_new_car.read_odometer()

my_new_car.update_odometer(101)
my_new_car.read_odometer()

my_new_car.increment_odometer(-5)
my_new_car.read_odometer()

# 练习9-4：就餐人数 　在为完成练习9-1而编写的程序中，添加一个名为
# number_served 的属性，并将其默认值设置为0。根据这个类创建一个名为
# restaurant 的实例。打印有多少人在这家餐馆就餐过，然后修改这个值并再次打印它。
class Restaurant:
    """模拟餐馆的类"""
    def __init__(self,restaurant_name,cuisine_type):
        """初始化餐馆名称和类型"""
        self.name = restaurant_name
        self.type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        """描述餐馆"""
        print(f"Retaurant name: {self.name}")
        print(f"Cuisine type: {self.type}")
    def open_restaurant(self):
        """餐厅正在营业"""
        print(f'The {self.name} is open. ')

    def set_number_served(self,number):
        """设置就餐人数"""
        self.number_served = number
    
    def increment_number_served(self,number):
        """增加就餐人数"""
        self.number_served += number
    def reset_number_served(self):
        """重置人数"""
        self.number_served = 0


my_res =Restaurant('大象拉面','中餐')

my_res.number_served = 10
print(f"{my_res.name} have {my_res.number_served} person.")

# 添加一个名为set_number_served() 的方法，让你能够设置就餐人数。调
# 用这个方法并向它传递一个值，然后再次打印这个值。
my_res.set_number_served(100)
print(f"{my_res.name} have {my_res.number_served} person.")

# 添加一个名为increment_number_served() 的方法，让你能够将就餐人数
# 递增。调用这个方法并向它传递一个这样的值：你认为这家餐馆每天可能接待
# 的就餐人数。
my_res.increment_number_served(10)
print(f"{my_res.name} have {my_res.number_served} person.")

# 练习9-5：尝试登录次数在为完成练习9-3而编写的User 类中，添加一个名
# 为login_attempts 的属性。编写一个名为
# increment_login_attempts() 的方法，将属性login_attempts 的值
# 加1。再编写一个名为reset_login_attempts() 的方法，将属性
# login_attempts 的值重置为0。
# 根据User 类创建一个实例，再调用方法increment_login_attempts()
# 多次。打印属性login_attempts 的值，确认它被正确地递增。然后，调用
# 方法reset_login_attempts() ，并再次打印属性login_attempts 的
# 值，确认它被重置为0。
my_res.reset_number_served
print(f"{my_res.name} have {my_res.number_served} person.")