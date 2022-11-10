import numpy as np
# Написать функцию, принимающую на вход одномерный массив и возвращающую наиболее частое
# значение в массиве и частоту его встречи. Протестировать на нескольких заданных вами примерах


def mostFrequent(array):
    return np.argmax(np.bincount(array))

array = np.array([1, 2, 3, 4, 4, 4])
print(mostFrequent(array))