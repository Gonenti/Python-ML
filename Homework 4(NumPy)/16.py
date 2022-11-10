import numpy as np
# Написать функцию, принимающую на вход вектор и возвращающую максимальный элемент в векторе
# среди элементов, перед которыми стоит 0.
# Например для:
# x = np.array([6, 2, 0, 3, 0, 0, 5, 7, 0])
# Ответ: 5

def getValue(vector):
    maxValue = 0
    flag = False
    for i in range(len(vector[0])-1):
        if vector[0][i] == 0 and vector[0][i+1] > maxValue:
            flag = True
            maxValue = vector[0][i+1]

    if flag:
        return maxValue
    else:
        return None



vector = np.random.randint(0,10,(1,10))
print("Vector: ", *vector[0])
print(getValue(vector))