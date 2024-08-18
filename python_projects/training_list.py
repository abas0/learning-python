#colocar como saída a quantidade de pessoas que foram e o nome de cada uma

def verificador_de_presenca(compareceu):
    return compareceu == 's'


class Pessoa():
    def __init__(self, nome: str, universidade: str, email: str):
        self.nome = nome
        self.universidade = universidade
        self.email = email

    def apresentar(self):
        return f'Nome: {self.nome} - Universidade: {self.universidade} - E-mail: {self.email}'

    def __eq__(self, __other):
        return self.email == __other.email


pessoas = []
qntd_alunos = int(input())
for i in range(0, qntd_alunos):
    pessoa = input().split()
    pessoa = Pessoa(pessoa[0], pessoa[1], pessoa[2])
    compareceu = input("Compareceu ao treinamento? s/n")
    if verificador_de_presenca(compareceu):
        pessoas.append(pessoa)

for pessoa in pessoas:
    print(pessoa.apresentar())
