# -*- coding: utf-8 -*-
# last 10 digits of 28433×2^7830457+1
# 7830457 = 7830456 + 1 = 641*509*24 + 1
k = 2**641
k = k % 10**10
k = (k**509)
k = k % 10**10
k = (k**24)
k = k % 10**10
k *= 2*28433
k = k % 10**10
k += 1
k = k % 10**10
print(k)