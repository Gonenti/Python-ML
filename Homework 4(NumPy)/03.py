import numpy as np
import numpy.random as rand
# Создайте случайную матрицу и вычтите из каждой строки среднее.

array = rand.randint(1, 10, (rand.randint(1, 10), rand.randint(1, 10)))
print('Before subtraction:')
print(array)
print()
print('After subtraction:')
print(array - np.mean(array))