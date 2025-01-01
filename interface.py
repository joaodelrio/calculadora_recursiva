import tkinter as tk
from main import divisao, subtracao, multiplicacao, soma

# Funções da calculadora
def btn_click(item):
    global expression
    global number
    global numbers
    global operators
    if(isinstance(item,(int,float))):
        number += str(item)
    else:
        numbers.append(int(number))
        number = ""
        operators.append(item)
    expression += str(item)
    input_text.set(expression)

def clear():
    global expression
    expression = ""
    input_text.set("")

def calculate():
    try:
        global expression
        global number
        global operators
        global numbers
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
            numbers = numbers[2:]
            operators = operators[1:]
            numbers.insert(0, result)
        result = str(numbers[0])
        input_text.set(result)
        numbers = []
        operators = []
        expression = ""
    except Exception as e:
        input_text.set("Erro")
        expression = ""

# Configurações da janela principal
window = tk.Tk()
window.title("Calculadora")
window.geometry("400x400")
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
    (7, 8, 9, '/'),
    (4, 5, 6, '*'),
    (1, 2, 3, '-'),
    ('C', 0, '=', '+')
]

for i, row in enumerate(btn_texts):
    for j, text in enumerate(row):
        if text == "=":
            btn = tk.Button(
                btns_frame, text=text, fg="white", bg="#4CAF50", font=('Arial', 18), width=5, height=2,
                command=calculate
            )
        elif text == "C":
            btn = tk.Button(
                btns_frame, text=text, fg="white", bg="#FF5722", font=('Arial', 18), width=5, height=2,
                command=clear
            )
        else:
            btn = tk.Button(
                btns_frame, text=text, fg="black", bg="#E0E0E0", font=('Arial', 18), width=5, height=2,
                command=lambda t=text: btn_click(t)
            )
        btn.grid(row=i, column=j, padx=5, pady=5)

window.mainloop()
