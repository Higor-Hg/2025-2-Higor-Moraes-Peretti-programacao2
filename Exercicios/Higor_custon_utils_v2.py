import re

menu_principal = """
========= MENU =========
1 - Operadores
2 - Palavras Reservadas no Python
3 - Tipos de dados no Python
4 - Conceito de Variável
5 - Verificar Ano Bissexto
6 - Contar vogais da frase
7 - Contar palavras da frase
8 - Inverter a frase
9 - Validar senha
10 - Validar formato e tamanho de um CPF
11 - Verificar triângulo
Sair - Finalizar programa
=========================
"""


def operadores(OperadoresALC):
     return (
        "Operadores Aritméticos: + (adição), - (subtração), * (multiplicação)\n"
        "Operadores de Comparação: == (igualdade), != (diferente), > (maior)\n"
        "Operadores Lógicos: and, or, not\n"
    )
        
    
Palavras_Reservadas = 'if, else, for, while, break, continue, def, return, class, import' 

Tipos_de_dados = 'int (inteiro), float (número decimal), str (texto), bool (verdadeiro/falso)'

Conceito_de_Variável = 'Variável é um espaço de memória para guardar dados.\não pode começar com número, não pode ter espaço, nem caracteres especiais (só _).\nSão usadas para armazenar valores que podem mudar no programa.'    

def ano_bissexto(ano):
    if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
        return True
        
    else:
        return False
    




















#programa principal

print(menu_principal)

menu = input("Digite o número que corresponde a qual você BUSCA no menu: ")

 if opcao.lower() == "sair":
        print("Programa finalizado. Até mais!")
        break
   
   
elif opcao == "1":
        print(operadores())    
    
elif menu == '2':  
   print() 
   
elif menu == '3':
   print() 
     

elif menu == '4':
   print() 

elif menu == '5':
    ano = int(input("Digite um ano para verificar se o mesmo é bissexto: "))
    
    if ano_bissexto(ano):
        print('É Bissexto')
        
    else:
        print('Não é bissexto')

    
elif menu == '6':
    print("")
  

elif menu == '7':
    print("")
    print()

elif menu == '8':
    print("")
    print()

elif menu == '9':
    print("")
    print()

elif menu == '10':
    print("")
  
elif menu == '11':
    print()