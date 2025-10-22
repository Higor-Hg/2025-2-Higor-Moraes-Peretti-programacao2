#INTRODUÇÃO DE ESTRUTURA DE DADOS LISTA DO PYTHON 

#Uma lista é uma equência de valores que podem ser ode qualquer tipo:
#Os valores em uma lista são chamados de elementos ou itens;
"""Há várias formas para criar uma lista. A mais simples é colocar os elementos
   entre COLCHETES [ e ]"""
   
variavelDoTipoLista = [10, 20, 30, 40]
variavelDoTipoLista2 = ['Programação', 'Bancos de Dados','Redes de Computadores']

"""Permite elementos de tipos diferentes: atring, número de ponto flutuante, um número inteiro etc..."""

variavelDoTipoLista3 = ['spam', 2.0, 5, [10,20]]

#O operador in funciona com listas:

variavelDoTipoLista2 = ['Programação','Banco de Dados','Redes de Computadores']

if"Banco de Dados" in variavelDoTipoLista2:
    print("True")
    
else:
     print("False")
     
"""A forma mais comum de percorrer os elementos em uma lista é com um loop for.
   A sintaxe é a mesma que a das strings;"""
   
for itemDalista in variavelDoTipoLista:
    print(itemDalista)

"""Para escrever ou atualizar elementos, será necessário utilizar os índices.
   Combinar as funções integradas range e len, permite alcançar esseresultado:"""
    
variavelDoTipoLista = [10, 20, 30, 40]

for i in range(len(variavelDoTipoLista)):
    variavelDoTipoLista[i] = variavelDoTipoLista[i] * 2
    
variavelDoTipoLista = [20, 40, 60, 80]





