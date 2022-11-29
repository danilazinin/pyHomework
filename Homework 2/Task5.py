from random import randint
 
 
def mix(lst):
    for index in range(len(lst)):
        index2 = randint(0, len(lst) - 1)
        lst[index], lst[index2] = lst[index2], lst[index]
 
 
lst_ = [1, 2, 3, 4, 5, 6, 7, 8, 9]
mix(lst_)
print(lst_)