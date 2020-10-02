'''

                            PRIME NUMBER in python
'''
def Prime(n)
    Flag=0
    for i in range(2,n):
         if n%i==0:
             Flag=1
         else:
             Flag=0
    return Flag       
e=int(input())
f=Prime(e)
if f==0:
    print("the number is prime")
else:
    print("the number is non prime")

