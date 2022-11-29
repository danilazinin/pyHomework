n = int(input("Введите число N:"))
a = int(input("Введите позицию 1:"))
b = int(input("Введите позицию 2:"))


lst = []
num = 0


for index in range(-n, n + 1):
    lst.append(index) 
    num = num + 1


sum = lst[a] + lst[b]


print(lst)
print(f"Сумма элемента на позиции {a} и элемента на позиции {b} равна {sum}")
