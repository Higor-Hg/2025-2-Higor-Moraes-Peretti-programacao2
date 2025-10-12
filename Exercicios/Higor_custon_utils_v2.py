import re

menu_principal = """
========= MENU =========
1 - Operadores
2 - Palavras Reservadas no Python
3 - Tipos de dados no Python
4 - Conceito de Variável
5 - Verificar Ano Bissexto
6 - Contar vogais da frase
7 - Contar palavras da frase
8 - Inverter a frase
9 - Validar senha
10 - Validar formato e tamanho de um CPF
11 - Verificar triângulo
Sair - Finalizar programa
=========================
"""


def operadores():
     return (
        "Operadores Aritméticos: + (adição), - (subtração), * (multiplicação)\n"
        "Operadores de Comparação: == (igualdade), != (diferente), > (maior)\n"
        "Operadores Lógicos: and, or, not\n"
    )
        
    
def palavras_reservadas():
    return (
        "if, else, for, while, break, continue, def, return, class, import"
        )

def tipos_de_dados(): 
    return (
        "int (inteiro), float (número decimal), str (texto), bool (verdadeiro/falso)"
            )


def conceito_de_variável(): 
    return (
       "Uma variável é um espaço na memória para armazenar valores.\n"
        "Regras:\n"
        "- Deve começar com letra ou underscore (_)\n"
        "- Não pode conter espaços ou caracteres especiais (exceto _)\n"
        "- Não pode ser palavra reservada\n"
        "As variáveis são usadas para armazenar e manipular dados no programa."
            )    

def ano_bissexto(ano):
    if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
        return True
        
    else:
        return False

def contar_vogais(frase):
    vogais = 'aeiouAEIOU'
    qtd = sum(1 for letra in frase if letra in vogais)
    return f"A frase digitada contém  {qtd} de vogais."



def contar_palavras(frase):
    qtd = len(frase.split())
    return f"A frase contém {qtd} palavras."


def inverter_frase(frase):
    return f"Frase original: {frase}\nFrase invertida: {frase[::-1]}"


def validar_senha(senha):
    if len(senha) < 6:
        return "Senha muito curta! Deve ter no mínimo 6 caracteres."
    elif len(senha) > 20:
        return "Senha muito longa! Deve ter no máximo 20 caracteres."
    elif not re.search(r"[A-Z]", senha):
        return "A senha deve ter pelo menos uma letra MAIÚSCULA."
    elif not re.search(r"[a-z]", senha):
        return "A senha deve ter pelo menos uma letra minúscula."
    elif not re.search(r"[$#@!&]", senha):
        return "A senha deve ter pelo menos um caractere especial ($#@!&)."
    elif re.search(r"\s", senha):
        return "Senha inválida! Não pode conter espaços ou quebras de linha."
    elif re.search(r"[^a-zA-Z0-9$#@!&]", senha):
        return "Senha inválida! Possui caracteres não permitidos."
    else:
        return "Senha válida!"


def validar_cpf(cpf):
    padrao = r"^\d{3}\.\d{3}\.\d{3}-\d{2}$"
    if re.match(padrao, cpf):
        return f"O CPF {cpf} é válido (formato correto)."
    return f"O CPF {cpf} é inválido. Formato esperado: 000.000.000-00"


def verificar_triangulo(a, b, c):
    if a < b + c and b < a + c and c < a + b:
        if a == b == c:
            return "O triângulo é equilátero."
        elif a == b or b == c or a == c:
            return "O triângulo é isósceles."
        else:
            return "O triângulo é escaleno."
    else:
        return "Os valores informados não formam um triângulo."

#programa principal

while True:
    print(menu_principal)

    menu = input("Digite o número que corresponde a qual você BUSCA no menu: ")

    if menu.lower() == "sair":
        print("Saindo...")
        break
   
   
    elif menu == "1":
       print(operadores())    
    
    elif menu == '2':  
        print(palavras_reservadas) 
   
    elif menu == '3':
        print(tipos_de_dados) 
     
    elif menu == '4':
        print(conceito_de_variável) 

    elif menu == '5':
        ano = int(input("Digite um ano para verificar se o mesmo é bissexto: "))
    
        if ano_bissexto(ano):
            print('É Bissexto')
        
        else:
            print('Não é bissexto')

    elif menu == "6":
        frase = input("Digite uma frase: ")
        contar_vogais(frase)

    elif menu == "7":
        frase = input("Digite uma frase: ")
        contar_palavras(frase)

    elif menu == "8":
        frase = input("Digite uma frase: ")
        inverter_frase(frase)

    elif menu == "9":
        senha = input("Digite a senha: ")
        validar_senha(senha)

    elif menu == "10":
        cpf = input("Digite o CPF (formato 000.000.000-00): ")
        validar_cpf(cpf)

    elif menu == "11":
        a = int(input("Digite o lado A: "))
        b = int(input("Digite o lado B: "))
        c = int(input("Digite o lado C: "))
        verificar_triangulo(a, b, c)

    else:
        print("Opção Inválida! Observe o menu e tente novamente.\n")