# На вход функция more_than_five(lst) получает список из целых чисел. Результатом работы функции
# должен стать новый список, в котором содержатся только те числа, которые больше 10 по модулю
from random import randint
def more_than_five(lst):
    return [i for i in lst if abs(i) > 10]

lst = [randint(-30, 30) for i in range(10)]
print("Before executing the function: ", lst)
print("After executing the function: ", more_than_five(lst))