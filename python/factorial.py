# Factorial of a number

def factorial(n):
   
           
    if n == 0: 
        return 1
      
    return n * factorial(n-1) 
   


num = int(input())
print('Factorial: {}'.format(factorial(num)))
