import numpy as np
# Написать функцию, принимающую на вход матрицу MxN и меняющую 2 любые строки в матрице.
# Протестировать на нескольких заданных вами примерах.

def swap(array): 
    buff = np.copy(array[0]) 
    array[0] = array[1] 
    array[1] = buff 
    return array

array = np.array([[ 4, 5, 6], [1, 2, 3]])
print("Before swap:")
print(array)

print()

print("After swap:")
print(swap(array))

print()

array = np.array([[ 1, 1, 1], [0, 0, 0]])
print("Before swap:")
print(array)

print()

print("After swap:")
print(swap(array))