import math
a=input("Enter side 1:")
b=input("Enter side 2:")
x = pow(a,2) + pow(b,2)
c = math.sqrt(x)
if(a>0 and b>0):
	print("Length of the hypotenuse is:"+ str(c))
else:
	print("Invalid input")
