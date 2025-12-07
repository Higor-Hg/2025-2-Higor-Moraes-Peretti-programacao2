import sys 

sys.path.append(r"C:\Users\Cliente\OneDrive\Documentos\GitHub\2025-2-Higor-Moraes-Peretti-programacao2")


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
    
# Programa principal Q4
try:
    num1 = float(input("Informe o 1º número: "))
    num2 = float(input("Informe o 2º número: "))
    num3 = float(input("Informe o 3º número: "))
    num4 = float(input("Informe o 4º número: "))

    media = calcular_media(num1, num2, num3, num4)
    print(f"A média dos números é: {media}")

except ValueError:
    print("Valor inválido para cálculo da média.")


# Programa principal Q5
texto_palindromo = input("Digite uma palavra ou frase para verificar se é palíndromo: ")

if eh_palindromo(texto_palindromo):
    print("A string é um palíndromo.")
else:
    print("A string NÃO é um palíndromo.")


# Programa principal Q6
texto_vogais = input("Digite uma palavra ou frase para contar as vogais: ")
quantidade_vogais = contar_vogais(texto_vogais)
print(f"Quantidade de vogais: {quantidade_vogais}")


# Programa principal Q7
texto_inverter = input("Digite uma palavra ou frase para inverter: ")
texto_invertido = inverter_string(texto_inverter)
print(f"Texto invertido: {texto_invertido}")


# Programa principal Q8
frase = input("Digite uma frase para contar as palavras: ")
total_palavras = contar_palavras(frase)
print(f"Quantidade de palavras: {total_palavras}")


# Programa principal Q9
texto_substituicao = input("Digite um texto: ")
caractere_antigo = input("Digite o caractere que deseja substituir: ")
caractere_novo = input("Digite o novo caractere: ")

texto_resultado = substituir_caractere(texto_substituicao, caractere_antigo, caractere_novo)
print(f"Texto atualizado: {texto_resultado}")


# Programa principal Q10
texto_pontuacao = input("Digite um texto com pontuação: ")
texto_sem_pontuacao = remover_pontuacao(texto_pontuacao)
print(f"Texto sem pontuação: {texto_sem_pontuacao}")
   
    
    