import re

import unicodedata

n = int(input())  #numero de listas
todos_itens = []
if 0 < n < 101:
    for i in range(0, n):
        itens = input().split()
        for j in range(0, len(itens)):
            if 0 < len(itens[j]) < 21:
                s_normalizada = unicodedata.normalize('NFD', itens[j])
                s_sem_acento = ''.join(c for c in s_normalizada if not unicodedata.combining(c))
                todos_itens.append(s_sem_acento.lower())
            else:
                continue
    thisset = set(todos_itens)
    todos_itens_ordenados = sorted(thisset)
    print(todos_itens_ordenados)
