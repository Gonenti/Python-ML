import math

thickness = int(input("Enter thickness: "))
marker = str(input("Enter marker: "))

#Top Cone
for i in range(1, thickness * 2, 2):
    print((thickness - int(i / 2))  * " " +  (i * marker))


#Top Pillars
for i in range(thickness + 1):
    print(math.ceil(thickness / 2) * " " + thickness * marker + (thickness * 3 * " ") + thickness * marker)

#Middle Belt
for i in range(math.ceil(thickness / 2)):
    print(math.ceil(thickness / 2) * " " + marker * thickness * 5)

#Bottom Pillars
for i in range(thickness + 1):
    print(math.ceil(thickness / 2) * " " + thickness * marker + (thickness * 3 * " ") + thickness * marker)

#Bottom Cone
for i in range(thickness * 2 - 1, 0, -2):
    print(" " * (thickness * 4)  + (thickness - int(i / 2))  * " " +  (i * marker))
