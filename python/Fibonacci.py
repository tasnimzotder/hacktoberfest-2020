"GENERATION OF FIBONACCI SERIES (USING LOOP)"


# Enter number of terms needed                       
a=int(input("Enter the terms"))
f=0                                                  
s=1                                                  
if a<=0:
    print("The requested series is
",f)
else:
    print(f,s,end=" ")
    for x in range(2,a):
        next=f+s                           
        print(next,end=" ")
        f=s
        s=next
        
        
"GENERATION OF FIBONACCI SERIES (USING RECURSION)"

def FibRecursion(n):  
   if n <= 1:  
       return n  
   else:  
       return(FibRecursion(n-1) + FibRecursion(n-2))  
 nterms = int(input("Enter the terms? "))  # take input from the user
  
if nterms <= 0:  # check if the number is valid 
   print("Please enter a positive integer")  
else:  
   print("Fibonacci sequence:")  
   for i in range(nterms):  
       print(FibRecursion(i))
