"""
## Advinhe o Número

Escreva um programa em Python que gera um número aleatório para que o usuário tente acertar o número. 
Algumas sugestões para o programa:

1. Utilizar um laço de repetição para que o programa execute até que o usuário informe um número referente a opção para sair do programa.
2. Utilizar o módulo random para gerar valores aleatórios dentro de um intervalo. Ex: 1 a 10.
3. Lê o número que o usuário digitar via input e comparar se é o mesmo número que o programa sorteou.

"""

import random

done = False

while not done:
    print("O que voce deseja fazer?")
    print("1. Advinhar um numero")
    print("2. Sair")
    
    choice = input(">")
    
    if choice == "1":
        print("*******Advinhe um numero de 1 a 10******\n")
        number = int(input("Digite um numero de 1 a 10:\n"))
        result = random.randint(1, 10)
        if number == result:
            print("Parabens, voce acertou!!!")
        else:
            print(f"Tente novamente, o numero sorteado foi {result}")
    elif choice == "2":
        done = True
    else:
        print("Opção inválida")