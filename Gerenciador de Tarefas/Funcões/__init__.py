def Confirmar(txt):
    while True:
        confimar = input(txt).strip().lower()
        if confimar == 's':
            return True
        elif confimar == 'n':
            return False
        else:
            print('ERRO! Digite [s/n]...')
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
