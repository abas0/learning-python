class Pessoa:
    cpfs = set()  # Conjunto para armazenar CPFs únicos

    def __init__(self, nome, idade, cpf):
        self.nome = nome
        self.idade = idade
        self.cpf = cpf

        # Verificar se o CPF já foi cadastrado
        if self.cpf in Pessoa.cpfs:
            raise ValueError("CPF já cadastrado.")
        else:
            Pessoa.cpfs.add(self.cpf)

    def apresentar(self):
        return f"Olá, meu nome é {self.nome}, eu tenho {self.idade} anos e meu CPF é {self.cpf}."


# Função para criar uma nova Pessoa e tratar exceções
def criar_pessoa(nome, idade, cpf):
    try:
        pessoa = Pessoa(nome, idade, cpf)
        print(pessoa.apresentar())
    except ValueError as e:
        print(e)


# Testes
'''criar_pessoa("Ana", 28, "123.456.789-00")
criar_pessoa("Carlos", 35, "987.654.321-00")
criar_pessoa("Maria", 22, "123.456.789-00")  # Este CPF já foi cadastrado'''


#criar_pessoa(entrada[0], entrada[1], entrada[2])

pessoas = []
qntd_alunos = int(input())
for i in range(0, qntd_alunos):
    pessoa = input().split()
    pessoa = Pessoa(pessoa[0], pessoa[1], pessoa[2])
    pessoas.append(pessoa)
    criar_pessoa(pessoa[0], pessoa[1], pessoa[2])

pessoas_presentes = 0
for pessoa in pessoas:
    print(pessoa.apresentar())
    pessoas_presentes += 1
print(f"Qunatidade de pessoas presentes: {pessoas_presentes}")