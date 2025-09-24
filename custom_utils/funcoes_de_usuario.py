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