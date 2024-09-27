courses = []

with open("4 -Arquivos/dados/courses.csv", "r", encoding="utf-8") as file:
    for line in file:
        language, category = line.rstrip().split(",")
        courses.append(f"{language}-{category}")

for course in sorted (courses, reverse=True): # reverse=True ele ordena de forma descrescente
    print(course)
    