'''
Напишите программу, которая будет преобразовывать десятичное число в двоичное.
Пример:
- 45 -> 101101
- 3 -> 11
- 2 -> 10
'''
number = int(input())
n = []

while number > 0:
   n.append(number % 2)
   number //= 2


print(*n[::-1], sep = '')