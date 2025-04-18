# -*- coding: utf-8 -*-
"""Cópia de eduardo-ga-knapsack

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1RWmjIADh0WP836wzkZK_UDSOYOzVcTGV
"""

#
#Vincenzo - Inteligência Computacional - 2023
#Algoritmo Genético em Python para resolver o problema da mochila
#Para teste coloquei 5 itens: 4, 2, 3, 6 e 5 Kg.
#E seus preços 4, 9, 12, 3 e 10 reais. O peso máximo foi setado como 13Kg.
#Apenas descomente se quiser
#Rode o código , ele pedirá pra escrever o peso e o valor
import numpy as np
"""
w = [4,2,3,6,5] # Pesos
v = [4,9,12,3,10] # Valores

weight = 13 # Capacidade Máxima
col = 5 # Total de itens, tem que ser igual ao numero de produtos acima em "w" e "v"

"""
num_itens = int(input("Quantos itens você deseja adicionar? "))
w = [] # Inicializar uma lista vazia para os pesos dos itens
v = [] # Inicializar uma lista vazia para os valores dos itens

for i in range(num_itens):
    peso = int(input(f"Informe o peso do item {i+1}: "))
    valor = int(input(f"Informe o valor do item {i+1}: "))
    w.append(peso)
    v.append(valor)

col = num_itens # Total de itens, igual ao número de produtos informados pelo usuário

weight = 13 # Capacidade Máxima

row = 20 # numero de individuos
taxa_mutacao = 0.05

print("Os pesos e valores são: ")
print("Pesos: ", w)
print("Valores: ", v)

rand_pop = np.random.randint(0,2,(row,col))
rand_popTemp = np.random.randint(0,2,(row,col))

addZeros = np.zeros((row,4))
rand_pop = np.append(rand_pop, addZeros, axis=1)

# O loop principal é responsável por executar as iterações do algoritmo genético,
# onde cada iteração representa uma geração.
# Durante cada iteração, as etapas de seleção,
# crossover e mutação são executadas para formar a próxima geração da população.
#
maxVal = 0
capIndividual = []
melhoresValores = []  # Lista para armazenar os melhores valores em cada geração

for itr in range(20): # NUMERO DE GERAÇÕES
    print("\nGeração nº:",itr+1)

    for i in range(row):
        sumWeight = sum(np.multiply(w, rand_pop[i,0:col])) # Cálculo do Peso Total
        rand_pop[i,col] = sumWeight
        sumValue = sum(np.multiply(v, rand_pop[i,0:col])) # Cálculo do Valor total

        if sumWeight>weight or np.isnan(sumWeight) or np.isnan(sumValue): # Verifica se o peso total não excede o peso máximo
            sumValue = 0
            rand_pop[i,col+1] = sumValue
            continue

        rand_pop[i,col+1] = sumValue

        if maxVal<sumValue:
            maxVal = sumValue
            capIndividual = rand_pop[i,0:col]
        melhoresValores.append(maxVal)

    print("A população inicial: \n",rand_pop[:,0:col])

    # é calculado o valor do fitness function
    # para cada indivíduo com o objetivo de avaliar o quão apto ele é em relação aos demais membros da população.
    for i in range(row):
        rand_pop[i,col+2] = rand_pop[i,col+1]/np.average(rand_pop[:,col+1])
        rand_pop[i,col+3] = round(rand_pop[i,col+2])

    print("\n\nEM RELAÇÃO ABAIXO\n ------------------------------------------------\nOs que excederem o peso máximo terão os valores iguais a 0")
    print("\n 1º elemento abaixo é a soma dos pesos,\n 2º é a soma dos valores,\n 3º é (FITNESS FUNCTION) calculada dividindo-se o valor total de cada indivíduo pela média dos valores totais de toda a população.:\n o 4º valor é apenas o FITNESS FUNCTION ARREDONDADO \n-------------------------------------------\n", rand_pop[:,col:col+4].tolist())
    print("\nA soma é :: ",sum(rand_pop[:,col+1]))
    print("A média é: ",np.average(rand_pop[:,col+1]))

    # Selecionados para reprodição com base em seu valor fitness
    count = 0
    c = 0
    for i in range(row):
        noc = rand_pop[i, col+3]
        count += noc
        if count >= row:
            noc -= 1

        for j in range(int(noc)):
            rand_popTemp[c] = rand_pop[i, 0:col]
            c +=1
    rand_pop[:, 0:col] = rand_popTemp

    print("\nA próxima geração: \n",rand_pop[:,0:col])

    # Início do cruzamento (crossover)
    # O cruzamento é um operador genético
    # que envolve a combinação de informações genéticas de dois indivíduos pais
    # para produzir novos indivíduos filhos.

    #Seleção aleatória dos índices para o cruzamento

    # Os índices para o cruzamento são selecionados aleatoriamente.
    # Isso significa que dois indivíduos pais serão escolhidos aleatoriamente
    # da população para participar da operação de cruzamento.
    # O local de cruzamento também é determinado aleatoriamente,
    # indicando onde as informações genéticas serão trocadas entre os pais para criar os filhos.
    dup = np.array([])
    while 1:
        ranIndex = np.random.randint(low=0, high=row, size=2)
        u, c = np.unique(ranIndex, return_counts=True)
        dup = u[c > 1]
        if dup.size == 0:
            break
    print("Dois indivíduos são selecionados aleatoriamente: ")

    c = 0
    for i in ranIndex:
        rand_popTemp[c] = rand_pop[i,0:col]
        c += 1

    #k = np.random.randint(low=1, high=col, size=1)
    k = np.random.randint(low=1, high=col, size=1).item()
     # significa que o local onde ocorrerá
     # o cruzamento entre os indivíduos pais
     # é escolhido aleatoriamente.
     # Esse local é uma posição específica dos cromossomos dos pais
     # onde ocorrerá a troca de informações genéticas para formar os cromossomos dos filhos.

     # Ao escolher aleatoriamente o local de cruzamento,
     # você está introduzindo diversidade nas soluções e permitindo a exploração de diferentes combinações genéticas.
    #print("The crossite is: ",int(k))
    #print("Antes do crossover:: \n",rand_popTemp[0:2])
    print("The crossite is: ", k)
    print("Antes do crossover:: \n", rand_popTemp[0:2])
    a = []
    b =[]
    #a = rand_popTemp[0,int(k):col].tolist()
    #b = rand_popTemp[1,int(k):col].tolist()
    #rand_popTemp[1,int(k):col] = a
    #rand_popTemp[0,int(k):col] = b
    #versão do numpy não recomenda mais essas práticas
    a = rand_popTemp[0, k:col].tolist()
    b = rand_popTemp[1, k:col].tolist()
    rand_popTemp[1, k:col] = a
    rand_popTemp[0, k:col] = b
    #print("Depois do crossover: \n",rand_popTemp[0:2])
    print("Depois do crossover: \n", rand_popTemp[0:2])
    c = 0
    for i in ranIndex:
        rand_pop[i,0:col] = rand_popTemp[c]
        c += 1

    print("\nA próxima geração após o crossover: \n",rand_pop[:,0:col])

    # Idica o início da operação de mutação no algoritmo genético.
    # A mutação é um operador genético que introduz pequenas alterações aleatórias nos indivíduos da população.
    # Essas alterações podem ajudar a diversificar a população
    # e explorar novas regiões do espaço de busca, aumentando a chance de encontrar soluções ótimas ou melhores.
    for i in range(row):
        for j in range(col):
            if np.random.random() <= taxa_mutacao / 100:
                rand_pop[i,j] = 1 - rand_pop[i,j]  # Realiza a mutação invertendo o valor do gene

    #rand_r = int(np.random.randint(0,row,(1,1)))
    #rand_c = int(np.random.randint(0,col,(1,1)))
    #print("Posição do gene a sofrer mutação: [",rand_r,",",rand_c,"]")
    #rand_pop[rand_r,rand_c] = 1-int(rand_pop[rand_r,rand_c])
    #versão do numpy não recomenda mais essas práticas
    rand_r = np.random.randint(0, row, (1,1)).item()
    rand_c = np.random.randint(0, col, (1,1)).item()
    print("Posição do gene a sofrer mutação: [", rand_r, ",", rand_c, "]")
    rand_pop[rand_r, rand_c] = 1 - rand_pop[rand_r, rand_c]

    print("\nDepois da mutção: \n",rand_pop[:,0:col])

    print("A soma dos pesos dos valores do melhor indivíduo é:", sum(np.multiply(w, capIndividual)) )
    print("O melhor valor é:", maxVal)
    print("O indivíduo é: ",capIndividual)
    print("O fitness function é:", maxVal / np.average(rand_pop[:,col+1]))
