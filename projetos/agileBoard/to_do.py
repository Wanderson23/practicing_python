from tabulate import tabulate

class User: 
    """
    Representa um usuário no quadro ágil.
    Atributos:
        name (str): O nome do usuário.
        tasks (list): Lista de tarefas atribuídas ao usuário.
    """
    def __init__(self, name):
        self.name = name
        self.tasks = []

    def __str__(self): #Retorna uma representação em string do usuário.
        return f"User: {self.name}, Tasks: {[task.title for task in self.tasks]}"

class Task: #Representa uma tarefa no quadro ágil.
    def __init__(self, title, description, priority, estimation, assignee=None): #Inicializa uma nova tarefa.
        self.title = title
        self.description = description
        self.priority = priority
        self.estimation = estimation
        self.assignee = assignee
        self.status = "To Do"

    def __str__(self): #Retorna uma representação em string da tarefa.
        return f"Task: {self.title}, Description: {self.description}, Priority: {self.priority}, Estimation: {self.estimation}, Assignee: {self.assignee.name if self.assignee else 'None'}, Status: {self.status}"

class UserStory: #  Representa uma user story no quadro ágil.
    def __init__(self, title, description, value):
        self.title = title
        self.description = description
        self.value = value
        self.tasks = []

    def add_task(self, task): # Adiciona uma tarefa à user story.
        self.tasks.append(task)

    def __str__(self): #Retorna uma representação em string da user story.
        return f"User Story: {self.title}, Description: {self.description}, Value: {self.value}, Tasks: {[task.title for task in self.tasks]}"


class Sprint: #    Representa um sprint no quadro ágil.
    def __init__(self, name, duration):
        self.name = name
        self.duration = duration
        self.user_stories = []

    def add_user_story(self, user_story):
        self.user_stories.append(user_story)

    def __str__(self):
        return f"Sprint: {self.name}, Duration: {self.duration} days, User Stories: {[story.title for story in self.user_stories]}"



class AgileBoard: #Representa o quadro ágil.
    def __init__(self): # Inicializa um novo quadro ágil.
        self.users = []
        self.user_stories = []
        self.sprints = []

    def add_user(self, user): # Adiciona um usuário ao quadro
        self.users.append(user)

    def add_user_story(self, user_story): #Adiciona uma user story ao quadro.
        self.user_stories.append(user_story)

    def add_sprint(self, sprint): #Adiciona um sprint ao quadro.
        self.sprints.append(sprint)

    def find_user(self, name): #Encontra um usuário pelo nome.
        return next((user for user in self.users if user.name.lower() == name.lower()), None)

    def find_task(self, title): #Encontra uma tarefa pelo título.
        for user in self.users:
            for task in user.tasks:
                if task.title == title:
                    return task
        return None

    def __str__(self): #  Retorna uma representação em string do quadro ágil.
        return f"Board Users: {[user.name for user in self.users]}, User Stories: {[story.title for story in self.user_stories]}, Sprints: {[sprint.name for sprint in self.sprints]}"


def display_board(board): #Exibe o estado atual do quadro ágil.
    users_data = [[user.name, ", ".join([task.title for task in user.tasks])] for user in board.users]
    print("\nUsuários:")
    print(tabulate(users_data, headers=["Nome", "Tarefas"], tablefmt="pretty"))

    stories_data = [[story.title, story.description, story.value, ", ".join([task.title for task in story.tasks])] for story in board.user_stories]
    print("\nUser Stories:")
    print(tabulate(stories_data, headers=["Título", "Descrição", "Valor", "Tarefas"], tablefmt="pretty"))

    for sprint in board.sprints:
        print(f"\nSprint: {sprint.name}")
        stories_data = [[story.title, story.description, story.value, ", ".join([task.title for task in story.tasks])] for story in sprint.user_stories]
        print(tabulate(stories_data, headers=["Título", "Descrição", "Valor", "Tarefas"], tablefmt="pretty"))



def get_valid_input(prompt, validation_fn, error_msg): #Obtém uma entrada válida do usuário.
    while True:
        value = input(prompt)
        if validation_fn(value):
            return value
        print(error_msg)


def get_valid_int_input(prompt, error_msg, min_value=None, max_value=None):
    while True:
        try:
            value = int(input(prompt))
            if (min_value is None or value >= min_value) and (max_value is None or value <= max_value): #Obtém uma entrada de int válida do usuário.
                return value
            else:
                print(error_msg)
        except ValueError:
            print(error_msg)




def test_agile_board(): #Função de teste para o quadro ágil.
    board = AgileBoard()
    print("******Cadastrando usuário*******")
    # Adicionando usuários
    while True:
        user_name = input("Digite o nome do usuário ou pressione Enter para terminar: ")
        if not user_name:
            break
        print(f"Usuário(a) {user_name} adicionado(a)")
        user = User(user_name)
        board.add_user(user)
        
        
    # Adicionando user stories
    print("\n******Adicionando user story*****\n")
    while True:
        story_title = input("Digite o título da user story ou pressione Enter para terminar:")
        if not story_title:
            break
        story_description = input("Digite a descrição da user story: ")
        story_value = int(input("Digite o valor da user story (1 a 10, onde 1 é menor valor e 10 é maior valor): "))
        story = UserStory(story_title, story_description, story_value)
        board.add_user_story(story)
        print("User story criado!\n")
        break
        
    # Adicionando tarefas
    print("\n******Adicionando tarefas*****\n")
    while True:
        story_title = input("Digite o título da user story que deseja adicionar tarefas ou pressione Enter para terminar:")
        if not story_title:
            break
        story = next((s for s in board.user_stories if s.title == story_title), None)
        if not story:
            print(f"User story '{story_title}' não encontrada.")
            continue
        while True:
            task_title = input(f"Digite o título da tarefa para adicionar ao user story {story_title} ou pressione Enter para terminar a adição de tarefas: ")
            if not task_title:
                break
            task_description = input("Digite a descrição da tarefa: ")
            task_priority = input("Digite a prioridade da tarefa (High, Medium, Low): ")
            task_estimation = int(input("Digite a estimativa da tarefa em horas: "))
            assignee_name = input("Digite o nome do responsável pela tarefa: ")
            assignee = board.find_user(assignee_name)
            if not assignee:
                print(f"Usuário {assignee_name} não encontrado. Por favor, adicione o usuário antes.")
                continue
            task = Task(task_title, task_description, task_priority, task_estimation, assignee)
            assignee.tasks.append(task)
            story.add_task(task)
            print(f"{assignee_name} será o responsável pela tarefa {task_title}")
            add_more = input("Deseja adicionar mais tarefas a esta user story? (sim/não): ")
            if add_more.lower() != 'sim':
                break

    # Adicionando sprints
    print("\n******Adicionando sprints*****\n")
    while True:
        sprint_name = input("Digite o nome do sprint ou pressione Enter para terminar: ")
        if not sprint_name:
            break
        sprint_duration = get_valid_int_input("Digite a duração do sprint em dias: ", "Duração inválida. Digite um número válido.")
        sprint = Sprint(sprint_name, sprint_duration)
        board.add_sprint(sprint)

        # Associar user stories aos sprints
        while True:
            story_title = input("Digite o título da user story para adicionar ao sprint ou pressione Enter para terminar: ")
            if not story_title:
                break
            story = next((s for s in board.user_stories if s.title == story_title), None)
            if not story:
                print(f"User story '{story_title}' não encontrada.")
                continue
            print(f"User Story: {story.title}, Description: {story.description}, Value: {story.value}")
            print(f"Tarefas associadas à User Story {story_title}:")
            for task in story.tasks:
                print(task)
            sprint.add_user_story(story)
            print(f"User story '{story_title}' foi associada ao sprint '{sprint_name}'.")
            add_more_stories = input("Deseja adicionar mais user stories a este sprint? (sim/não): ")
            if add_more_stories.lower() != 'sim':
                break

      # Exibindo o estado final do quadro ágil
    print("\nEstado final do quadro ágil:")
    display_board(board)


    # Atualizando status de uma tarefa
    while True:
        task_title = input("\nDigite o título da tarefa para atualizar o status ou pressione Enter para terminar: ")
        if not task_title:
            break
        task = board.find_task(task_title)
        if not task:
            print(f"Tarefa {task_title} não encontrada.")
            continue
        new_status = input(f"Digite o novo status para a tarefa '{task_title}': ")
        task.status = new_status
        print(f"Status da tarefa '{task_title}' atualizado para '{new_status}'.")
        break
    
     # Exibindo o estado final do quadro ágil após atualização
    print("\nEstado final do quadro ágil após atualização:")
    display_board(board)

# Chama a função de teste
test_agile_board()
