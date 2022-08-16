from datetime import date  # Para importar o date de hoje
ano = date.today().year  # Dia, mês ou ano de hoje na máquina

if x != y:  # Diferente e nao esquecer dos :
    # Tabulação
elif x == y:  # Para dar continuidade nos if
    x += 1  # Adiciona um valor ao montante
else:

    # incia no valor exato e finaliza um antes do final, e a razão é como que vai rodar (2 em 2, 3 em 3 ou x em x)
for c in range(inicial, final(-1), razão(2, 3, x)):
    # Tabulação

c = 1
while c != 10:  # Inicial e final do Enquanto
    break  # Interrompe o While

while True:  # While infinito
    break:

        # simplifica, só colocar o f a frente e a constante dentro das aspas
        # Alinhamento de string (< Esq, > Dir, ^ Cen, - Complemento, 10 Tamanho)
FString - -> print(f'TESTE {nome:-^10} {soma:.2f}')

# Alinhamento de texto centralizado com cor
print(f'\033[0;33;45m{"Desafio 071 - Caixa Eletrônico !":^50}\033[m\n')
print(f'{"BANCO Perdeu Playboy !":>50}')  # Alinhamento do texto Direita

// // LISTA // //

Lista.append('X')  # Adiciona um item a lista

# Adiciona um item no inicio da Lista, movendo os outros para frente
Lista.insert(0, "X")  # insere o valor 'X' na posição 0

del Lista[3]  # Remove o item da Lista

# O metodo pop é para eliminar o último elemento, mas pode elimir o indice
Lista.pop(3)
Lista.remove('X')  # Remove pelo conteúdo da lista
# Na remoção, o item, a posição some e o índice é refeito
if "x" in Lista:
    # Para não receber o erro do sistema se não existir o item
    Lista.remove('X')

Lista = list(range(4, 11))  # vai do 4 ao 10.
Lista.sort()  # Ordena os itens
Lista.sort(reverse=True)  # Ordena em ordem decrescente

enumerate(Lista)  # enumara as chaves C
for c, v in enumerate(Lista):
    print(f'Na posição {c} encontrei o valor{v}')


ListaA = ListaB  # Cria uma ligação entre as listas
ListaA = ListaB[:]
