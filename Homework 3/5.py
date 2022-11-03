string = str(input("Enter your string: "))

answer = False
word_counter = 0
for i in string.split(" "):
    if word_counter == 3:
        answer = True
    if i.isdigit():
        word_counter = 0
    else:
        word_counter += 1

print(answer)