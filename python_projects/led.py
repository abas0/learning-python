qtd = int(input())
entradas = []
leds = 0

for i in range(0, qtd):
    entrada = input().split()
    entradas.append(entrada)
    for j in range(0, len(entradas[i])):
        leds = 0
        for k in range(0, len(entradas[i][j])):
            if entradas[i][j][k] == '1':
                leds += 2
            elif entradas[i][j][k] == '2' or entradas[i][j][k] == '3' or entradas[i][j][k] == '5':
                leds += 5
            elif entradas[i][j][k] == '4':
                leds += 4
            elif entradas[i][j][k] == '6' or entradas[i][j][k] == '9' or entradas[i][j][k] == '0':
                leds += 6
            elif entradas[i][j][k] == '7':
                leds += 3
            elif entradas[i][j][k] == '8':
                leds += 7
            else:
                raise ValueError("Válido apenas tipos numéricos")
    print(f"{leds} leds")
