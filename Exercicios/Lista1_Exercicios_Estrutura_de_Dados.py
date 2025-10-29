'''
1.Crie 03 variáveis do tipo tupla que contenham: os dias da semana, os meses
do ano, as estações do ano. Crie uma função, que tenha 1 parâmetro, que
imprima na tela os valores definidos em cada uma das tuplas.
'''

dias_da_semana_tupla = ('1ºDomingo', '2ºSegunda', '3ºTerça', '4ºQuarta', '5ºQuinta', '6ºSexta', '7ºSábado')
meses_do_ano_tupla = ('Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro')
estacoes_do_ano_tupla = ('Verão', 'Outono', 'Inverno', 'Primavera')

def imprimir_tupla(tuplas):
 
  for item in tuplas:
    print(item)


'''
2. Crie 03 variáveis do tipo lista que contenham: os dias da semana, os meses
do ano, as estações do ano. Crie uma função, que tenha 1 parâmetro, que
imprima na tela os valores definidos em cada uma das listas.
'''

dias_da_semana_list =['1ºDomingo', '2ºSegunda', '3ºTerça', '4ºQuarta', '5ºQuinta', '6ºSexta', '7ºSábado']
meses_do_ano_list = ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro']
estacoes_do_ano_list = ['Verão', 'Outono', 'Inverno', 'Primavera']


def imprimir_lista(lista):
    
    for item in lista:
        print(item)

'''
3. Exiba o tamanho e os elementos: primeiro, terceiro e último das estruturas de
dados criadas e inicializadas nas questões 1 e 2.
'''

#resposta no programa principal




'''
4. Crie uma lista de compras de supermercado com 15 itens. Através de um
laço de repetição, exiba na tela, cada um dos itens dessa lista de compras.
Você deve decidir que tipo de estrutura de dados utilizar e imprimir, logo
abaixo da lista de compras, os motivos da sua decisão, ou seja, explique
porque utilizou tal estrutura de dados.
'''

lista_de_compra = ['Arroz', 'Feijão', 'Manteiga', 'Queijo', 'Presunto', 'Cebola', 'Alho', 'Tomate', 'Pão', 'Bolachas', 'Macarão', 'Bacon', 'Pimentão', 'Frutas', 'Papel Higiênico']

def compras(i):
    
   for i in lista_de_compra:
    print(i)

'''
5.Crie um programa que atualize a lista de compras da questão 4. O programa
deve solicitar ao usuário, através de um menu de opções, que tipo de
operação deseja efetuar sobre a lista de compras: incluir um novo item,
remover um item ou atualizar um item existente. Crie uma função para cada
tipo de operação permitida. Após o usuário informar uma das opções válida
do menu, o programa deve solicitar que o usuário digite o nome do
produto\item para que a função correta seja chamada e a alteração da lista
de compras possa ser feita. Implemente uma forma de encerrar o programa
através da interação do usuário.
'''

menu_alteracao = '''
========= MENU (Lista de Compra)=========
1 - Incluir um novo item
2 - Remover um item
3 - Atualizar um item existente
Sair - Finalizar Alterações
=========================
'''

def incluir_item():
    novo = input("Digite o nome do item que deseja incluir: ")
    novo = novo.lower().title()
    lista_de_compra.append(novo)
    print(f"'{novo}' foi adicionado à lista.")


def remover_item():
    remover = input("Digite o nome do item que deseja remover: ")   
    if remover.lower().title() in lista_de_compra:
        lista_de_compra.remove(remover)
        print(f"'{remover}' foi removido da lista.")
    else:
        print(f"O item '{remover}' não foi encontrado na lista.")


def alterar_item():
    antigo = input("Digite o nome do item que deseja atualizar: ")
    if antigo.lower().title() in lista_de_compra:
        novo = input("Digite o novo nome do item: ")
        indice = lista_de_compra.index(antigo)
        lista_de_compra[indice] = novo
        print(f"'{antigo}' foi atualizado para '{novo}'.")
    else:
        print(f"O item '{antigo}' não foi encontrado na lista.")

'''
6. Crie uma estrutura de dados que armazene o nome das linguagens de
programação: C, C++, JavaScript, Java, Lua e Python. Implemente um
programa que solicite ao usuário que tente adivinhar quais linguagens de
programação constam em uma lista oculta de nomes, informando, para tanto,
nomes de linguagens de programação. Exiba mensagem na tela para o
usuário informando se a linguagem consta ou não na lista oculta. A
funcionalidade de procurar em uma lista oculta de nomes deverá ser
implementada através de função.
'''

linguagens = ['C', 'C++', 'JavaScript', 'Java', 'Lua', 'Python']


def verificar_linguagem(nome):
    if nome in linguagens:
        print(f"A linguagem '{nome}' está na lista oculta!")
    else:
        print(f"A linguagem '{nome}' NÃO está na lista oculta.")

'''
7. Crie um programa que possa marcar uma consulta médica. Utilize uma
estrutura de dados para armazenar o nome dos médicos que atendem na
clínica. Solicite ao usuário que informe com qual profissional deseja marcar
uma consulta médica. Implemente funções que possam: imprimir na tela o
nome dos profissionais, procurar na lista de profissionais o nome informado,
exibir na tela mensagem de que a consulta foi marcada com sucesso. Em
caso de falha, exibir mensagem na tela informando o usuário do ocorrido.
'''

medicos = ["Dra. Ana Souza", "Dr. João Silva", "Dr. Carlos Mendes", "Dra. Fernanda Lima"]

def exibir_medicos():
    print("\n--- MÉDICOS DISPONÍVEIS ---")
    for medico in medicos:
        print(medico)
    print("---------------------------")

def verificar_medico(nome):
    return nome in medicos

def marcar_consulta():
    while True:
        exibir_medicos()
        nome = input("\nDigite o nome do médico com quem deseja marcar a consulta: ")

        if verificar_medico(nome):
            print(f"\nConsulta marcada com sucesso com {nome}!")
            break  
        else:
            print("\nMédico não encontrado. Tente novamente.\n")





#Programa Principal

print("\n!-------------------------------INÍCIO-----------------------------------!")

#Q1

print("\n___________QUESTÃO-1__________________")


print("\n--- Dias da Semana ---")
imprimir_tupla(dias_da_semana_tupla)

print("\n--- Meses do Ano ---")
imprimir_tupla(meses_do_ano_tupla)

print("\n--- Estações do Ano ---")
imprimir_tupla(estacoes_do_ano_tupla)

#Q2

print("___________QUESTÃO-2________________")

print("\nDias da semana:")
imprimir_lista(dias_da_semana_list)

print("\nMeses do ano:")
imprimir_lista(meses_do_ano_list)

print("\nEstações do ano:")
imprimir_lista(estacoes_do_ano_list)

print("___________QUESTÃO-3________________")

print("\n--- TUPLAS ---")
print(f"Dias da Semana → tamanho: {len(dias_da_semana_tupla)}, primeiro: {dias_da_semana_tupla[0]}, terceiro: {dias_da_semana_tupla[2]}, último: {dias_da_semana_tupla[-1]}")
print(f"Meses do Ano → tamanho: {len(meses_do_ano_tupla)}, primeiro: {meses_do_ano_tupla[0]}, terceiro: {meses_do_ano_tupla[2]}, último: {meses_do_ano_tupla[-1]}")
print(f"Estações do Ano → tamanho: {len(estacoes_do_ano_tupla)}, primeiro: {estacoes_do_ano_tupla[0]}, terceiro: {estacoes_do_ano_tupla[2]}, último: {estacoes_do_ano_tupla[-1]}")

print("\n--- LISTAS ---")
print(f"Dias da Semana → tamanho: {len(dias_da_semana_list)}, primeiro: {dias_da_semana_list[0]}, terceiro: {dias_da_semana_list[2]}, último: {dias_da_semana_list[-1]}")
print(f"Meses do Ano → tamanho: {len(meses_do_ano_list)}, primeiro: {meses_do_ano_list[0]}, terceiro: {meses_do_ano_list[2]}, último: {meses_do_ano_list[-1]}")
print(f"Estações do Ano → tamanho: {len(estacoes_do_ano_list)}, primeiro: {estacoes_do_ano_list[0]}, terceiro: {estacoes_do_ano_list[2]}, último: {estacoes_do_ano_list[-1]}")


print("___________QUESTÃO-4________________")
print("\n--lista de compras--")
compras(lista_de_compra)



print("\n___________QUESTÃO-5________________")

while True:
    print(menu_alteracao)
    
    menu = input("\nDigite o número que corresponde a qual o que você BUSCA no menu: ")
    
    if menu.lower() == "sair":
        print("Fim das Alterações")
        break
    
    elif menu == '1':
        incluir_item()
        
    elif menu == '2':
        remover_item()
        
    elif menu == '3':
        alterar_item()
        
    elif menu == '4':
        print("\nLista de Compras Atualizada:")
        for item in lista_de_compra:
            print(item)
            
    elif menu == '0' or menu.lower() == 'sair':
        print("Saindo do programa... Alterações finalizadas.")
        
        break
    else:
        print("Opção inválida. Tente novamente.")
        

print("\n___________QUESTÃO-6________________")

print("\n=== Jogo: Adivinhe a Linguagem de Programação ===")
print("Tente adivinhar quais linguagens estão na lista oculta.")
print("Digite 'sair' para encerrar o jogo.\n")


while True:
    tentativa = input("Digite o nome de uma linguagem: ").strip()
    
    if tentativa.lower() == 'sair':
        print("Encerrando o jogo. Até mais!")
        break
    
    verificar_linguagem(tentativa)
    

print("\n___________QUESTÃO-7________________")

print("\n=== CLÍNICA SAÚDE E VIDA ===")
marcar_consulta()





