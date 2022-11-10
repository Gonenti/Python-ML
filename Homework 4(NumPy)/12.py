import numpy as np
# Написать функцию, принимающую на вход два вектора одинакого размера и считающую расстояние
# между векторами. Протестировать на нескольких заданных вами примерах

def calculateDistance(vector1, vector2):
    return np.sqrt(np.dot(vector1-vector2, vector1-vector2))

vector1 = np.random.randint(10,99,(1,3))
vector2 = np.random.randint(10,99,(1,3))

print(calculateDistance(vector1, vector2))