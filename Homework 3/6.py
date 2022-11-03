number_of_string = int(input("Enter the number of string: "))

string = []
for i in range(number_of_string):
    string.append(str(input(f"{i + 1})")))

for i in range(number_of_string):
    if i != number_of_string - 1:
        print(string[i].replace("right", "left"), end=", ")
    else:
        print(string[i].replace("right", "left"))