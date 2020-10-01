'''

                            Palindrome checker by python

'''
#Palindrome check for String inputs.

def palindrome (s):
    r=s[::-1]
    if(r==s):
        print("Yes It is a palindrome")
    else:
        print("No It is not a palindrome")
s = input("Enter a String to check whether it is palindrome or not")
palindrome(s)

#Palindrome check for Number (Integer) inputs.

num=int(input("Enter a number:"))
temp=num
rev=0
while(num>0):
    dig=num%10
    rev=rev*10+dig
    num=num//10
if(temp==rev):
    print("The number is Palindrome!")
else:
    print("The number is Not a palindrome!")

