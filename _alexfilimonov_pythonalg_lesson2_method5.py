k = 32
n = 127
s = ""
i = 0
while  (k<=n) :   
    s+=(" "+chr(k))
    i+=1	
    if (i==10) :
        print(s)	
        s=""    	
        i=0
    k+=1
print(s)
