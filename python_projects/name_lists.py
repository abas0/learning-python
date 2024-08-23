def ordenar_por_caracteres(lista):
    ordenada = sorted(lista, key=len)
    return ordenada


n = int(input())
nomes = []
if n < 2 or n > 1000:
    print("Quantidade de nomes inválidas")
else:
    print("Insira os nomes na lista")
    for i in range(0, n):
        nome = input()
        while len(nome) < 2 or len(nome) > 19:
            print("Quantidade de caracteres inválida. Tente novamente")
            nome = input()
        nomes.append(nome)
        nomes.sort()
print("Lista de nomes: {}" .format(', '.join(map(str, ordenar_por_caracteres(nomes)))))
