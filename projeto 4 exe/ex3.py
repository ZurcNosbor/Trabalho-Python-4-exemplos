#CRIANDO LISTAS DAS FASES
posicaoFase1 = [['*','*','-','G'],['R','-','*','*']]
posicaoFase2 = [['-','*','*','*'],['*','C','-','-']]
posicaoFase3 = [['-','*','*','*'],['-','G','-','*']]
posicaoFase4 = [['-','-','-','*'],['*','R','*','*']]

#LAÇO DE REPETIÇÃO PARA FASE 1
while True:

    # PROGRAMA PRINCIPAL
    print('HOTEL DOS ANIMAIS')
    print('Especificando posições:')
    print('[1,2,3,4]')
    print('[5,6,7,8]')
    print()
    print('Bem vindo a fase 1:')
    print('Nessa fase o jogador deve alocar o RATO e o GATO na seguinte matriz que representa os quartos:')
    for p in posicaoFase1:
        print(p)
    print('- = Quartos disponíveis')
    print('* = Quartos indisponíveis')
    print('R,G,C = Quartos já ocupados')
    print()

    # PEDINDO JOGADAS FASE 1
    jogada1 = input('Em qual posição quer alocar o RATO (R)? ')
    jogada2 = input('Em qual posição quer alocar o GATO (G)? ')
    print()

    #CONDICIONAL FASE 1
    if jogada1 == '6' and jogada2 == '3':

        #TROCANDO OS ESPAÇOS VAZIOS PELAS STRINGS
        posicaoFase1[1][1] = 'R'
        posicaoFase1[0][2] = 'G'

        # MOSTRA A LISTA AO USUÁRIO DEPOIS DE ELE ESCOLHER OS QUARTOS
        print('Hotel depois das suas escolhas:')
        print()
        for i in posicaoFase1:
            print(i)
        print()
        break
    else:
        print('Você perdeu infelizmente!')
        break

#CONDICIONAL PARA VALIDAR FASE 2
if jogada1 == '6' and jogada2 == '3':

    # LAÇO DE REPETIÇÃO PARA FASE 2
    while True:
        print('Você passou!! Se prepare para a fase 2!!')
        print()

        # FASE 2
        print('Bem vindo a fase 2:')
        print('Nessa fase o jogador deve alocar o CÃO, CÃO e OSSO:')
        for i in posicaoFase2:
            print(i)
        print('- = Quartos disponíveis')
        print('* = Quartos indisponíveis')
        print('R,G,C = Quartos já ocupados')
        print()

        # PEDINDO JOGADAS FASE 2
        jogada1 = input('Em qual posição quer alocar o CÃO (C)? ')
        jogada2 = input('Em qual posição quer alocar o CÃO (C)? ')
        jogada3 = input('Em qual posição quer alocar o OSSO (O)? ')
        print()

        #CONDICIONAL FASE 2
        if jogada1 == '7' and jogada2 == '8' and jogada3 == '1' or jogada1 == '8' and jogada2 == '7' and jogada3 == '1':

            # TROCANDO OS ESPAÇOS VAZIOS PELAS STRINGS
            posicaoFase2[1][2] = 'C'
            posicaoFase2[1][3] = 'C'
            posicaoFase2[0][0] = 'O'

            # MOSTRA A LISTA AO USUÁRIO DEPOIS DE ELE ESCOLHER OS QUARTOS
            print('Hotel depois das suas escolhas:')
            print()
            for i in posicaoFase2:
                print(i)
            print()
            break

        else:
            print('Você perdeu infelizmente!')
            break

#CONDICIONAL PARA VALIDAR FASE 3
if jogada1 == '7' and jogada2 == '8' and jogada3 == '1' or jogada1 == '8' and jogada2 == '7' and jogada3 == '1':

    #LAÇO DE REPETIÇÃO PARA FASE 3
    while True:
        print('Você passou!! Se prepare para a fase 3!!')
        print()

        # FASE 3
        print('Bem vindo a fase 3:')
        print('Nessa fase o jogador deve alocar o GATO (G), RATO (R) e OSSO (O):')
        for i in posicaoFase3:
            print(i)
        print('- = Quartos disponíveis')
        print('* = Quartos indisponíveis')
        print('R,G,C = Quartos já ocupados')
        print()

        # PEDINDO JOGADAS FASE 3
        jogada1 = input('Em qual posição quer alocar o GATO (G)? ')
        jogada2 = input('Em qual posição quer alocar o RATO (R)? ')
        jogada3 = input('Em qual posição quer alocar o OSSO (O)? ')
        print()

        # CONDICIONAL FASE 3
        if jogada1 == '7' and jogada2 == '1' and jogada3 == '5':

            # TROCANDO OS ESPAÇOS VAZIOS PELAS STRINGS
            posicaoFase3[1][2] = 'G'
            posicaoFase3[0][0] = 'R'
            posicaoFase3[1][0] = 'O'

            # MOSTRA A LISTA AO USUÁRIO DEPOIS DE ELE ESCOLHER OS QUARTOS
            print('Hotel depois das suas escolhas:')
            print()
            for i in posicaoFase3:
                print(i)
            print()
            break

        else:
            print('Você perdeu infelizmente!')
            break

#CONDICIONAL PARA VALIDAR FASE 4
if jogada1 == '7' and jogada2 == '1' and jogada3 == '5':

    # LAÇO DE REPETIÇÃO PARA FASE 4
    while True:
        print('Você passou para a última fase!! Se prepare!!')
        print()

        # FASE 4
        print('Bem vindo a fase 4:')
        print('Nessa fase o jogador deve alocar o QUEIJO (Q), QUEIJO (Q) e OSSO (O):')
        for i in posicaoFase4:
            print(i)
        print('- = Quartos disponíveis')
        print('* = Quartos indisponíveis')
        print('R,G,C = Quartos já ocupados')
        print()

        # PEDINDO JOGADAS FASE 4
        jogada1 = input('Em qual posição quer alocar o QUEIJO (Q)? ')
        jogada2 = input('Em qual posição quer alocar o QUEIJO (Q)? ')
        jogada3 = input('Em qual posição quer alocar o OSSO (O)? ')
        print()

    # CONDICIONAL FASE 4
        if jogada1 == '1' and jogada2 == '3' and jogada3 == '2' or jogada1 == '3' and jogada2 == '1' and jogada3 == '2' :

            # TROCANDO OS ESPAÇOS VAZIOS PELAS STRINGS
            posicaoFase4[0][2] = 'Q'
            posicaoFase4[0][0] = 'Q'
            posicaoFase4[0][1] = 'O'

            #MOSTRA A LISTA AO USUÁRIO DEPOIS DE ELE ESCOLHER OS QUARTOS
            print('Hotel depois das suas escolhas:')
            print()
            for i in posicaoFase4:
                print(i)
            print()
            print('PARABÉNS!!!! VOCÊ VENCEU TODAS AS FASES DA COMPETIÇÃO!!')
            print()
            break

        else:
            print('Você perdeu infelizmente!')
            break

#MOSTRA AO USUÁRIO O FIM DO PROGRAMA
print('Encerrando programa...')







