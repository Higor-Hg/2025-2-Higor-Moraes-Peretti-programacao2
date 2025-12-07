
# 1) Percorrer a string na horizontal e vertical
texto = "Instituto Federal de Santa Catarina"

print("\nHorizontal:")
for letra in texto:
    print(letra, end=" ")

print("\n\nVertical:")
for letra in texto:
    print(letra)


# 2) Contagem de 0 a 20 exibindo apenas os pares
print("\n\nNúmeros pares de 0 a 20:")
for numero in range(0, 21):
    if numero % 2 == 0:
        print(numero)


# 3) Tabuada de um número digitado pelo usuário
numero = int(input("\n\nDigite um número para ver a tabuada: "))

print(f"\nTabuada do {numero}:")
for i in range(1, 11):
    print(f"{numero} x {i} = {numero * i}")


# 4) Contagem regressiva de 20 segundos
import time

print("\n\nContagem regressiva:")
for seg in range(20, 0, -1):
    print(seg)
    time.sleep(1)

print("\nTempo esgotado!")


# 5) Contar ímpares de 1 a 100, quantidade e soma
quantidade_impares = 0
soma_impares = 0

for n in range(1, 101):
    if n % 2 != 0:
        quantidade_impares += 1
        soma_impares += n

print("\n\nResultado dos números ímpares:")
print("Quantidade:", quantidade_impares)
print("Soma:", soma_impares)


# 6) Verificar se número é primo e contar divisores
numero = int(input("\n\nDigite um número: "))

divisores = 0
for i in range(1, numero + 1):
    if numero % i == 0:
        divisores += 1

if divisores == 2:
    print(f"\n{numero} é primo.")
else:
    print(f"\n{numero} NÃO é primo.")
    print(f"Quantidade de divisores: {divisores}")


# 7) Verificar se é palíndromo
frase = input("\n\nDigite uma palavra ou frase: ")

frase_formatada = ""
for letra in frase:
    if letra != " ":
        frase_formatada += letra.lower()

if frase_formatada == frase_formatada[::-1]:
    print("\nÉ um palíndromo!")
else:
    print("\nNão é um palíndromo.")


# 8) Contar letras maiúsculas e minúsculas
texto = input("\n\nDigite uma palavra ou frase: ")

maiusculas = 0
minusculas = 0

for letra in texto:
    if letra.isupper():
        maiusculas += 1
    elif letra.islower():
        minusculas += 1

print("\nMaiúsculas:", maiusculas)
print("Minúsculas:", minusculas)

