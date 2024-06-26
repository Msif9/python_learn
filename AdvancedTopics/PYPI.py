import reader
reader.__version__


from reader import feed
feed.get_titles()

#配置程序包
import requests
requests.__version__
# git clone https://github.com/realpython/rptree 克隆了包的 Git 存储库
# cd rptree  将工作目录更改为 
# python3 -m venv venv   创建并激活了一个虚拟环境
# venv\Scripts\activate.bat
# python -m pip install -e .  将当前目录的内容安装为可编辑的包。


#使用PIP包
import camelcase
c = camelcase.CamelCase()
txt = 'Hello, world!'
print(c.hump(txt))

#列表推导
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []

for x in fruits:
  if "a" in x:
    newlist.append(x)

print(newlist)

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

newlist = [x for x in fruits if "a" in x]

print(newlist)

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x for x in fruits if x != "apple"]   #返回True
newlist = [x for x in fruits]
#创建一个方块列表
suqares = []
for x in range(10):
  suqares.append(x**2)
# suqares = list(map(lambda x: x**2,range(10)))
# suqares = [x**2 for x in range(10)]
suqares

[(x, y) for x in [1,2,3] for y in [3,1,4] if x != y]#相当于
combs = []
for x in [1,2,3]:
  for y in [3,1,4]:
    if x != y :
      combs.append((x,y))
combs

vec = [-4, -2, 0, 2, 4]
[x*2 for x in vec]                       # 创建一个新列表，其值加倍
[x for x in vec if x >= 0]                # 过滤列表以排除负数
[abs(x) for x in vec]                   # 对所有元素应用一个函数
freshfruit = ['  banana', '  loganberry ', 'passion fruit  '] 
[weapon.strip() for weapon in freshfruit]          # 对每个元素调用一个方法                            
[(x, x**2) for x in range(6)]       # 创建一个 2 元组列表，如 (number, square)
[x, x**2 for x in range(6)]        # 元组必须加括号，否则会出现错误

vec = [[1,2,3], [4,5,6], [7,8,9]]
[num for elem in vec for num in elem]   # 使用带有两个 'for 的 listcomp 压平列表

from math import pi
[str(round(pi, i)) for i in range(1, 6)]

#嵌套列表推导
matrix = [[1, 2, 3, 4],[5, 6, 7, 8],[9, 10, 11, 12]]     # 矩阵实现为 3 个长度为 4 的列表
[[row[i] for row in matrix] for i in range(4)]         #实现行，列转置

#内部推导
transposed = []
for i in range(4):
    transposed.append([row[i] for row in matrix])
transposed

transposed = []
for i in range(4):
   # 下面3行实现嵌套listcomp
    transposed_row = []
    for row in matrix:
        transposed_row.append(row[i])
    transposed.append(transposed_row)
transposed
list(zip(*matrix))

#声明del
a = [-1, 1, 66.25, 333, 333, 1234.5]
del a[0]
a
del a[2:4]
a
del a[:]
a
del a             #删除整个变量

#元组和序列
t = 12345, 54321, 'hello!'
t[0]
t
# 元组可以嵌套：
u = t, (1, 2, 3, 4, 5)
u
# 元组是不可变的：
t[0]
# 但它们可以包含可变对象
v = ([1, 2, 3], [3, 2, 1])
v
empty = ()
singleton = 'hello',    # <-- 注意尾随逗号
len(empty)
len(singleton)
singleton

#集合
basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
print(basket)                      # 表明重复项已被删除

'orange' in basket                 # 快速会员测试
'crabgrass' in basket

# 演示对两个单词中的唯一字母的集合运算

a = set('abracadabra')
b = set('alacazam')
a                                  # unique letters in a
a - b                              # letters in a but not in b
a | b                              # letters in a or b or both
a & b                              # letters in both a and b
a ^ b                              # letters in a or b but not both

a = {x for x in 'abracadabra' if x not in 'abc'}
a

#词典
tel = {'jack': 4098, 'sape': 4139}
tel['guido'] = 4127
tel

tel['jack']

del tel['sape']
tel['irv'] = 4127
tel

list(tel)
sorted(tel)
'guido' in tel
'jack' not in tel

#构造函数直接从以下序列构建字典 键值对
dict([('sape', 4139), ('guido', 4127), ('jack', 4098)])
{x: x**2 for x in (2, 4, 6)}
#使用 关键字参数
dict(sape=4139, guido=4127, jack=4098)

#循环技术
#键和对应值同时检索
knights = {'gallahad': 'the pure', 'robin': 'the brave'}
for k, v in knights.items():
    print(k, v)
#位置索引和相应的值可以 使用该函数同时检索
for i, v in enumerate(['tic', 'tac', 'toe']):
    print(i, v)

#要同时循环两个或多个序列，可以配对条目 与函数
questions = ['name', 'quest', 'favorite color']
answers = ['lancelot', 'the holy grail', 'blue']
for q, a in zip(questions, answers):
    print('What is your {0}?  It is {1}.'.format(q, a))
#要反向循环序列，首先在正向中指定序列 方向，然后调用该函数
for i in reversed(range(1, 10, 2)):
    print(i)
#要按排序顺序循环序列，请使用 返回一个新的排序列表，同时保持源不变
basket = ['apple', 'orange', 'apple', 'pear', 'orange', 'banana']
for i in sorted(basket):
    print(i)
#在序列上使用可消除重复元素
basket = ['apple', 'orange', 'apple', 'pear', 'orange', 'banana']
for f in sorted(set(basket)):
    print(f)
#
import math
raw_data = [56.2, float('NaN'), 51.7, 55.3, 52.5, float('NaN'), 47.8]
filtered_data = []
for value in raw_data:
    if not math.isnan(value):
        filtered_data.append(value)

filtered_data

#生成器表达式
def squares(length):
   for n in range(length):
      yield n ** 2
for square in squares(5):
      print(square)
#    该表达式返回从 0 到 4 的整数的平方数：
squares = (n ** 2 for n in range(5))
for square in squares:
      print(square)
# 使用列表推导式
square_list = [n** 2 for n in range(5)]     #列表方括号
square_generator = (n** 2 for n in range(5))

a = 12
b = "this is text"
my_list = [0, b, ['element', 'another element'], (1, 2, 3), a]
print(my_list)

a = ['red', 'green', 'blue']
print(a[0])

#创建列表
my_list = [0, 1, 2, 3, 4, 5]
my_list = list()
# 将字符串拆分为单独的符号：
string = 'string'
list(string)

#列表推导
my_list = []
for x in range(10):
  my_list.append(x * 2)
print(my_list)

comp_list = [x ** 2 for x in range(7) if x % 2 == 0]
print(comp_list)

nums = [1, 2, 3, 4, 5]
letters = ['A', 'B', 'C', 'D', 'E']
nums_letters = [[n, l] for n in nums for l in letters]
#推导式列表将两个简单列表组合成一个复杂的列表列表。
print(nums_letters)

iter_string = "some text"
comp_list = [x for x in iter_string if x !=" "]
print(comp_list)

# 使用 Python 集生成器创建字典和集推导式
dict_comp = {x:chr(65+x) for x in range(1, 11)}
type(dict_comp)
print(dict_comp)
set_comp = {x ** 3 for x in range(10) if x % 2 == 0}
type(set_comp)
print(set_comp)

customers = [{"is_kyc_passed": False}, {"is_kyc_passed": True}]
kyc_results = []
for customer in customers:
   kyc_results.append(customer["is_kyc_passed"])
all(kyc_results)
customers = [{"is_kyc_passed": False}, {"is_kyc_passed": True}]
all(customer["is_kyc_passed"] for customer in customers)


simple_list = [1, 2, 3]
my_iterator = iter(simple_list) #首先对对象调用 iter（） 方法，将其转换为迭代器对象。
print(my_iterator)
next(my_iterator)  #在迭代器对象上调用 next（） 方法以获取序列的下一个元素。
next(my_iterator)
next(my_iterator)
next(my_iterator)   #当没有剩余的元素可以调用时，将引发 StopIteration 异常。

#生成器表达式
def my_gen():
   for x in range(5):
    yield x
gen_exp = (x ** 2 for x in range(10) if x % 2 == 0)
for x in gen_exp:
 print(x)

#  Python 生成器表达式和列表推导式返回的数据类型不同
list_comp = [x ** 2 for x in range(10) if x % 2 == 0]
gen_exp = (x ** 2 for x in range(10) if x % 2 == 0)
print(list_comp)

print(gen_exp)

# 使用 sys.getsizeof（） 方法检查这两种类型占用了多少内存。
from sys import getsizeof
my_comp = [x * 5 for x in range(1000)]
my_gen = (x * 5 for x in range(1000))
getsizeof(my_comp)

getsizeof(my_gen)

#生成器表达式
# Python code to illustrate generator, yield() and next(). 使生成器函数更加紧凑可靠
def generator(): 
	t = 1
	print ('First result is ',t) 
	yield t 

	t += 1
	print ('Second result is ',t) 
	yield t 

	t += 1
	print('Third result is ',t) 
	yield t 

call = generator() 
next(call) 
next(call) 
next(call) 
# 用于说明生成器表达式的 Python 代码
# Python code to illustrate generator expression 
generator = (num ** 2 for num in range(10)) 
for num in generator:
	print(num)
#生成一个列表
string = 'geek'
li = list(string[i] for i in range(len(string)-1, -1, -1))
print(li)


#面向对象的编程范式
# class Emp has been defined here 
class Emp: 
	def __init__(self, name, age): 
		self.name = name 
		self.age = age 
	
	def info(self): 
		print("Hello, % s. You are % s old." % (self.name, self.age)) 

# Objects of class Emp has been 
# made here		 
Emps = [Emp("John", 43), 
	Emp("Hilbert", 16), 
	Emp("Alice", 30)] 

# Objects of class Emp has been 
# used here 
for emp in Emps: 
	emp.info() 
#过程化编程范式
# Procedural way of finding sum 
# of a list 

mylist = [10, 20, 30, 40] 

# modularization is done by 
# functional approach 
def sum_the_list(mylist): 
	res = 0
	for val in mylist: 
		res += val 
	return res 

print(sum_the_list(mylist)) 

#函数式编程范例
# Functional way of finding sum of a list 
import functools 

mylist = [11, 22, 33, 44] 

# 递归函数方法
def sum_the_list(mylist): 
	
	if len(mylist) == 1: 
		return mylist[0] 
	else: 
		return mylist[0] + sum_the_list(mylist[1:]) 

# 使用lambda函数 
print(functools.reduce(lambda x, y: x + y, mylist)) 
