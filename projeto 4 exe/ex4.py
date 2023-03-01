#IMPORTAÇÃO DO NÚMERO ALEATÓRIO PARA O VOUCHER
import random as r

#CRIANDO DICIONÁRIO
inscricaoDicionario = {}

#CRIANDO LISTA
inscricaoLista = []

#PROGRAMA PRINCIPAL
print('_'* 5, 'MENU', '_' * 5)
print('Digite uma opção:')
print('1 - Nova inscrição')
print('2 - Visualizar inscrição')
print('0 - Encerrar')


#LAÇO DE REPETIÇÃO PARA A ESCOLHA DA OPÇÃO
while True:

    #ESCOLHENDO UMA OPÇÃO
    op = input('Escolha uma das opções: ')
    op2 = op
    print('Opção escolhida: {}'.format(op2))

    #OPÇÃO 1: FAZER UMA NOVA INSCRIÇÃO
    if op2 == '1':

            #PEDE OS ITENS AO USUÁRIO PARA UMA NOVA INSCRIÇÃO
            inscricaoDicionario['Voucher'] = r.randint(0,999999)
            inscricaoDicionario['Nome'] = input('Digite seu nome: ')
            inscricaoDicionario['Email'] = input('Digite seu email: ')
            inscricaoDicionario['Telefone'] = input('Digite seu telefone: ')
            inscricaoDicionario['Curso'] = input('Digite seu curso: ')
            #ADICIONA OS ITENS NA LISTA
            inscricaoLista.append(inscricaoDicionario.copy())

    #OPÇÃO 2: MOSTRAR A LISTA DE INSCRITOS
    elif op2 == '2':

        #CONDICIONAL PARA SABER SE A LISTA DE INSCRIÇÃO ESTA VAZIA
        if inscricaoLista == []:
            print('_' * 5, 'LISTA DE INSCRITOS', '_' * 5)
            print('Nehuma inscrição cadastrada!!!')

        #SE NÃO ESTIVER VAZIA, MOSTRA OS ITENS
        else:
            print('_'* 5, 'LISTA DE INSCRITOS', '_' * 5)
            for e in inscricaoLista:
                for i,j in e.items():
                    print(f'{i} : {j}')

    #OPÇÃO 0: ENCERRA O PROGRAMA
    elif op2 == '0':
        print('Encerrando Programa...')
        break

    #OPÇÃO MAIOR QUE 2 OU QUALQUER TECLA QUE NÃO SEJA UM NÚMERO INTEIRO: OPÇÃO INVÁLIDA
    elif op2 != int or op2 > 2:
        print('Erro: Digite uma opção válida!!')

    print('_' * 5, 'MENU', '_' * 5)
    print('Digite uma opção:')
    print('1 - Nova inscrição')
    print('2 - Visualizar inscrição')
    print('0 - Encerrar')

