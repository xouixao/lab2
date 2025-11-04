import math
a = int(input("The first base of the trapezoid "))
b = int(input("The second base of the trapezoid "))
c = int(input("The height of the trapezoid "))
d = math.sqrt(pow(c, 2) + pow((abs(a - b)/2), 2))
print(a + b + 2 * d)
