# -*- coding: utf-8 -*-
"""
Created on Tue Apr 19 22:04:10 2016

@author: vanne
"""

import random
import math


#Generacion de una v.a exponencial
def exponencial(l):
    return (- (1.0 / l)) * math.log(random.random())

#Metodo de la transformada inversa    
def met_transformada_inversa(pi):
    i = 0
    s = pi[i]
    r = random.random()
    while s < r:
        i += 1
        s += pi[i]   
    return i
            

def met_composicion(pi,si):
    
    assert sum(pi) == 1

    #seleccionar la distribucion de probabilidad fi(x) con la cual 
    #se va a simular el valor de x
    #Aplicar el metodo de la transformada inversa    
    i = met_transformada_inversa(pi)
    
    return si[i]()

#Funcion de distribucion 
def s1():
    return exponencial(1)

def s2():
    return exponencial(5)
    
s1 = lambda: exponencial(1)    

pi = [0.7, 0.3]
si = [s1, s2]

for _ in range(10):
   print met_composicion(pi,si)