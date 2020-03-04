# -*- coding: utf-8 -*-

f = open("18.txt")
txt = f.read()

t = txt.split(chr(10))

for i in range(len(t)):
    t[i] = t[i].split(" ")

def combi():
    tab = []
    for i in range(2**14):
        temp = bin(i)[2:]
        while len(temp) != 15:
            temp = '0' + temp
        tab.append(temp)
    return tab
        
comb = combi()

maxi = 0
for i in range( len(comb) ):
    s = 0
    d = 0
    for k in range(15):
        d += int( comb[i][k] )
        s += int( t[k][d] )
    if s > maxi:
        maxi = s
        temp = comb[i]
print(maxi)
print(temp)