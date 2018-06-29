# -*- coding: utf-8 -*-   

list = ['abc','efg','anc']

for str1 in list:
    print(str1)

def f2(a, b, c=0, *, d, **kw):
    print('a =', a, 'b =', b, 'c =', c, 'd =', d, 'kw =', kw)

args = (1, 2)
kw = {'d': 99, 'x': '#'}

f2(*args, **kw)