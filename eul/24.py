# -*- coding: utf-8 -*-
import itertools

def permutations(elts, index_list=[]):
    r = itertools.permutations(elts)
    i = 0
    for p in r:
        if i in index_list:
            yield p
        i += 1

print(list(permutations([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], index_list=[999999])))