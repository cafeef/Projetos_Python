from random import randint 
from random import choice

def Criacao_Matriz():
    sudoku = []
    linha = 0 
    while (linha <= 6):
        lista = []
        coluna = 0 
        while (coluna <= 6):
            elemento = randint(1,9)
            if elemento in lista:
                elemento = randint(1,9)                   
            lista.append(elemento)
            coluna += 1
        sudoku.append(lista)
        linha += 1
    return sudoku

def Atribuicao_Zeros(sudoku):
    indices = [0, 1, 2, 3, 4, 5]
    cont = 0
    while cont <= 10:
        indice1 = choice(indices)
        indice2 = choice(indices)
        sudoku[indice1][indice2] = 0
        cont += 1

def Exibicao_Matriz(sudoku_final):
    i = 0
    while i <= 5:
        print(sudoku_final[i])
        i += 1

def Validade_Matriz(sudoku):
    i = 0
    fim = 6
    while fim >= 0:
        while i <= (fim - 1):
            if sudoku[i][fim - 1] in sudoku:
                sudoku[i][fim - 1] = randint(1, 9)
            i += 1
        fim -= 1
    return sudoku


sudoku = Criacao_Matriz()
Atribuicao_Zeros(sudoku)
sudoku_final = Validade_Matriz(sudoku)
Exibicao_Matriz(sudoku_final)