"""6. Faça um programa que faça 5 perguntas para uma pessoa sobre um crime.
As perguntas são:
"Telefonou para a vítima?"
"Esteve no local do crime?"
"Mora perto da vítima?"
"Devia para a vítima?"
"Já trabalhou com a vítima?"
O programa deve no final emitir uma classificação sobre a participação da
pessoa no crime. Se a pessoa responder positivamente a 2 questões ela
deve ser classificada como "Suspeita", entre 3 e 4 como "Cúmplice" e 5 como
"Assassino". Caso contrário, ele será classificado como "Inocente"""

cont = 0
print("Responda com sim ou nao")
lista = []
r1 = input("Telefonou para a vítima?").upper()
r2 = input("Esteve no local do crime?").upper()
r3 = input("Mora perto da vítima?").upper()
r4 = input("Devia para a vítima?").upper()
r5 = input("Já trabalhou com a vítima?").upper()

if r1 == "SIM":
    lista.append(r1)
if r2 == "SIM":
    lista.append(r2)
if r3 == "SIM":
    lista.append(r3)
if r4 == "SIM":
    lista.append(r4)
if r5 == "SIM":
    lista.append(r5)

print(lista)

result = lista.count("SIM")

if result == 2:
    print("É um suspeito!")

elif result == 3 or result == 4:
    print("É cumplice!")
elif result == 5:
    print("É o assassino!")