# -*- coding: utf-8 -*-

def sumd( n ):
    for i in range( 101 ):
        n *= 100
    x = 10**101
    lx = 0
    while x != lx:
        lx = x
        x = (x + n/x)/2
    x = str(x)
    s = 0
    for i in range( 100 ):
        s += int(x[i])
    return s


sqrs = [4,9,16,25,36,49,64,81]
su = 0
for n in range( 2, 100 ):
    if n not in sqrs:
        su += sumd( n )
        print(su)


