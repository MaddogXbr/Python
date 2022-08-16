from ast import If


entrada = input('digite o que vier a cabeça: ')
print(type(entrada))
print('Num : ', entrada.isnumeric())
print('Alpha: ', entrada.isalpha())
print('ASCII: ', entrada.isascii())
print('Upper: ', entrada.isupper())
print('Lower: ', entrada.islower())
print('Tem espaço: ', entrada.isspace())
print('Alphanum: ', entrada.isalnum())
