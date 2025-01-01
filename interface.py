import tkinter as tk
from main import divisao, subtracao, multiplicacao, soma, exponencial, fatorial

# Funções da calculadora
def btn_click(item):
    global expression
    global number
    global numbers
    global operators
    if isinstance(item, (int, float)):
        number += str(item)
    else:
        numbers.append(int(number))
        number = ""
        operators.append(item)
    expression += str(item)
    input_text.set(expression)

def clear():
    global expression
    global number
    global numbers
    global operators
    expression = ""
    number = ""
    numbers = []
    operators = []
    input_text.set("")

def calculate():
    try:
        global expression
        global number
        global operators
        global numbers
        
        if number == "":
            if "!" not in operators:
                raise ValueError("Nenhum número foi fornecido para cálculo")
        else:
            numbers.append(int(number))
            number = ""
        

        while len(operators) > 0:
            if operators[0] == '+':
                result = soma(numbers[0], numbers[1])
            elif operators[0] == '-':
                result = subtracao(numbers[0], numbers[1])
            elif operators[0] == '*':
                result = multiplicacao(numbers[0], numbers[1])
            elif operators[0] == '/':
                result = divisao(numbers[0], numbers[1])
            elif operators[0] == '^':
                result = exponencial(numbers[0], numbers[1])
            elif operators[0] == '!':  # Adicionando o fatorial
                result = fatorial(numbers[0])
            numbers = numbers[2:]  # Atualiza a lista de números
            operators = operators[1:]  # Remove o operador já processado
            numbers.insert(0, result)  # Insere o resultado como o primeiro número
        result = str(numbers[0])
        input_text.set(result)
        numbers = []
        operators = []
        expression = ""
    except Exception as e:
        input_text.set("Erro: " + str(e))
        expression = ""
        numbers = []
        operators = []

# Configurações da janela principal
window = tk.Tk()
window.title("Calculadora")
window.geometry("400x300")
window.resizable(False, False)

number = ""
numbers = []
operators = []
expression = ""
input_text = tk.StringVar()

# Campo de entrada
input_frame = tk.Frame(window)
input_frame.pack()

input_field = tk.Entry(input_frame, textvariable=input_text, font=('Arial', 18), justify='right', bd=10, bg="#F5F5F5")
input_field.grid(row=0, column=0)
input_field.pack(ipady=10)

# Botões da calculadora
btns_frame = tk.Frame(window)
btns_frame.pack()

# Botões layout
btn_texts = [
    (7, 8, 9, '/','^'),
    (4, 5, 6, '*', '!'),  # Fatorial adicionado aqui
    (1, 2, 3, '-', 'f'),
    ("", 0, '=', '+', 'C'),
]

for i, row in enumerate(btn_texts):
    for j, text in enumerate(row):
        if text == "=":
            btn = tk.Button(
                btns_frame, text=text, fg="white", bg="#4CAF50", font=('Arial', 18), width=3, height=1,
                command=calculate
            )
        elif text == "":
            btn = tk.Button(
                btns_frame, text=text, fg="white", bg="#E0E0E0", font=('Arial', 18), width=3, height=1,
                state="disabled"
            )
        elif text == "C":
            btn = tk.Button(
                btns_frame, text=text, fg="white", bg="#FF5722", font=('Arial', 18), width=3, height=1,
                command=clear
            )
        else:
            btn = tk.Button(
                btns_frame, text=text, fg="black", bg="#E0E0E0", font=('Arial', 18), width=3, height=1,
                command=lambda t=text: btn_click(t)
            )
        btn.grid(row=i, column=j, padx=5, pady=5)

window.mainloop()
