# Напишите код, который все элементы массива x с нечетными индексами переставит в обратном
# порядке.
from random import randint

lst = [randint(0,9) for i in range(10)]

def oddPermutations(lst):
    for i in range(1,len(lst)//2, 2):
        buff = lst[i]
        lst[i] = lst[len(lst)//2 + (len(lst)//2-i)]
        lst[len(lst)//2 + (len(lst)//2-i)] = buff
    return lst

print(lst)
print(oddPermutations(lst))