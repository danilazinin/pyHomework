data ='/Users/danilazinin/Desktop/Нужный хлам/Pyth0n Homework 1/Homework 6/text'
f = open(data, 'r')
data = f.read()
f.close


print(f"Исходный текст: {data}")
find_txt = "абв"
lst = [i for i in data.split() if find_txt not in i.lower()]
print(f'Результат: {" ".join(lst)}')