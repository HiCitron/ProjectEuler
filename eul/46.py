# -*- coding: utf-8 -*-
from math import sqrt

def isprem(x):
    if x % 2 == 0:
        return False
    else:
        for i in range(3, int( 1 + sqrt(x)), 2 ):
            if x % i == 0:
                return False
        return True


def Conj( k, p, s):
    for a in range( len(p) ):
        b = 0
        nb = s[b]*2 + p[a]
        while nb <= k:
            nb = s[b]*2 + p[a]
            if nb == k:
                return True
            b += 1
    return False
    
    
b = True
s = [0,1,4,9,16,25]
p = [2,3,5]

k = 5
while Conj(k, p, s):
    k += 2
    s.append(k*k-2*k+1)
    s.append(k*k)
    if isprem(k):
        p.append(k)

print( k )
    
