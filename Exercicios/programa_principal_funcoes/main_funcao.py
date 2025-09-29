import sys 

sys.path.append(r"C:\Users\ADM\Documents\GitHub\2025-2-Higor-Moraes-Peretti-programacao2")

from custom_utils.funcoes_de_usuario import *


#Programa principal Q1
numero = 0
try:
   numero = int(input("Verificar número primos. Digite um número: ")) 
   
   if verifica_primo(numero):
       print(f"{numero} é um número primo.")
   
   else:
        print(f"{numero} NÃO um número primo.")
          

except ValueError:
    print(f"{numero} não é um número válido para calculo de números primos.")  
    
#Programa principal Q2
try:
    numero1 = int(input("Informe o 1º número interio: ")) 
    numero2 = int(input("Informe o 2º número interio: "))
    numero3 = int(input("Informe o 3º número interio: "))
    
    resultado = maior_entre_tres(numero1, numero2, numero3)
    print(f"O maior numero entre: {numero1}, {numero2}, e {numero3} é {resultado}")
    
except ValueError:
    print("Valor inválido")
    
#Programa principal Q3
numero_fatorial = 0
try:
    numero_fatorial = int(input("informe um número para calcular seu fatorial: "))
    if (numero_fatorial > 0):
        print(f"O fatorial de {numero_fatorial} é : {fatorial(numero_fatorial)}")
    
    else:
        print("Digite um número maior que zero")
        
except ValueError:
    print(f"{numero_fatorial} não é um número válido")                   
    
#Programa principal Q4    
    
    