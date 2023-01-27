#!/usr/bin/env python3
"""
Helo, world! Multi Line Comment.

Dependendo da lingua configurada no ambiente, o programa vai imprimir a 
mensagem abaixo.

Como usar:

Tenha a variavel LANG configurada no ambiente, exemplo:

    export LANG=pt_BR.UTF-8

Execute o programa:

    python3 hello.py
    ou 
    ./hello.py

"""
__version__ = '0.0.1'
__Author__ = 'Luan Amorim Leite'
__license__ = 'UNLICENSE'

import os

current_language = os.getenv("LANG")[:5]
msg = 'Hello, world!'

if current_language == 'pt_BR':
    msg = 'Olá, mundo!'
elif current_language == 'it_IT':
    msg = 'Ciao, mondo!'
elif current_language == 'es_EP':
    msg = 'Hola, mundo!'

print(msg)