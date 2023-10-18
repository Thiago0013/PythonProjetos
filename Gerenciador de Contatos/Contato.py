from functions import *
while True:
    print("=" * 40)
    print('Menu'.center(40))
    print("=" * 40)
    print('''[1] - Adicionar Contato
[2] - Ver Contatos
[3] - Editar Contatos
[4] - Excluir Contatos
[5] - Sair''')
    print("=" * 40)
    opc = verifyInt('Digite um numero do menu: ')
    if opc == 1:
        Adicionar()
    elif opc == 2:
        Mostrar()
    elif opc == 3:
        Editar()
    elif opc == 4:
        Excluir()
    elif opc == 5:
        break
    else:
        print('ERRO! Digite o numero recorrente as opções!')
        sleep(2)
