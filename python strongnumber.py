def strongnumber(n):
    sum=0
    r=0
    while n!=0:
        r=n%10
        fact=1
        
        while r!=0:
            fact=fact*r
            r=r-1
            
        sum=sum+fact    
        n=n//10
    return sum

N=int(input("enter the number"))
f=strongnumber(N)
if N==f:
    print("the number is strongnumber")
else:
    print("not")   
