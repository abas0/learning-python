# apenas quatro entradas [OK]
# só pode ser 0 ou 1 [OK]
# só uma pode ter 1
# adivinhar qual lugar tá o 1

entradas = input()

entradas_divididas = entradas.split()
entradas_invalidas = []
qtd_um = 0

if len(entradas_divididas) < 4:
    raise Exception("Entradas insuficientes!")

elif len(entradas_divididas) > 4:
    for i in range(4, len(entradas_divididas)):
        entradas_invalidas.append(entradas_divididas[i])
    print(f"Entradas desconsideradas: {entradas_invalidas}")

for i in range(0, 4):
    loop = True
    while loop:
        if all(c in '01' for c in entradas_divididas):
            loop = False
        else:
            entradas = input("Entrada inválida! Tente novamente")
            entradas_divididas = entradas.split()
    if entradas_divididas[i] == '1':
        qtd_um = qtd_um + 1

if qtd_um != 1:
    raise Exception("ERRO na quantidade de 1")

else:
    for i in range(0,4):
        if entradas_divididas[i] == '1':
            print(i+1)