"""
## Avaliação e Média da Nota de Filmes

Desenvolva novas funcionalidades para complementar o nosso gerenciamento da classe Filmes. Segue o escopo das funcionalidades:

1. Uma das funcionalidades requeridas é que o usuário possa realizar a avaliação de um filme passando uma nota com parâmetro e que essa nota seja salva no 
atributo específico da classe.
2. Assim que uma avaliação for realizada, deve ser incrementado o total de avaliadores daquele filme. Obs: Considere criar um atributo específico para esse fim.
3. Para cada filme, ter uma nota de avaliação média que consiste na divisão do total de avaliação pelo total de avaliadores.
"""

# criar um metodo para avaliar um filme


class avalia:
    def __init__(self, name, yearLaunch, includedPlan, durationMinutes): #Metodo construtor
        self.name = name
        self.yearLaunch = yearLaunch
        self.includedPlan = includedPlan
        self.totalEvaluation = 0
        self.durationMinutes = durationMinutes
        self.evaluators = 0
                
    def __str__(self): #Metodo para sobescrever uma informação
        return f"Filme: {self.name} \nNota: {self.totalEvaluation}"    
    
    def technical_sheet(self):
        print("**Dados do filme**")
        print(f"Nome do filme: {self.name}")
        print(f"Ano de lançamento: {self.yearLaunch}")
        print(f"Está no plano? {self.includedPlan}")
        print(f"Avaliação do filme: {self.totalEvaluation}")
        print(f"Duração do filme {self.durationMinutes}")
        print(f"Total avaliadores: {self.evaluators}\n")
        
    def evaluate(self, note):
        self.totalEvaluation += note 
        self.evaluators += 1
        
    def average(self): #average, metodo para calcular média
        print(f"Média do filme {self.name}: {self.totalEvaluation / self.evaluators} \n")
        

mario = avalia("Super Mario", 2023, True, 135)
avatar = avalia("Avatar", 2023, False, 220)
mario.evaluate(9.5)
mario.evaluate(10)
mario.evaluate(8.5)
mario.technical_sheet()
mario.average()
avatar.evaluate(8.5)
avatar.evaluate(9)
avatar.technical_sheet()
avatar.average()