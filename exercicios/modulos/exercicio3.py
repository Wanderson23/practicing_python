"""
## Verificar conteúdo da String

Escreva um programa em Python para verificar se uma string contém apenas um determinado 
conjunto de caracteres (neste caso, a-z, A-Z e 0-9).

Uma lógica muito util seria para quando for necessário verificar determinados caracteres obrigatórios numa senha por exemplo
"""

import re

def check_caracther(string):
    rule = re.compile(r'[^a-zA-Z0-9]')
    string = rule.search(string)
    return not bool(string)

print(check_caracther("AJDADONajscnasncj"))
#print(check_caracther("@#$%{}"))