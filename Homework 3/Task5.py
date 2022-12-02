'''
Задайте число. Составьте список чисел Фибоначчи,
 в том числе для отрицательных индексов.
Пример:
- для k = 8 список будет выглядеть так: 
[-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]
'''

mem = {1: -1, 2: -1}
 
def fib1(n):
    if n not in mem:
        mem[n] = (fib1(n - 1) + fib1(n - 2)) 
    return mem[n]

fib1(8)
print(mem)


mem = {1: 1, 2: 1}

def fib(n):
    if n not in mem:
        mem[n] = fib(n - 1) + fib(n - 2)
 
    return mem[n]


fib(8)
fib1(8)
print(mem)


