from random import *
k = randint(0,100)
i = 1
b = 0
print("Try to guess number from 0 to 100. You have 10 attempts:")
while  (i<=10 and b==0) :
    print("Attempt #",i,":")	
    n = int(input("Enter number:"))
    if(n==k) :
        print("This is the number!")
        b = 1
    elif(k<n) :
            print("The number is less than ",n)	
    elif(k>n) :
            print("The number is higher than ",n)	
    i+=1	
if (b == 0) :	
    print("The number was ",k)	
