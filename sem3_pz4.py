# Задача 4. Напишите программу, которая будет преобразовывать десятичное число в двоичное. 
# Нельзя использовать готовые функции.

# *Пример:*

# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10

n = int(input('Введите число: ')) 
b = ''
while n > 0:
    b = str(n % 2) + b
    n = n // 2
print(f'Binary number: {b}')