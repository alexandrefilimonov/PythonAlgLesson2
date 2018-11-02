i=1
n = int(input("Enter integer number more than 0:"))
s = 1.0 
while  (i<n) :
    k = 5**i/10**i 
    if(i%2==0) :
        s+=k
    else :
        s-=k	    		
    i+=1
print("Sum is ",s)