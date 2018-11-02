n = int(input("Enter integer number more than 0:"))
s = str(n)
i=len(s)-1
n1=0
n2=0
while  (i>=0) :
    d = int(s[i:i+1])
    if (d%2==1) :
        n2+=1
    else :
        n1+=1        	
    i-=1
#четные	
print("Even digits qty is ",n1)

#нечетные	
print("Odd digits qty is ",n2)
