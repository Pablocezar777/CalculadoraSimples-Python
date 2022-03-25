from time import sleep
while True:
    print('---'*30)
    n1 = int(input('Selecione a operação desejada: \n1)Adição 2)Subtração 3)Multplicação 4)Divisão:'))
    n2 = int(input('Digite o primeiro número:'))
    n3 = int(input('Digite o segundo número:'))
    print('...')
    print('---'*30)
    sleep(1)
    if n1 == 1:
        print('{} + {} = {}'.format(n2, n3, n2+n3))
        n = int(input('Deseja continuar? Se sim digite 1 caso não digite 0:'))
        if n == 1:
            continue
        if n != 1:
            break
    if n1 == 2:
        print('{} - {} = {}'.format(n2, n3, n2-n3))
        n = int(input('Deseja continuar? Se sim digite 1 caso não digite 0:'))
        if n == 1:
            continue
        if n != 1:
            break
    if n1 == 3:
        print('{} x {} = {}'.format(n2, n3, n2*n3))
        n = int(input('Deseja continuar? Se sim digite 1 caso não digite 0:'))
        if n == 1:
            continue
        if n != 1:
            break
    if n1 == 4:
        print('{} % {} = {:.0f}'.format(n2, n3, n2/n3))
        n = int(input('Deseja continuar? Se sim digite 1 caso não digite 0:'))
        if n == 1:
            continue
        if n != 1:
            break
print('SISTEMA ENCERRADO, VOLTE SEMPRE!!!')

