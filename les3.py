# def f(x):
#     return x**2

# g = f

# print(type(f))
# print(type(g))

# print(f(2))
# print(g(2))

# def calc1(x):
#     return x*10

# print(calc1(10))

# def calc2(x):
#     return x + 10

# print(calc2(10))

# def math(op, x):
#     print(op(x))

# math(calc2, 10)
################### РАБОТА С ОДНОЙ ПЕРЕМЕННОЙ ##############################


# def sum(x, y):
#     return x + y

# sum = lambda x, y: x+y+1

# def mult(x, y):
#     return x*y

# def calc(op, a, b):
#     print(op(a, b))

# calc(lambda x, y: x+y+1, 6, 5)

############################## РАБОТА СО СПИСКАМИ ################################

# list = []

# for i in range(1, 101):
#     # if (i % 2 == 0):
#         list.append(i)


# def f(x):
#     return x**3

# list = [(i,f(i)) for i in range(1, 21) if i % 2 == 0] # упрещенная версия
# print(list)

######################## list

# def select(f, col):
#     return[f(x) for x in col]

# def where(f, col):
#     return[x for x in col if f(x)]


# data = '1 2 3 5 8 15 23 38'.split()

# res = select(int, data)
# res = where(lambda x: not x % 2, res)
# res = select(lambda x: (x, x**2), res)
# print(res)

######################### ФУНКЦИЯ map ниже ############################

# li = [x for x in range(1, 20)]

# li = list(map(lambda x: x+10, li))

# print(li)

#########################

# data = list(map(int, input().split()))
# print(data)
# 1
# ######################### ФУНКЦИЯ filter #################

# data = [x for x in range(10)]

# res = list(filter(lambda x: not x % 2, data))

# print(res)

###################### ФУНКЦИЯ zip #####################

# users = ['user1', 'user2', 'user3', 'user4', 'user5']

# ids = [4, 5, 9, 14, 7]

# data = list(zip(users, ids ))

# print(data)

##################  ФУНКЦИЯ enumerate ####################

users = ['user1', 'user2', 'user3', 'user4', 'user5']

ids = [4, 5, 9, 14, 7]

data = list(enumerate(users))

print(data)
