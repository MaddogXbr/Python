print('-'*40)
print("\nDesafio 009 !\n")
N1 = int(input('Digite um número inteiro: '))
print('\nTabuada de {0}\n \n{0} x 1 = {0:2} | {0} x 2 = {1} | {0} x 3 = {2} \n{0} x 4 = {3} | {0} x 5 = {4} | {0} x 6 = {5} \n{0} x 7 = {6} | {0} x 8 = {7} | {0} x 9 = {8}\n'.format(
    N1, (N1*2), (N1*3), (N1*4), (N1*5), (N1*6), (N1*7), (N1*8), (N1*9)))
print('-'*40)
print("\nDesafio 010 !\n")
Carteira = float(input('\nDinheiro na carteira: '))
print('\nCom R$ {:.2f} dá para comprar US$ {:.2f} !\nCom a cotação de US$ 1 = R$ 3,27 \n'.format(
    (Carteira), (Carteira/3.27)))
print('-'*40)
print("\nDesafio 011 !")
altura = float(input('\nEntre com a Altura: '))
largura = float(input('Entre com a Largura: '))
print('\nA área à ser pintada é de {:.2f} m2 e será necessário {} litros de tinta!\n'.format(
    (altura*largura), ((altura*largura)//2)))
print('-'*40)
print('\nDesafio 012 !\n')
valor = float(input('Digite o valor do produto: '))
print('O valor do produto com 5% de desconto é: R$ {:.2f} !\n'.format(
    valor*(95/100)))
print('-'*40)
print('\nDesafio 013 !\n')
salario = float(input('Digite o salário: '))
print('\nO salário anterior R$ {:.2f}, e com o aumento de 15% vai para R$ {:.2f} !\n'.format(
    salario, (salario*1.15)))
