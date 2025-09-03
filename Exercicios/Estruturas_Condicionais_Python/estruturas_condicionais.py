#Exercicio

'''1. Crie 2 variáveis. Inicialize-as com dois valores numéricos inteiros informados pelo
#usuário. Se o primeiro valor informado for maior do que o segundo, exiba na tela
#uma mensagem informando essa constatação, caso contrário, exiba na tela uma
#mensagem dizendo que o segundo valor informado é maior do que o primeiro. Os
#números informados pelo usuário devem aparecer em ambas as mensagens.
#Verifique se ambos os números são pares, exiba mensagem na tela. Verifique
#se pelo menos um deles é múltiplo de 5 e exiba mensagem na tela.'''

#Resposta:

num1 = int(input("Digite o primeiro valor inteiro: "))
num2 = int(input("Digite o segundo valor inteiro: "))


if num1 > num2:
    print(f"O primeiro valor informado ({num1}) é maior que o segundo ({num2}).")
else:
    print(f"O segundo valor informado ({num2}) é maior que o primeiro ({num1}).")


if num1 % 2 == 0 and num2 % 2 == 0:
    print("Ambos os números são pares.")

if num1 % 5 == 0 or num2 % 5 == 0:
    print("Pelo menos um dos números é múltiplo de 5.")

'''2.Crie um programa que possa marcar uma consulta médica. Como opções, teremos
#disponíveis apenas 03 médicos, que devem ter seus nomes exibidos na tela, p/ que
#possam ser escolhidos. Após a escolha do profissional médico, exibir mensagem na
#tela informando que a consulta foi marcada com o médico escolhido (nome do
#médico). Caso o usuário faça uma escolha inválida, exiba uma mensagem de
#erro na tela.'''

#Resposta
   
print ("Olá,escolha um dos médicos que você queira consultar.")
print ("1.Dr Andressa")
print ("2.Dr Osman")
print ("3.Dr Luis")

medico  = int(input("Digite o número do médico escolhido (1, 2 ou 3): "))
   
if medico == 1:
        print(f"Consulta marcada com Dr Eliane.")        
elif medico == 2:
        print(f"Consulta marcada com Dr Osman.")        
elif medico == 3:
        print(f"Consulta marcada com Dr Luis.")        
else:
        print("Erro: Escolha inválida. Por favor, escolha um número entre 1 e 3.")

'''3. Escreva um programa que verifica se uma determinada palavra consta em um texto
de origem. O texto não será conhecido pelo usuário que usará de palavras aleatórias
na tentativa de adivinhar que palavras compõem a frase oculta. Frase: "Python é
uma excelente linguagem de programação!!!”. Se acertar, a mensagem: "A
palavra (palavra digitada pelo usuário) está na frase". Se errar, a mensagem: "A
palavra (palavra digitada pelo usuário) não está na frase". Use a função "find",
referenciada na documentação:
https://docs.python.org/3/library/stdtypes.html
Ignorar maiúsculas/minúsculas. Pesquise por um determinado operador
Python que resolverá o problema. faça duas implementações:
➢ Uma com a função “find”;
➢ Uma com o operador que você descobrirá na pesquisa.'''

'''4. Crie um programa que leia um número e verifique se ele é par, ímpar ou zero (0).
Caso seja diferente de zero, verifique se o tal número é positivo, negativo.'''
 
#Resposta

Numero1 = float(input("Digite um número: "))
if Numero1 == 0:
    print("O valor do número que você digitou é 0")
    
elif Numero1 %2 == 0:
    print(f"O número {Numero1} é par")

else:
    print(f"O número {Numero1} é ímpar")
    
if Numero1 != 0:
    if Numero1 > 0:
        print(f"O número {Numero1} é positivo")
    else:
        print(f"O número {Numero1} é negativo")


'''5. Escreva um programa que receba dois números e verifique se ambos são
positivos. Se pelo menos um dos números for negativo, exibir mensagem
informando o ocorrido.'''

#Resposta

Numero1 = float(input("Digite um número: "))
Numero2 = float(input("Digite outro número: "))

if Numero1 and Numero2 > 0:
    print("Os dois números são positivos")

elif Numero1 or Numero2 < 0:
    print("Pelo menos um dos dois números são negativos")



'''6. Crie Crie um programa que receba o peso e a altura de uma pessoa e calcule seu
Índice de Massa Corporal (IMC). imc = peso / (altura * altura) . O programa deve
exibir uma mensagem na tela de acordo com a seguinte tabela:
➢ Abaixo de 18.5: Abaixo do peso;
➢ Entre 18.5 e 24.9: Peso normal;
➢ Entre 25 e 29.9: Sobrepeso;
➢ Acima de 30: Obesidade.
Validar se a entrada de dados é válida: peso e altura positivos e do tipo float;
Usar a função round(imc, 2) para arredondar o valor do IMC para duas casas
decimais.'''


peso = float(input("Digite seu peso em KG: "))
altura = float(input("Digite sua altura em metros: "))

imc = peso (altura * altura)

round(imc, 2)

if imc < 18.5:
    print("Você está abaixo do peso")
    
elif imc >= 18.5 and imc <= 24.9 :
    print("Você está no peso normal")
    
elif imc >= 25 and imc <= 29.9 :
    print("Você está acima do peso")
    
else:
    print("Você está obeso")

















