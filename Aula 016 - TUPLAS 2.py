'''
print('\033[36mDesafio 076 - Lista de Preços !\033[m\n')
lista = ('Pão', 1.3, "Leite", 6.80, "Creme de leite",
         4.2, 'Café', 8.65, 'Presunto', 12.52, 'Cafeteira', 120.00)
print('--'*20)
print(f'{"LISTAGEM DE PREÇO":^40}')
print('--'*20)
x = 0
while x != len(lista):
    print(f'{lista[x]:.<30}R$ {lista[x+1]:>7.2f}')
    x += 2
print('--'*21)
print('\nfim do programa !\n')
'''

print('***'*30)
print('\033[37;43mDesafio 077 - Vogais em Tupla !\033[m\n')
palavras = ('estrutura', 'compostas', 'TUPLAS', 'armazenar', 'valores', 'Python',
            'aula', 'individuais', 'aprender', 'seguinte', 'acessiveis', 'curso')
# print(palavras[0][2].upper())
x = 0
while x != len(palavras):
    l = 0
    print(f'\nA palavra {palavras[x].upper().strip()} tem: ', end='')
    while l != len(palavras[x]):
        if palavras[x][l].upper() == 'A':
            print(f'a', end=' ')
        elif palavras[x][l].upper() == 'E':
            print('e', end=' ')
        elif palavras[x][l].upper() == 'I':
            print('i', end=' ')
        elif palavras[x][l].upper() == 'O':
            print('o', end=' ')
        elif palavras[x][l].upper() == 'U':
            print('u', end=' ')
        l += 1
    x += 1
"""
 **** Solução do Professor: 
for p in palavras:
    print(f'\nNa palavra {p.upper()} temos ', end='')
    for letra in p:
        if letra.lower() in 'aeiou':
            print(letra.lower(), end=' ')
"""
print('\n\nFim do Programa !\n')
