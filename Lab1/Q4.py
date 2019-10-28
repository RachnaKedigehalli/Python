import math
a=input("Enter length of side 1:")
b=input("Enter length of side 2:")
x = (a*a) + (b*b)
c = math.sqrt(x)
if(a>0 and b>0):
	print("Length of the hypotenuse is:"+ str(c))
else:
	print("Invalid input")
