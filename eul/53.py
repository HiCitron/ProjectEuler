# -*- coding: utf-8 -*-

def etage(n):
    t = [1]
    for i in range(n-2):
        t.append(0)
    t.append(1)
    return t


t = [[1],[1,1]]
for i in range(2,101):
    t.append(etage(i+1) )
    for k in range(1, int(i+1/2) ):
        t[i][k] = t[i-1][k] + t[i-1][k-1]
        if t[i][k] > 10**6:
            t[i][k] = 10**6
        t[i][i-k] = t[i][k]

n = 0
for i in range( len(t) ):
    for k in range( len(t[i]) ):
        if t[i][k] == 10**6:
            n+=1
print(n)