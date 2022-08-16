print('--'*30)
print('\nDesafio 033 !\n')
N1 = int(input('Digite o primeiro número: '))
N2 = int(input('Digite o segundo número: '))
N3 = int(input('Digite o terceiro número: '))
if N1 > N2:
    if N1 > N3:
        print('\nO maior número é {}! N1'.format(N1))
        if N2 > N3:
            print('\nO menor número é o {}! N3'.format(N3))
        else:
            print('\nO menor número é o {}! N2'.format(N2))
    else:
        print('\nO maior número é o {}! 3'.format(N3))
        print('\nO menor número é o {}! 2'.format(N2))
else:
    if N2 > N3:
        print('\nO maior número é o {}! 2!'.format(N2))
        if N1 > N3:
            print('\nO menor número é o {}! 3!'.format(N3))
        else:
            print('\nO menor número é o {}! 1!'.format(N1))
    else:
        print('\nO maior número é o {}! #3'.format(N3))
        print('\nO menor número é o {}! #1'.format(N1))
print('\n--FIM--\n')

# Resolução do Professor

menor = N1
if N2 < N1 and N2 < N3:
    menor = N2
if N3 < N1 and N3 < N2:
    menor = N3

maior = N1
if N2 > N1 and N2 > N3:
    maior = N2
if N3 > N1 and N3 > N2:
    maior = N3
print('\nO menor número é o {}.'.format(menor))
print('\nO maior número é o {}.'.format(maior))
