"""5. Faça um programa que peça um número inteiro e determine se ele é ou não
um número primo. Um número primo é aquele que é divisível somente por ele
mesmo e por 1.
"""


numero = int(input("Digite um numero:"))
lista = [2,3,5,7]
if numero in lista:
    print(f"{numero} é um numero primo!")

elif numero % 2 == 0 or numero % 3 == 0 or numero % 5 == 0 or numero % 7 == 0:
    print(f"{numero} Não é primo")

else:
    print(f"{numero}É um numero primo")