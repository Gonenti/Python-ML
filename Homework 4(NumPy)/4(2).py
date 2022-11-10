import numpy as np

# Написать функцию, принимающую на вход массив и вычитающую среднее из каждой строки в
# матрице. Протестировать на нескольких заданных вами примерах.

def subtractTheAverageFromEachRow(array):
    for i in range(len(array)):
        array[i] = array[i] - np.mean(array[i])
    return array

array = np.full((5,5), 5)
print(subtractTheAverageFromEachRow(array))
print()

array = np.array([[1., 2.], [6., 8.], [8., 12.]])
print(subtractTheAverageFromEachRow(array))