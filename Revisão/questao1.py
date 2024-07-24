"""1. Crie um programa em Python que peça dois números ao usuário. Em
seguida, você vai mostrar a soma, subtração, multiplicação, divisão,
exponenciação e resto da divisão do primeiro número pelo segundo."""

N1 = float(input("Digite um numero:"))
N2 = float(input("Digite outro numero:"))

soma = N1 + N2
sub = N1 - N2
mult = N1 * N2
div = N1 / N2
expo = N1 ** N2
rest = N1 % N2

print(f"Soma:{soma}\nSubtração:{sub}\nMultiplicação:{mult}\nDivisão:{div}\nExponenciação:{expo}\nResto:{rest}")
