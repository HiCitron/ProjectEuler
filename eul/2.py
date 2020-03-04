# -*- coding: utf-8 -*-
U = [1,1]
s = 0
while U[-1] < 4000000:
    U.append(U[-1]+U[-2])
    if U[-1]%2 == 0:
        s += U[-1]
print(s)