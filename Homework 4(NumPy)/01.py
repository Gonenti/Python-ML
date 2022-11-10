import numpy as np

# Создать матрицу размером 10х10 с 0 внутри, и 1 на границах. Например для 3х3.
# 1 1 1
# 1 0 1
# 1 1 1

array = np.full((10,10), 0)
for i in range(10):
    array[0][i] = 1
    array[9][i] = 1
    array[i][0] = 1
    array[i][9] = 1

print(array)