'''
Menu do Gerenciador de Lista de Tarefas:
1. Adicionar tarefa 
2. Ver tarefas
3. Atualizar tarefa
4. Completar tarefa 
5. Deletar tarefas completadas
6. Sair
Digite sua escolha: 
'''

#menu em loop que recebe a resposta do usuario
def Menu():
    print('\nMenu do Gerenciador de Lista de Tarefas:')
    print('1. Adicionar tarefa')
    print('2. Ver tarefas')
    print('3. Atualizar tarefa')
    print('4. Completar tarefa')
    print('5. Deletar tarefas')
    print('6. Sair')
    r = int(input('Digite sua escolha: '))
    return r

#função de adicionar tarefas (em lista)
def AdicionarTarefas(tarefas, checktarefas):
    TarefaAdicionar = input('Digite a tarefa a ser adicionada: ')
    tarefas.append(TarefaAdicionar)
    checktarefas.append(0)
    print(f'Você adicionou a tarefa: {TarefaAdicionar}\n')

#função que exibe as tarefas
def ExibirTarefas(tarefas, checktarefas):
    i = 0
    fim = len(tarefas)
    if fim == 0:
        print('Você não tem tarefas adicionadas. \n')
    print('Suas tarefas adicionadas:')
    if fim > 0: 
        while fim >= 0:
            while i <= (fim -1):
                if checktarefas[i] == 0:
                    print(f'{i + 1}. [ ] {tarefas[i]}')
                if checktarefas[i] == 1:
                    print(f'{i + 1}. [X] {tarefas[i]}')
                i += 1
            fim -= 1
    
#função que atuliza as tarefas
def AtualizarTarefas(tarefas, checktarefas):
    ExibirTarefas(tarefas, checktarefas)
    TarefaAtualizar = int(input('Digite o número da tarefa que deseja atualizar: '))
    if (TarefaAtualizar - 1) in range(0, len(tarefas)):
        print(f'A tarefa que deseja atualizar é: {tarefas[(TarefaAtualizar - 1)]}')
        tarefas[(TarefaAtualizar - 1)] = input('Informe o que deseja atualizar: ')
        print(f'A tarefa foi atualizada: {tarefas[(TarefaAtualizar - 1)]}\n')

#função que seleciona as tarefas a ser completadas 
def CompletarTarefas(tarefas, checktarefas):
    ExibirTarefas(tarefas, checktarefas)
    TarefaCompletar = int(input('Digite o número da tarefa que deseja completar: '))
    if (TarefaCompletar - 1) in range(0, len(tarefas)):
        print(f'A tarefa que deseja completar é: {tarefas[(TarefaCompletar - 1)]}')
        checktarefas[(TarefaCompletar - 1)] = 1
        print(f'A tarefa foi completada: {tarefas[(TarefaCompletar - 1)]}\n')

#Deletar as tarefas da lista
def DeletarTarefas(tarefas, checktarefas):
    ExibirTarefas(tarefas, checktarefas)
    TarefaDeletar = int(input('Digite o número da tarefa que deseja deletar: '))
    if (TarefaDeletar - 1) in range(0, len(tarefas)):
        print(f'A tarefa que deseja deletar é: {tarefas[(TarefaDeletar - 1)]}')
        tarefas.remove(tarefas[(TarefaDeletar - 1)])
        checktarefas.remove(checktarefas[(TarefaDeletar - 1)])
        print('Tarefa deletada.')
#################

tarefas = []
checktarefas = []
r = 0
while r != 6:
    r = Menu()
    if r == 1:
        AdicionarTarefas(tarefas, checktarefas)
    if r == 2:
        ExibirTarefas(tarefas, checktarefas)
    if r == 3:
        AtualizarTarefas(tarefas, checktarefas)
    if r == 4:
        CompletarTarefas(tarefas, checktarefas)
    if r == 5:
        DeletarTarefas(tarefas, checktarefas)
    if r == 6:
        print('Programa encerrado.')