import numpy as np
# Написать функцию, принимающую на вход матрицу 5х3 и считающую длину каждого вектора в
# матрице (строка) и ищущую самый длинный вектор, вернуть его координаты и длину.
# Как выглядит матрица:
#  | x | y | z |
#  | 1 | 2 | 3 |
#  | 3 | 4 | 1 |
#  | ... |

def getLength(vector):
    return np.sqrt(vector[0]**2 + vector[1]**2 + vector[2]**2)

def getMaxVector(vector):
    maxVector = vector[0]
    for i in vector:
        if getLength(i) > getLength(maxVector):
            maxVector = i
    return maxVector

vector = np.random.randint(0,10,(5,3))
print(*vector, sep="\n")
maxVector = getMaxVector(vector)
print("Max Vector: ", maxVector)
print("Length: ", getLength(maxVector))