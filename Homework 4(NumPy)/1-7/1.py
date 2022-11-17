import numpy as np
from random import randint
# Даны четыре действительных числа: x1, y1, x2, y2. Напишите функцию distance(x1, y1, x2, y2),
# вычисляющая евклидово расстояние
def calculateDistance(x1, x2, x3, x4):
    vector1 = np.array([x1, x2])
    vector2 = np.array([x3, x4])
    return np.sqrt(np.dot(vector1-vector2, vector1-vector2))

x1 = randint(1, 10); x2 = randint(1,10); x3 = randint(1,10); x4 = randint(1,10)
print(x1,x2,x3,x4)
print(calculateDistance(x1,x2,x3,x4))