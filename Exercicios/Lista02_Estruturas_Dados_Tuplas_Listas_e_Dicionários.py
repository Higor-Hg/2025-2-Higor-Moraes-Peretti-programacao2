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

"""produtos = {'maçã': 7,
    'feijão': 10,
    'pão': 3,
    'carne': 9
    }
maior_valor = max(produtos.values())
print(f"O maior valor entre os produtos é {maior_valor}")"""

#8. Crie uma tupla com 10 números e encontre o maior e o menor valor.

#Questâo Resosta 8

"""varios_numeros = (1,2,3,4,5,6,7,8,9,10)
maior_numero = max(varios_numeros)
menor_numero = min(varios_numeros)
print(f"O maior valor é {maior_numero} e o menor é {menor_numero}")"""

"""9. Crie uma lista de dicionários, onde cada dicionário representa um aluno com as
chaves: "nome", "nota". Imprima os nomes dos alunos com nota maior que 7."""

#Questâo Resosta 9

"""alunos = [{"nome": "João V.",     "nota": 7.1,},
          {"nome": "Cleiton",     "nota": 4,  },
          {"nome": "Vitor",       "nota": 6,  },
          {"nome": "João G.",     "nota": 10, },
          {"nome": "Maria",       "nota": 9,  }
         ]

for aluno in alunos:
    if aluno["nota"] > 7:
        print(aluno["nome"])"""
        
#10. Inverta uma lista de palavras e imprima o resultado.

#Questâo Resosta 10

"""palavrinhas = ["Uva", "pera", "Maçã", "melancia"]
palavras_invertidas = palavrinhas [::-1]
print(palavras_invertidas)"""


"""11. Crie um dicionário onde a chave é o nome de uma pessoa e o valor é uma lista de
suas notas. Imprima a média de cada pessoa."""

#Questâo Resosta 11

"""notas = {"Lucas": [9, 3, 10],
         "maria": [5, 7, 1],
         "vitor": [10, 10, 10,]}

for aluno, nota in notas.items():
    media = sum(nota) / len(nota)
    print(f"{'nome'}={media}")"""
    
"""12. Dado uma lista de tuplas representando transações (cliente, valor), calcule o total
gasto por cada cliente."""

#Questâo Resosta 12

clientes = [
    ("Claudio", [9.0, 32.5, 9.0]),
    ("Marcos", [45.0, 29.99, 30.0]),
    ("Lucas", [100.0, 99.99, 1.0])
]

for cliente, valor in clientes:
    gasto_total = sum(valor)
    print(f"O cliente {cliente} gastou um total de R$ {gasto_total:.2f}")

"""13. Crie uma função que recebe uma lista de strings e retorna um dicionário com a
contagem de cada letra."""

#Questâo Resosta 13

"""def contador_palavras(lista_string):
    contagem = {}

    for palavra in lista_string:
        for letra in palavra:
            letra = letra.lower()
            
            if letra not in contagem:
                contagem[letra] = 1
            
            else:
                contagem[letra] +=1
                
    return contagem"""

#Programa principal

"""palavras = ["Maçã", "Vida", "Morte"]
resultado = contador_palavras(palavras)
print(resultado)"""
"""14. Crie um dicionário invertido: dado um dicionário {chave: valor}, crie um novo
dicionário {valor: chave}."""

#Questâo Resosta 14

normal ={"Pessoas": 10,
         "Animais": 23,
         "Casas":   12,}

invertido = dict(reversed(list(normal.items())))
print(invertido)

"""15. Crie uma lista de números e use um dicionário para contar quantas vezes cada
número aparece na lista."""

#Questâo Resosta 15

def contador_numeros(lista_numeros):
    contagem = {}

    for numero in lista_numeros:
        for digito in str(numero):
            if digito not in contagem:
                contagem[digito] = 1
            else:
                contagem[digito] += 1
                
    return contagem
    
# Programa principal
numeros = [1234, 231, 1]
resultado = contador_numeros(numeros)
print(resultado)