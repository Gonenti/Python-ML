import numpy as np
# Создать 5x5 матрицу с 1,2,3,4 над диагональю. Все остальные элементы - 0

array = np.full((5,5), 0)
for i in range(1, 5):
    array[i-1][i] = i

print(array)