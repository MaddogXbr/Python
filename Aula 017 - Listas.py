'''
print('**'*35)
print('\033[33;43mDesfio 078 - Maior e Menor na Lista!\033[m\n')
Lista = []

for c in range(0, 5):
    Lista.append(int(input('Digite um valor: ')))
    if c == 0:
        maior = menor = Lista[c]
    if maior < Lista[c]:
        maior = Lista[c]
    if menor > Lista[c]:
        menor = Lista[c]

# for c, v in enumerate(Lista):
#    if maior == Lista[c]:
#        maior.append(c)
#    if menor == Lista[c]:
#        menor.append(c)
print('-='*40)
print(f'Você digitou os valores {Lista}')
print(f'\nO maior valor foi o {maior} nas posição(ões): ', end='')
for c, v in enumerate(Lista):
    if v == maior:
        print(f'{c} ', end='')
print(f'\n\nO menor valor foi o {menor} nas posição(ões): ', end='')
for c, v in enumerate(Lista):
    if v == menor:
        print(f'{c} ', end='')
# print(f'Lista{Lista}, Maior - {maior}, Menor - {menor}')
print('\n\nFim do Programa !\n')

                                                                     
print('\n\033[37,42mDesafio 079 - Valores únicos na Lista !\033[m\n')
valores = []
while True:
    N = int(input('Digite um número: '))
    if N not in valores:
        valores.append(N)
        print('Adicionado com sucesso !')
    else:
        print('Valor duplicado, não adicionado !')
    s = str(input('Deseja inserir outro valor? (S/N) ')).upper().strip()
    while s not in 'SN':
        s = str(input('Deseja inserir outro valor? (S/N) ')).upper().strip()
    if s == 'N':
        break
valores.sort()
print(f'\nOs valores digitados foram {valores} !')
print('\nFim do Programa !\n')


print('\033[36mDesafio 080 - Lista Ordenada sem o Sort !\033[m')
ordem = []
x = 0
for c in range(0, 5):
    N1 = int(input('Digite um valor: '))
    if c == 0: # "or N1 >ordem[-1]"
        ordem.append(N1)
    else:
        x = 0
        while True:
            if x == len(ordem):
                ordem.insert(x, N1)
                break
            elif N1 < ordem[x]:
                ordem.insert(x, N1)
                break
            x += 1
    if x != (len(ordem)-1):
        print(f'Valor adicionado na posição {x} da lista !')
    else:
        print('Item adicionado no final da lista !')
print(f'\nOs valores adicionados foram {ordem}')
print('\nFim do Programa !\n')

'''
print('####'*30)
print('\033[36;44mDesafio 081 - Dados de uma lista!\033[m\n')
lista = []
c = count = 0
sel = 'S'
while sel != "N":
    n1 = int(input('Digite um número: '))
    if n1 == 5:
        count += 1
    if c == 0:
        lista.append(n1)
        c += 1
    else:
        x = 0
        while True:
            if x == len(lista):
                lista.insert(x, n1)
                break
            elif n1 > lista[x]:
                lista.insert(x, n1)
                break
            x += 1
    while True:
        sel = str(input('Deseja continuar (s/n): ')).upper().strip()
        if sel in "SN":
            break
# lista.sort(reverse=True)
print('--'*35)
print(f'\nForam digitados {len(lista)} números !')
print(f'\nOs valores adicionados foram: {lista}')
if count != 0:
    print('\nO número 5 aparece na lista !')
else:
    print('\nO número 5 não aparece na lista !')
# if 5 in lista:

print('\nFim do Programa !\n')
