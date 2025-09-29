'''1. Crie uma função que verifica se um número é primo. Lembrando
que: números primos são números naturais maiores que 1 que
possuem apenas dois divisores positivos: 1 e o próprio número (2,
3, 5, 7,11, etc…).'''
#Respota

def verifica_primo(numero):
    if numero < 2:
        return False
    
    '''Verifica se o numero é divisível por qualquer número entre 2 e a raiz quadrada do número
    pssado por parâmetro, ele NÃO É PRIMO'''
    for i in range(2, int(numero ** 0.5) + 1):
        if numero % i == 0:
            return False

    return True

'''2. Crie uma função que retorna o maior valor inteiro, dentre 3
passados como parâmetro, para a função.'''

def maior_entre_tres(numero1, numero2, numero3):
    if numero1 > numero2 and numero1 > numero3:
        return numero1
    
    elif numero2 > numero1 and numero2 > numero3:
        return numero2    
    
    elif numero3 > numero1 and numero3 > numero2:
        return numero3
    
    else:
        print("Os valores passados por parâmetro são iguais.")
        
'''3. Crie uma função para calcular o fatorial de um número.'''

def fatorial(numero):
    if numero == 0 or numero == 1:
        return 1
    
    return numero * fatorial(numero - 1)        
    
'''4. Crie uma função que retorna a média entre 4 números passados
como parâmetros.'''    
#Resposta
def calcular_media(num1, num2, num3, num4):
    #média = (num1 + num2 + num3 + num4) / 4
    return (num1 + num2 + num3 + num4) / 4

'''5. Função que verifica se uma string é um palíndromo.'''
#Resposta
def






'''6. Crie uma função que receba uma string como parâmetro e retorne
a quantidade de vogais (a, e, i, o, u) presentes nela.'''
#resposta
def contar_vogais(palavra_ou_frase):
    VOGAIS = "aeiou"
    contador_de_vogais
        