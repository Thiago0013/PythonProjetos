from time import sleep
from Funcões import *
while True:
    print('=' * 40)
    print('GERENCIADOR DE TAREFAS'.center(40))
    print('=' * 40)
    print('''[1] - Adicionar Tarefa
[2] - Ver Tarefas
[3] - Marcar Tarefas
[4] - Ver historico de tarefas
[5] - Sair''')
    print('=' * 40)
    opc = verifyInt('Escolha a opção: ')
    if opc == 1:
        Adicionar()
    elif opc == 2:
        Mostrar()
    elif opc == 3:
        pass
    elif opc == 4:
        pass
    elif opc == 5:
        break
    else:
        print('ERRO! Numero incorreto! Digite um numero recorrente ao menu...')
        sleep(2.5)
