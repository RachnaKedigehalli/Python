mt=input("Amount paid by Abhiraj: ")
bt=input("Amount paid by Leon: ")
m=input("Amount paid by Vigyan: ")
m = m*1.00
total = mt + bt + m
print ("Total expense:" + str(total))	
x = total/3
a = x - mt
l = x - bt
v = x - m
print ("The due amount:")
print ("Abhiraj: " + str(a))
print ("Leon: " + str(l))
print ("Vigyan: " + str(v))
