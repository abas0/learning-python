entrada = input()
caracteres_entrada = list(entrada)

caracteres = ['`', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0',
              '-', '=', 'Q', 'W', 'E', 'R', 'T', 'Y', 'U', 'I', 'O', 'P', '[', ']', '\\', 'A', 'S', 'D',
              'F', 'G', 'H', 'J', 'K', 'L', ';', '\'', 'Z', 'X', 'C', 'V', 'B', 'N', 'M', ',', '.', '/']

convertido = ''
for i in range(0, len(caracteres_entrada)):
    if caracteres_entrada[i] == ' ':
        convertido += caracteres_entrada[i]
    else:
        posicao = caracteres.index(caracteres_entrada[i])
        posicao = posicao - 1
        convertido += caracteres[posicao]

print(convertido)
