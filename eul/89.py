# -*- coding: utf-8 -*-

handle = open('89.txt','r')
text = handle.read()
num = text.split('\n')
handle.close()

def toDIGIT(s):
    conv = { 'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
    nb = 0
    i = 0
    while i < len(s)-1:
        if conv[s[-i-1]] > conv[s[-i-2]]:
            nb = nb + conv[s[-i-1]] - conv[s[-i-2]]
            i += 1
        else:
            nb += conv[s[-i-1]]
        i += 1
    nb += conv[s[0]]
            
    return nb
    
def toROMAN(x):
    s = str(x)
    r = ''
    for i in range( len(s) ):
        r += toROMANn(int(s[i]),len(s)-i)
    return r

def toROMANn(x,n):
    if n==1:
        if x == 1:
            return 'I'
        elif x == 2:
            return 'II'
        elif x == 3:
            return 'III'
        elif x == 4:
            return 'IV'
        elif x == 5:
            return 'V'
        elif x == 6:
            return 'VI'
        elif x == 7:
            return 'VII'
        elif x == 8:
            return 'VIII'
        elif x == 9:
            return 'IX'
    elif n==2:
        if x == 1:
            return 'X'
        elif x == 2:
            return 'XX'
        elif x == 3:
            return 'XXX'
        elif x == 4:
            return 'XL'
        elif x == 5:
            return 'L'
        elif x == 6:
            return 'LX'
        elif x == 7:
            return 'LXX'
        elif x == 8:
            return 'LXXX'
        elif x == 9:
            return 'XC'
    elif n==3:
        if x == 1:
            return 'C'
        elif x == 2:
            return 'CC'
        elif x == 3:
            return 'CCC'
        elif x == 4:
            return 'CD'
        elif x == 5:
            return 'D'
        elif x == 6:
            return 'DC'
        elif x == 7:
            return 'DCC'
        elif x == 8:
            return 'DCCC'
        elif x == 9:
            return 'CM'
    elif n==4:
        if x == 1:
            return 'M'
        elif x == 2:
            return 'MM'
        elif x == 3:
            return 'MMM'
        elif x == 4:
            return 'MMMM'
    return ''

t = 0
dig = []
rom = []
for i in range( len(num) ):
    dig.append( toDIGIT( num[i] ) )
    rom.append( toROMAN( dig[-1] ) )
    if rom[-1] <> num[i]:
        t += len(num[i]) -len(rom[-1])
        print(t)


