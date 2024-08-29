num = int(input())


def analisar_caracter(c):
    string_aux = []
    for j in range(0, len(c)):
        if 'z' >= c[j] >= 'a' or 'Z' >= c[j] >= 'A':
            letra_ascii = ord(c[j])
            letra_ascii = letra_ascii + 3
            string_aux.append(chr(letra_ascii))  # strings são imutáveis, por isso a necessidade de uma string auxiliar
        else:
            string_aux.append(c[j])
    nova_stirng = ''.join(string_aux)
    return nova_stirng


def inverter_caracteres(c):
    string_aux = []
    for j in range(len(c) - 1, -1, -1):
        string_aux.append(c[j])
    nova_stirng = ''.join(string_aux)
    return nova_stirng


def ajustar_metade(c):
    string_aux = []
    if len(c)/2 % 2 != 0:
        primeira_metade = c[:int(len(c) / 2) + 1]
        segunda_metade = c[int(len(c) / 2) + 1:]
    else:
        primeira_metade = c[:int(len(c) / 2)]
        segunda_metade = c[int(len(c) / 2):]

    for j in range(0, len(segunda_metade)):
        letra_ascii = ord(segunda_metade[j])
        letra_ascii -= 1
        string_aux.append(chr(letra_ascii))
    nova_stirng = primeira_metade + ''.join(string_aux)
    return nova_stirng


for i in range(0, num):
    caracteres = input()
    primeira_conversao = analisar_caracter(caracteres)
    segunda_conversao = inverter_caracteres(primeira_conversao)
    terceira_conversao = ajustar_metade(segunda_conversao)
    print(terceira_conversao)
