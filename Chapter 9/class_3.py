#继承
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
    def fill_gas_tank(self):
        """描述油箱"""
        print("This car have a gas tank.")

class Battery:
    """一次模拟电动汽车电池的尝试"""
    def __init__(self,battery_size=75):
        self.battery_size = battery_size

    def describe_battery(self):
        """描述电池容量消息"""
        print(f"This car has a {self.battery_size}-Kwh battery.")
    
    def get_range(self):
        """描述指出电池的续航里程"""
        if self.battery_size == 75:
            range = 260
        elif self.battery_size == 100:
            range = 315
        print(f"This car can go about {range} miles on a full charge.")

    def upgrade_battery(self):
        """更新电池电量"""
        if self.battery_size != 100:
            self.battery_size = 100

class ElectricCar(Car):
    """电动汽车的独特之处"""
    def __init__(self, make, model, year):
        """初始化父类属性"""
        super().__init__(make, model, year)
        self.battery = Battery()

    def fill_gas_tank(self):
        """重写"""
        print("This car doesn't need a gas tank!")

my_tesla = ElectricCar('tesla','model s', 2024)
print(my_tesla.get_descriptive_name())
my_tesla.fill_gas_tank()

my_tesla.battery.describe_battery()
my_tesla.battery.get_range()

# 练习9-6：冰激凌小店 　冰激凌小店是一种特殊的餐馆。编写一个名为
# IceCreamStand 的类，让它继承为完成练习9-1或练习9-4而编写的
# Restaurant 类。这两个版本的Restaurant 类都可以，挑选你更喜欢的那
# 个即可。添加一个名为flavors 的属性，用于存储一个由各种口味的冰激凌组
# 成的列表。编写一个显示这些冰激凌的方法。创建一个IceCreamStand 实
# 例，并调用这个方法。
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

class IceCreamStand(Restaurant):
    """继承餐厅类"""
    def __init__(self, restaurant_name, cuisine_type):
        """初始化冰激凌餐厅参数"""
        super().__init__(restaurant_name, cuisine_type)
        self.flavors  = [1,2,3,4]

    def show_ice_flavors(self):
        """描述冰激凌口味"""
        for flavor in self.flavors:
            print(flavor)

my_ice = IceCreamStand('大象冰激凌','甜品')
print(my_ice.show_ice_flavors())

# 练习9-9：电瓶升级 　在本节最后一个electric_car.py版本中，给Battery
# 类添加一个名为upgrade_battery() 的方法。该方法检查电瓶容量，如果不
# 是100，就将其设置为100。创建一辆电瓶容量为默认值的电动汽车，调用方法
# get_range() ，然后对电瓶进行升级，并再次调用get_range() 。你将看
# 到这辆汽车的续航里程增加了。
my_tesla.battery.get_range()
my_tesla.battery.upgrade_battery()
my_tesla.battery.get_range()