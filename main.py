#- Fibonacci com hash é para n repetir cálculos
#- fazer a função de multiplicar recursivo

# def multiplicacao(x, y):
#     resultadoMulti = 0
#     for i in range(y):
#         resultadoMulti = resultadoMulti + x

#     return resultadoMulti

# def fibonacci(x):
#     if x == 1 or x == 2:
#         return 1
#     return fibonacci(x-1) + fibonacci(x-2)

def multiplicacao(x,y):
    if y == 0 or x==0:
        return 0
    # Quando y = 1, vai ser a multiplicação por 1 então o resultado é ele mesmo acabando a recursividade
    if y == 1:
        return x
    return x + multiplicacao(x,y-1)

def divisao(x,y,parteInt=0):
    if y == 0:
        raise ValueError("Divisão por zero não é permitida!")
    # Se o resto for 0, então não tem mais como dividir
    if x==0:
        return (parteInt, x)
    # Se o resto for menor que o valor que ta dividindo então não tem mais como dividir, e se não for 0, então tem que tirar um valor da parteInt 
    if x < y:
        return (parteInt-1, x)
    return divisao(x-y, y,parteInt+1)

def soma(x, y):
    return x+y

def subtracao(x, y):
    return x-y


