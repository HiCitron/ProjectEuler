# -*- coding: utf-8 -*-
from math import sqrt

def prem( n ):
    prem = [2,3,5,7]    
    for i in range(11, n, 2):
        b = True
        k = 0
        while sqrt(i) >= prem[k]:
            if i % prem[k] == 0:
                b = False
                break
            k += 1
        if b:
            prem.append( i )
    return prem

p = prem( 10**5 )

def IsPrime( n , prem):
    k = 0
    while sqrt(n) >= prem[k]:
        if n % prem[k] == 0:
            return False
        k += 1
    return True



ms = [1,2,3,4,5,6,7]
for a2 in range( 7 ):
    ms9 = ms[:]
    c2 = ms9.pop( a2 )
    for a3 in range( 6 ):
        ms0 = ms9[:] 
        c3 = ms0.pop( a3 )
        for a4 in range( 5 ):
            ms1 = ms0[:]
            c4 = ms1.pop( a4 )
            for a5 in range( 4 ):
                ms2 = ms1[:]
                c5 = ms2.pop( a5 )
                for a6 in range( 3 ):
                    ms3 = ms2[:]
                    c6 = ms3.pop( a6 )
                    for a7 in range( 2 ):
                        ms4 = ms3[:]
                        c7 = ms4.pop( a7 )
                        c8 = ms4[0]
                            
                        nb = c2*10**6 + c3*10**5 + c4*10**4 + c5*10**3 + c6*10**2 + c7*10 + c8 
                        if IsPrime( nb , p):
                            print( nb , 'yay')
                                