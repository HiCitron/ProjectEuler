# -*- coding: utf-8 -*-
from math import sqrt

def prem(n):
    p = []
    for i in range( 2, n ):
        bp = True
        for k in range( 2, int(sqrt(i)) + 1)   :
            if i % k == 0:
                bp = False
                break
        if bp:
            p.append(i)
    return p

p = prem(100000)


k = 0
maxi = 0
b = 0
while b < 1700:
    b = p[k]
    for i in range(1001):
        a = 1 + 2*(500 - i)
        
        n = 0
        while (n*n + a*n + b) in p:
            n += 1
        if n > maxi:
            maxi = n
            print(n, a, b)
    
    k += 1