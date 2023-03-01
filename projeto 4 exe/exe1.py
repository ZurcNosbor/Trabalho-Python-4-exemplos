#MENU INICIAL
cadastro = input('Deseja verificar a matrícula do aluno? 0 - NÃO  1 - SIM: ')

#LAÇO DE REPETIÇÃO QUE VERIFICA A MATRÍCULA
while True:

    #CONDICIONAL DA OPÇÃO ESCOLHIDA
    #OPÇÃO 1: VERIFICA UM ALUNO
    if cadastro == '1':

        #PEDINDO O NOME E IDADE DO ALUNO(A)
        nomeCrianca = input('Nome do aluno(a): ')
        idadeCrianca = int(input('Idade do aluno(a: '))

        #CONDICIONAL PARA SABER O ENSINO DO ALUNO
        if (idadeCrianca == 0):
            ensino = 'não tem idade para ser aluno(a)'
        elif (idadeCrianca >= 1) and (idadeCrianca <= 5):
            ensino = 'está na Educação Infantil'
        elif (idadeCrianca >= 6) and (idadeCrianca <= 10):
            ensino = 'está no Ensino Fundamental I'
        elif (idadeCrianca >= 11) and (idadeCrianca <= 14):
            ensino = 'está no Ensino Fundamental II'
        elif (idadeCrianca >= 15) :
            ensino = 'está no Ensino Médio'

        #SAÍDA PARA O USUÁRIO
        print('Nome do aluno(a): {}'.format(nomeCrianca))
        print('Idade do aluno(a): {}'.format(idadeCrianca))
        print('O(A) aluno(a) {} tem {} anos e {}'.format(nomeCrianca,idadeCrianca,ensino))
        cadastro = input('Deseja continuar: 0 - NÃO    1 - SIM ')

    # OPÇÃO 0: ENCERRA O PROGRAMA
    elif cadastro == '0':
        break

    #OPÇÃO MAIOR QUE 1 OU QUALQUER TECLA QUE NÃO SEJA UM NÚMERO INTEIRO: OPÇÃO INVÁLIDA
    elif cadastro != int or cadastro > 1:
        print('Opção inválida!! ')
        cadastro = input('Deseja verificar a matrícula do aluno? 0 - NÃO  1 - SIM: ')



print('Fim do programa! Volte sempre!!')

