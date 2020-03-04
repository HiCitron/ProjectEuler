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


def pf( n , p):
    k = 0
    pf = []
    while n != 1:
        if n%p[k] == 0:
            pf.append( p[k] )
            while n%p[k] == 0:
                n = n/p[k]
        else:
            k += 1
    return pf


def distinct( a, b):
    c = []
    for i in range( len(a) ):
        bo = True
        for k in range( len(b) ):
            if a[i] == b[k]:
                bo = False
                break
        if bo:
            c.append(a[i])
    
    for k in range( len(b) ):
        bo = True
        for i in range( len(a) ):        
            if a[i] == b[k]:
                bo = False
                break
        if bo:
            c.append(b[k])
    return c


def f47( k, p ):
    t1 = pf( k, p)
    for n in range(k+1, k + 4):
        t2 = pf( n, p)
        t = distinct( t1, t2)
        if len(t) < 8:
            return False
        else:
            t1 = t2[:]
    return True
    
p = iniprem( 150000 )

k = 100000
while not f47( k, p ):
    k += 1
    if k%1000 == 0:
        print(k)
print( k )