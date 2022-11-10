import numpy as np
import math
# Написать функцию, принимающую на вход вектор A содержит float числа как больше, так и меньше
# нуля.
# Функция должна округлить их до целых и результат записать в глобальную переменную Z. Округление
# должно быть "от нуля", т.е.:
# * положительные числа округляем всегда вверх до целого
# * отрицательные числа округляем всегда вниз до целого
# * 0 остаётся 0
# Протестировать на нескольких заданных вами примерах.

Z = np.zeros(3)

def round(matrix):
    global Z
    matrix = matrix[0]
    for i in range(len(matrix)):
        if matrix[i] > 0:
            Z[i] = math.ceil(matrix[i])
        else:
             Z[i] = math.floor(matrix[i])

matrix = np.random.uniform(-10, 10, (3, 3))
round(matrix)
print(matrix[0])
print(Z)