# Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
# Пример: пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)


input_num = int(input('Введите число: '))
list = [1]

for i in range (1,input_num):
    list.append ((i+1) * list [i-1])

print(list)


#либо чеез переменную а не список
temp_num = 1
for i in range (input_num):
    temp_num *= i+1
    print(temp_num, end=' ')

print ()