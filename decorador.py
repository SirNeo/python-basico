#!/usr/bin/python
# -*- coding: UTF-8 -*-

def decorador(funcion):
    def funcionDecorada(*args, **kwargs):
        print 'Funcion ejecutada', funcion.__name__
        funcion(*args, **kwargs)
    return funcionDecorada

@decorador
def resta(n,m):
    print(n-m)

resta(10,2)