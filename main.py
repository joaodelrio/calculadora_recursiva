#- Fibonacci com hash é para n repetir cálculos

# def fibonacci(x):
#     print(x)
#     if x == 1 or x == 2:
#         return 1
#     return fibonacci(x-1) + fibonacci(x-2)

def fibonacci_hash(x, memo={}):
    if x in memo:
        return memo[x]
    if x == 1 or x==2:
        return 1
    memo[x] = fibonacci_hash(x-1) + fibonacci_hash(x-2)
    return memo[x]

def multiplicacao(x,y):
    if y == 0 or x==0:
        return 0
    if y < 0:
        return -x + multiplicacao(x,y+1)
    return x + multiplicacao(x,y-1)

def divisao(x,y,parteInt=0,negativo=False):
    if x<0 and y<0:
        x = -x
        y = -y
        negativo = False
    if x<0:
        x = -x
        negativo = True
    if y<0:
        y = -y
        negativo = True
    if y == 0:
        raise ValueError("Divisão por zero não é permitida!")
    # Se o resto for 0, então não tem mais como dividir
    if x==0:
        if negativo:
            return (-parteInt, x)
        return (parteInt, x)
    # Se o resto for menor que o valor que ta dividindo então não tem mais como dividir, e se não for 0, então tem que tirar um valor da parteInt 
    if x < y:
        if negativo:
            return (-parteInt-1, x)
        return (parteInt-1, x)
    return divisao(x-y, y,parteInt+1,negativo)

def soma(x, y):
    return x+y

def subtracao(x, y):
    return x-y

def exponencial(x, y):
    if y == 0:
        return 1
    return multiplicacao(x, exponencial(x, y-1))

def fatorial(x):
    if x < 0:
        raise ValueError("Entrada invalida!")
    if x == 0:
        return 1
    return multiplicacao(x, fatorial(x-1))


