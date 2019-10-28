print ("1. Add\n2. Multiply\n3. Average")
a = input("Enter the operation number:")
x = input("Enter first number: ")
y = input("Enter second number: ")
add = x+y
multiply = x*y
average = (x+y)/2.00
if (a==1):
	print("The sum is: " +str(add))
elif (a==2):
	print("The product is: " + str(multiply))
elif (a==3):
	print("The average is: " +str(average))
