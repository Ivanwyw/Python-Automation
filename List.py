""""
list_hogwarts=[1,4,6,3]
list_hogwarts.append(0)
#list_hogwarts.insert(1,0)
#list_hogwarts.remove(1)
#y=list_hogwarts.pop(0)
list_hogwarts.sort(reverse=True)

print(list_hogwarts)
"""
# 生成一个平方列表  比如[1，4，9]...  用for循环和列表推导式
list_square=[]
for i in range(4):
    list_square.append(i**2)

print(list_square)

list_square2=[i**2 for i in range(1,4)]

print(list_square2)

list_square3=[i**2 for i in range(1,4) if i!=1]
# for i in range(1,4):
#    if i!=1:
#        list_square3.append(i**2)
print(list_square3)

list_square4=[i*j for i in range(1,4) for j in range(1,4)]
# for i in range(1,4):
#    for j in range(1,4):
#        list_square4.append(i*j)
print(list_square4)