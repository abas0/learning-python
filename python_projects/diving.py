organizar_tudo = []
rankeando_notas = []
organizar_todas_as_notas = []
qtd_nadadores = int(input())
nadadores = []


def ranking_participantes(lista_media_organizadas):
    lista_media_organizadas.sort(key=lambda media_organizadas: media_organizadas['nota'], reverse=True)
    return lista_media_organizadas


class Nadador:
    def __init__(self, nome: str, grau: float, notas: []):
        self.nome = nome
        self.grau = grau
        self.notas = notas

    def validador_de_dificuldade(self):
        interruptor = True
        while interruptor:
            if 1.2 <= self.grau <= 3.8:
                interruptor = not interruptor
            else:
                novo_grau = float(input("Grau inválido! Tente novamente"))
                self.grau = novo_grau

    def imprimir_notas_de_um_nadador(self):
        for j in range(0, 7):
            nota = float(input("Insira uma nota: "))
            interruptor = True
            while interruptor:
                if 0 <= nota <= 10:
                    self.notas.append(nota)
                    interruptor = not interruptor
                else:
                    nota = float(input("Nota inválida. Insira novamente"))

    def notas_para_calculo(self):
        self.notas.sort()
        self.notas.pop(0)
        self.notas.pop(len(self.notas) - 1)
        return self.notas

    def calcular_nota(self, notas_organizadas):
        somatorio = 0
        for j in range(0, len(notas_organizadas)):
            somatorio += notas_organizadas[j]
        nota_final = somatorio * self.grau
        return nota_final


for i in range(0, qtd_nadadores):
    dados_nadador = input("Digite o nome do nadador e o grau de dificuldade do seu nado").split()
    nadador = Nadador(dados_nadador[0], float(dados_nadador[1]), [])
    nadador.validador_de_dificuldade()
    nadador.imprimir_notas_de_um_nadador()
    nota_calculada = nadador.calcular_nota(nadador.notas_para_calculo())
    print(nadador.nome, nota_calculada)
    organizar_tudo.append({'nota': nota_calculada, 'nome': nadador.nome})
    rankeando_notas = ranking_participantes(organizar_tudo)


print("Ranking: ")
for nadador in rankeando_notas:
     print(f"{nadador['nome']}")
