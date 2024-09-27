courses = [] #criando lista

with open("4 -Arquivos/dados/courses.csv", "r", encoding="utf-8") as file:
    for line in file:
        language, category = line.rstrip().split(",") #Para cada linha do arquivo, line.rstrip() remove espaços em branco no final da linha, 
        #e split(",") divide a linha em uma lista usando a vírgula como delimitador. A linha é dividida em duas partes: language e category.
        course = {} #criando dicionário
        course["language"] = language
        course["category"] = category
        courses.append(course) #Adicionando o Dicionário à Lista courses:
    print(courses)
    
    def get_language(course):
        return course["language"]
    
    def get_category(course):
        return course["category"]
    
    for course in sorted (courses, key=get_language):
        print(f"{course['language']}-{course['category']}")
        
     