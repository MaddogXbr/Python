''''
# Explicação do Professor Gustavo
# TUPLA 0,1,2,3 - TUPLAS são imutáveis
lanche = ('Hamburger', 'suco', 'pizza', 'pudim')
for c in range(0, len(lanche)):
    # for c in lanche:
   # print(lanche[-2:])  # Vai do -3 (Suco até o final)
    print(f'Eu vou comer {lanche[c]}!')
print('Comi pra caramba !')
print(sorted(lanche))  # Sorted - Coloca em ordem !!!
# Count - conta quantas vezes aparece o item na tupla
print(lanche.count('suco'))
print(lanche.index('suco'))  # Index - mostra em que posição esta o item


print('==='*30)
print('\033[32;45mDesafio 072 - Número por extenso !\033[m\n')
num = ('zero', 'um', 'dois', 'tres', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze',
       'doze', 'treze', 'quatorze', 'quinze', 'dezeseis', 'dezesete', 'dezoito', 'dezenove', 'vinte')
while True:
    n = int(input('Digite um número de 0 a 20: '))
    while True:

        if 0 <= n <= 20:
            break
        else:
            n = int(input('Tente novamente. Digite um número de 0 a 20: '))
    print(f'\nO número escolhido foi o {num[n]}, {n}\n')
    s = str(input('Deseja fazer novamente (S/N)? ')).upper().strip()
    while s not in 'SN':
        s = str(input('Opção incorreta. Deseja fazer novamente (S/N)? ')
                ).upper().strip()
    if s == 'N':
        break
print('Fim do Programa !\n')


print('***'*30)
print('\033[25;41mDesafio 073 - Times de Futebol !\033[m\n')
times = ('Palmeiras', 'Corinthians', 'Fluminense', 'Atlético-MG', 'Athletico-PR', 'Flamengo', 'Internacional', 'Red Bull Bragantino',
         'Santos', 'São Paulo', 'Botafogo', 'Ceará', 'Goiás', 'América-MG', 'Avaí', 'Cuiabá', 'Coritiba', 'Atlético-GO', 'Juventude', 'Fortaleza')
print('Primeiros 5 times da tabela: ', times[0: 5], '\n')
print('Os lanternas : ', times[-4:], '\n')
print('Times em ordem alfabética: ', sorted(times), '\n')
print(f'O Avaí está em {times.index("Avaí")}º lugar!\n')


from random import randint, sample
print('*-'*35)
print('\033[33;42mDesafio 074 - Maior e menor valor !\033[m\n')
tup = (randint(0, 10), randint(0, 10), randint(
    0, 10), randint(0, 10), randint(0, 10))
menor = maior = 0
cont = 0
# print(tup)
print(f'\nOs valores da Tupla são: ', end=" ")
while True:
    print(f'{tup[cont]}', end=" ")
    if cont == 0:
        menor = maior = tup[0]
    if menor > tup[cont]:
        menor = tup[cont]
    if maior < tup[cont]:
        maior = tup[cont]
    cont += 1
    if cont == 5:
        break
print(f'\n\nO menor número é o {menor} !\n')
print(f'O maior número é o {maior} !\n')
print('Fim do Programa !\n')
'''

print('***'*35)
print('\033[35;43mDesfio 075 - Quatro numeros !\033[m\n')
n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))
n3 = int(input('Digite o terceiro número: '))
n4 = int(input('Digite o quarto número: '))
tupn = (n1, n2, n3, n4)
# tupn = (int(input('Digite um valor: ')), int(input('Digite mais um valor: ')), int(
#    input('Digite outro valor: ')), int(input('Digite outro valor: ')))
par = c = 0
print("\n", tupn)
print(f'\nO número 9 aparece {tupn.count(9)} vezes !\n')
if tupn.count(3) != 0:
    print(f'O número 3 aparece na posição {tupn.index(3)+1} !\n')
else:
    print(f'O número 3 não aparece na Tupla !\n')

while True:
    if tupn[c] % 2 == 0:
        par += 1
    c += 1
    if c == 4:
        break
print(f'Existem {par} número(s) par(es) !\n')
print('Fim do Programa !\n')
