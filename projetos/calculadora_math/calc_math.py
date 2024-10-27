import flet as ft
import math
import statistics

def main(page: ft.Page):
    # Configuração inicial da página
    page.title = "Calculadora Científica"
    page.window_width = 750  # Largura fixa
    page.window_height = 400  # Altura fixa para evitar rolagem
    page.bgcolor = "#000000"  # Fundo preto
    page.window_min_width = 500  # Largura mínima da janela
    page.window_min_height = 500  # Altura mínima da janela

    # Campo de entrada e campo de resultado com estilização
    input_field = ft.TextField(
        label="Digite a expressão",
        expand=True,
        label_style=ft.TextStyle(color="#6699FF"),  # Cor do rótulo em azul vibrante
        bgcolor="#1C1C1C",  # Fundo cinza escuro para contraste
        border_color="#FF1493",  # Rosa vibrante para a borda
        color="#FF1493",  # Texto em rosa vibrante
    )

    result_text = ft.Text(
        value="Resultado: ",
        size=20,
        expand=True,
        color="#FFFFFF"  # Branco para o resultado
    )

    # Função para processar a expressão
    def calculate_expression(e):
        expression = input_field.value.lower().replace("^", "**")  # Aceita "^" para potências
        try:
            # Avalia funções e expressões
            if "sin" in expression:
                result = math.sin(math.radians(float(expression.split("sin")[1].strip("()"))))
            elif "cos" in expression:
                result = math.cos(math.radians(float(expression.split("cos")[1].strip("()"))))
            elif "tan" in expression:
                result = math.tan(math.radians(float(expression.split("tan")[1].strip("()"))))
            elif "log" in expression:
                result = math.log(float(expression.split("log")[1].strip("()")))
            elif "exp" in expression:
                result = math.exp(float(expression.split("exp")[1].strip("()")))
            elif "mean" in expression:
                nums = [float(x) for x in expression.split("mean")[1].strip("()").split(",")]
                result = statistics.mean(nums)
            elif "median" in expression:
                nums = [float(x) for x in expression.split("median")[1].strip("()").split(",")]
                result = statistics.median(nums)
            elif "variance" in expression:
                nums = [float(x) for x in expression.split("variance")[1].strip("()").split(",")]
                result = statistics.variance(nums)
            elif "stdev" in expression:
                nums = [float(x) for x in expression.split("stdev")[1].strip("()").split(",")]
                result = statistics.stdev(nums)
            else:
                # Calcula operações básicas e expressões matemáticas
                result = eval(expression)
            result_text.value = f"Resultado: {result}"
        except Exception as ex:
            result_text.value = f"Erro: {str(ex)}"
        page.update()

    # Função auxiliar para adicionar texto ao campo de entrada
    def append_text_to_input(text):
        input_field.value += text
        page.update()

    # Função para limpar o campo de entrada
    def clear_input(e):
        input_field.value = ""
        result_text.value = "Resultado: "  # Limpa também o resultado
        page.update()

    # Função para definir o estilo de hover
    def on_hover(button: ft.ElevatedButton, is_hovered: bool):
        if is_hovered:
            button.bgcolor = "#FF69B4"  # Cor de fundo rosa vibrante ao passar o mouse
            button.color = "#FFFFFF"  # Cor do texto em branco
        else:
            button.bgcolor = "#1C1C1C"  # Cor de fundo padrão
            button.color = "#FF1493"  # Cor do texto padrão
        button.update()

    # Criando os botões e referenciando-os
    button1 = ft.ElevatedButton("Adição (+)", on_click=lambda e: append_text_to_input(" + "), expand=True,
                                 on_hover=lambda e: on_hover(button1, e.hovered), bgcolor="#1C1C1C", color="#FF1493")
    button2 = ft.ElevatedButton("Subtração (-)", on_click=lambda e: append_text_to_input(" - "), expand=True,
                                 on_hover=lambda e: on_hover(button2, e.hovered), bgcolor="#1C1C1C", color="#FF1493")
    button3 = ft.ElevatedButton("Multiplicação (*)", on_click=lambda e: append_text_to_input(" * "), expand=True,
                                 on_hover=lambda e: on_hover(button3, e.hovered), bgcolor="#1C1C1C", color="#FF1493")
    button4 = ft.ElevatedButton("Divisão (/)", on_click=lambda e: append_text_to_input(" / "), expand=True,
                                 on_hover=lambda e: on_hover(button4, e.hovered), bgcolor="#1C1C1C", color="#FF1493")
    button5 = ft.ElevatedButton("Potência (^)", on_click=lambda e: append_text_to_input(" ^ "), expand=True,
                                 on_hover=lambda e: on_hover(button5, e.hovered), bgcolor="#1C1C1C", color="#FF1493")
    button6 = ft.ElevatedButton("Seno (sin)", on_click=lambda e: append_text_to_input("sin()"), expand=True,
                                 on_hover=lambda e: on_hover(button6, e.hovered), bgcolor="#1C1C1C", color="#FF1493")
    button7 = ft.ElevatedButton("Cosseno (cos)", on_click=lambda e: append_text_to_input("cos()"), expand=True,
                                 on_hover=lambda e: on_hover(button7, e.hovered), bgcolor="#1C1C1C", color="#FF1493")
    button8 = ft.ElevatedButton("Tangente (tan)", on_click=lambda e: append_text_to_input("tan()"), expand=True,
                                 on_hover=lambda e: on_hover(button8, e.hovered), bgcolor="#1C1C1C", color="#FF1493")
    button9 = ft.ElevatedButton("Logaritmo (log)", on_click=lambda e: append_text_to_input("log()"), expand=True,
                                 on_hover=lambda e: on_hover(button9, e.hovered), bgcolor="#1C1C1C", color="#FF1493")
    button10 = ft.ElevatedButton("Exponencial (exp)", on_click=lambda e: append_text_to_input("exp()"), expand=True,
                                  on_hover=lambda e: on_hover(button10, e.hovered), bgcolor="#1C1C1C", color="#FF1493")
    button11 = ft.ElevatedButton("Média (mean)", on_click=lambda e: append_text_to_input("mean()"), expand=True,
                                  on_hover=lambda e: on_hover(button11, e.hovered), bgcolor="#1C1C1C", color="#FF1493")
    button12 = ft.ElevatedButton("Mediana (median)", on_click=lambda e: append_text_to_input("median()"), expand=True,
                                  on_hover=lambda e: on_hover(button12, e.hovered), bgcolor="#1C1C1C", color="#FF1493")
    button13 = ft.ElevatedButton("Variância (variance)", on_click=lambda e: append_text_to_input("variance()"), expand=True,
                                  on_hover=lambda e: on_hover(button13, e.hovered), bgcolor="#1C1C1C", color="#FF1493")
    button14 = ft.ElevatedButton("Desvio Padrão (stdev)", on_click=lambda e: append_text_to_input("stdev()"), expand=True,
                                  on_hover=lambda e: on_hover(button14, e.hovered), bgcolor="#1C1C1C", color="#FF1493")
    
    # Botões para calcular e limpar
    calculate_button = ft.ElevatedButton("Calcular", on_click=calculate_expression, expand=True,
                                          on_hover=lambda e: on_hover(calculate_button, e.hovered), bgcolor="#6699FF", color="#FFFFFF")
    clear_button = ft.ElevatedButton("Limpar", on_click=clear_input, expand=True,
                                      on_hover=lambda e: on_hover(clear_button, e.hovered), bgcolor="#6699FF", color="#FFFFFF")

    # Organizando botões em uma grade
    buttons = ft.Column([
        ft.Row([button1, button2, button3, button4], alignment="center"),
        ft.Row([button5, button6, button7, button8], alignment="center"),
        ft.Row([button9, button10, button11, button12], alignment="center"),
        ft.Row([button13, button14], alignment="center"),
    ], alignment="center")

    # Linha para os botões Calcular e Limpar (invertidos)
    action_buttons = ft.Row(
        [calculate_button, clear_button],
        alignment="center"
    )

    # Adicionando elementos à página
    page.add(
        ft.Column([
            ft.Text("Calculadora Científica", size=30, weight="bold", color="#FF1493"),
            input_field,
            action_buttons,  # Linha com os botões Calcular e Limpar
            result_text,
            buttons,
        ], alignment="center", horizontal_alignment="center", expand=True)
    )

# Executando a aplicação com Flet
ft.app(target=main)