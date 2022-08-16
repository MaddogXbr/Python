import datetime
'''nome = str(input('Digite um nome: '))
if nome == 'Marcelo':
    print('\nQue nome bonito!\n')
elif nome in 'Juliane Isabella Clara':
    print('\nQue nome lindo!\n')
else:
    print('\nSeu nome é normal!\n')'''

'''
print('-*'*30)
print('Desafio 036!\n')
casa = float(input('Digite o valor do imóvel: '))
salario = float(input('\nDigite o seu salário: '))
anos = int(input('\nEm quantos anos você pretende pagar: '))
parcelas = int(anos*12)
prestacao = float(casa/parcelas)
# print('\n{} parcelas de R$ {:.2f}'.format(parcelas, prestacao))
print(salario*0.3)
if anos <= 50 and prestacao <= (salario*0.3):
    print('\n\033[1;32mO financiamento foi aprovado em {} parcelas de R$ {:.2f}\033[m\n'.format(
        parcelas, prestacao))
else:
    print(
        '\n\033[4;35mInfelizmente o seu financiamento não foi aprovado!\033[m\n')
print('\n--Fim do Programa! ---\n')

print('-*'*30)
print('\033[0;36mDesafio 037!\033[m\n')
num = int(input('Digite o número a ser convertido: '))
opcao = int(
    input('\n1 - Binário;\n2 - Octa;\n3 - Hexadecimal;\nEscolha uma opção: '))
if opcao == 1:
    print('\nO número {} em binário é: {}'.format(num, bin(num)[2:]))
elif opcao == 2:
    print('\nO número {} em Octa é : {}'.format(num, format(num, 'o')))
elif opcao == 3:
    print('\nO número {} em Hexadecimal é : {}'.format(num, format(num, 'x')))
else:
    print('\n\033[0;35mOpção inválida!\033[m\n')
print('\nFim do Programa!\n')

print('-*'*30)
print('\033[0;34mDesafio 038!\033[m\n')
N1 = float(input('Digite o primeiro número: '))
N2 = float(input('\nDigite o segundo número: '))
if N1 > N2:
    print(
        '\nO primeiro número {:.1f} é maior que o segundo número {:.1f}!\n'.format(N1, N2))
elif N2 > N1:
    print(
        '\nO segundo número {:.1f} é maior que o primeiro número {:.1f}!\n'.format(N2, N1))
else:
    print(
        '\n\033[1;33mOs números {:.1f} e {:.1f} são iguais!\033[m\n'.format(N1, N2))
print('\n\033[1;32;41mFim do Programa!\033[m\n')

print('-*'*30)
print('\033[1,33mDesafio 039!\033[m\n')
ano = int(input('Digite o ano do seu nascimento: '))
date = datetime.date.today()
atual = int(date.strftime('%Y'))
idade = atual - ano
if idade == 18:
    print('\n\033[0;32mVocê já está na época de se alistar!\033[m\n')
elif idade < 18:
    print('\nFaltam {} anos para você se alistar!'.format(18 - idade))
else:
    print('\n\033[1;35mVocê deveria ter se alistado a {} anos atras!\033[m\n'.format(
        idade - 18))
print('\n\033[7;33;42mFim do Programa!\033[m\n')


print('-*'*30)
print('\033[4;34;41mDesafio 040!\033[m\n')
nota1 = float(input('Digite a primeira nota do aluno: '))
nota2 = float(input('\nDigite a segunda nota do aluno: '))
media = (nota1 + nota2) / 2
if media < 5.0:
    print(
        '\n\033[4;35mO aluno está reprovado com a média: {:.1f}\033[m\n'.format(media))
elif media >= 5.0 and media <= 6.9:
    print(
        '\n\033[0;33mO aluno está de recuperação com a média: {:.1f}\033[m\n'.format(media))
else:
    print(
        '\n\033[1;32mO aluno está aprovado com a média: {:.1f}\033[m\n'.format(media))
print('\033[4;44mFim do Programa!\033[m\n') '''

from datetime import date
print('-*'*30)
print('\n\033[0;38;42mDesafio 041!\033[m\n')
birth = int(input('Digite o ano do nascimento do nadador: '))
data = date.today().year
#year = int(data.strftime('%Y'))
age = data - birth
if age <= 9:
    print('\nMIRIM !')
elif age > 9 and age <= 14:
    print('\nINFANTIL !')
elif age > 14 and age <= 19:
    print('\nJUNIOR !')
elif age > 19 and age <= 20:
    print('SÊNIOR !')
else:
    print('\nMASTER !')
print('\n\033[1;33;46mFim do Programa !\033[m\n')
