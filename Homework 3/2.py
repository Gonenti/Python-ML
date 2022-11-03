x = int(input("Enter number: "))

if x % 2 != 0:
    print("Плохо")

elif 2 <= x <= 5:
    print("Неплохо")

elif 6 <= x <= 20:
    print('Так себе')
    
elif x > 20:
    print("Отлично")