'''

                            Fibonnaci series in python
'''
def Fibonacci(c):
    a=0
    b=1
    n=int(input("enter the value of n"))
    print(a,b)
    for i in range(2,n-2):
         c=a+b
         a,b=b,c 
         return c
e=0
f=Fibonacci(e)
print("the Fibonacci series is",f)


