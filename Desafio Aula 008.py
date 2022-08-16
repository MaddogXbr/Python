from random import choice
from math import sin, cos, tan, radians  # Pode ser Import math
import random

ang = radians(float(input('\nDigite um ângulo: ')))
print('O ângulo {:0.1f} tem:\n Seno {:0.2f}\n Cosseno {:0.2f}\n Tangente {:0.2f}\n'.format(
    ang, (sin(ang)), (cos(ang)), (tan(ang))))

print('--'*30)
print('\nDesafio 019 e 020!\n')
n1 = str(input('Primeiro aluno: '))
n2 = str(input('Segundo aluno: '))
n3 = str(input('Terceiro aluno: '))
n4 = str(input('Quarto aluno: '))
lista = [n1, n2, n3, n4]
random.shuffle(lista)
print('\nO aluno escolhido foi o {}!\n'.format((random.choice(lista))))
print(lista)
