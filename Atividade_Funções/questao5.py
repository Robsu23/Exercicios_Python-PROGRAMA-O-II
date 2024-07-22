""". Escreva um programa que possa cadastrar clientes ou funcionários para uma
loja. Se o usuário quiser cadastrar um cliente, dados de nome, endereço,
CPF devem ser solicitados. Caso o usuário prefira adicionar um novo
funcionário, dados de nome, salário, cargo e CPF devem ser requisitados.
Utilize comandos de manipulação de string para personalizar a saída.
"""

def cliente():
    cliente = input("Digite o nome:").capitalize()
    endereço = input("Digite o endereço:")
    cpf = input("Digite o CPF:")
    print(f"Cliente:{cliente}\nEndereço:{endereço}\nCPF:{cpf}") 

def funcionario():
    funcionario = input("Digite o nome:").capitalize()
    salario = float(input("Digite o salario:"))
    cargo = input("Digite o cargo:").capitalize()
    cpf = input("Digite o CPF:")
    print(f"Funcionario:{funcionario}\nSalario:R${salario}\nCargo:{cargo}\nCPF:{cpf}")

menu = int(input("""O que deseja fazer?
1 - Cadastrar clientes
2 - Cadastrar funcionarios
0 - sair

R:"""))

print(menu)

if menu == 1:
    cliente()

elif menu == 2:
    funcionario()

elif menu == 0:
    print("Finalizado!")