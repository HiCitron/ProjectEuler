# -*- coding: utf-8 -*-
from math import sqrt

def premier(x):
    for i in range(2,int(sqrt(x)+1)):
        if x%i == 0:
            return False
    return True

x = 600851475143
for i in range(1,int(sqrt(x)+1)):
    if x%i == 0 and premier(i):
        print(i)