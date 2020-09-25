# Factorial of a number

def factorial(n):
    if n == 1:
        return n
    elif n < 1:
        return ("NA")
    else:
        return n*factorial(n-1)
    


num = int(input())
print('Factorial: {}'.format(factorial(num)))
