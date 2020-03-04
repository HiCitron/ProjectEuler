# -*- coding: utf-8 -*-

n = 100
# 1,2,1 1,4,1 1,6,1 1

def cx(k,n):
    if k == n:
        return 2
    else:
        if (n-k)%3 == 2:
            return 2*(int((n-k)/3)+1)
        else:
            return 1

def sumd(n):
    x = str(n)
    s = 0
    for i in range(len(x)):
        s += int(x[i])
    return s

for i in range(n):
    un = [ cx(0,i), 1 ]
    for k in range(1,i+1):
        un = [ un[0]*cx(k,i) + un[1], un[0] ]
    print(un, sumd(un[0]) )
        
