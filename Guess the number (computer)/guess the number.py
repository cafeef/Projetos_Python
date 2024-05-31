from random import randint
def numero_aleatorio():
    intervalo = randint(1, 10) #gera um intervalo aleatório
    numero = randint(1, intervalo) #gera o número secreto a ser descoberto, aleatório entre 1 e o intervalo gerado anteriormente
    tentativa = 0 #declaração da variável que o usuário vai modificar em suas respostas, responsável por continuar o loop while
    while tentativa != numero: #loop que só é finalizado se o usuário digitar o número a se descoberto
        tentativa = int(input(f'Adivinhe um número entre 1 e {intervalo}: ')) #input que recebe a resposta do usuário
        if tentativa > numero: #verifica se o número digitado é maior que o secreto
            print('Incorreto. O número é menor que sua tentativa.')
        if tentativa < numero: #verifica se o número digitado é menor que o secreto
            print('Incorreto. O número é maior que sua tentativa.')
    print('Correto! Você digitou o número secreto!') #mensagem de sucesso quando o número fornecido é o secreto

#programa principal
numero_aleatorio()
