'''1) Crie uma estrutura de repetição que percorra a String “Instituto Federal
de Santa Catarina” exibindo na tela letra por letra dessa String, tanto na
orientação horizontal quanto na vertical.'''
#Resposta
texto = "Instituto Federal de Santa Catarina"


for letra in texto:
    print(letra, end=" ")
print() 


for letra in texto:
    print(letra)



'''2) Crie um programa que realiza a contagem de 0 a 20, exibindo apenas os
números pares.'''
#Resposta

for numero in range(0, 21, 2):
    print(numero)



'''3) Crie um programa que exiba na tela a tabuada de um determinado número
fornecido pelo usuário.'''
#Resposta

numero = int(input("Digite um número para ver a tabuada: "))

for i in range(1, 11):
    print(f"{numero} x {i} = {numero * i}")



'''4) Crie um programa que realiza a contagem regressiva de 20 segundos.'''
#Resposta

import time

for seg in range(20, 0, -1):
    print(seg)
    time.sleep(1)  
print("Tempo esgotado!")



'''5) Crie um programa que realiza a contagem de 1 até 100, considerando
apenas os números ímpares. Exiba na tela quantos números ímpares
foram encontrados nesse intervalo e qual a soma desses números
ímpares.'''
#Resposta







'''6) Crie um programa que pede ao usuário que digite um número qualquer,
em seguida retorne se esse número é primo ou não, caso não, retorne
também quantas vezes esse número é divisível.'''
#Resposta




'''7) Crie um programa que pede que o usuário digite um nome ou uma frase,
verifique se esse conteúdo digitado é um palíndromo ou não, exibindo em
tela esse resultado.'''
#Resposta





'''8) Escreva um programa que lê uma palavra ou frase digitada pelo usuário,
retornando o número de letras maiúsculas e minúsculas da mesma.
Quando necessário, utilize funções nativas do Python (built-in).'''
#Resposta



