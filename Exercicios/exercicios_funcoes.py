import string

# 1) Verifica se um número é primo
def verifica_primo(primo):
    if primo <= 1:
        return False
    for i in range(2, int(primo ** 0.5) + 1):
        if primo % i == 0:
            return False
    return True


# 2) Retorna o maior entre 3 números
def maior(numero1, numero2, numero3):
    if numero1 > numero2 and numero1 > numero3:
        return numero1
    elif numero2 > numero1 and numero2 > numero3:
        return numero2
    elif numero3 > numero1 and numero3 > numero2:
        return numero3
    else:
        return "Valores iguais"


# 3) Calcula o fatorial
def fatorial(numero):
    if numero == 0 or numero == 1:
        return 1
    return numero * fatorial(numero - 1)


# 4) Calcula média de 4 números
def calcular_media(n1, n2, n3, n4):
    return (n1 + n2 + n3 + n4) / 4


# 5) Verifica se é palíndromo
def eh_palindromo(texto):
    texto_formatado = texto.replace(" ", "").lower()
    return texto_formatado == texto_formatado[::-1]


# 6) Conta vogais
def contar_vogais(texto):
    vogais = "aeiouAEIOU"
    contador = 0
    for letra in texto:
        if letra in vogais:
            contador += 1
    return contador


# 7) Inverte string
def inverter_string(texto):
    return texto[::-1]


# 8) Conta palavras
def contar_palavras(frase):
    palavras = frase.strip().split()
    return len(palavras)


# 9) Substitui caracteres
def substituir_caractere(texto, antigo, novo):
    return texto.replace(antigo, novo)


# 10) Remove pontuação
def remover_pontuacao(texto):
    return texto.translate(str.maketrans("", "", string.punctuation))


# ---------- PROGRAMA PRINCIPAL ----------
print("\n=== TESTE DAS FUNÇÕES ===\n")

# Teste 1 - Primo
num = int(input("1) Digite um número para verificar se é primo: "))
print("Resultado:", verifica_primo(num))

# Teste 2 - Maior de 3
print("\n2) Digite três números:")
n1 = int(input("Primeiro: "))
n2 = int(input("Segundo: "))
n3 = int(input("Terceiro: "))
print("Maior valor:", maior(n1, n2, n3))

# Teste 3 - Fatorial
num = int(input("\n3) Digite um número para calcular o fatorial: "))
print("Fatorial:", fatorial(num))

# Teste 4 - Média
print("\n4) Digite quatro números:")
a = float(input("Número 1: "))
b = float(input("Número 2: "))
c = float(input("Número 3: "))
d = float(input("Número 4: "))
print("Média:", calcular_media(a, b, c, d))

# Teste 5 - Palíndromo
texto = input("\n5) Digite um texto para verificar se é palíndromo: ")
print("É palíndromo?", eh_palindromo(texto))

# Teste 6 - Contar vogais
texto = input("\n6) Digite um texto para contar vogais: ")
print("Quantidade de vogais:", contar_vogais(texto))

# Teste 7 - Inverter string
texto = input("\n7) Digite um texto para inverter: ")
print("Texto invertido:", inverter_string(texto))

# Teste 8 - Contar palavras
frase = input("\n8) Digite uma frase: ")
print("Quantidade de palavras:", contar_palavras(frase))

# Teste 9 - Substituir caractere
texto = input("\n9) Digite um texto: ")
antigo = input("Caractere a ser substituído: ")
novo = input("Novo caractere: ")
print("Texto modificado:", substituir_caractere(texto, antigo, novo))

# Teste 10 - Remover pontuação
texto = input("\n10) Digite um texto com pontuação: ")
print("Texto sem pontuação:", remover_pontuacao(texto))
