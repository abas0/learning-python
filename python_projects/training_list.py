import re


def verificador_de_presenca(compareceu):
    return compareceu == 's'


class Pessoa():
    emails = set()
    def __init__(self, nome: str, universidade: str, email: str):
        self.nome = nome
        self.universidade = universidade
        self.email = email

    def email_repetido(self):
        if self.email not in Pessoa.emails:
            return Pessoa.emails.add(self.email)
        else:
            return f"E-mail repetido"

    def apresentar(self):
        return f'Nome: {self.nome} - Universidade: {self.universidade} - E-mail: {self.email}'

    def validar_email(self):
        padrao_email = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        return re.match(padrao_email, self.email) is not None


pessoas = []
qntd_alunos = int(input())
for i in range(0, qntd_alunos):
    pessoa = input("Digite os dados do estudante").split()
    pessoa = Pessoa(pessoa[0], pessoa[1], pessoa[2])
    if not pessoa.validar_email():
        print("Email inválido")
        continue
        #print("Email já existe. Tente novamente")
        #continue
    if pessoa.email_repetido() != "E-mail repetido":
        compareceu = input("Compareceu ao treinamento? s/n")
        if verificador_de_presenca(compareceu) and pessoa.validar_email():
            pessoas.append(pessoa)

pessoas_presentes = 0
for pessoa in pessoas:
    print(pessoa.apresentar())
    pessoas_presentes += 1
print(f"Qunatidade de pessoas presentes: {pessoas_presentes}")
