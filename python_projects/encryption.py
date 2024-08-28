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
    print(nova_stirng)


for i in range(0, num):
    caracteres = input()
    analisar_caracter(caracteres)
