n1 = int(input("Enter the number: "))
n2 = 0
flag = True

if n1 < 0:
    flag = True
    n1 *= -1

while n1 > 0:
    digit = n1 % 10
    n1 = n1 // 10
    n2 = n2 * 10
    n2 = n2 + digit  
 
if flag:
    n2 *= -1

print('reverse number:', n2)