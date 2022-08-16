print('--'*30)
print('\nDesafio 035! \n')
salario = float(input('Digite o seu salário: '))
if salario <= 1250.00:
    print('\nO seu aumento foi de R$ {:.2f} (15%)\n e o seu salário foi para R$ {:.2f}\n'.format(
        (salario*0.15), (salario*1.15)))
else:
    print('\nO seu aumento foi de R$ {:.2f} (10%)\n e o seu salário foi para R$ {:.2f}\n'.format(
        (salario*0.1), (salario*1.1)))
print('\n--FIM--\n')


print('--'*30)
print('\nDesafio 035!\n')
print('-=-'*20)
print('Analisador de triângulos !')
print('-=-'*20)
reta1 = float(input('\nDigite o valor da primeira reta: '))
reta2 = float(input('\nDigite o valor da segunda reta: '))
reta3 = float(input('\nDigite o valor da terceira reta: '))
'''
if reta1 > reta2:
    if reta1 > reta3:
        soma = reta2 + reta3
        maior = reta1
    else:
        soma = reta1 + reta2
        maior = reta3
else:
    if reta2 > reta3:
        soma = reta1 + reta3
        maior = reta2
    else:
        soma = reta1 + reta2
        maior = reta3
if soma > maior:
    '''
if reta1 < reta2+reta3 and reta2 < reta1 + reta3 and reta3 < reta1 + reta2:
    print('\nAs retas {}, {} e {} podem formar um triângulo!\n'.format(
        reta1, reta2, reta3))
else:
    print('\nAs retas {}, {} e {} não podem formar um triângulo!\n'.format(
        reta1, reta2, reta3))
print('--Fim--\n')
