import numpy as np
# Написать функцию, принимающую на вход двумерный массив и находящую все различные строки.
# Протестировать на нескольких заданных вами примерах.

def checkMatrix(array):
    for i in range(len(array)):
        flag = False
        for j in range(len(array)):
            if np.array_equal(array[i], array[j]) and i != j:
                flag = True
        if flag:
            print(i+1, 'not a unique string')
        else:
            print(i+1, 'unique string')


matrix = np.random.randint(10,99,(10,3))
print(*matrix, sep="\n")

checkMatrix(matrix)

matrix[8] = np.array([1,1,1])
matrix[9] = np.array([1,1,1])
print()
checkMatrix(matrix)
