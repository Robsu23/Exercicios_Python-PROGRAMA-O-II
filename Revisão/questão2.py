"""2. Faça um Programa que verifique se uma letra digitada é vogal ou consoante.
"""

lista = ["a","e","i","o","u"]

letra = input("Digite uma letra:").lower

if letra in lista:
    print(f"A letra {letra} é uma vogal.")

else:
    print(f"A letra {letra} não é uma vogal")