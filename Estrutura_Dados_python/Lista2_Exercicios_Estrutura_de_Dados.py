#1. Crie uma tupla com 5 nomes e imprima o segundo nome.

#Questâo Resosta 1

"""nomes = ("Higor", "Enzin", "Otávio", "Douglas", "Jackson")

print(f"O segundo nome na tupla é {nomes[1]}")"""

#2. Crie uma lista com 5 números inteiros e imprima a soma de todos os elementos.

#Questâo Resosta 2

"""numeros = [1, 2, 3, 4, 5]

soma_total = sum(numeros)
print(f"A soma dos números é igual a {soma_total} ")
"""
"""3. Crie um dicionário com 3 pares (chave: valor) representando um aluno (nome, idade,
curso). Imprima cada valor."""

#Questâo Resosta 3

"""dicionario = {1: "Creito",
        2: 46,
        3: "TDS"
        }

print(f"Nome = {dicionario[1]}, Idade = {dicionario[2]}, curso = {dicionario[3]} ")"""

#4. Converta uma lista em tupla e imprima o tipo antes e depois da conversão.

#Questâo Resosta 4

"""minha_lista = [1, 2, 3, 4, 5]
print(f"Imprimindo a lista: {minha_lista}")

minha_tupla = tuple(minha_lista)
print(f"Imprimindo a tupla: {minha_tupla}")
"""
#5. Adicione um novo elemento ao final de uma lista de frutas e imprima a nova lista.

#Questâo Resosta 5
"""
lista = ['Maçã', 'banana', 'laranja']
print(f"Lista antes da adição: {lista}")

lista.append('uva')
print(f"Lista depois da adição: {lista}")
"""
"""6. Crie uma lista com números de 1 a 10. Remova os números pares da lista e imprima
o resultado."""

#Questâo Resosta 6

"""LISTA = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
numeros_impares = [num for num in LISTA if num % 2 != 0]
print(numeros_impares)
"""
#7. Dado um dicionário com nomes de produtos e preços, encontre o produto mais caro.

#Questâo Resosta 7

produtos = {'maçã': 7,
    'feijão': 10,
    'pão': 3,
    'carne': 9
    }
maior_valor = max(produtos.values())
print(f"O maior valor entre os produtos é {maior_valor}")

#8. Crie uma tupla com 10 números e encontre o maior e o menor valor.

#Questâo Resosta 8

varios_numeros = (1,2,3,4,5,6,7,8,9,10)
maior_numero = max(varios_numeros)
menor_numero = min(varios_numeros)
print(f"O maior valor é {maior_numero} e o menor é {menor_numero}")

"""9. Crie uma lista de dicionários, onde cada dicionário representa um aluno com as
chaves: "nome", "nota". Imprima os nomes dos alunos com nota maior que 7."""

#Questâo Resosta 9



#10. Inverta uma lista de palavras e imprima o resultado.
"""11. Crie um dicionário onde a chave é o nome de uma pessoa e o valor é uma lista de
suas notas. Imprima a média de cada pessoa."""
"""12. Dado uma lista de tuplas representando transações (cliente, valor), calcule o total
gasto por cada cliente."""
"""13. Crie uma função que recebe uma lista de strings e retorna um dicionário com a
contagem de cada letra."""
"""14. Crie um dicionário invertido: dado um dicionário {chave: valor}, crie um novo
dicionário {valor: chave}."""
"""15. Crie uma lista de números e use um dicionário para contar quantas vezes cada
número aparece na lista."""