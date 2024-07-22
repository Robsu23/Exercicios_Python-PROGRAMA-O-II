"""Faça um programa que calcule a área de um terreno e imprima na tela."""

def terreno():
    lado = float(input("Digite o lado:"))
    comprimento = float(input("Digite o comprimento:"))
    calculo = lado * comprimento
    print(f"Medida do terreno:{calculo}")

terreno()