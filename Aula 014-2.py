'''
print('---'*35)
print('\033[42mDesafio 061 - PA 2.0\033[m\n')
# for x in range(0, 10, c)
fecha = "S"
while fecha != "N":
    pa = int(input('\nDigite um número para PA: '))
    razao = int(input('Digite a razão da PA: '))
    count = 1
    soma = pa
    print('\nA Pa de {} = {}'.format(pa, soma), end=' ')
    while count != 10:
        soma += razao
        print(soma, end=" ")
        count += 1
    fecha = str(input('\n\nDeseja fazer outra PA ? (S ou N): ')).upper()
print('\nFim do programa !\n')


print('***'*40)
print('\033[37;41mDesafio 062 - Super PA\033[m\n')
fecha = "S"
while fecha != "N":
    pa = int(input('\nDigite um número para PA: '))
    razao = int(input('Digite a razão da PA: '))
    count = 1
    soma = pa
    termos = 1
    total = 10
    print('\nA Pa de {} = {}'.format(pa, soma), end=' ')
    while count != 10:
        soma += razao
        print(soma, end=" ")
        count += 1
    while termos != 0:
        termos = int(
            input('\n\nDeseja adicionar mais quantos termos (0 para sair): '))
        total += termos
        if termos != 0:
            count = termos
            while count != 0:
                soma += razao
                print(soma, end=' ')
                count -= 1
    print('\nO apresentados {} termos da PA {} com razão {}'.format(total, pa, razao))
    fecha = str(input('\n\nDeseja fazer outra PA ? (S ou N): ')).upper()
print('\nFim do programa !\n')


print('---'*45)
print('\033[34;41mDesafio 063 - Fibonacci !\033[m\n')
cont = "S"
while cont != "N":
    T1 = 0
    T2 = 1
    T3 = 0
    n = int(input('Digite o número elementos da sequência de Fibonacci (0 para sair): '))
    if n != 0:
        print(
            '\nOs primeiros {} elementos da sequência de Fibonacci : 0'.format(n), end=' ')
        while n != 0:
            print('-> {}'.format(T2), end=" ")
            T3 = T2 + T1
            T1 = T2
            T2 = T3
            n -= 1
    cont = str(input('\n\nDeseja recomeçar? (S ou N): ')).upper()
print('\nFim do Programa !\n')


print('---'*40)
print('\033[46mDesafio 064 - Vários Valores !\033[m\n')
# x = 'S'
soma = 0
quant = 0

# while x != 'N':
num = int(input('Digite um número (999 para Sair): '))
while num != 999:
    # if num != 999:
    soma += num
    quant += 1
    # else:
    #    x = "N"
    num = int(input('Digite um número (999 para Sair): '))
print('\nForam digitados {} números\nCom a soma = {}\n'.format(quant, soma))
print('\nFim do Programa\n')
'''

print('==='*40)
print('\033[35;43mDesafio 065 - Maior e Menor!\033[m\n')
y = "S"
maior = quant = total = menor = 0
#menor = 1000
while y != 'N':
    n = int(input('\nDigite um número: '))
    quant += 1
    total += n
    if quant == 1:
        maior = menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n
    y = str(input('\nQuer continuar? (S ou N): ')).upper().strip()[0]
print('\nA média entre todos os {} números foi: {:.1f} \n'.format(quant, total/quant))
print('O maior número foi o {} e o Menor {} !'.format(maior, menor))
print('\nFim do Programa !\n')
