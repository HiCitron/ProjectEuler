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

def dfp( n, prem ):
    t = []
    a = n
    k = 0
    while a <> 1:
        if a % prem[k] == 0:
            a /= prem[k]
            t.append( prem[k] )
        else:
            k += 1
    return t

def s( n, prem ):
    t = dfp( n, prem )


p = prem( 1000 )
k = 7830432
print( k, (dfp(k,p)))