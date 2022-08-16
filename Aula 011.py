cores = {'limpa': '\033[m', 'azul': '\033[34m',
         'amarelo': '\033[33m', 'pretoebranco': '\033[7;30m'}
print('\033[0;30;41mOlá \033[4;30;42mMundo!\033[m\n')
print('\033[1;35mTESTE!\033[m\n')
nome = input('\033[1;37;46mDigite o seu nome:\033[m ')
print('Seja bem vindo \033[7;31;45m {}! \033[m'.format(nome))

print('\n{}Teste {}de {}Cores{}!'.format(
    cores['azul'], cores['amarelo'], cores['pretoebranco'], cores['limpa']))
