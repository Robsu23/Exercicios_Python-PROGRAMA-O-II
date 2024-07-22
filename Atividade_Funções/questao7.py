"""Crie uma função que receba um número indeterminado de valores inteiros e
depois apresente a soma deles na tela. Use: def nome_da_funcao (* parametro):"""



def numeros():
    lista = [ ]
    while True:
        R = input("Quer digitar numeros?").lower()
        if R == "sim":
            numero = int(input("Digite um numero:"))
            lista.append(numero)
    
        else:
            print(f"A soma dos numeros é:{sum(lista)}")
            break

numeros()
