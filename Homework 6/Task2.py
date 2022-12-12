''' 
 Создайте программу для игры с конфетами человек против человека.
Условие задачи: На столе лежит 2021 конфета.
Играют два игрока делая ход друг после друга.
Первый ход определяется жеребьёвкой.
За один ход можно забрать не более чем 28 конфет.
Все конфеты оппонента достаются сделавшему последний ход.
Сколько конфет нужно взять первому игроку, чтобы забрать все
конфеты у своего конкурента?

a) Добавьте игру против бота
b) Подумайте как наделить бота "интеллектом"

'''
from random import randint
 

print(f'Вы участвуете в СУПЕР ИГРЕ, которая не является ЛОХОТРОНОМ. Будеш играть нечестно, вычислю твой айпи, жди меня аххахахахаххах')
print('Игра НАЧАЛАСЬ')
CANDIES = 200
MAX_STEP = 28
 
human = True
cur_candies = CANDIES
 
 
def get_ai_step(cur_candies):
    if cur_candies <= 28:
        return cur_candies
    if cur_candies > 28 and cur_candies < 56:
        return cur_candies - 29
    else:
        return 28
            
    
 
 
def get_human_step():
    while True:
        cnt = input('Введите количество конфет: ')
        if cnt.isdigit() and 1 <= int(cnt) <= min(MAX_STEP, cur_candies):
            return int(cnt)
        print('ЭЙ ты че? Вообще афанарел? играй по правилам, последнее предупреждение')
 
 
while cur_candies:
    if human:
        cnt = get_human_step()
        cur_candies -= cnt
        print(f'Пользователь взял {cnt} конфет. Осталось {cur_candies}.')
    else:
        cnt = get_ai_step(cur_candies)
        cur_candies -= cnt
        print(f'Бот взял {cnt} конфет. Осталось {cur_candies}.')
    human = not human
 
if human:
    print('ПФФФФ, тебя даже Бот обыграл')
else:
    print('Победил человек, тебе просто повезло')