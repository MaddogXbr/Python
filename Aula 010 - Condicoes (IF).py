tempo = int(input('\nQual é a idade do seu carro? '))
if tempo <= 3:
    print('\nCarro novo !\n')
else:
    print('\nCarro Velho !\n')
print('--FIM--\n')

nome = str(input('\nDigite o seu primeiro nome: '))
print('\nQue nome lindo !\n' if nome ==
      'Juliane' else '\nBom dia {} !\n'.format(nome))

notas = input('\nDigite as notas: ')
notas = notas.split()
N1 = float(notas[0])
N2 = float(notas[1])
media = ((N1+N2)/2)
if media >= 5:
    print('\nVocê passou com a nota {:.1f} !\n'.format(media))
else:
    print('\nVocê está de recuperação com a nota {:.1f} !\n'.format(media))
print('\n--FIM--\n')
