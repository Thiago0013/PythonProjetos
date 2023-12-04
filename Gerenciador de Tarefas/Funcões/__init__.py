from time import sleep
import datetime
SaveName = 'DataGerenciador.txt'
def Menu(txt):
    print('=' * 40)
    print(txt.center(40))
    print('=' * 40)
def Dados(Valor=False, Salvar='S'):
    if Salvar == 'S':
        with open(SaveName, 'a') as file:
            for d in Valor:
                d = str(d)
                file.write(f'{d} ')
    elif Salvar == 'R':
        with open(SaveName, 'w') as file:
            file.write('')
        with open(SaveName, 'a') as file:
            for d in Valor:
                d = str(d)
                file.write(f'{d} ')
    elif Salvar == 'P':
        try:
            with open(SaveName, 'r') as file:
                ver = file.read().split()
        except: 
            print('Arquvo não existe! Adicione uma tarefa para criar o arquivo...')
            return None
        else:
            Save = list()
            while len(ver) != 0:
                dados = {'Nome': EditText(ver[0], False), 'Descrição':EditText(ver[1], False), 'Data de criação': ver[2], 'Data de validade': ver[3], 'Situação':ver[4]}
                Save.append(dados)
                for _ in range(0,5):
                    ver.pop(0)
            return Save
def VerifyDate():
        while True:
            ano = verifyInt('Ano: ')
            while True:
                mes = verifyInt('Mês: ')
                if 0 < mes <= 12:
                    if mes < 10:
                        mes = f'0{mes}'
                        mes = int(mes)
                        break
                    break
                else:
                    print('ERRO! Digite um mês de 01 a 12')
            while True:
                dia = verifyInt('Dia: ')
                if ano % 4 > 0 and mes == 2 and 0 < dia >= 29: #Verifica se o ano é bissexto
                    print(f'ERRO! Em ano bissexto o mês de Fevereiro só vai até o dia 29!')
                elif ano % 4 == 0 and mes == 2 and 0 < dia <= 29:
                    break
                elif 0 < dia <= 31:
                    break
                else:
                    print('ERRO! Digite a data entre 0 a 31')
            while True:
                if int(datetime.datetime.now().strftime('%Y')) == ano: #Verifica se o ano é igual o ano atual
                    if int(datetime.datetime.now().strftime('%m')) == mes: #Verifica se o mês é igual o mês atual
                        if int(datetime.datetime.now().strftime('%d')) < dia: #Verifica se o dia é maior que o dia atual
                            data = f'{str(ano)}-{str(mes)}-{str(dia)}'
                            return data
                        else:
                            print('ERRO! O dia adicionado é menor ou igual que o dia atual!')
                            sleep(3)
                            break
                    elif int(datetime.datetime.now().strftime('%m')) < mes: #Verifica se o mês é maior que o atual
                        data = f'{str(ano)}-{mes:02d}-{dia:02d}'
                        return data
                    else:
                        print('ERRO! O mês adicionado é menor que o mês atual!')
                        sleep(3)
                        break
                elif int(datetime.datetime.now().strftime('%Y')) < ano: #Verifica se o ano é maior que o atual
                    data = f'{str(ano)}-{mes:02d}-{dia:02d}'
                    return data
                else:
                    print('ERRO! O ano adicionado é menor que o ano atual!')
                    sleep(3)
                    break
def Tempo():
    data_atual = datetime.datetime.now().strftime('%Y-%m-%d')
    return data_atual
def CriarArquivo():
    try:
        with open(SaveName, 'r') as file:
            file.read()
    except:
        print('Criando arquivo...')
        sleep(3)
        with open(SaveName, 'w') as file:
            file.write('')
def Confirmar(txt):
    while True:
        confimar = input(txt).strip().lower()
        if confimar == 's':
            return True
        elif confimar == 'n':
            return False
        else:
            print('ERRO! Digite [s/n]...')
def EditText(txt, editar=True):
    if editar:
        txt = txt.replace(' ', '-')
        return txt
    else:
        txt = txt.replace('-', ' ')
        return txt
def verifyInt(txt):
    while True:
        try:
            num = int(input(txt))
        except:
            print('ERRO! Digite um numero inteiro valido!')
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
def Excluir(Lista, opc):
    print('Apagando...')
    Lista.pop(opc)
    sleep(2)
    print('Apagado!')
    return Lista
def Marcar():
    while True:
        Menu('Marcar')
        Lista = Dados(Salvar='P')
        if Lista is not None:
            for n,d in enumerate(Lista):
                print(f"{n+1}º {d['Nome']}; Va:{d['Data de validade']}; Marcado[{'✓' if d['Situação'] == True else 'X'}]")
            while True:
                print('=' * 40)
                opc = verifyInt('Escolha a opção que deseja marcar: ') - 1
                if opc < len(Lista):
                    print('=' * 40)
                    print(f'''Nome: {Lista[opc]['Nome']}
Descrição :{Lista[opc]['Descrição']}
Data de criação: {Lista[opc]['Data de criação']}
Data de validade: {Lista[opc]['Data de validade']}
Marcado[{'✓' if Lista[opc]['Situação'] == True else 'X'}]''')  
                    print('=' * 40)
                    sleep(2)
                    print('''[1] - Marcar como feita
[2] - Marcar como não feita
[3] - Excluir
[4] - Cancelar''')
                    break
                else:
                    print('ERRO! Esse numero não existe no menu')
            while True:
                print('=' * 40)
                opc2 = verifyInt('Escolha a opção: ')
                print('=' * 40)
                if opc2 == 1:
                    Lista[opc]['Situação'] = True
                    print(f'Marcado como feita!')
                    break
                elif opc2 == 2:
                    if Lista[opc]['Situação'] == True:
                        Lista[opc]['Situação'] = False
                        print(f'Marcado como não feita!')
                        break
                    else:
                        print('Essa opção já está como não feita!')
                elif opc2 == 3:
                    salva = list()
                    Lista = Excluir(Lista,opc)
                    for d in Lista:
                        for s in d.values():
                            salva.append(s)
                    Dados(salva, 'R')
                    break
                elif opc2 == 4:
                    break
                else:
                    print('ERRO! Digite o numero mostrado no menu')  
        else:
            break
def Editar(dado, opc):
    while True:
        Menu('Editar')
        number = 0
        for n,d in dado[opc - 1].items():
            number += 1
            if 1 <= number < 3 or 4 == number < 5:
                if n == 'Name' or n == 'Descrição':
                    print(f'{n}: {EditText(d, False)}')
                else:
                    print(f'{n}: {d}')
        print('Sair')
        print('=' * 40)
        opc2 = (input('Digite o nome do item que deseja editar: ').capitalize())
        if opc2 in dado[opc - 1]:
            if opc2 == 'Nome':
                dado[opc - 1][opc2] = input('Digite o novo nome: ')
            elif opc2 == 'Descrição':
                dado[opc - 1][opc2] = input('Digite a nova descrição: ')
            elif opc2 == 'Data de validade':
                dado[opc - 1][opc2] = VerifyDate()
            print(dado)
        elif opc2 == "Sair":
            dado[opc - 1]['Nome'] = EditText(dado[opc - 1]['Nome'])
            dado[opc - 1]['Descrição'] = EditText(dado[opc - 1]['Descrição'])
            return dado
        else:
            print('ERRO! Digite a palavra da forma que aparece no menu')
def Mostrar():
    while True:
        save = list()
        Lista = Dados(Salvar='P')
        if Lista is not None:
            Menu('Mostrar dados')
            for n,d in enumerate(Lista,1):
                print(f"{n}º {d['Nome']} [{'✓' if d['Situação'] == True else 'X'}]")
            print(f'{len(Lista) + 1}º Sair')
            print('=' * 40)
            opc = verifyInt('Digite um numero mostrado: ')
            if 1 <= opc <= len(Lista):
                print('=' * 40)
                for n,v in Lista[opc - 1].items():
                    if n != 'Situação':
                        print(f'{n}: {v}')
                    else:
                         print(f'{n}: [{"Marcada" if v == True else "Não marcada"}]')
                while True:
                    opc2 = input('Deseja editar? [s/n]: ')
                    if opc2 in 'Ss':
                        Lista = Editar(Lista, opc)
                        for dicio in Lista:
                            for dado in dicio.values():
                                save.append(dado)
                        Dados(save, 'R')
                        break
                    elif opc2 in 'Nn':
                        break
                    else:
                        print('ERRO! Digite s ou n')
            elif opc == 3:
                print(Lista)
                break
            else:
                print('ERRO! Digite um numero mostrado na lista!')
                sleep(2)
        else:
            break
def Adicionar():
    Menu('Adicionar Tarefa')
    nome = EditText(input('Nome: '))
    descrição = EditText(input('Descrição: '))
    print('Atenção: Data de validade contem o formato xxxx-xx-xx')
    data_validade = VerifyDate()
    Valor = [nome, descrição, Tempo(), data_validade, False]
    print('Aguarde...')
    Dados(Valor, 'S')
    sleep(3)
    print('Arquivo criado!')
Marcar()