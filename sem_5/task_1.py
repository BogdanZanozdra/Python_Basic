# 1. Напишите программу, удаляющую из текста все слова, содержащие ""абв"".

# str = 'Мы неабв очень любим Питон иабв Джавабв'
# lst = str.split()

# res = ' '.join([i for i in lst if 'абв' not in i])

# # for i in lst:
# #     if 'абв' not in i:
# #         res.append(i)
# print(res)

# 2. Создайте программу для игры с конфетами человек против человека.
# Условие задачи: 
# На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга. Первый ход определяется жеребьёвкой. 
# За один ход можно забрать не более чем 28 конфет. Все конфеты оппонента достаются сделавшему последний ход.
# Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?
# a) Добавьте игру против бота
# b) Подумайте как наделить бота ""интеллектом""

from random import randint

balance = 2021
print(balance)
count = 0
while balance > 0: 
    print('Введите число до 28')
    g1 = int(input('gamer1: '))
    while g1 > 28 or g1 <= 0:
        print('Введите число до 28 еще раз!')
        g1 = int(input('gamer1: '))
    balance -= g1
    print(f'Осталось {balance}')
    print('Введите число до 28')
    count += 1
    if balance > 0: 
        bot = randint(1, 28)
        print(f'gamer2: {bot} ')
        # g2 = int(input('gamer2: '))
        balance -= bot
        print(f'Осталось {balance}')
        count += 1
if count // 2:
    print("Победил 2 игрок")
else:
    print("Победил 1 игрок")














# 4.Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Входные и выходные данные хранятся в отдельных текстовых файлах.