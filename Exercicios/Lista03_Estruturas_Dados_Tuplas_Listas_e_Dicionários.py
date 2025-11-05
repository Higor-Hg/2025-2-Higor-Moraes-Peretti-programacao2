
# Lista03 Estruturas Dados Python#VAI CAIR NA PROVA***

''' 
1. A partir de uma sequência de números digitados pelo usuário, separados por
vírgula, converta tal sequência numérica em uma lista. Crie uma função que
receba como ***parâmetro*** a sequência de números, e retorne uma lista. Crie
uma segunda função que receba uma lista e a imprima na tela.
Função que recebe uma sequência de números e converte em lista
'''
#!singular
def criar_lista(sequencia):
    # separa pelos espaços ou vírgulas e transforma em inteiros
    
    lista = [int(num) for num in sequencia.split(',')]#list compreension
    return lista


def converter_lista (sequencia):
    try:
        lista= []
        for numero in sequencia.split(","): #!se não for usada a virgula a lista vai ficar em branco 
            lista.append (int(numero))
        return lista
    
    except ValueError as e:
        print("Erro na conversão da lista ")
        #!para converter em lista é preciso de um separador com espaço ou vírgula
    
     
    
# Função que recebe uma lista e imprime na tela
def imprimir_lista(lista):
    print("Lista criada:", lista)

# Programa principal
entrada = input("Digite uma sequência de números separados por vírgula: ")
minha_lista = criar_lista(entrada)
imprimir_lista(minha_lista)


#2º opção
# Função que cria uma lista a partir de uma sequência digitada
def criar_lista(sequencia):
    # split separa a string onde houver vírgula e cria uma lista
    lista = [int(num) for num in sequencia.split(',')]
    return lista

# Função que imprime a lista
def imprimir_lista(lista):
    print("Lista:", lista)


'''2. Crie uma função que receba dois parâmetros: 1 - uma lista de números
# inteiros; 2 - crescente ou decrescente. Se for chamada com o segundo
# parâmetro = crescente, ordene e retorne a lista de números em ordem
# crescente. Se for chamada com o segundo parâmetro = decrescente, ordene
# e retorne a lista de números em ordem decrescente. Utilize a função de
# impressão de estrutura de dados criada na questão 1 e imprima na tela a lista
# retornada. Teste a função na ordem crescente e na decrescente. Faça com
# que o usuário forneça a lista de números.
'''

# Dica: sempre comece pedindo os dados e depois pensando na ordem


#2º
def criar_lista(sequencia):
    lista = [int(num) for num in sequencia.split(',')]
    return lista

def ordenar_lista(lista, ordem):
    if ordem.lower() == 'crescente':
        lista.sort()
    elif ordem.lower() == 'decrescente':
        lista.sort(reverse=True)
    return lista



'''3. Crie uma função que receba duas listas de números informadas pelo usuário,
de tamanhos idênticos, e retorne uma nova lista que contenha apenas os
elementos comuns às duas listas, sem elementos duplicados. Utilize a função
de impressão de estrutura de dados criada na questão 1 e imprima na tela a
lista retornada. Fiquem atentos às responsabilidades do programa principal
nessa implementação e as responsabilidades da função.
'''

def elementos_comuns(lista1, lista2):
    # Convertemos as listas para conjuntos (set) para remover duplicatas automaticamente
    # O operador & (interseção) pega apenas os elementos que estão em ambas as listas
    comuns = list(set(lista1) & set(lista2))
    return comuns


'''
4. Crie uma função que receba uma lista do tipo String e retorne um dicionário
onde cada elemento da lista será uma chave do dicionário e o valor vinculado
a cada chave será o tamanho da chave String. Crie uma segunda função que
imprima o dicionário retornado pela primeira função. Exemplo de uma
chave\valor do dicionário retornado pela função: “Python”: 6.
'''

def lista_para_dicionario(lista_strings):
    # Cria um dicionário onde:
    # chave = palavra
    # valor = tamanho da palavra (usando len())
    dicionario = {palavra: len(palavra) for palavra in lista_strings}
    return dicionario

def imprimir_dicionario(dic):
    # Percorre o dicionário e imprime chave e valor
    print("\nDicionário de tamanhos:")
    for chave, valor in dic.items():
        print(f"{chave}: {valor}")


'''
5. Crie uma função que receba 02 listas, de mesmo tamanho, e retorne uma
lista de tuplas contendo os elementos das duas listas passadas por
parâmetro. Pesquise e utilize a função “zip()” nessa implementação. Imprima
a lista de tuplas, avalie se as funções de impressão já implementadas podem
ser usadas, caso não possa, crie uma nova função para impressão de listas
de tuplas.
'''
def combinar_listas(lista1, lista2):
    # zip() combina os elementos das duas listas na mesma posição
    # list() transforma o resultado de zip em uma lista de tuplas
    return list(zip(lista1, lista2))

def imprimir_tuplas(lista_tuplas):
    print("\nLista de tuplas (pares):")
    for tupla in lista_tuplas:
        print(tupla)


#PROGRAMA PRINCIPAL

print("-----------------------------------------------------------------")

#Q1:
entrada = input("\nDigite números separados por vírgula: ").strip()
numeros = criar_lista(entrada)
imprimir_lista(numeros)


#Q2:

entrada = input("\nDigite números separados por vírgula: ").strip()
ordem = input("Deseja ordem crescente ou decrescente? ").strip()

# Aqui está a parte em que usamos a função da questão 1 👇
lista = criar_lista(entrada)
lista_ordenada = ordenar_lista(lista, ordem)
print("Lista ordenada:", lista_ordenada)

#Q3:

entrada1 = input("\nDigite a primeira lista de números separados por vírgula: ").strip()
entrada2 = input("Digite a segunda lista de números separados por vírgula: ").strip()

# Reutilizando a função da questão 1 para criar listas
lista1 = criar_lista(entrada1)
lista2 = criar_lista(entrada2)

# Chamando a função que encontra os elementos comuns
resultado = elementos_comuns(lista1, lista2)

# Reutilizando a função de impressão da questão 1
print("\nElementos comuns (sem duplicados):")
imprimir_lista(resultado)

#Q4:

entrada_palavras = input("\nDigite palavras separadas por vírgula: ").strip()

# .strip() remove espaços desnecessários no começo/fim
# .split(',') transforma a string em lista separando pelas vírgulas
lista_palavras = [palavra.strip() for palavra in entrada_palavras.split(',')]

# Cria o dicionário com base na lista
dic_resultado = lista_para_dicionario(lista_palavras)

# Imprime o resultado
imprimir_dicionario(dic_resultado)

#Q5:

entrada1 = input("\nDigite a primeira lista (números separados por vírgula): ").strip()
entrada2 = input("Digite a segunda lista (números separados por vírgula): ").strip()

# Reutilizando a função da questão 1 novamente
lista1 = criar_lista(entrada1)
lista2 = criar_lista(entrada2)

# Cria lista de tuplas
tuplas = combinar_listas(lista1, lista2)

# Usa função de impressão específica para tuplas
imprimir_tuplas(tuplas)

print("---------------------------------------------------------------")


