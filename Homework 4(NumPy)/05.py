import numpy as np
#Дан вектор [1, 2, 3, 4, 5], построить новый вектор с тремя нулями между каждым значением

a = np.array([1, 2, 3, 4, 5])
b = np.array(np.zeros(17))
j = 0
for i in range(0, 18, 4):
    b[i] = a[j]
    j += 1
print(b)