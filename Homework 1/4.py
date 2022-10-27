amount = str(input("Enter amount: "))


def get_Fractional_Part(amount: str) -> str:
    return amount[amount.find("."):]


def get_Integer_Part(amount: str) -> str:
    return amount[0:amount.find(".")]


def get_Result(amount:str) -> str:
    number = ""
    integer_part = get_Integer_Part(amount)
    integer_part = integer_part[::-1]

    for i in range(0, len(integer_part), 1):
        number += ""
        if (i % 3 == 0) and (i != 0) :
            number += ","
        number += integer_part[i]

    fractional_part = get_Fractional_Part(amount)
    if len(fractional_part) > 0:
        number = number[::-1] + "."
        number += str(round(float(fractional_part), 2))[2:]
        
    return number


print(get_Result(amount))