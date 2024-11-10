def validar_input(joia):
    return all(c in '()' for c in joia)

joias = set()

with open("arquivo.txt", "r") as arquivo:
    for linha in arquivo:
        linha = linha.strip()
        if validar_input(linha):
            joias.add(linha)
        else:
            print(f"Entrada inválida para uma joia: {linha}")

print(f"Joias: {joias}")
print(f"Quantidade de joias: {len(joias)}")
