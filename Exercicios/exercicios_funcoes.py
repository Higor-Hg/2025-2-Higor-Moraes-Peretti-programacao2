'''1. Crie uma função que verifica se um número é primo. Lembrando
que: números primos são números naturais maiores que 1 que
possuem apenas dois divisores positivos: 1 e o próprio número (2,
3, 5, 7,11, etc…).'''
#Respota

def verifica_primo(primo):
    if primo <= 1:
        return False
    for i in range(2, int(primo ** 0.5) + 1):
        if primo % i == 0:
            return False
    return True


numero = int(input("Digite o número a ser verificado: "))

if verifica_primo(numero):
    print(f"{numero} é primo!")
else:
    print(f"{numero} não é primo.")

       
'''2. Crie uma função que retorna o maior valor inteiro, dentre 3
passados como parâmetro, para a função.'''


'''3. Crie uma função para calcular o fatorial de um número.'''

'''4. Crie uma função que retorna a média entre 4 números passados
como parâmetros.'''

'''5. Função que verifica se uma string é um palíndromo.'''

'''6. Crie uma função que receba uma string como parâmetro e retorne
a quantidade de vogais (a, e, i, o, u) presentes nela.'''

'''7. Crie uma função que receba uma string e retorne a mesma
invertida.'''

'''8. Crie a função que receba uma frase e retorne a quantidade de
palavras existentes nela.'''

'''9. Crie uma função que receba uma string e substitua todas as
ocorrências do caractere antigo pelo novo.'''

'''10. Usando a biblioteca “string” (importação externa), crie a função
remover_pontuacao(texto) que remova todos os sinais de
pontuação da string texto passado por parâmetro.'''