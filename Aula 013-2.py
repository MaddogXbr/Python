'''
print('--'*30)
print('\033[47mDesafio 055 - Maior e menor da sequência!\033[m\n')
maior = 0
menor = 0
for c in range(0, 5):
    peso = float(input('Digite o peso: '))
    if peso > maior:
        maior = peso
    elif peso < menor or menor == 0:
        menor = peso
print('\nO maior peso foi o {:.1f}kg\n'.format(maior))
print('O menor peso foi o {:.1f}Kg\n'.format(menor))
print('\nFim do Programa !\n')
'''

print('*-'*40)
print('\n\033[36;44mDesafio 056 - Analisador Completo !\033[m\n')
media = 0
mulheres = 0
velho = ""
age = 0
for x in range(0, 4):
    nome = str(input('\nDigite o nome: '))
    idade = int(input('Digite a idade: '))
    sexo = str(input('Digite o Sexo (M ou F): '))
    media += idade
    if sexo == 'M' and idade > age:
        velho = nome
        age = idade
    elif sexo == 'F' and idade < 20:
        mulheres += 1
print('\nA média de idade do grupo é de {} anos!\n'.format(media/4))
print('O homem mais velho é o {} !\n'.format(velho))
if mulheres != 0:
    print('{} mulheres tem menos de 20 anos !'.format(mulheres))
print('\nFim do Programa !\n')
