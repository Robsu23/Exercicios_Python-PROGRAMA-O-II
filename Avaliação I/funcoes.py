import os


lista_musica = []

def abrir_musica(nome_musica):
    if nome_musica in lista_musica:
        os.startfile(nome_musica)
    else:
        print(f"A musica {nome_musica} não está na lista.")

def adicionar_nome_musica(nome_musica):
    if nome_musica not in lista_musica:
        lista_musica.append(nome_musica)
        print(f" musica '{nome_musica}' adicionada com sucesso.")
    else:
        print(f" '{nome_musica}' já está na lista.")

def listar_nomes_musica():
    """Retorna a lista de nomes de musica .exe."""
    return lista_musica

def buscar_nome_musica(nome_musica):
    """Verifica se o musica está na lista."""
    if nome_musica in lista_musica:
        return True
    return False

def remover_nome_musica(nome_musica):
    """Remove o nome do musica da lista, se estiver presente."""
    if nome_musica in lista_musica:
        lista_musica.remove(nome_musica)
        print(f" musica '{nome_musica}' removido com sucesso.")
    else:
        print(f" '{nome_musica}' não está na lista.")