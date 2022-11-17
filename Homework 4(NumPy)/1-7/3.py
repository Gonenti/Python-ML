from random import randint
# Написать функцию is_prime, принимающую 1 аргумент — число от 0 до 1000, и возвращающую True,
# если оно простое, и False - иначе.

def is_prime(number: int):
    if number in [0, 2]:
        return True

    if number % 2 == 0:
        return False

    for i in range(2, number//2 + 1):
        if number % i == 0:
            return False
    
    return True

number = randint(0,1000)
print(number)
print('result: ', is_prime(3))