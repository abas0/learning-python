import unicodedata

qtd = int(input())
entradas = []

for i in range(0, qtd):
    entrada = input().split()
    nome = entrada[0]
    nome_normalizado = unicodedata.normalize('NFD', nome)
    nome_sem_acento = ''.join(char for char in nome_normalizado if unicodedata.category(char) != 'Mn')
    entradas.append(nome_sem_acento.lower())
    if entradas[i] == 'thor':
        print("Y")
    else:
        print("N")
