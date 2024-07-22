"""Crie um programa de câmbio. Nesse programa adicione funções que
realizem conversões de real para dólar, real para euro e real para peso
argentino, conforme o nome do país fornecido pelo usuário. Utilize os valores:
1,00 real = 0,18 dólar para Estados Unidos;
1,00 real = 0,16 euro para Portugal;
1,00 real = 0,0061 peso para Argentina;
"""

def dolar():
    valor = float(input("Digite um valor:"))
    converção = valor * 0.18
    print(f"A converção para Dolar é:{converção}")

def euro():
    valor = float(input("Digite um valor:"))
    converção = valor * 0.16
    print(f"A converção para Dolar é:{converção}")

def peso():
    valor = float(input("Digite um valor:"))
    converção = valor * 0.0061
    print(f"A converção para Dolar é:{converção}")


dolar()
euro()
peso()
