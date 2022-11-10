import numpy as np

# Написать функцию, принимающую на вход массив и меняющую знак у элементов, значения которых
# между 3 и 8. Протестировать на нескольких заданных вами массивах.

def changeValue(array):
    for i in range(len(array)):
        for j in range(len(array[i])):
            if 3 < array[i][j] < 8:
                array[i][j] *= -1 
    return array

array = np.full((5,5), 0)
print(changeValue(array))
print()

array = np.full((5,5), 5)
print(changeValue(array))