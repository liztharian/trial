import random
item=[1,2,3,4,5,6,7,8,9,10]

u=input('enter a number')
l=len(item)/2-1
s= item[l]
#print s
d=u-s
g=s-u
#print g
#print d
if d>1:

    for i in range(l,10):
        if item[i]==u:
            print i+1
if d==0:
    print(l+1)


if g>1:

    for i in range(0,l):
        if item[i]==u:
            print i+1
