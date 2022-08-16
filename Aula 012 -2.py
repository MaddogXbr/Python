'''
print('-*'*30)
print('\033[1;36mDesafio 042 - Tipo de Triângulo !\033[m\n')
R1 = float(input('Digite o valor da primeira reta: '))
R2 = float(input('\nDigite o valor da segunda reta: '))
R3 = float(input('\nDigite o valor da terceira reta: '))
if R1 < R2+R3 and R2 < R1+R3 and R3 < R1+R2:
    if R1 == R2  == R3:
        print('\nAs retas geram um triângulo Equilátero !')
    elif R1 != R2 and R2 != R3 and R3 != R1:
        print('\nAs retas geram um triângulo Escaleno !')
    else:
        print('\nAs retas geram um triângulo Isósceles !')
else:
    print('\n\033[0;31mAs retas {:.1f}, {:.1f} e {:.1f} não podem formar um triângulo\033[m'.format(
        R1, R2, R3))
print('\nFim do Programa !\n')
-----
print('-*'*30)
print('\033[0;35mDesafio 043 - IMC !\033[m\n')
peso = float(input('Digite o seu peso: '))
altura = float(input('\nDigite a sua altura: '))
imc = (peso / (altura * altura))
if imc < 18.5:
    print('\nIMC = {:.1f}\nAbaixo do peso !'.format(imc))
elif imc >= 18.5 and imc < 25:
    print('\nIMC = {:.1f}\nPeso ideal !'.format(imc))
elif imc >= 25 and imc < 30:
    print('\nIMC = {:.1f}\nSobrepeso !'.format(imc))
elif imc >= 30 and imc < 40:
    print('\nIMC = {:.1f}\nObesidade !'.format(imc))
else:
    print('\nObesidade Mórbida !')
print('\nFim do Programa !\n')
---
print('-*'*30)
print('\nDesafio 044 - Parcelamento Compra !\n')
produto = float(input('Digite o valor do produto: '))
parc = int(input(
    '\n1 - À vista \033[0;34mdinheiro/Cheque\033[m (10% desconto)\n2 - À vista cartão (5% desconto)\n3 - 2x no cartão (sem juros)\n4 - 3x ou mais (20% juros)\nEscolha uma das opções: '))
if parc == 1:
    print('\nO valor do produto será R$ {:.2f} !'.format(produto*0.9))
elif parc == 2:
    print('\nO valor do produto será R$ {:.2f} !'.format(produto*0.95))
elif parc == 3:
    print('\nO valor da parcela será R$ {:.2f} !'.format(produto/2))
elif parc == 4:
    print('\nO valor do produto será R$ {:.2f} !'.format(produto*1.2))
else:
    print('\nOpção incorreta !')
print('\nFim do programa !\n')
'''
from time import sleep
from emoji import emojize
from random import randint

print('-*'*30)
print('\nDesafio 045 - Jokenpô !\n')
# Descrição dos emojis
pedra = emojize(':oncoming_fist:')
papel = emojize(':hand_with_fingers_splayed:')
tesoura = emojize(':victory_hand:')
esc_user = int(input(
    '1 - Pedra {}\n2 - Papel {}\n3 - Tesoura {}\nEscolha a opção: '.format((pedra), (papel), (tesoura))))
esc_cpu = randint(1, 3)  # Escolha randomica
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PÔ!!!')
# Print do Emoji
if esc_user == 1:
    emoj_user = pedra
elif esc_user == 2:
    emoj_user = papel
else:
    emoj_user = tesoura
if esc_cpu == 1:
    emoj_cpu = pedra
elif esc_cpu == 2:
    emoj_cpu = papel
else:
    emoj_cpu = tesoura

if esc_user < 1 or esc_user > 3:  # Inicio do Jogo
    print('\n\033[4;30;41mOpção Inválida !\033[m\n')
elif (esc_user == 1 and esc_cpu == 3) or (esc_user == 2 and esc_cpu == 1) or (esc_user == 3 and esc_cpu == 2):
    print('\n\033[1;32mVocê ganhou !\nVocê  {}  x {}  CPU !\033[m\n'.format(
        emoj_user, emoj_cpu))
elif esc_user == esc_cpu:
    print(
        '\n\033[1;33mEmpatou !\nAmbos escolheram  {}  !\033[m\n'.format(emoj_user))
else:
    print('\n\033[1;31mVocê perdeu !\nVocê  {}  x {}  CPU !\033[m\n'.format(
        emoj_user, emoj_cpu))
print('\n\033[4;32;43mFim do Programa !\033[m\n')
