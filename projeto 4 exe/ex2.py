#FUNÇÃO PARA CONVERTER LETRA PARA SÍMBOLO
def converteLetra(letra):
    letra = letra.upper()
    if (letra == 'A'):
        return '@'
    elif (letra == 'E'):
        return '&'
    elif (letra == 'I'):
        return '!'
    elif (letra == 'O'):
        return '#'
    elif (letra == 'U'):
        return '*'

#PROGRAMA PRINCPAL // PEDINDO UM NOME
nome = input('Digite um nome: ')
nomeInserido = ''

#LAÇO DE REPETIÇÃO ''FOR'' PARA FAZER A VERIFICAÇÃO SOBRE AS PALAVRAS
for verificaPalavra in nome:

    #VERIFICA SE UMA LETRA É UMA VOGAL
    if (verificaPalavra.upper() == 'A' or verificaPalavra.upper() == 'E' or
        verificaPalavra.upper() == 'I' or verificaPalavra.upper() == 'O' or
        verificaPalavra.upper() == 'U'):

        #CHAMAR A FUNÇÃO PARA CONVERTER A PALAVRA
        nomeInserido += converteLetra(verificaPalavra.upper())

    else:
        nomeInserido += verificaPalavra.upper()

#MOSTRAR O NOME INSERIDO NA TELA
print(nomeInserido)