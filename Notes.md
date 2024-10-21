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
  - 如需修改请直接赋值修
# Chapter 5 
-条件测试 
  - if
  ```
  if xxx:
    xxx
  elif xxx:
    xxx
  else:
    xxx
  ```
- 比较
  - == 比较是否相等
  - != 比较是否不相等
  - and 与
  - or  或
  - in 包含
  - not in 不包含在列表
# Chapter 6
  - 字典
    - 字典是一列的的键值对
    - dict = {'key1':'value1",'key2':'value2'}
    - 修改键值对：dict['key3'] = 'value'
    - 删除键值对：del dict['key4']
    - get()用法value = dict.get('key1','No key1 value assigned.')
  - 字典方法
    - dict.items() 字典的键值对列表
    - dict.keys() 字典键列表
    - dict.values() 字典值列表
  - 遍历字典
    - for key, value in dict.items(): 键值对
    - for key in dict.keys() 键
    - for value in dict.values()值
    - for key in sorted(dict.keys()) 按顺序
    - for value in set(dict.values()) 不重复
# Chapter 7
  - 输入
    - input("xxx:")
    - int()字符串转换为数字
    - %是个很有用的工具，它将两个数相除并返回余数
    - print(4 % 3) print(7 % 3) 
  - while
    - while xxx <= number :运行几次
    - 标志位
      - active = True
      - whiel active: 
    - break 退出
    - continue 跳过后续循环，返回循环开头
    - while list: 当list.pop()变为空时为假
    - 列表删除所有特定值
      ```
      while 'val' in list:
          list.remove('val')
      ```
# Chapter 8
- 函数
  ```
  def func(形参1，形参2):    # 函数定义
      """文档字符串"""       # 描述函数
      xxxxxx                # 函数执行代码
  func(实参1，实参2)         # 函数调用
  func(形参1 = 实参1，形参2 = 实参2)     #关键字实参
  return xxx                # 返回值
  ```
- 函数与元组
  - def func(形参1，*形参2)  #形参2为一个空元组
  - func(实参1，实参2，实参3，实参4) #实参2-4会组合成元组
- 函数与字典
  - def func(形参1，**形参2) #形参2为一个空字典
  - func(实参1，实参2，实参3) #实参2，3添加到字典