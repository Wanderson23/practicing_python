import math
import statistics

def menu():
    print("Calculadora Científica")
    print("1. Adição")
    print("2. Subtração")
    print("3. Multiplicação")
    print("4. Divisão")
    print("5. Seno")
    print("6. Cosseno")
    print("7. Tangente")
    print("8. Logaritmo")
    print("9. Exponencial")
    print("10. Média")
    print("11. Mediana")
    print("12. Variância")
    print("13. Desvio Padrão")
    print("0. Sair")

def get_numbers():
    nums = input("Digite os números separados por espaço: ").split()
    return [float(num) for num in nums]

def main():
    while True:
        menu()
        choice = input("Escolha uma opção: ")
        
        if choice == '0':
            break
        elif choice in ['1', '2', '3', '4']:
            num1 = float(input("Digite o primeiro número: "))
            num2 = float(input("Digite o segundo número: "))
            if choice == '1':
                print(f"Resultado: {num1 + num2}")
            elif choice == '2':
                print(f"Resultado: {num1 - num2}")
            elif choice == '3':
                print(f"Resultado: {num1 * num2}")
            elif choice == '4':
                print(f"Resultado: {num1 / num2}")
        elif choice in ['5', '6', '7', '8', '9']:
            num = float(input("Digite um número: "))
            if choice == '5':
                print(f"Resultado: {math.sin(num)}")
            elif choice == '6':
                print(f"Resultado: {math.cos(num)}")
            elif choice == '7':
                print(f"Resultado: {math.tan(num)}")
            elif choice == '8':
                print(f"Resultado: {math.log(num)}")
            elif choice == '9':
                print(f"Resultado: {math.exp(num)}")
        elif choice in ['10', '11', '12', '13']:
            nums = get_numbers()
            if choice == '10':
                print(f"Resultado: {statistics.mean(nums)}")
            elif choice == '11':
                print(f"Resultado: {statistics.median(nums)}")
            elif choice == '12':
                print(f"Resultado: {statistics.variance(nums)}")
            elif choice == '13':
                print(f"Resultado: {statistics.stdev(nums)}")
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()