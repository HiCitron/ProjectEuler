# -*- coding: utf-8 -*-




t = []
for a in range(2,101):
    for b in range(2,101):
        if pow(a,b) not in t:
            t.append( pow(a,b) )
    print(a)