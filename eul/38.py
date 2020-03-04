# -*- coding: utf-8 -*-



for n in range(1,10000):
    s = ''
    k = 1
    while len(s) < 9:
        s += str(n * k)
        k += 1
    if len(s) == 9:
        if ''.join(sorted(s)) == '123456789':
            print (n, k, s)

