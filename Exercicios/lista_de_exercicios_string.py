# 1 - Crie uma função que receba uma string como parâmetro, 
# e retorne a string em maiúsculo.

def converter_maiuscula(texto):
    return texto.upper()


# 2 - Crie uma função que receba uma frase e uma palavra
# e retorne True se a palavra estiver na frase, senão False.

def palavra_na_frase(frase, palavra):
    return palavra.lower() in frase.lower()


# 3 - Crie uma função que receba uma frase, uma palavra antiga 
# e uma nova palavra e retorne a frase com a substituição.

def substituir_palavra(frase, palavra_antiga, palavra_nova):
    return frase.replace(palavra_antiga, palavra_nova)


# 4 - Crie uma função que receba uma palavra e verifique 
# se ela é um palíndromo (ignorando espaços e maiúsculas).

def eh_palindromo(texto):
    texto = texto.lower().replace(" ", "")
    return texto == texto[::-1]


# 5 - Crie uma função que receba um texto e retorne 
# a quantidade de vogais desse texto.

def contar_vogais(texto):
    vogais = "aeiouAEIOU"
    contador = 0
    for letra in texto:
        if letra in vogais:
            contador += 1
    return contador


# 6 - Crie uma função que receba uma frase e retorne 
# a primeira palavra dela.

def primeira_palavra(frase):
    return frase.split()[0]


# 7 - Crie uma função que receba uma frase, um caractere inicial 
# e um caractere final e retorne um booleano.

def verifica_inicio_fim(frase, inicio, fim):
    return frase.startswith(inicio) and frase.endswith(fim)


# 8 - Crie uma função que receba um texto e retorne 
# a quantidade de palavras.

def contar_palavras(texto):
    return len(texto.split())


# 9 - Crie uma função que receba um texto com pontuação 
# e retorne o texto sem pontos, vírgulas e exclamações.

def remover_pontuacao(texto):
    pontuacoes = ".,!"
    for p in pontuacoes:
        texto = texto.replace(p, "")
    return texto

# ---------------- PROGRAMA PRINCIPAL ----------------

print("\nTRATAMENTO DE STRINGS - TESTE DE FUNÇÕES\n")

# 1
print("1) Converter para maiúsculas")
texto = input("Texto: ")
print("Resultado:", converter_maiuscula(texto))
print()

# 2
print("2) Verificar palavra na frase")
frase = input("Frase: ")
palavra = input("Palavra: ")
print("Resultado:", palavra_na_frase(frase, palavra))
print()

# 3
print("3) Substituir palavra")
frase = input("Frase: ")
antiga = input("Palavra antiga: ")
nova = input("Nova palavra: ")
print("Resultado:", substituir_palavra(frase, antiga, nova))
print()

# 4
print("4) Verificar palíndromo")
texto = input("Texto: ")
print("Resultado:", eh_palindromo(texto))
print()

# 5
print("5) Contar vogais")
texto = input("Texto: ")
print("Resultado:", contar_vogais(texto))
print()

# 6
print("6) Primeira palavra da frase")
frase = input("Frase: ")
print("Resultado:", primeira_palavra(frase))
print()

# 7
print("7) Verificar início e fim")
frase = input("Frase: ")
inicio = input("Caractere inicial: ")
fim = input("Caractere final: ")
print("Resultado:", verifica_inicio_fim(frase, inicio, fim))
print()

# 8
print("8) Contar palavras")
texto = input("Texto: ")
print("Resultado:", contar_palavras(texto))
print()

# 9
print("9) Remover pontuação")
texto = input("Texto com pontuação: ")
print("Resultado:", remover_pontuacao(texto))
print()
