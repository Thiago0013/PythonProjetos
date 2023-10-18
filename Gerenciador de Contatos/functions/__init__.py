from time import sleep
import os
Save = 'Salvar.txt'
def Reescrever(dado):
    os.remove(Save)
    for d in dado:
        Salvar(d)
def Confirmar(txt):
    while True:
        confimar = input(txt).strip().lower()
        if confimar == 's':
            return True
        elif confimar == 'n':
            return False
        else:
            print('ERRO! Digite [s/n]...')
def Dados():
    try:
        with open(Save, 'r') as file:
            dados = file.read().split()
    except:
        print('O arquivo ainda não foi criado... Adicione contatos para criar o arquivo!')
    else:
        Salvo = list()
        while len(dados) != 0:
            dado = {'Nome': dados[0], 'Sobrenome': dados[1], 'Telefone Celular': dados[2], 'E-mail': dados[3]}
            Salvo.append(dado)
            for _ in range(0,4):
                dados.pop(0)
    return Salvo
def Editar():
    while True:
        print("=" * 40)
        print('Editar Contatos'.center(40))
        print("=" * 40)
        print('Contatos:')
        valor = Dados()
        for num,valores in enumerate(valor):   
            print(f'[{num}] - {valores["Nome"]}')
        print(f'[{len(valor)}] - Sair do modo edição')
        print("=" * 40)
        opc = verifyInt(f'Escolha o numero das opções de quem deseja editar: ')
        if 0 <= opc <= len(valor) - 1:
            while True:
                print("=" * 40)
                numerar = 1
                for n,d in valor[opc].items():
                    print(f'[{numerar}] - {n}: {d}')
                    numerar += 1
                print(f'[5] - Finalizar e Salvar')
                print(f'[6] - Cancelar e Sair')
                print("=" * 40)
                opc2 = verifyInt(f'Digite o numero do item que deseja editar: ')
                print("=" * 40)
                if opc2 == 1: #nome
                    print('Você está editando o nome')
                    novo_nome = input('Digite o novo nome: ')
                    valor[opc]["Nome"] = novo_nome
                elif opc2 == 2: #Sobrenome
                    print('Você está editando o Sobrenome')
                    novo_sobrenome = input('Digite o novo nome: ')
                    valor[opc]["Sobrenome"] = novo_sobrenome
                elif opc2 == 3: #Numero de Telefone
                    print('Você está editando o Numero de Telefone')
                    novo_telefone = Telefone()
                    valor[opc]["Telefone Celular"] = novo_telefone
                elif opc2 == 4: #E-mail
                    print('Você está editando o E-mail')
                    novo_Email = Email('Seu novo E-mail: ')
                    valor[opc]["E-mail"] = novo_Email
                elif opc2 == 5: #Finalizar
                    print('Salvando', end='')
                    for _ in range(0,5):
                        print('.', end='',flush=True)
                        sleep(1)
                    Reescrever(valor)
                    print("\nSalvado com sucesso!")
                    sleep(2)
                elif opc2 == 6: #Finalizar e Sair
                    certeza = Confirmar('Essa ação sairá sem salvar, tem certeza que deseja sair? [s/n]: ')
                    if certeza:
                        break
        elif opc == len(valor):
            break
        else:
            print('ERRO! Digite um dos numeros mostrados...')
def verifyInt(txt):
    while True:
        try:
            num = int(input(txt))
        except:
            print('ERRO! Digite um numero intetiro valido!')
        else:
            return num
def verifyFloat(txt):
    while True:
        try:
            num = float(input(txt))
        except:
            print('ERRO! Digite um numero valido!')
        else:
            return num
def Salvar(dados):
    salvolist = list()
    for dado in dados.values():
        salvolist.append(dado)
    with open(Save, 'a') as file:
        file.write(f'{" ".join(salvolist)} \n')
def Telefone():
    while True:
        print('ATENÇÃO: Trabalhamos apenas com o DDI nacional Brasil (+55)...')
        print('Exemplo: (xx) 9xxxx-xxxx (exatamente assim substituindo os x.)')
        ddd = input('Digite seu DDD: ')
        while True:
            if '(' in ddd and ')' in ddd:
                if ddd[ddd.index('(') + 1].isnumeric() and ddd[ddd.index(')') - 1].isnumeric() and len(ddd) == 4:
                    telefone= input(f'Digite seu numero de telefone: {ddd} ').replace('-', '')
                    print('Validando...')
                    sleep(3)
                    if len(telefone) == 8:
                        numero = ddd
                        verificar = True
                        if '-' in telefone:
                            verificar = False
                        for n,a in enumerate(telefone):
                            numero += a
                            if n == 3 and verificar:
                                numero += '-'
                        confirma = Confirmar(f'Seu numero é: {numero}? [s/n]: ')
                        if confirma:
                            print('Numero validado!')
                            sleep(2)
                            return numero
                        else:
                            break
                    else:
                        print('Numero inválido! Digite o numero com 8 casas...')
                        sleep(2)
                else:
                    print('DDD inválido! Digite novamente...')
                    sleep(2)
                    break
            else:
                remodel = '('
                for n in ddd:
                    remodel += n
                remodel += ')'
                ddd = remodel
def Email(txt):
    while True:
        email = input(txt)
        if email[-10:] == '@gmail.com':
            return email
        else:
            print('ERRO! Houve um erro na digitação do seu email... Digite novamente!')
def Mostrar():
    valor = Dados()
    print("=" * 40)
    for valores in valor:   
        for n, d in valores.items():
            print(f'{n}: {d}')
        print("=" * 40)
        sleep(4)   
def Adicionar():
    print("=" * 40)
    print('Adicionar'.center(40))
    print("=" * 40)
    nome = input('Nome: ')
    sobrennome = input('Sobrenome: ')
    telefone = Telefone('Nummero de Telefone: ')
    email = Email('Email: ')
    dados = {'Nome':nome, 'Sobrenome': sobrennome, 'Telefone_Celular' : telefone, 'E-mail': email}
    print('Cadastrando... Aguarde!')
    Salvar(dados)
    sleep(4)
    print("=" * 40)
    for k,d in dados.items():
        print(f'{k.replace("_", " ")}: {d}')
    sleep(3)