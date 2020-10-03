def binarysearch(sp,ep,l1,item):
    for i in range(sp,ep):
        mid=(sp+ep)//2
        if l1[mid]==item:
            return mid
        elif item>l1[mid]:
            sp=mid+1
        elif item<l1[mid]:
            ep=mid-1
    else:
        return 0
l=eval((input()))
element=int(input())
e_p=len(l)-1
s_p=0
f=binarysearch(s_p,e_p,l,element)
if f!=0:
    print("ELEMENT IS FOUND AT",f)
else:
    print("ELEMENT IS NOT FOUND")

            
