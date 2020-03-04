# -*- coding: utf-8 -*-
# 519432,525806
# 632382,518061 ...
# lines in the format a,b
# value is a^b
# Find which line has the biggest value
from math import log
handle = open('99.txt','r')
text = handle.read()
tab = []
temp = text.split('\n')
for i in range(len(temp)):
    temp2 = temp[i].split(',')
    tab.append( [int(temp2[0]),int(temp2[1])] )
print(tab)

maxi = 0
for i in range( len(tab) ):
    temp = tab[i][1] * log( tab[i][0] )
    if temp > maxi:
        maxi = temp
        indice = i
        print( maxi, indice )