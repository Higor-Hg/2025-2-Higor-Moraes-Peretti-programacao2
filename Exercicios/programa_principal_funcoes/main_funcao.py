from custom_utils.funcoes_de_usuario import*

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