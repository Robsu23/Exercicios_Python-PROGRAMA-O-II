"""8. Para ter acesso a fila de prioridade, você deve ser idoso, gestante ou PCD.
Escreva um programa que pergunta a situação do usuário (se é idoso, se é
gestante, se é PCD ou nenhum destes) e diga se ele pode ter acesso a fila
prioridade ou não"""

menu = int(input(("""Qual sua categoria?
1-Gestante
2-PCD
3-Idoso
4-Nenhum
              
R:""")))

if menu >= 1 and menu <= 3:
    print("Você pode ter acesso a fila!")

elif menu == 4:
    print("Não pode ter acesso a fila!")

else:
    print("Resposta invalida!")




