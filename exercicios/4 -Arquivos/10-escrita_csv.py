import csv #para manipular arquivos csv

name = input("Informe o nome da linguagem que deseja aprender:\n")
category = input("Qual a categoria que a linguagem se encaixa?\n")

with open("4 -Arquivos/dados/courses.csv", "a", encoding="utf-8") as file:
    writer = csv.writer(file, lineterminator="\n") # .writer: Cria um objeto writer que permite escrever dados no arquivo CSV. lineterminator="\n" especifica que cada linha no arquivo CSV será terminada com uma nova linha
    writer.writerow([name, category]) #Adiciona uma nova linha ao arquivo CSV com os valores name e category inseridos pelo usuário.