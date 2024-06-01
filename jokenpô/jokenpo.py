from random import choice
def jokenpo():
    lista_jokenpo = ['PEDRA', 'PAPEL', 'TESOURA']
    print('Vamos jogar pedra, papel e tesoura!')
    Resposta_Usuario = input('| [PEDRA]\n| [PAPEL]\n| [TESOURA]\n')
    Resposta_Computador = choice(lista_jokenpo)
    print(f'Sua resposta: {Resposta_Usuario}')
    print(f'Minha resposta: {Resposta_Computador}')
    if Resposta_Usuario == Resposta_Computador:
        print('Empatamos!')
    if Resposta_Usuario == 'PEDRA':
        if Resposta_Computador == 'PAPEL':
            print('Papel cobre pedra! Eu venci.')
        if Resposta_Computador == 'TESOURA':
            print('Pedra quebra tesoura. Você venceu!')
    if Resposta_Usuario == 'PAPEL':
        if Resposta_Computador == 'PEDRA':
            print('Papel cobre pedra. Você venceu!')
        if Resposta_Computador == 'TESOURA':
            print('Tesoura corta papel! Eu venci.')
    if Resposta_Usuario == 'TESOURA':
        if Resposta_Computador == 'PAPEL':
            print('Tesoura corta papel. Você venceu!')
        if Resposta_Computador == 'PEDRA':
            print('Pedra quebra tesoura. Eu venci!')
while True:
    jokenpo()
    r = input('Quer jogar de novo? [ S | N ]')
    if r == 'N':
        break