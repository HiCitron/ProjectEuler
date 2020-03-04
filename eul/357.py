# -*- coding: utf-8 -*-
from math import sqrt

def prem( n ):
    prem = [2]
    k = 3
    while k <> n:
        i = 0
        b = True
        while prem[i] <= sqrt(k):
            if k % prem[i] == 0:
                b = False
                break
            i += 1
        if b:
            prem.append( k )
        k += 1
    return prem

p = prem( 1000 )

def isOK( n, prem ):
    k = 1
    while k <= sqrt(n):
        if n%k == 0:
            if n//k <> k:
                if not n//k + k in prem:
                    return False
            else:
                return False
        k += 1
    return True

n = 0
while n < 100000000:
    n += 2
    
