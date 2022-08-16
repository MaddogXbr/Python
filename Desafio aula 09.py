from tracemalloc import start
from unicodedata import name


print('\nDesafio 022 !\n')
nome = input('Nome completo: ')
print(nome.upper())
print(nome.lower())
print(nome.replace(' ', '').count(''))
print(nome.replace(' ', ''))
lista = nome.split()
print('O primeiro nome é "{}" e tem {} letras. '.format(
    lista[0], (len(lista[0]))))
print('\nCidade começa com "SANTO"? ',
      ('santo' in str(lista[0].lower())))  # Desafio 024
print('Tem SILVA no nome: ', ('silva' in nome.lower()))  # Desafio 025
print('\nO primeiro nome é: {} '.format(lista[0]))  # Desafio 027
print('O último nome é:  {}\n'.format(lista[-1]))

print('--'*30)
print('\nDesafio 023 !\n')
numero = input('Digite um número(0 a 9999): ')
numero = "000" + numero
print('Unidade = ', numero[-1])
print('Dezena = ', numero[-2])
print('Centena = ', numero[-3])
print('Milhar = ', numero[-4])

print('--'*30)
print('\nDesafio 026 !\n')
frase = input('Escreva uma frase: ')
print('A letra "A" aparece {} vezes. \n'.format(frase.lower().count('a')))
print('A primeira posição da letra "A" é {}. \n'.format(
    frase.lower().find('a')+1))  # Primeira posição da letra A
print('A última posição da letra "A" é {} !\n'.format(
    frase.lower().rfind('a')+1))
