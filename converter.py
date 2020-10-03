def reverse(a):
          l=len(a)
          b=''
          for i in range(l-1,-1,-1):
                    b=b+a[i]
          return b
def hexpicker(n):
    n=int(n)
    if n>=10:
        if n==10:
            z='A'
        elif n==11:
            z='B'
        elif n==12:
            z='C'
        elif n==13:
            z='D'
        elif n==14:
            z='E'
        elif n==15:
            z='F'
    else:
        z=str(n)
    return z

def binary(n):
    n=int(n)
    b=''
    while n!=0:

        a=n%2
        b+=str(a)
        n=n//2
    return reverse(b)
def decimal(na):
    w=int(na)
    count=0
    s=0
    while w!=0:
        a=w%10
        s+=(a*(2**count))
            
        count+=1
        w=w//10
    return str(s)




def octal(n):
    
    l=str(n)
    size=len(l)
    if size>=3:
        s=size%3
        a=''
        d=''
        l=list(l)
        if s!=0:
            
            if s==1:                
                a=l.pop(0)
            else:
                a=l.pop(0)
                a+=l.pop(0)
                a=decimal(a)
        size=len(l)
        count=1
        
        for i in range(size-1,-1,-1):    
            if count==1:  
                c=l[i-2]+l[i-1]+l[i]
                d=decimal(c)+d
                count=3
            else:
                count-=1
        f=a+d
    else:
        f=decimal(l)
        
    return f




def hexadecimal(n):
    l = str(n)
    size=len(l)
    if size>=4:
        l=list(l)

        s=size % 4
        a=''
        if s!=0:

            if s==1:

                a=l.pop(0)
            elif s==2:
                a=l.pop(0)
                a+=l.pop(0)
            elif s==3:
                a=l.pop(0)
                a+l.pop(0)
                a+= l.pop(0)

        size=len(l)
        count=1
        d=''
        for i in range(size - 1, -1, -1):

            if count==1:
                de=decimal(l[i-3]+l[i-2]+l[i-1]+l[i])
                if de=="0000":
                    c='0'
                    d=c+d
                else:
                    
                    c=hexpicker(de)
                    d=c+d
                    count= 4
            else:
                count-= 1
        m=decimal(a)
        f=m+d
    else:
        f=decimal(l)

    return f


def hex2bin(inp):
    a=''
    for i in inp:
        if i=="A" or i=="B" or i=="C" or i=="D" or i=="E" or i=="F" :
            if i=="A":
                a+="1010"
            elif i=="B":
                a+="1011"
            elif i=="C":
                a+="1100"
            elif i=="D":
                a+="1101"
            elif i=="E":
                a+="1110"
            elif i=="F":
                a+="1111"
        else:
            b=int(i)
            c=binary(b)
            while len(c)!=4:
                c='0'+c

            a+=c
    return a


def oct2bin(inp):

    s=''

    for i in inp:

        a=int(i)
        a=binary(a)
        while len(a)!=3:
            a='0'+a

        s+=str(a)

    return s






