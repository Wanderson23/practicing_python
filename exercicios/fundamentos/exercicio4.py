"""Contagem Regressiva
Faça um programa para escrever a contagem regressiva do lançamento de um foguete. 
O programa deve imprimir 10, 9, 8, …, 1, 0 e disparar um “beep”."""

import winsound #para o som de beep
x = 10
while x >= 0:
    print(x)
    x -= 1

winsound.Beep(5000, 2000)




"""Tabuada
Faça um programa que calcule a tabuada de um número, com valores iniciais e 
finais informados pelo usuário"""

number = int(input("Tabuada de: \n"))
inicio = int(input("De: \n"))
fim = int(input("Até: \n"))

x = inicio

while x <= fim:
    print(f"Tabuada de {number} x {x} = {number * x}")
    x = x+1
  