'''
print('==='*35)
print('\033[35;43mDesafio 066 - Sem flag\033[m\n')
cont = soma = 0
while True:
    n = int(input('Digite um número inteiro (999 para Sair): '))
    if n == 999:
        break
    cont += 1
    soma += n
print(f'\nForam digitados {cont} números e a soma é: {soma} \n')
print('Fim do Programa !\n')


print('==='*40)
print('\033[32;46mDesafio 067 - Tabuada V.3.0\033[m\n')
while True:
    n = int(input('Quer ver a tabuada de qual número (negativo para sair): '))
    print('---'*20)
    if n < 0:
        break
    else:
        count = 1
        while count != 11:
            print(f'{n} x {count:2} = {n*count}')
            count += 1
    print('---'*20)
print('\nFim do Programa !\n')

from random import randint

print('***'*30)
print('\033[45mDesafio 068 - Par ou Ímpar\033[m\n')
print('=-=-'*20)
print('Vamos jogar Par ou Ímpar ?')
print('=-=-'*20)
jogos = 0
while True:
    cpu = randint(0, 10)
    n = int(input('\nDigite um número: '))
    escolha = str(input('Escolha Par ou Ímpar (P/I):')).upper().strip()[0]
    if escolha in 'PI':
        if (n+cpu) % 2 == 0:
            if escolha == 'P':
                print('\n\033[32mVocê Venceu !\033[m')
                print('Vamos mais um jogo !')
                jogos += 1
            else:
                print('\n\033[35mVocê Perdeu !\033[m')
                break
        else:
            if escolha == 'I':
                print('\n\033[32mVocê Venceu !\033[m')
                print('Vamos mais um jogo?')
                jogos += 1
            else:
                print('\n\033[35mVocê Perdeu !\033[m')
                break
    else:
        print('Opção inválida !\n')
print(f'\nGAME OVER ! Você venceu {jogos} partidas seguidas !\n')


print('-*-*'*30)
print('\033[36;41mDesafio 069 - Dados de Grupo !\033[m\n')
m20 = homens = p18 = 0
while True:
    print('---'*20)
    print('Cadastro de pessoal !')
    print('---'*20)
    idade = int(input('Digite a idade da pessoa: '))
    sexo = str(input('Digite o sexo da pessoa (M/F): ')).upper().strip()[0]
    while sexo not in "MF":
        sexo = str(input('Opção incorreta ! (M/F): ')).upper().strip()[0]
        print(sexo)
    if sexo == "M":
        homens += 1
    elif sexo == "F":
        if idade < 20:
            m20 += 1
    if sexo in 'MF' and idade > 18:
        p18 += 1
       # print(p18)
    opt = str(input('\nContinar cadastrando (S/N)?')).upper().strip()[0]
    while opt != 'S' and opt != 'N':
        opt = str(input('\nOpção inválida ! Continuar (S/N): ')
                  ).upper().strip()[0]
    if opt == 'N':
        break
print(f'\nA) Foram cadastradas {p18} pessoas acima de 18 anos !')
print(f'B) Foram cadastrados {homens} homen(s)!')
print(f'C) Foram cadastradas {m20} mulher(es) abaixo de 20 anos !\n')
print('\033[1;34mFim do Programa !\033[m\n')
'''
