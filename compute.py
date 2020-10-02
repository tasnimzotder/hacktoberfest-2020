import tkinter

def mp(a,b,c,d):
    x=(a+c)/2
    y=(b+d)/2
    x+=10
    y+=8
    return x,y
def liner(a,b,c,d):
    x=(a-c)**2
    y=(b-d)**2
    dist=(x+y)**(1/2)
    dist=dist//1
    return dist
def getter(x):
    if x==123:
        a=1/(10**12)
        return a
    elif x==234:
        a=0.01
        return a
    elif x==345:
        a=0.001
        return a
    elif x==456:
        a=1/(10**9)
        return a               
def forcecalc(c1,c2,factordenom,dist,factornumerator):
    force=((9*(10**8))*c1*c2)*(factornumerator**2)
    force=force//((dist*factordenom)**2)
    return force
