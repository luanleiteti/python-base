#!/usr/bi/env python3

"""
Exibe o relatorio de criancas por atividade.

Imprimir a lista de criacas agrupadas por salas que frequentam cada uma das atividades.
"""

__version__ = '0.0.1'
__author__ = 'Luan Amorim Leite'


sala1 = ['Erik', 'Maia', 'Gustavo', 'Luan', 'Larissa', 'Leticia', 'Livia']

sala2  = ['Carlos', 'Jessica', 'Monica', 'Mariana']

aula_ingles = ['Erik', 'Maia', 'Gustavo', 'Luan', 'Larissa', 'Livia']

aula_espanhol = ['Monica', 'Mariana']

# Quais sao os alunos que fazem parte de casa ativadade ?

ingles_sala1 = []
ingles_sala2 = []

espanhol_sala1 = []
espanhol_sala2 = []


for i in aula_ingles:
    if i in sala1:
        ingles_sala1.append(i)
    elif i in sala2:
        ingles_sala2.append(i)
        
print("Alunos que fazem aula de ingles na sala 1: ", ingles_sala1)
print("Alunos que fazem aula de ingles na sala 2: ", ingles_sala2)