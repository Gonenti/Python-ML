import numpy as np

# Написать функцию, принимающую на вход 2 вектора целых чисел A и B.
# Функция должна находить числа, встречающиеся в обоих векторах и добавлять их по возрастанию в
# глобальную переменную - вектор Z.
# Если пересечений нет, то вектор Z будет пустым.
# Протестировать на нескольких заданных вами примерах.

Z = np.zeros(6)
def addInZ(vector1, vector2):
    global Z
    vector1, vector2 = vector1[0], vector2[0]
    matchCounter = 0
    for i in range(len(vector1)):
        for j in range(len(vector2)):
            if vector1[i] == vector2[j]:
                Z[matchCounter] = vector1[i]
                matchCounter += 1


vector1 = np.random.randint(10,99,(1,3))
vector2 = np.random.randint(10,99,(1,3))
addInZ(vector1, vector2)
print("Vector 1: ", vector1[0])
print('Vector 2: ', vector2[0])
print("Z: ", Z)