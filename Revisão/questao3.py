"""Faça um Programa que pergunte em que turno você estuda. Peça para
digitar M-matutino ou V-Vespertino ou N- Noturno. Imprima a mensagem
"Bom Dia!", "Boa Tarde!" ou "Boa Noite!" ou "Valor Inválido!", conforme o
caso.
"""

turno = """Em que turno você estuda?
Digite:
M-matutino
V-vespertino
N-noturno
"""
print(turno)

entrada = input("Em que turno você estuda?").upper()

if entrada == "M":
    print("Bom dia!")

elif entrada == "V":
    print("Boa tarde!")

elif entrada == "N":
    print("Boa noite!")

else:
    print(f"{entrada} Não é uma resposta valida")