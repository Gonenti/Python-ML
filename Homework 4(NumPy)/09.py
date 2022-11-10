import numpy as np
# Написать функцию, принимающую на вход матрицу и возвращающую n наибольших значений в
# массиве. n вводится с клавиатуры. Протестировать на нескольких заданных вами примерах

def getLists(array):
    lst = []
    if type(array) == np.int32:
        return array
    else:
        for i in range(len(array)):
            lst.append(getLists(array[i]))
        return lst
    
def ArrayToList(array):
    lst = []
    for lists in getLists(array):
        for list in lists:
            lst.append(list)
    return lst


def getMaxValues(array, n = 1):
    lst = ArrayToList(array)
    lst.sort()
    return lst[len(lst)- n: len(lst)]


array = np.random.randint(0,99,(5,5))
print(*array, sep="\n")
print(*getMaxValues(array, int(input("Enter n: "))))