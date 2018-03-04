#!/usr/bin/python
# -*- coding: UTF-8 -*-

def suma(m, n):
    return n+m

def filtrar(n):
    return (n == 'o')

li = [1, -2, 1, -4]
lo = [5, 3, 6, 7]
s = "Hoola Mundo"

print map(suma, li, lo)
print map(lambda m,n: n+m, li, lo)
print filter(lambda n:n=='o', s)
print reduce(suma, lo)

