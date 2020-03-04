# -*- coding: utf-8 -*-
from math import sqrt

def iniprem(n):
    p = [2]
    for i in range(3,n):
        k = 0
        b = True
        while sqrt(i) >= p[k]:
            if i % p[k] == 0:
                b = False
                break
            k += 1
        if b:
            p.append(i)
    return p

def isprime(n, p):
    k = 0
    while sqrt(n) >= p[k]:
        if n % p[k] == 0:
            return False
            break
        k += 1
    return True

p = iniprem( 10000 )

maxi = 0
for i in range(len(p)):
    s = 0
    k = i
    while s < 1000000:
        s += p[k]
        k += 1
        if isprime(s,p) and s < 1000000 and (k-i) > maxi:
            maxi = (k-i)
            print(s, k-i)
    
    