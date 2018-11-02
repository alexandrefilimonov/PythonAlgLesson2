i=0
#i=1 +
#i=2 -
#i=3 *
#i=4 /
n1=-1
n2=-1
while (0<1) :
    if (i==0) : 
        s = str(input("Enter op symbol:"))
    elif (n1==-1) : n1 = int(input("Enter positive number 1:"))
    elif (n2==-1) : n2 = int(input("Enter positive number 2:"))	
    if (n2!= -1 and i==1) :
        print("Sum of numbers",n1," and ",n2," is ",n1+n2)	
        i=0; n1=-1; n2=-1; s=""
    if (n2!= -1 and i==2) :
        print("Substraction of numbers",n1," and ",n2," is ",n1-n2)	
        i=0; n1=-1; n2=-1; s=""
    if (n2!= -1 and i==3) :
        print("Multiplication of numbers",n1," and ",n2," is ",n1*n2)	
        i=0; n1=-1; n2=-1; s=""
    if (n2!= -1 and i==4 and n2==0) :
        print("Its forbidden to divide by 0!")	
        i=0; n1=-1; n2=-1; s=""		
    if (n2!= -1 and i==4) :
        print("Division of numbers",n1," and ",n2," is ",n1/n2)	
        i=0; n1=-1; n2=-1; s=""		
    if (s == "0") :
        break
    elif (s == "+") : i=1
    elif (s == "-") : i=2
    elif (s == "*") : i=3
    elif (s == "/") : i=4
print("Good bye!")

