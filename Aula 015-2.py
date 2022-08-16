'''
print('-*-*'*20)
print('\033[31;44mDesafio 070 - Estatística em Produtos !\033[m\n')
nbarato = pbarato = tgasto = altos = cont = 0
while True:
    produto = str(input('\nDigite o nome do produto: ')).strip()
    preco = float(input('Digite o valor do produto: '))
    if cont == 0:
        nbarato = produto
        pbarato = preco
        cont += 1
    if preco < pbarato:
        nbarato = produto
        pbarato = preco
    if preco > 1000:
        altos += 1
    tgasto += preco
    cadastro = str(input('Cadastrar outro produto (S/N): ')).upper().strip()[0]
    while cadastro not in "SN":
        cadastro = str(input('Opção inválida! (S/N): ')).upper().strip()[0]
    if cadastro == "N":
        break
print(f'\nO total da compra foi de R$ {tgasto:.2f} ')
print(f'Temos {altos} produtos acima da R$ 1.000,00')
print(f'O produto mais barato foi o {nbarato}, custando R$ {pbarato:.2f}')
print('\nFim do Programa !\n')
'''

print('***'*25)
print(f'\033[0;33;45m{"Desafio 071 - Caixa Eletrônico !":^50}\033[m\n')
print('$$$'*20)
print(f'{"BANCO Perdeu Playboy !":^50}')
print('$$$'*20)
while True:
    n50 = n20 = n10 = n1 = r50 = r20 = 0
    valor = int(input('\nQuanto que deseja sacar: '))
    if valor >= 50:
        n50 = int(valor/50)
        r50 = int(valor % 50)
        if r50 >= 20:
            n20 = int(r50/20)
            r20 = int(r50 % 20)
            if r20 >= 10:
                n10 = int(r20/10)
                n1 = int(r20 % 10)
            else:
                n1 = int(r20)
        elif r50 >= 10:
            n10 = int(r50/10)
            n1 = int(r50 % 10)
        else:
            n1 = int(r50)
    elif valor >= 20:
        n20 = int(valor/20)
        r20 = int(valor % 20)
        if r20 >= 10:
            n10 = int(r20/10)
            n1 = int(r20 % 10)
        else:
            n1 = int(r20)
    elif valor >= 10:
        n10 = int(valor/10)
        n1 = int(valor % 10)
    else:
        n1 = int(valor)
    print(f'\nO quantidade de notas:\n')
    print(f'O saque de R$ {valor:.2f} em:')
    print(f'{n50} notas de 50 reais;')
    print(f'{n20} notas de 20 reais;')
    print(f'{n10} notas de 10 reais;')
    print(f'{n1} notas de  1 real.')
    segue = str(input('\nGostaria de sacar mais ?(S/N) ')).upper().strip()[0]
    while segue not in "SN":
        segue = str(input('Opção inválida! Escolha (S/N): ')
                    ).upper().strip()[0]
    if segue == 'N':
        break
print('\nFim do Programa !\n')
'''

print('Resolução do professor Gustavo !')
print('==='*30)
valor = int(input('Digite o valor a ser sacado: '))
total = valor
ced = 50
totalced = 0
while True:
    if total >= ced:
        total -= ced
        totalced += 1
    else:
        if totalced > 0:
            print(f'O Total de {totalced} de R$ {ced:.2f}')
        if ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 1
        totalced = 0
        if total == 0:
            break
print('==='*30)
print('Fim do Programa !\n')
