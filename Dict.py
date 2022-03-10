"""
序列是以连续的整数为索引，与此不同的是，字典以关键字为索引，关键字可以是任意不可变类型，通常用字符串或数值。

理解字典的最佳方式是把它看做无序的键=>值对集合。在同一个字典之内，关键字必须是互不相同。

一对大括号创建一个空的字典：{}。
"""

# hogwarts_dic ={"a":1,"b":2}
# hogwarts_dic2 =dict(a=1,b=2)
# hogwarts_dic3 ={}
# print(type(hogwarts_dic))
# print(hogwarts_dic)
# print(hogwarts_dic2)
# print(hogwarts_dic3)

a={"a":1,"b":2}
b=dict(a=1,b=2)

# print(a.keys())
# print(a.values())

# #返回指定删除键的值
# print(a.pop("a"))
# #返回被删除键值对
# print(a.popitem())
# print(a)
print(a)
print({i:i*2 for i in range(1,4)})