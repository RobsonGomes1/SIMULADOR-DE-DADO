try:
    dados = [ 1, 2, 3, 4, 5, 6, 7 ,8 ,9 ,10]
except:
    print('Error... Invalid code')
else:
    op = 0
    while op != 2:
        print('-' *10, 'Jogando dado', '-' *10)
        print('Opção: Escrava [1] para jogar '.strip().upper())
        print('Opção: Escreva [2] para sair'.strip().upper())
        op = int(input('Qual opção: \n'.strip()))

        if op == 1:
            op1 = int(input('Qual numero irá cair!? \n'))
            from time import sleep
            from random import randint

            sor = randint(1, 10)

            print('Analisando...')
            sleep(1)
            print('Dado jogado...')
            sleep(1.3)
            print('Girando...')
            sleep(0.7)
            print('Resultado é:\n....')
            sleep(0.0)
            print('Resultado: {} do valor escolhido: {}'.format(sor, op1))
            sleep(0.1)
        elif op == 2:
            from time import sleep
            print('Finalizando...')
            sleep(0.1)
        else:
            from time import  sleep

            print('................')
            sleep(1.1)
            print('................')
            sleep(1.1)
            print('Operação não reconhecida')
            sleep(1.0)
finally:
    print('Volte Sempre! Very Ty. :)')

