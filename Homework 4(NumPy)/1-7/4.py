# Написать функцию reverse_list(lst), которая принимает в качестве аргумента список и возвращаем его
# в перевернутом виде
from random import randint

lst = [randint(0,9) for i in range(11)]

def reverse(lst: list):
    return lst[::-1]

print(lst)
print(reverse(lst))