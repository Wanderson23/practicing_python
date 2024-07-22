""""Cálculo da Distância

Escreva um programa que pergunte a distância que um passageiro deseja percorrer em km.
Calcule o preço da passagem, cobrando R$ 0,50 por km para viagens de até de 200 km, e R$
0,35 para viagens mais longas."""


distancia = float(input("Digite a distância a percorrer: "))

if distancia <= 200:
    cobranca = 0.5 * distancia
else:
    cobranca = 0.35 * distancia
print(f"O preço da passagem é {cobranca:.2f}") #.2f para formatar em duas casas decimais






"""Aumento salário funcionário

Escreva um programa que pergunte o salário do funcionário e calcule o valor do aumento. Para
salários superiores a R$ 1.250,00, calcule um aumento de 10%. Para os inferiores ou iguais, de
15%."""

salario = float(input("Digite o salário do funcionário: "))
percentual = 0.15

if salario > 1250:
    percentual = 0.10
acrescimo = salario *percentual
print(f"Seu aumento será de {acrescimo:.2f}")
