
def sum_number(num):
    sum = 0
    while num > 0:
        sum += num % 10
        num //= 10
    return sum


print(sum_number(int(input("Введите число: ")))) 