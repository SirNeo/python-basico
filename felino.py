#!/usr/bin/python
# -*- coding: UTF-8 -*-

class Felino: #Clase Padre
    @property
    def garras_retractiles(self):
        return True
    
    def cazar(self):
        print('El felino está cazando')

class Gato(Felino):
    def gato_cazador(self):
        self.cazar()

class Jaguar(Felino):
    pass

gato = Gato()
jaguar = Jaguar()

print(gato.garras_retractiles)
print(jaguar.garras_retractiles)