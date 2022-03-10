# # 元组的定义
# tuple_hogwarts = (1,2,3)
# tuple_hogwarts2 = 1,2,3
# print(tuple_hogwarts)
# print(tuple_hogwarts2)

# 元组的不可变特性
# a = [1,2,3]
# tuple_hogwarts3=(1,2,a)
# print(id(tuple_hogwarts3[2]))
# tuple_hogwarts3[2][0]='a'
# print(tuple_hogwarts3[2])
# print(id(tuple_hogwarts3[2]))

a = (1,2,3,"a","a")
# print(a.count("a"))
print(a.index("a"))