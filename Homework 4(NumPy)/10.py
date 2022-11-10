import numpy as np

matrix = np.random.randint(10,99,(10,3))

def checkMatrix(matrix):
    for row in range(len(matrix)):
        if np.all(matrix[row] == matrix[row][0]):
            print(row+1, *matrix[row], "True")
        else:
            print(row+1, *matrix[row], "False")

checkMatrix(matrix)

matrix[9] = np.array([1,1,1])
print()
checkMatrix(matrix)