# -*- coding: utf-8 -*-
from math import sqrt

def importprem():
    f = open('500prem.txt')
    txt = f.read()
    f.close()
    prem = txt.split(' ')
    prem.pop()
    for i in range( len(prem) ):
        prem[i] = int( prem[i] )
    return prem

def gentable( prem ):
    t = prem[:]
    m = prem[-1]
    k = 0
    while prem[k] < int(sqrt(m)):
        i = 1
        while prem[k]**(2**i) < m:
            t.append( prem[k]**(2**i) )
            i += 1
        k += 1
    t.sort()
    temp = 0
    while len(t) <> 500500:
        temp += 1
        t.pop()
    print(temp)
    return t

prem = importprem()
t = gentable( prem )

n = 1
for i in range( len(t) ):
    n *= t[i]
    n = n%500500507
print(n)
