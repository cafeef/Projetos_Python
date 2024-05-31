from random import randint
def adivinhar_numeros():
    r = 'N'
    lista_tentativas = []
    print('Vamos jogar de adivinhar o número!\nPense em um número e eu vou tentar adivinhar!')
    primeiro_intervalo = int(input('Me diga onde o intervalo começa: '))
    ultimo_intervalo = int(input('Me diga onde o intervalo termina: '))
    tentativa = randint(primeiro_intervalo, ultimo_intervalo)
    while r != 'S':
        if tentativa not in lista_tentativas:
            lista_tentativas.append(tentativa)
            print(f'Eu acho que o número é: {tentativa}')
            r = input('Acertei? [ S | N ] ')
            if r == 'N':
                rA = input('O número que supus é maior ou menor? [ MA | ME ]')
                if rA == 'MA': 
                    ultimo_intervalo = tentativa - 1
                if rA == 'ME':
                    primeiro_intervalo = tentativa + 1
        tentativa = randint(primeiro_intervalo, ultimo_intervalo)
    print(f'Minhas tentativas: {lista_tentativas}')
    repeat = input('Boa! Consegui acertar! Quer jogar de novo? [ S | N ] ')
    if repeat == 'S':
        adivinhar_numeros()
    else:
        print('Que pena! Espero que volte logo :(')

adivinhar_numeros()
