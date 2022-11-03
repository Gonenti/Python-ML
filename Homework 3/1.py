number = int(input("Enter number: "))

answer = ""

if number % 3 == 0:
    answer += "Fizz"

# Чтобы не было лишнего пробела
if number % 5 == 0 and number % 3 == 0:
    answer +=' Buzz'
else:
    answer += 'Buzz'


print(answer)