# -*- coding: utf-8 -*-
# Find all nth digit number that are also a nth power
def nd(k):  # returns the nb of digits of a number
    a = str(k)
    return len(a)

nb = 0
n = 1
while 9**n >= 10**(n-1):
    k = 9
    while k**n >= 10**(n-1):
        print( k, n, nd(k**n))
        nb += 1
        k -= 1
    n += 1
print(nb)