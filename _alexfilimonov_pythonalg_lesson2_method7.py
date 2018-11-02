def checksum(n):
    i=1
    sum1=0
    sum2=0
    while  (i<=n) :
        sum1=sum1+i	
        i+=1
    sum2=n*(n+1)/2	
    if  sum1 == sum2 : 
        print("Sums are equal!")
    else :
        print("Sums are NOT equal!")
print("Please enter natural number N:") 
n = int(input("N:"))
checksum(n) 
