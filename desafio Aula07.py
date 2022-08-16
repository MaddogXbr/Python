n1 = int(input('Digite um número: '))
print('\nO número {} tem o Sucessor = {}, e o Antecessor = {}\n'.format(n1, n1+1, n1-1))
print('O dobro do número {} é = {}, \nTriplo é = {}, \nRaiz quadrada é = {:.2f}\n'.format(
    n1, n1*2, n1*3, n1**(1/2)))
Nota1 = float(input('Digite a primeira nota: '))
Nota2 = float(input('\nEntre com a segund nota: '))
print('\nA média do aluno foi {:.2f}\n'.format((Nota1+Nota2)/2))
m = float(input('Digite a metragem: '))
print('\n{:.2f} metros é igual a {:.2f} cm ou {:.2f} mm\n'.format(
    m, (m*100), (m*1000)))
