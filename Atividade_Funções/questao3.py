""" Faça um programa que receba três números do usuário, e identifique o maior
através de uma função e o menor número através de outra função"""
def maior():
    lista = []

    n1 = float(input("Digite um numero:"))
    lista.append(n1)
    n2 = float(input("Digite outro numero:"))
    lista.append(n2)
    n3 = float(input("Digite mais um numero:"))
    lista.append(n3)
    print(f"O maior numero é:{max(lista)}")

def menor():
    lista = []

    n1 = float(input("Digite um numero:"))
    lista.append(n1)
    n2 = float(input("Digite outro numero:"))
    lista.append(n2)
    n3 = float(input("Digite mais um numero:"))
    lista.append(n3)
    print(f"O menor numero é:{min(lista)}")

maior()
menor()