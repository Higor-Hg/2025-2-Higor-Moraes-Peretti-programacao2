'''
1 - Crie uma função que receba uma string como parâmetro, e retorne uma string em maiúsculo da 
string que foi passada por parâmetro.
'''
def converter_maiuscula(texto):

  return texto.upper()


'''
2 – Crie uma função que receba 2 parâmetros: o 1º parâmetro deve ser uma frase do tipo string; o 2º
parâmetro deve ser uma palavra do tipo string. A função deverá retornar True se a palavra estiver
na frase passada como parâmetro, caso contrário, deverá retornar False.
'''

def palavra_frase(frase,palavra):
    frase = frase.lower()
    palavra = palavra.lower()
    if palavra in frase:
        return True
    
    else:
        return False


'''
3 – Crie uma função que receba 3 parâmetros:
➢ 1º parâmetro deve ser uma frase;
➢ 2º parâmetro deve ser uma palavra que esteja na frase;
➢ 3º parâmetro deve ser uma nova palavra, que vai substituir na frase do 1º parâmetro, a
palavra passada no 2º parâmetro.
A função deverá retornar uma nova frase contendo a alteração solicitada no requisito da função.
'''
def substituir_palavra(frase, palavra_antiga, palavra_nova):
    return frase.replace(palavra_antiga, palavra_nova)

'''
4 – Crie uma função que receba uma palavra e verifique se ela é um palíndromo (ignorar espaços e
maiúsculas/minúsculas). A função deve retornar um booleano.
'''
def palavra_palindromo()
    print()


'''
5 – Crie uma fun'ção que receba um texto como parâmetro. A função deve retornar a quantidade de
vogais do texto.
'''

'''
6 – Crie uma função que receba uma frase como parâmetro e retorne uma nova string que é a
primeira palavra dessa frase.
'''

'''
7 – Crie uma função que receba 3 parâmetros:
➢ 1º parâmetro deve ser uma frase;
➢ 2º parâmetro deve ser um caracter (uma letra) que será utilizado p/ saber se a frase inicia
com esse caracter;
➢ 3º parâmetro deve ser um caracter (uma letra) que será utilizado p/ saber se a frase termina
com esse caracter.
A função deve usar expressões lógicas e retornar um booleano.
'''

'''
8 – Crie uma função que receba um texto como parâmetro e retorne um valor inteiro que represente
a quantidade de palavra desse texto.
'''

'''
9 – Crie uma função que receba um texto como parâmetro que contenha pontuação: pontos, vírgulas
e pontos de exclamação. A função deverá remover essa pontuação e retornar um novo texto.
'''



#Programa Principal

print("---------------------------------INÍCIO----------------------------------------")

#Q1
minha_string = "olá, mundo!"
string_maiuscula = converter_maiuscula(minha_string)

print(f"String original: {minha_string}")
print(f"String em maiúsculo: {string_maiuscula}")

#Q2

frase = input("Digite uma Frase:")
palavra = input("Digite UMA PALAVRA da frase:")
print(f'Palavra na frase: {palavra_frase(frase, palavra)}')

#Q3
frase_original = input("Digite a Frase:")
palavra_a_substituir = input("Digite a palavra a substituir:")
nova_palavra = input("Digite a nova palavra:")

frase_alterada = substituir_palavra(frase_original, palavra_a_substituir, nova_palavra)

print("Frase original:", frase_original)
print("Nova frase:", frase_alterada)

#Q4



