string = str(input("Enter your string: "))
print(*[i for i in string if i.isupper()], sep='')