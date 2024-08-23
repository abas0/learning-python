qntd = int(input())
valores = []
for i in range(0, qntd):
    valor = int(input())
    if valor in valores:
        print("Esse valor já existe!")
        continue
    else:
        valores.append(valor)
print(valores)