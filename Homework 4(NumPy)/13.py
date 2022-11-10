import numpy as np
# Написать функцию, принимающую на вход два вектора одинакого размера и находящую косинус угла
# между векторами. Протестировать на нескольких заданных вами примерах.




def calculateCos(v1, v2):
    dot_pr = v1.dot(v2)
    norms = np.linalg.norm(v1) * np.linalg.norm(v2)
 
    return np.rad2deg(np.arccos(dot_pr / norms))

vector1 = np.random.randint(10,99,(1,3))
vector2 = np.random.randint(10,99,(1,3))

print(calculateCos(vector1[0], vector2[0]))