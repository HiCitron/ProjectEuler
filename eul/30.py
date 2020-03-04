# -*- coding: utf-8 -*-
"""
def fifth(n):
    n = str(n)
    s = 0
    for i in range(len(n)):
        s += int(n[i])**5
    return s
    
    

k = 10
n = 0
s = 0
while k < 1000000:
    k += 1
    if fifth(k) == k:
        n += 1
        s += k
        print( k, n)
print(s)
"""

target = 200
coins = [1, 2, 5, 10, 20, 50, 100, 200]
ways = [1] + [0]*target
print(ways)

for coin in coins:
    for i in range(coin, target+1):
        ways[i] += ways[i-coin]

print "Ways to make change =", ways[target]