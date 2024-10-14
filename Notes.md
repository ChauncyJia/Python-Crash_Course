# Chapter 1
- print("xxxx")

# Chapter 2
- 变量的使用以及规则
    ```
    message = "Hello Python world!"
    print(message)
    ```
- 字符串
  - 灵活使用单双引号
  - xxx.title() 单词首字母大写，其他小写
  - xxx.upper() 单词大写
  - xxx.lower() 单词小写
  - f"{var1}{var2}" / f"xxxx,{var1}" f字符串的使用
  - var3= "{} {}".format(var1,var2) py3.5之前的f字符串用法
  - var1 = "\nxxx" var2 ="\txxx" var3 = "\n\txxx"  制表符和回车符 
  - xxx.rstrip() 删除末尾空白
  - xxx.lstrip() 删除开头空白
  - xxx.strip()  删除开头和末尾空
- 数
  -  [+ - * / ]运算符
  -  整数 浮点数
  -  数字中的下划线忽略 19_000_000 = 19000000
  -  同时多个变量赋值：x, y, z, = 0, 0, 0
  - 常量 全大写 值始终不变 → MAX_CONNECTIONS = 5000
# Chapter 3
- 列表
  - list = ['x1','x2','x3']
  - 列表索引从0开始,最后一个元素为-1
- 修改列表
  - list[index] = 'var'
- 末尾增加
  - list.append('new')
- 插入元素
  - list.insert(index,'var')
- 删除元素
  - del list.[index]
  - var = list.pop() 删除末尾元素，并将其赋值var
  - var = list.pop(index) 删除指定元素并赋值
  - list.remove('var') 根据元素值删除元素(第一个值，删除其他需要循环)
- 列表排序
  - list.sort() 列表正序排列，永久的修改
  - list.sort(reverse=True) 列表倒序，永久修改
  - sorted(list) 临时正序排列，不改变列表
  - sorted(list,reverse=True) 临时倒序排列，不改变列表
- 反转列表
  - list.reverse()
- 列表长度
  - len(list)
# Chapter 4
-for循环
  - for car in cats:
  - for dog in dogs:
  - for item in list_of_items:
- range()创建数值列表
  - for value in range(1, 5):
- 创建数字列表
  - list(range(1,6))创建数字列表[1,2,3,4,5]
  - list(range(2,11,2)) 步长为2
- 列表统计
  - min(list)  最小值
  - max(list)  最大值
  - sum(list)  和
- 列表解析
  - squares = [value **2 for value in range(1, 11)]
- 列表切片
  - list[start_index,end_index] end_index不显示
  - list[:3]前3个
  - list[-3:]后3个
  - list[:] 复制
- 元组
  - 不能修改的列表叫元组
  - tuples = (200, 50)
  - 如需修改请直接赋值修改