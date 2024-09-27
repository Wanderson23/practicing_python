names = []

with open("4 -Arquivos/dados/names.txt", "r", encoding="utf-8") as file:
    for line in file:
        names.append(line.rstrip())
        
for name in sorted(names): #Metodo sorted para ordenar a lista
    print(f"Olá, {name}")
    
        
 