# -*- coding: utf-8 -*-
"""
Created on Thu Apr 21 00:28:22 2016

@author: vanne
"""

import random
import math 

#La idea es generar una variable aleatoria con distribución exponencial de 
#parámetro 1 y luego elevar otra variable aleatoria con distribución 
#uniforme en (0,1) por la variable exponencial.

def exponencial():
    return -math.log(random.random())
    
for _ in range(10):
    print random.random() ** (1/exponencial())