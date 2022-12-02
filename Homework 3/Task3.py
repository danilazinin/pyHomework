'''
Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между 
максимальным и минимальным значением дробной части элементов.
Пример:
- [1.1, 1.2, 3.1, 5, 10.01] => 0.19
'''

lst = [1.1, 1.2, 3.1, 5, 10.01]
def fraction(lst):
    for index in range(0, len(lst)):
        a = lst[index]
        b = a % 1
        a = round(b, 4)
        lst[index] = a


fraction(lst)

def max(lst):
    max1 = lst[1]
    for index in range(0, len(lst)):
        if lst[index] > max1:
            max1 = lst[index]
    return max1

def min(lst):
    min = lst[1]
    for index in range(0, len(lst)):
        if lst[index] > 0:
            if lst[index] < min:
                min = lst[index]
    return min

sum = max(lst) - min(lst)


print(sum)
        


