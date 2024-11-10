class Pessoa:
    cpfs = set()  # Conjunto para armazenar CPFs únicos

    def __init__(self, nome, idade, cpf):
        self.nome = nome
        self.idade = idade
        self.cpf = cpf

        # elementos_anteriores = todos_cpfs.pop()
        print(f"Pessoa.cpfs {Pessoa.cpfs}")
        if self.cpf in Pessoa.cpfs:
            raise ValueError("CPF já cadastrado.")
        else:
            Pessoa.cpfs.add(self.cpf)

    def apresentar(self):
        if not self.idade.isdigit() or int(self.idade) < 0:
            raise ValueError("Idade inválida")
        elif len(self.cpf) != 11 or not self.cpf.isdigit():
            raise ValueError("CPF inválido")
        else:
            print(f"Olá, meu nome é {self.nome}, eu tenho {self.idade} anos e meu CPF é {self.cpf}.")


pessoas = []
qntd_alunos = int(input())
for i in range(0, qntd_alunos):
    pessoa = input().split()
    nome = pessoa[0]
    idade = pessoa[1]
    cpf = pessoa[2]
    pessoa = Pessoa(nome, idade, cpf)
    pessoas.append(pessoa)

pessoas_presentes = 0
for pessoa in pessoas:
    print(pessoa.apresentar())
    pessoas_presentes += 1
print(f"Qunatidade de pessoas presentes: {pessoas_presentes}")
