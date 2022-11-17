from random import randint
# Написать функцию season(month), принимающую 1 аргумент — номер месяца (от 1 до 12), которая
# присваивает глобальной переменной s время года, которому этот месяц принадлежит (зима, весна,
# лето или осень).

s = ""

def changeS(number: int):
    global s
    winter = [12, 1, 2]
    spring = [3, 4, 5]
    summer = [6, 7, 8]
    fall = [9, 10, 11]

    if number in winter:
            s = "winter"

    elif number in spring:
        s = 'spring'
    
    elif number in summer:
        s = 'summer'
    
    elif number in fall:
        s = 'fall'

number = randint(1,12)
print(number)
changeS(number)
print(s)