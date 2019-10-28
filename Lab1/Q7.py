n = input("Enter amount:")
n200 = n - n%200
a=n%200

n50= a- a%50
b = a%50

n10 =b - b%10
c=b%10

n5 = c - c%5
d = c%5

n2 = d - d%2
n1= d%2

x=(n200/200) + (n50/50) + (n10/10) + (n5/5) + (n2/2) + n1
print ("Smallest number of notes required:"+ str(x))
