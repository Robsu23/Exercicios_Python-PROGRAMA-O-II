from funcoes import adicionar_nome_musica,listar_nomes_musica,buscar_nome_musica,remover_nome_musica,abrir_musica


def menu():
    while True:
        print("BEM VINDO A PYTHONLIST")
        print()
        print('''
              Menu
-------------------------------
1. Listar  musicas
2. Adicionar musicas
3. Buscar  musicas
4. Remover musicas
5. abrir musicas
5. sair..
-------------------------------
              ''')
        
        resp = input("Qual musica deseja adicionar? ")
        
        if resp == '1':
            nomes = listar_nomes_musica()
            print("\nNomes das musicas da playlist:")
            for nome in nomes:
                print(nome)
        
        elif resp == '2':
            nome_musica = input("Digite o nome da musica a ser adicionada: ")
            adicionar_nome_musica(nome_musica)
        
        elif resp == '3':
            nome_musica = input("Digite o nome da musica a ser buscada: ")
            encontrado = buscar_nome_musica(nome_musica)
            if encontrado:
                print(f"A musica '{nome_musica}' foi encontrada na playlist.")
            else:
                print(f"A musica '{nome_musica}' não está na playlist.")
        
        elif resp == '4':
            nome_musica = input("Digite o nome da musica a ser removida: ")
            remover_nome_musica(nome_musica)
        
        elif resp == '5':
            nome_musica = input("Digite o nome da musica para tocar: ")
            abrir_musica(nome_musica)

        elif resp == '6':
            print("Saindo do sistema...")
            break
        
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == '__main__':
    menu()