from datetime import date
from random import choice
print('--'*30)
print('\nDesafio 028 !\n')
num_us = int(input('Tente adivinhar o número (0-5): '))
num_maq = choice([0, 5])
print('\nAcertou !\n' if num_maq ==
      num_us else '\nErrou !\nEu escolhi o número {} e o seu foi {} !\n'.format(num_maq, num_us))
print('--Fim do Desafio--\n')

print('--'*30)
print('\nDesafio 029 !\n')
V1 = int(input('\nDigite a velocidade do carro: '))
if V1 <= 80:
    print('\nVocê está a {}Km/h !\n'.format(V1))
else:
    multa = int((V1-80)*7)
    print(
        '\nVocê foi multado em R${:.2f}\nE a sua velocidade é de {}Km/h\n'.format(multa, V1))
print('--Fim do Desafio--\n')

print('--'*30)
print('\nDesafio 030 !\n')
numint = int(input('Digite um número: '))
print('\nO número {} é par !\n'.format(numint) if (numint % 2)
      == 0 else ('\nO número {} é impar !\n'.format(numint)))
print('--Fim do Desafio--\n')

print('--'*30)
print('\nDesafio 031 !\n')
distancia = int(input('Digite a ditância de sua viagem: '))
if distancia <= 200:
    print('\nO valor da sua passagem é de R${:.2f} para a distância de {}Km\n'.format(
        float(distancia*0.5), distancia))
else:
    print('\nO valor da sua passagem é de R${:.2f} para a distância de {}Km\n'.format(
        float(distancia*0.45), distancia))
print('--Fim do Desafio !--')

print('--'*30)
print('\nDesafio 032 !\n')
ano = int(input('Digite um ano para analisar se é bissexto ou 0 para o ano atual: '))
if ano == 0:
    ano = date.today().year
print('\nO ano {} é bissexto !\n'.format(ano) if (ano % 4) ==
      0 and ano % 100 != 0 or ano % 400 == 0 else ('\nO ano {} não é bissexto !\n'.format(ano)))
print("--Fim do Desafio--\n")
