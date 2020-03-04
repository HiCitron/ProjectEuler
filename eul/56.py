# -*- coding: utf-8 -*-

def sumd(n):
# n = 569
    s = 0
    k = len(str(n))-1
    while k >= 0:
        a = int(n/10**k)
        n -= a*10**k
        s += a
        k -= 1
    return s

m = 0
for a in range(2,100):
    for b in range(2,100):
        t = sumd(a**b)
        if t > m:
            m = t
            print( m, a ,b )
    print(a)
print(m)