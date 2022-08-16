'''
print('==='*30)
print('\033[42mDesafio 082 - Dividindo os valores da lista !\033[m\n')
ltotal = []
lpar = []
limpar = []
while True:
    N1 = int(input('Digite um número: '))
    ltotal.append(N1)
    while True:
        sel = str(input('Deseja continuar (S/N): ')).upper().strip()
        if sel in "SN":
            break
    if sel in "N":
        break
for c in range(0, len(ltotal)):
    if ltotal[c] % 2 == 0:
        lpar.append(ltotal[c])
    else:
        limpar.append(ltotal[c])
print('\n', '==='*30)
print(f'\nA lista principal é : {ltotal}')
print(f'A lista par ficou: {lpar}')
print(f'A lista impar ficou: {limpar}')
print('\nFim do Programa !\n')
'''


print('---'*35)
print('\033[42mDesafio 083 - Validando Expressões Matemáticas\033[m\n')
expressao = []
a = 0
entrada = str(input('Digite uma expressão Matemática: '))
expressao = list(entrada)
for x in range(0, len(expressao)):
  #  print('Passo', x)
    if expressao[x] in "(":
        a += 1
    elif expressao[x] in ")" and a == 0:
        a -= 1
        break
    elif expressao[x] in ")" and a != 0:
        a -= 1
if a == 0:
    print(f'\nA sua expressão: \033[42m {entrada} \033[m é válida !')
else:
    print(f'\nA sua expressão: \033[41m {entrada} \033[m é inválida !')
print('\n Fim do Programa\n')
