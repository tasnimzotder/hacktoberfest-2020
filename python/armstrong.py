def armstrong(n,sum=0):
    r=0
    while n!=0:
        r=n%10
        sum=sum+r**3
        n=n//10
    return sum
N=int(input("eneter the number"))
f=armstrong(N)
if N==f:
    print("the number is armstrong")
else:
    print("not")    
