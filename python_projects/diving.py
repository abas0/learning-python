notas = []
organizar_todas_as_notas = []

def imprimir_notas_de_um_nadador():
    for j in range(0, 7):
        nota = float(input("Insira uma nota: "))
        interruptor = True
        while interruptor:
            if 0 <= nota <= 10:
                notas.append(nota)
                interruptor = not interruptor
            else:
                nota = float(input("Nota inválida. Insira novamente"))


def notas_para_calculo():
    notas.sort()
    notas.pop(0)
    notas.pop(len(notas) - 1)
    print(f"Notas dentro de organizar_notas(): {notas}")
    return notas


# def organizar_todas_as_notas():
    # return []


class Nadador:
    def __init__(self, nome: str, grau: float):
        self.nome = nome
        self.grau = grau

    def validador_de_dificuldade(self):
        interruptor = True
        while interruptor:
            if 1.2 <= self.grau <= 3.8:
                interruptor = not interruptor
            else:
                novo_grau = float(input("Grau inválido! Tente novamente"))
                self.grau = novo_grau

    def calcular_nota(self, notas_organizadas):
        somatorio = 0
        for j in range(0, len(notas_organizadas)):
            somatorio += notas_organizadas[j]
        nota_final = somatorio * self.grau
        return nota_final


qtd_nadadores = int(input())
nadadores = []
for i in range(0, qtd_nadadores):
    dados_nadador = input("Digite o nome do nadador e o grau de dificuldade do seu nado").split()
    nadador = Nadador(dados_nadador[0], float(dados_nadador[1]))
    nadador.validador_de_dificuldade()
    imprimir_notas_de_um_nadador()
    print(nadador.nome, nadador.calcular_nota(notas))
    organizar_todas_as_notas.append(nadador.calcular_nota(notas))
    print(organizar_todas_as_notas)
    # 2 parte: organizar as notas dos participantes em ordem decrescente
    # 3 parte: organizar a lista de participantes em ordem decrescente pelos seus nomes
