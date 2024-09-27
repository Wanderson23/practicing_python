from exercício_agenda import add_contact, view_contacts, delete_contacts

def main():
    while True:
        print("\nAgenda de contatos\n")
        print("1. Adicione Contato")
        print("2. Listar Contato")
        print("3. Remover Contato")
        print("4. Sair")
        
        choice = input("Escolha a opção (1-4)\n")
        if choice == "1":
            add_contact()
        if choice == "2":
            view_contacts()
        if choice == "3":
            delete_contacts()
        if choice == "4":
            break
        else: 
            print("Informe uma opção valida")
            
main()