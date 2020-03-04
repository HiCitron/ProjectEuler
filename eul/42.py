# -*- coding: utf-8 -*-
fichier = open("42.txt")
text = fichier.read()
tab = text.split('","')
tab[0] = 'A'
tab[-1] = 'YOUTH'
t = []
for i in range(len(tab)):
    s = 0
    for k in range(len(tab[i])):
        s += ord(tab[i][k])-64
    t.append(s)


res = []
for i in range(len(t)):
    k = 0
    while k*(k+1)*0.5 < t[i]:
        k += 1
    if k*(k+1)*0.5 == t[i]:
        res.append([tab[i],t[i],k])
print(res,len(res))