#INTRODUÇÃO DE ESTRUTURA DE DADOS LISTA DO PYTHON 

#---------------------------------------------------------------------------------
'''Uma lista é uma sequência de valores que pode ser de qualquer tipo;
Os valores em uma lista são chamados de elementos ou itens;
Há várias formas de criar uma lista.A mais simples é clocar os elementos entre
colchetes [e];'''
variavleDoTipoLista = [10,20,30,40]

for itemDaLista in variavleDoTipoLista:
    print(itemDaLista)

for i in range(len(variavleDoTipoLista)):
    variavleDoTipoLista[i] = variavleDoTipoLista[i] * 2
    
variavleDoTipoLista == [20,40,60,80]   

#-----------------------------------------------------------------------------------

variavleDoTipoLista2 = ['Programação', 'Banco de Dados', 'Redes de Computadores']

if "Banco de Dados" in variavleDoTipoLista2:
    print("True")

else:
    print("False")
    
#-----------------------------------------------------------------------
   
'''Permite elementos de tipos diferentes: string, número de ponto'''

variavleDoTipoLista3 = ['spam',20,5[10,20]]





