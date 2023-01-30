#!/usr/bin/env python3

"""
imprimre a  tabuada de 1 a 10
"""

__version__ = '0.0.1'
__author__ = 'Luan Amorim Leite'

numeros = list(range(1, 11))

for numero in numeros:
    print("tabuada do: ", numero)
    for outro_numero in numeros:
        print(numero * outro_numero)
    print("-----------------")