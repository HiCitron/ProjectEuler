# -*- coding: utf-8 -*-

def prem(n):
    p = [2]
    for i in range(3,n+1):
        k = 0
        while i % p[k] != 0:
            if p[k] > i**0.5:
                k = -1
                break
            k += 1
        if k < 0:
            p.append(i)
    return p

p2 = prem(7071)
p3 = prem(368)
p4 = prem(84)
limit = 50000000
t = range(1,limit)
for a in range( len(p2) ):
    print( a, len(p2) )
    for b in range( len(p3) ):
        for c in range( len(p4) ):
            if p2[a]**2 + p3[b]**3 + p4[c]**4 < limit:
                t[p2[a]**2 + p3[b]**3 + p4[c]**4] = 0

s = 0
for i in range( len(t) ):
    if t[i] == 0:
        s += 1
print(s)
            


