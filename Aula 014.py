'''
print('*-'*30)
print('\033[35;41mDesafio 57 - Sexo !\033[m\n')

x = str(input('Digite o sexo: ')).strip().upper()[0]
while x not in "MF":
    print('Dados inválidos. Digite o sexo: ')
print(x)
print('\nAté que enfim !\n')

from random import randint
print('---'*45)
print('\033[46mDesafio 058 - Pensar 2.0 !\033[m\n')
acertou = "N"
count = 0
ncpu = randint(0, 10)
while acertou != "S":
    nuser = int(input('Tente adivinhar o número (0 - 10): '))
    if 0 <= nuser <= 10:
        if ncpu != nuser:
            if nuser < ncpu:
                print('\n\033[31mErrou, o número é maior !\033[m\n')
            else:
                print('\n\033[31mErrou, o número é menor!\033[m\n')
        else:
            acertou = "S"
    else:
        print('Favor digitar um número entre 0 e 10 !\n')
        count -= 1
    count += 1
print('\n\033[32mVocê acertou ! O número foi o {} !\033[m'.format(ncpu))
if count == 1:

    print('\033[42mParabéns acertou de primeira !\033[m\n')
else:
    print('Você acertou o número {} e Foram necessárias {} tentativas !\n'.format(
        ncpu, count))
print('Fim do Programa !\n')


print('***'*45)
print('\033[37;42mDesafio 059 - Menu de opções !\033[m\n')
cont = 1
while cont != 0:
    N1 = float(input('Digite o primeiro número: '))
    N2 = float(input('Digite o segundo número: '))
    x = int(input('' # Tres aspas
    [1] Somar
    [2] Multiplicar
    [3] Maior
    [4] Novos Números
    [5] Sair do Programa

    Escolha uma opção: ''))  # Tres aspas
    if 1 <= x <= 5:
        if x != 5:
            if x == 1:
                print(
                    '\nA soma de {:.1f} + {:.1f} = {:.1f}\n'.format(N1, N2, N1+N2))
            elif x == 2:
                print(
                    '\nA Multiplicação de {:.1f} * {:.1f} = {:.1f}\n'.format(N1, N2, N1*N2))
            elif x == 3:
                if N1 > N2:
                    print(
                        '\nO primeiro número {:.1f} é maior que o segundo número {:.1f}\n'.format(N1, N2))
                elif N2 > N1:
                    print(
                        '\nO segundo número {:.1f} é maior que o primeiro número {:.1f}\n'.format(N2, N1))
                else:
                    print('\nOs números {:.1f} são iguais !\n'.format(N1))
            else:
                print('\nOK, aguardando novos números...\n')
        else:
            cont = 0
    else:
        print('\nOpção Inválida !\n')
print('\nFim do Programa!\n')
'''

print('--'*45)
print('\033[44mDesafio 060 - Cálculo Fatorial !\033[m\n')
c = 1
while c != 0:
    fat = 1
    num = int(input('\nDigite o fatorial ou 0 para sair: '))
    if num != 0:
        print('{}! ='.format(num), end=' ')
        fat *= num
        for x in range(num, 0, -1):
            print('{}'.format(x), end=" ")
            print("x " if x != 1 else "", end="")
            fat *= x
    else:
        c = 0
    if c != 0:
        print('= {}'.format(fat))
print('\nFim do Programa !\n')
