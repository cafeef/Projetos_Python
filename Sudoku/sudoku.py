from random import randint 
from random import choice
Matriz1, Matriz2, Matriz3, Matriz4 = [], [], [], [] * 3


def atribuicao_linhas():
    fim = 3
    while fim >= 0:
        i = []
        index = 0
        while index <= (fim - 1):
            i.append(randint(1, 9))
            index += 1
        fim -= 1
    return i

def atribuicao_matrizes(linhas, Matriz1, Matriz2, Matriz3, Matriz4):
    linhas = atribuicao_linhas()
    Matriz1.append(i)
    i = atribuicao_linhas()
    Matriz2.append(i)
    i = atribuicao_linhas()
    Matriz3.append(i)
    i = atribuicao_linhas()
    Matriz4.append(i)
    Matriz_Total = [Matriz1, Matriz2, Matriz3, Matriz4]    
    return Matriz_Total

linhas = atribuicao_linhas()
Matriz_Total = atribuicao_matrizes(i, Matriz1, Matriz2, Matriz3, Matriz4)
print(Matriz_Total)
    