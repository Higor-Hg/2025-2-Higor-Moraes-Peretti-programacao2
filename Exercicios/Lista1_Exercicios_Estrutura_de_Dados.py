'''1.Crie 03 variáveis do tipo tupla que contenham: os dias da semana, os meses
do ano, as estações do ano. Crie uma função, que tenha 1 parâmetro, que
imprima na tela os valores definidos em cada uma das tuplas.'''


dias_da_semana = ('1ºDomingo', '2ºSegunda', '3ºTerça', '4ºQuarta', '5ºQuinta', '6ºSexta', '7ºSábado')
meses_do_ano = ('Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro')
estacoes_do_ano = ('Verão', 'Outono', 'Inverno', 'Primavera')

def imprimir_tupla(tuplas):
 
  for item in tuplas:
    print(item)


'''2. Crie 03 variáveis do tipo lista que contenham: os dias da semana, os meses
do ano, as estações do ano. Crie uma função, que tenha 1 parâmetro, que
imprima na tela os valores definidos em cada uma das listas.'''

dias_da_semana =['1ºDomingo', '2ºSegunda', '3ºTerça', '4ºQuarta', '5ºQuinta', '6ºSexta', '7ºSábado']
meses_do_ano = ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro']
estacoes_do_ano = ['Verão', 'Outono', 'Inverno', 'Primavera']


def imprimir_lista(lista):
    
    for item in lista:
        print(item)

'''3. Exiba o tamanho e os elementos: primeiro, terceiro e último das estruturas de
dados criadas e inicializadas nas questões 1 e 2.
'''

'''4. Crie uma lista de compras de supermercado com 15 itens. Através de um
laço de repetição, exiba na tela, cada um dos itens dessa lista de compras.
Você deve decidir que tipo de estrutura de dados utilizar e imprimir, logo
abaixo da lista de compras, os motivos da sua decisão, ou seja, explique
porque utilizou tal estrutura de dados.
'''

lista_de_compra = ['Arroz', 'Feijão', 'Manteiga', 'Queijo', 'Presunto', 'Cebola', 'Alho', 'Tomate', 'Pão', 'Bolachas', 'Macarão', 'Bacon', 'Pimentão', 'Frutas', 'Papel Higiênico']

def compras(i):
    
   for i in lista_de_compra:
    print(i)

'''5.Crie um programa que atualize a lista de compras da questão 4. O programa
deve solicitar ao usuário, através de um menu de opções, que tipo de
operação deseja efetuar sobre a lista de compras: incluir um novo item,
remover um item ou atualizar um item existente. Crie uma função para cada
tipo de operação permitida. Após o usuário informar uma das opções válida
do menu, o programa deve solicitar que o usuário digite o nome do
produto\item para que a função correta seja chamada e a alteração da lista
de compras possa ser feita. Implemente uma forma de encerrar o programa
através da interação do usuário.'''

menu_alteracao = '''
========= MENU (Lista de Compra)=========
1 - Incluir um novo item
2 - Remover um item
3 - Atualizar um item existente
Sair - Finalizar Alterações
=========================
'''
def incluir_item():
    print()

def remover_item():
    print()

def alterar_item():
    print()






#Programa Principal

print("\n!-------------------------------INÍCIO-----------------------------------!")

#Q1

print("\n___________QUESTÃO-1__________________")


print("\n--- Dias da Semana ---")
imprimir_tupla(dias_da_semana)

print("\n--- Meses do Ano ---")
imprimir_tupla(meses_do_ano)

print("\n--- Estações do Ano ---")
imprimir_tupla(estacoes_do_ano)

#Q2

print("___________QUESTÃO-2________________")

print("\nDias da semana:")
imprimir_lista(dias_da_semana)

print("\nMeses do ano:")
imprimir_lista(meses_do_ano)

print("\nEstações do ano:")
imprimir_lista(estacoes_do_ano)

#print("___________QUESTÃO-3________________")


print("___________QUESTÃO-4________________")
print("\n--lista de compras--")
compras(lista_de_compra)



print("___________QUESTÃO-5________________")

while True:
    print(menu_alteracao)
    
    menu = input("Digite o número que corresponde a qual você BUSCA no menu: ")
    
    if menu.lower() == "sair":
        print("Fim das Alterações")
        break





