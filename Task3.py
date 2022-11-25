x = int(input('Введите значение X:'))
y = int(input('Введите значение Y:'))

if x > 0 and y > 0:
    print(("x = {x}, y = {y} -> 1"))
elif x > 0 and y < 0:
     print(("x = {x}, y = {y} -> 2"))
elif x < 0 and y < 0:
     print(("x = {x}, y = {y} -> 3"))
elif x < 0 and y > 0:
     print(("x = {x}, y = {y} -> 4"))