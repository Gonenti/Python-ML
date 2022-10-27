width = int(input("Enter weidth: "))
hight = width / 3


for j in range(0, int(hight / 2), 1):
    half_line = '-' * int(width / 2 - 1 - j * 3) + ".|." * j
    print(half_line + ".|." + half_line[::-1])

print("-" * int((width / 2) - 3) + "WELCOME" + "-" * int((width / 2) - 3))

for j in range(int(hight / 2) - 1, -1, -1):
    half_line = '-' * int(width / 2 - 1 - j * 3) + ".|." * j
    print(half_line + ".|." + half_line[::-1])