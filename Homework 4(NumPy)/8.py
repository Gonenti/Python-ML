import numpy as np
# Написать функцию, принимающую на вход массив 16x16 и считающую сумму по блокам 4x4.
# Протестировать на нескольких заданных вами примерах

array = np.random.randint(10,99,(16,16))
print('Matrix:')
print(array)

def Sum(array):  
    blockCount = 0
    for i in range(0, 16,4):
            for j in range(0,16,4):
                blockCount += 1
                print(f'Block: {blockCount}')
                print(array[i:i+4,j:j+4])
                print('Sum of block: ',np.sum(array[i:i+4,j:j+4]))

Sum(array)