
n = int(input("Enter integer number more than 0:"))
s = str(n)
s2="" 
i=len(s)-1
while  (i>=0) :
    d = s[i:i+1]
    s2+=d	    		
    i-=1
print("Reversed number is ",s2)
