# 5. Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
    
#     *Пример:*
    
#     - для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21] [Негафибоначчи]

number = int(input('Введите целое число: '))
list_pos = [0, 1]
list_neg = [0, 1]
for i in range(number-1):
    list_pos.append(list_pos[-1] + list_pos[-2])
    list_neg.append(list_pos[-2] - list_pos[-1])

list_result = list_neg[::-1] + list_pos[1:]
print(list_result)