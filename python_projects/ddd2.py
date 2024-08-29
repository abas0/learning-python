ddd = int(input("Insira um DDD: "))
loop = True
while loop:
    if ddd == 61:
        print("Brasilia")
        loop = not loop
    elif ddd == 71:
        print("Salvador")
        loop = not loop
    elif ddd == 11:
        print("São Paulo")
        loop = not loop
    elif ddd == 21:
        print("Rio de Janeiro")
        loop = not loop
    elif ddd == 32:
        print("Juiz de Fora")
        loop = not loop
    elif ddd == 19:
        print("Campinas")
        loop = not loop
    elif ddd == 27:
        print("Vitória")
        loop = not loop
    elif ddd == 31:
        print("Belo Horizonte")
        loop = not loop
    else:
        ddd = int(input("DDD Inválido. Tente novamente: "))
