# Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга.
# Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет.
# Все конфеты оппонента достаются сделавшему последний ход.
# Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?
# a) Добавьте игру против бота
# b) Подумайте как наделить бота ""интеллектом""

# ОТВЕТ: Первому  игроку  надо первым ходом забрать остаток от целочисленного деления
# имеющегося количества конфет на то, которое можно взять за 1 ход максимально + 1
# В дальнейшем первому игроку нужно повторять стратегию, хотя без калькулятора не всегда это удобно посчитать))))
# Пример :  2021 % ( 28 + 1 ) = 20 , первый игрок первым ходом должен взять 20 конфет.
# если вторым ходом второй игрок взял 10 конфет, то первый должен взять 28 + 1 - 10 = 19 и так далее..



from random import *
import os


welcome_text = ('Приветствую Вас, дорогой игрок!\n'
                'Предлагаю сыграть в игру "2021 шаг до Вилли Волка"\n'
                'Правила таковы:\n'
                 'На столе находится 2021 конфета, игроки должны брать их по очереди,\n'
                'причем, за один раз можно взять не больше 28 конфет.\n'
                'Выигрывает тот, кто последним ходом заберет все конфеты.\n'
                'Пора начинать!')
print(welcome_text)

message = ['Твоя очередь будет первой!', 'Поэтому не стоит ждать!']

def player_vs_player():
    candies_total = 2021
    max_take = 28
    count = 0
    player1 = input('\nКак твоё имя?: ')
    player2 = input('\nА твоего соперника?: ')

    print(f'\nНУ что, {player1} и {player2}, начинаем игру!\n')
    print('\nДля начала определим какой игрок делает первый ход.\n')

    x = randint(1, 2)

    if x ==1:
        lucky = player1
        loser = player2
    else:
        lucky = player2
        loser = player1
    print(f'Поздравляю {lucky}, твой ход первый!')

    while candies_total > 0:
        if count == 0:
            step = int(input(f'\n{choice(message)} {lucky} = '))
            if step > candies_total or step > max_take:
                step = int(input(f'\nМожно взять только {max_take} конфет {lucky}, так что попробуй снова: '))
            candies_total = candies_total - step
        if candies_total > 0:
            print(f'\nОсталось ещё {candies_total} конфет!')
            count = 1
        else:
            print('Все конфеты закончились.')

        if count == 1:
            step = int(input(f'\n{choice(message)}, {loser} '))
            if step > candies_total or step > max_take:
                step = int(input(f'\nМожно взять только {max_take} конфет {loser}, попробуй снова: '))
            candies_total = candies_total - step
        if candies_total > 0:
            print(f'\nОСталось ещё {candies_total} конфет! ')
            count == 0
        else:
            print('Все конфеты закончились')

    if count == 1:
        print(f'{loser} победил!!!')
    if count == 0:
        print(f'{lucky} победил!!!')

player_vs_player()

def player_vs_bot():
    candies_total = 2021
    max_take = 28
    player1 = input(f'\nКак тебя зовут?: ')
    player2 = 'Компьютер'
    players = [player1, player2]
    print(f'\nНу что, {player1} и {player2}, приступим к игре!\n ')
    print(f'\nДля начала определим кто первым начнет игру\n')

    lucky = randint(-1, 0)

    print(f'Поздравляю {lucky[players+1]}, твой ход будет первым!')

    while candies_total > 0:
        lucky += 1

        if players[lucky % 2 ] == 'Компьютер':
            print(f'\nХодит {players[lucky%2]}  \nНа кону {candies_total} конфет. \n{choice(message)}: ')

            if candies_total < 29:
                step = candies_total
            else:
                delenie = candies_total // 28
                step = candies_total - ((delenie*max_take)+1)
                if step == 1:
                    step = max_take -1
                if step == 0:
                    step = max_take
            while step > 28 or step < 1:
                step = randint(1, 28)
            print(step)
        else:
            step = int(input(f'\nНу что, ходи {players[lucky%2]} \nНа кону {candies_total} {choice(message)} '))
            while step > max_take or step > candies_total:
                step = int(input(f'\nЗа один ход можно взять только {max_take} конфет, попробуй еще раз: '))
        candies_total = candies_total - step
    print(f'\nНа кону осталось {candies_total} \nПобедил {players[lucky%2]}')

player_vs_bot()
                