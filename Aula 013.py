'''
for c in range(12, 0, -2):
    print('Passo {}'.format(c))
print('fim')

from time import sleep

print('***'*30)
print('Desafio 046 - Contagem regressiva !\n')
enter = input('Pressione ENTER para iniciar a contagem regressiva: ')
for c in range(10, -1, -1):
    print(c)
    sleep(1)
print('\n\033[1;32;46mBOOM!!!\033[m\n')
print('\nFim do Programa !\n')

print('***'*40)
print('Desafio 047 - Contagem de Pares !\n')
input('Pressione Enter para iniciar a contagem dos pares!')
for c in range(2, 51, 2):
    print(c)
print('\nFinal da Contagem\n')
print('Fim do Programa\n')


print('---'*30)
print('Desafio 048 - Soma ímpares multiplos 3 !\n')
s = 0

for x in range(1, 501, 2):
    if x % 3 == 0:
        s += x
print('\nValor de {}'.format(s))
print('\nFim do Programa !\n')

print('----'*30)
print('Desafio 049 - Tabuada do FOR !\n')
tab = int(input('Digite um número para ver a sua tabuada: '))
print('')
for x in range(1, 11):
    print('{} x {:2} = {}'.format(tab, x, (tab*x)))
print('\nFim do Programa !\n')


print('***'*35)
print('\033[1;36;41mDesafio 050 - Soma dos Pares !\033[m\n')
soma = 0
for x in range(0, 6):
    num = int(input('\nDigite um número inteiro: '))
    if num % 2 == 0:
        soma += num
print('\nO valor total é \033[1;45m{}\033[m\n'.format(soma))
print('Fim do Programa !\n')
'''

from datetime import date
from turtle import end_fill
print('-*'*40)
print('\033[46mDesafio 051 - PA !\033[m\n')
termo = int(input('Digite o primeiro termo da PA: '))
razao = int(input('Digite a razão da PA: '))
decimo = termo + (10-1) * razao
for x in range(termo, decimo + razao, razao):
    print(x, end=' - ')
print('\n', termo, razao, x)
print('\nFinal do Programa!\n')

'''
print('--'*30)
print('\033[42mDesafio 052 - Número primo !\033[m\n')
primo = int(input('Digite o número a ser analisado: '))
mult = 0
for x in range(2, primo):
    if primo % x == 0:
        mult += 1
if mult == 0:
    print('\nO número {} é PRIMO !\n'.format(primo))
else:
    print('\nO número {} tem {} múltiplos entre 2 e {}\n'.format(primo, mult, primo))
print('Fim do Programa !\n')

print('***'*30)
print('\033[32;44mDesafio 053 - Palíndromo!\033[m\n')
frase = str(input('Digite a frase a ser analisada: ')).stip().upper()
frase1 = frase.replace(' ', '')
x = int(len(frase1))
nao = 0
metade = int(x/2)
print(x, metade)
for c in range(0, metade):
    print(frase1[c:(c+1)], ' ', frase1[(x-c-1):(x-c)])
    if (frase1[c:(c+1)] != frase1[(x-c-1):(x-c)]):
        nao += 1
if nao == 0:
    print('\nA frase "{}" é um palíndromo !\n'.format(frase))
else:
    print('\nA frase "{}" não é um palíndromo !\n'.format(frase))
'''
print('\n', '-*'*30)
print('\033[4;35;42mDesafio 054 - Grupo de Maioridade!\033[m\n')
maior = 0
menor = 0
data = int(date.today().year)
for c in range(0, 7):
    idade = int(input('Digite o ano do nascimento: '))
    if (data-idade) < 21:
        menor += 1
    else:
        maior += 1
print('\n{} pessoas não atingiram a maioridade!\n'.format(menor))
print('{} pessoas atingiram a maioridade !\n'.format(maior))
print('Fim do Programa !\n')
