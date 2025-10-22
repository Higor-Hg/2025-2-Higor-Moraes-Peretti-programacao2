#INTRODUÇÃO ESTRUTURAS DE DADOS TUPLAS 

#Maneiras de se declarar uma tupla:

variavelDoTipoTupla = 'a','b','c','d','e'

"""Embora não seja sepre necessário, é comum colocar tuplas entre parêmteses.
   Usaremos essa forma de declaração:"""

variavelDoTipoTupla = ('a','b','c','d','e')

"""A maior parte dos operadores de lista também funionam em tuplas. O operador de índeice(colchetes) permiteacesso a um elemento9 através
   do seu índice:"""
   
variavelDoTipoTupla = ('a','b','c','d','e')
variavelDoTipoTupla[0] == 'a'

#O operador de fatia permite selecionar vários elementos:

variavelDoTipoTupla = ('a','b','c','d','e')
variavelDoTipoTupla[1:3] == ('b','c')

#1. count(x): retorna o número de vezes que o valor de variável "x" aparece na  tupla.

"""2. index(x, star=0, stop=len(tuple)): retorna o ídice da primeira ocorrência do calor x.
 Pode receber ìndices start e stop como limite de busca."""
 
 #3. len(tuple): Retorna o número de elementos da tupla.
 
 #4. max(tuple): retorna o maximo da tupla
 
 #5. min (tuple): retorna o menor elemento da tupla.
 
 #6. sum (tuple): retorna a soma dos elementos(funciona apenas se forem todos numéricos)
 
 #7. sorted (tuple): retorna a lista co os elementos da tupla ordenados.
 
 #8. tuple (interável): converte um interável (como lista ou string) em uma tupla.
 
 #9. in (Operador de pertencimento): verifica se um elemento está presente na tupla.
 
 #10. enumerate (tuple): retorna um interador com pares (índice, valor), útil para loops.
 
t7 = ('a','b','c')
for i, v in enumerate(t7):
    print(i,v)
#Saida:

# 0, a
# 1, b
# 2, c
