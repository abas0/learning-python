ddd = int(input("Insira um DDD: "))

if ddd == 61:
    print("Brasilia")
elif ddd == 71:
    print("Salvador")
elif ddd == 11:
    print("São Paulo")
elif ddd == 21:
    print("Rio de Janeiro")
elif ddd == 32:
    print("Juiz de Fora")
elif ddd == 19:
    print("Campinas")
elif ddd == 27:
    print("Vitória")
elif ddd == 31:
    print("Belo Horizonte")
else:
    raise Exception("ERRO: DDD inválido")