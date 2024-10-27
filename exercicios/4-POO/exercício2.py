"""
## Classe Produto e método desconto

Desenvolva uma classe em Python para atender as seguintes especificidades de um Produto:

1. Cada produto deve ter um preço e um nome.
2. A classe deve ter um método construtor e o método dundle str.
3. A classe deve ter um método para desconto. O método deve receber o desconto em percentual e realizar o cálculo de quanto ficaria o preço final com o desconto.

"""

    
class Produto:
    def __init__(self, name, price):
        self.name = name
        self.price = price
        
    def __str__(self):
        return f"Produto {self.name} - R$ {self.price} reais"
    
    def discount(self, perc_discount):
        valorDiscount = (self.price/100) * perc_discount
        finalPrice = self.price - valorDiscount
        return int(finalPrice)
        
    
xbox = Produto("Xbox SerieX", 4600)  #Instanciei dois produtos(objetos) para testar o metodo de desconto, passando os parametros
iphone = Produto("Iphone 14pro", 7900)
print(xbox)
print(iphone)
print(xbox.discount(25)) #Para visualizar o metodo discount aqui precisa passar num print pq tem um return no metodo, aplica usando a instancia.metodo(parametro)
print(f"o preço do xbox com o desconto fica: {xbox.discount(10)}")
print(f"o preço do iphone com o desconto fica: {iphone.discount(10)}")