def Easy_numbers(n):
    lst = []
    d = 2
    while d * d <= n:
        if n % d == 0:
            lst.append(d)
            n //= d
        else:
            d += 1
    if n > 1:
        lst.append(n)
    return lst
print(Easy_numbers(int(input('Введите число: '))))
