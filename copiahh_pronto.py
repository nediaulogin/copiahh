import re


def le_assinatura():
    '''A funcao le os valores dos tracos linguisticos do modelo e devolve uma assinatura a ser comparada com os textos fornecidos'''
    
    print("Bem-vindo ao detector automtico de COH-PIAH.")
    print("Informe a assinatura típica do aluno:")

    wal = float(input("Entre o tamanho mdio de palavra:"))
    ttr = float(input("Entre a relao Type-Token:"))
    hlr = float(input("Entre a Razão Hapax Legomana:"))
    sal = float(input("Entre o tamanho médio de sentença:"))
    sac = float(input("Entre a complexidade média da sentença:"))
    pal = float(input("Entre o tamanho médio de frase:"))

    return [wal, ttr, hlr, sal, sac, pal]


def le_textos():
    '''A funcao le todos os textos a serem comparados e devolve uma lista contendo cada texto como um elemento'''
    i = 1
    textos = []

    texto = input("Digite o texto " + str(i) + " (aperte enter para sair):")
    while texto:
        textos.append(texto)
        i += 1
        texto = input("Digite o texto " + str(i) + " (aperte enter para sair):")

    return textos


def separar_tudo(texto):
    '''essa fun��o recebi um texto e devolve um lista de palavras '''
    lista = re.split(r'[ ,.;:!?]+', texto)

    lista.remove(lista[-1])
    return lista

    pass


def separa_sentencas(texto):
    '''A funcao recebe um texto e devolve uma lista das sentencas dentro do texto'''
    sentencas = re.split(r'[.!?]+', texto)
    if sentencas[-1] == '':
        del sentencas[-1]
    return sentencas


def separa_frases(sentenca):
    '''A funcao recebe uma sentenca e devolve uma lista das frases dentro da sentenca'''
    return re.split(r'[,:;]+', sentenca)


def separa_palavras(frase):
    '''A funcao recebe uma frase e devolve uma lista das palavras dentro da frase'''
    return frase.split()


def n_palavras_unicas(lista_palavras):
    '''Essa funcao recebe uma lista de palavras e devolve o numero de palavras que aparecem uma unica vez'''
    freq = dict()
    unicas = 0
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            if freq[p] == 1:
                unicas -= 1
            freq[p] += 1
        else:
            freq[p] = 1
            unicas += 1

    return unicas


def n_palavras_diferentes(lista_palavras):
    '''Essa funcao recebe uma lista de palavras e devolve o numero de palavras diferentes utilizadas'''
    freq = dict()
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            freq[p] += 1
        else:
            freq[p] = 1

    return len(freq)


def compara_assinatura(as_a, as_b):
    '''IMPLEMENTAR. Essa funcao recebe duas assinaturas de texto e deve devolver o grau de similaridade nas assinaturas.'''
    similiaridade = 0

    for i in range(6):

        diferenca = 0
        diferenca = abs(as_a[i] - as_b[i])
        similiaridade += diferenca / 6

    return similiaridade


def calcula_assinatura(texto):
    '''Essa funcao recebe um texto e deve devolver a assinatura do texto.'''

    '''primeiro calculo tamanho medio das palavras WAL!'''
    palavras = separar_tudo(texto)
    letras = 0
    for pal in palavras:
        letras += len(pal)
    tam_med_palavras = letras/len(palavras)

    '''segundo calculo o numero de (palavras diferentes/total de palavras) TTR'''
    type_t = n_palavras_diferentes(palavras)/len(palavras)

    '''terceiro calculo (palavras utilizadas uma unica vez/ total de palavras.) HLR'''
    pal_unicas = n_palavras_unicas(palavras)/len(palavras)

    '''quarto calculo caracters das sentenças/ numero de sentenças SAL'''
    sentencas = separa_sentencas(texto)
    tam_sentenca = 0
    tam_frase = 0

    for i in sentencas:
        tam_sentenca += len(i)
        '''para calcular o 6 tamanho das frases'''
        frases = separa_frases(i)
        for cont in frases:
            tam_frase += len(cont)

    med_sentenca = tam_sentenca/len(sentencas)

    '''quinto calculo Media simples do numero de frases por sentença SAC'''
    n_frases = 0

    for i in sentencas:

        n_frases += len(separa_frases(i))

    med_frase_senteca = n_frases/len(sentencas)

    '''sexto calculo tamanho medio da frase'''
    tam_med_frase = tam_frase/n_frases

    assinatura = [tam_med_palavras, type_t, pal_unicas, med_sentenca, med_frase_senteca, tam_med_frase]
    return assinatura


def avalia_textos(textos, ass_cp):
    '''Essa funcao recebe uma lista de textos e uma assinatura ass_cp e deve devolver o numero (1 a n) do texto com maior probabilidade de ter sido infectado por COH-PIAH.'''
    assinaturas = []
    for texto in textos:
        assinaturas.append(calcula_assinatura(texto))
    n = 0
    similiaridades = []
    ordem = []
    for i in assinaturas:
        similiaridades.append(compara_assinatura(ass_cp, i))
        ordem.append(compara_assinatura(ass_cp, i))
    ordem.sort()

    n = int(similiaridades.index(ordem[0]))

    return n+1


assinatura = le_assinatura()
textos = le_textos()
print('O autor do texto', avalia_textos(textos, assinatura), 'está infectado com COH-PIAH')
