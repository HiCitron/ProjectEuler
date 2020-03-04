# -*- coding: utf-8 -*-
from math import sqrt
mini = int(sqrt(1020304050607080900))-1
maxi = int(sqrt(1929394959697989990))+1

def ok(x):
    x = str(x)
    if x[18] == '0':
        if x[16] == '9':
            if x[14] == '8' and x[12] == '7' and x[10] == '6':
                if x[8] == '5' and x[6] == '4' and x[4] == '3' and x[2] == '2' and x[0] == '1':
                    return True
    return False

for k in range(380):
    print(k)
    for i in range(0,1000000):
        a = mini + k*1000000 + i
        if ok(a*a):
            print(a,a*a)