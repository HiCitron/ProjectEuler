# -*- coding: utf-8 -*-
from math import sqrt

def prem( nth ):
    prem = [2]
    k = 3
    while len(prem) <> nth:
        i = 0
        b = True
        while prem[i] <= sqrt(k):
            if k % prem[i] == 0:
                b = False
                break
            i += 1
        if b:
            prem.append( k )
            if len(prem)%(nth/100) == 0:
                print( "Prem list: "+str(int(100*len(prem)/nth))+" %" )
        k += 1
    print( prem[-1] )
    return prem

p = prem( 500500 )
f = open('500prem.txt','w')
for i in range(len(p)):
    f.write( str(p[i]) + ' ' )
f.close()


