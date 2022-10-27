number = str(input("Enter number: "))

def correctNumber(number: str):
    newNumber = ""

    for i in number:
        if i in ['1', '2', '3', '4', '5', '6', '7', '8', '9']:
            newNumber += i
    return newNumber

number = correctNumber(number)


if len(number) == 0:
    print("value cannot be calculated")
else:
    result = 1
    for i in number:
        result *= int(i)

    print(result)
