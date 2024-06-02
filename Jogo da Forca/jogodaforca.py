from random import choice
def escolha_palavra():
    lista_palavrascomdicas = [('maçã', 'fruta vermelha'), ('laranja', 'fruta que também é cor'), ('carro', 'automóvel que todos podem comprar'), ('paralelepípedo', 'forma geométrica espacial'), ('cachorro', 'animal doméstico que não cai em pé'), ('anitta', 'cantora brasileira pedro álvares cabral')]
    lista_palavras = ['maçã', 'laranja', 'carro', 'paralelepípedo', 'cachorro', 'anitta']
    palavras = dict(lista_palavrascomdicas)
    escolha = choice(lista_palavras)
    Quantidade_Erros = 0
    Quantidade_Tracos = len(escolha)
    adivinhar = ['_'] * Quantidade_Tracos
    gabarito = list(escolha)
    print(adivinhar)
    print(f'DICA: {palavras[escolha]}')
    while adivinhar != gabarito:
        resposta = input('Digite sua tentativa: ')
        if resposta in gabarito:
            print('Você acertou!')
            i = 0
            fim = Quantidade_Tracos
            while fim >= 0:
                while i <= (fim - 1):
                    if resposta == gabarito[i]:
                        adivinhar[i] = resposta
                    i += 1
                fim -= 1
            print(adivinhar)
        if resposta not in gabarito:
            if Quantidade_Erros == 0:
                print('--\n |')
                print(' O')
            if Quantidade_Erros == 1:
                print('--\n |')
                print(' O\n/')
            if Quantidade_Erros == 2:
                print('--\n |')
                print(' O\n/I')
            if Quantidade_Erros == 3:
                print('--\n |')
                print(' O\n/I\\')
            if Quantidade_Erros == 4:
                print('--\n |')
                print(' O\n/I\\\n I')
            if Quantidade_Erros == 5:
                print('--\n |')
                print(' O\n/I\\\n I\n/')
            if Quantidade_Erros == 6:
                print('--\n |')
                print(' O\n/I\\\n I\n/ \\')
                print('Você perdeu!')
                break                
            Quantidade_Erros += 1
    print('Você venceu!')


    # O
    #/I\
    # I
    #/ \

#Programa principal
escolha_palavra()