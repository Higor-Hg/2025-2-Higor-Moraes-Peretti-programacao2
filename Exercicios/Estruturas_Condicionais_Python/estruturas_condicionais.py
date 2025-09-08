#Exercicio

'''1. Crie 2 variáveis. Inicialize-as com dois valores numéricos inteiros informados pelo
#usuário. Se o primeiro valor informado for maior do que o segundo, exiba na tela
#uma mensagem informando essa constatação, caso contrário, exiba na tela uma
#mensagem dizendo que o segundo valor informado é maior do que o primeiro. Os
#números informados pelo usuário devem aparecer em ambas as mensagens.
#Verifique se ambos os números são pares, exiba mensagem na tela. Verifique
#se pelo menos um deles é múltiplo de 5 e exiba mensagem na tela.'''

#Resposta:

try:
    numero1 = int(input("Digite o primeiro número inteiro: "))
    numero2 = int(input("Digite o segundo número inteiro: "))

    if numero1 > numero2:
       print(f"{numero1}  é maior do que {numero2}") 
       
    elif numero2 > numero1:
         print(f"{numero2}  é maior do que {numero1}")   
         
    else:
        print("Os valores informdos são iguais.")
        
    if (numero1 % 2 == 0) and (numero2 % 2 == 0):
        print(f"{numero1} e o número {numero2} são números pares.")
        
    else:
        print("Um ou ambos os números são pares.")
        
    if (numero1 % 5 == 0) or (numero2 % 5 == 0):
        print("Pelo menos um dos números é multiplo de 5")
        
    else:
        print("Os números informados não são multiplos de 5")                       

except ValueError:
    print(f"Número inválido. O valor informado não é um inteiro válido. Erro do compilador {e}")

'''2.Crie um programa que possa marcar uma consulta médica. Como opções, teremos
#disponíveis apenas 03 médicos, que devem ter seus nomes exibidos na tela, p/ que
#possam ser escolhidos. Após a escolha do profissional médico, exibir mensagem na
#tela informando que a consulta foi marcada com o médico escolhido (nome do
#médico). Caso o usuário faça uma escolha inválida, exiba uma mensagem de
#erro na tela.'''

#Resposta
   
print ("Olá,escolha um dos médicos que você queira consultar.")
print ("1.Dr Eliane")
print ("2.Dr Osman")
print ("3.Dr Henrique")

medico  = int(input("Digite o número do médico escolhido (1, 2 ou 3): "))
   
if medico == 1:
        print(f"Consulta marcada com Dr Eliane.")        
elif medico == 2:
        print(f"Consulta marcada com Dr Osman.")        
elif medico == 3:
        print(f"Consulta marcada com Dr Henrique.")        
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

#Resposta

Frase =  "python é uma excelente linguagem de programação!!!"

palavra = input("digite uma palavra")


if palavra. lower() in Frase. lower():
    print(f"A palavra {palavra} esta na frase oculta...")

else:
    print(f" a palavra {palavra} nao esta na frase oculta...")


if Frase.find(palavra) >= 0:
    print(f"A palavra {palavra} esta na frase oculta...")
    
else:
    print(f"A palavra {palavra} NÂO esta na frase oculta")

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

numero1 = float(input("Digite um número: "))
numero2 = float(input("Digite outro número: "))

if numero1 > 0 and numero2 > 0:
    print("Os dois números são positivos")
elif numero1 < 0 or numero2 < 0:
    print("Pelo menos um dos dois números é negativo")
else:
    print("Um dos números é zero")




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

#Resposta

peso = float(input("Digite seu peso em KG: "))
altura = float(input("Digite sua altura em metros: "))

imc = peso / (altura ** 2)

round(imc, 2)

if imc < 18.5:
    print("Você está abaixo do peso")
    
elif imc >= 18.5 and imc <= 24.9 :
    print("Você está no peso normal")
    
elif imc >= 25 and imc <= 29.9 :
    print("Você está acima do peso")
    
else:
    print("Você está obeso")
    
'''7. Solicite ao usuário que digite um número. Converta-o para float usando conversão
explícita de tipo do Python. Exiba na tela tanto o número informado pelo usuário
quanto o seu tipo de dado. Verificar se o número informado é inteiro ou decimal,
usando o operador módulo.'''
   
#Resposta   
   
numero = float(input("Digite um número: "))

print("Número informado:", numero)
print("Tipo de dado:", type(numero))

if numero % 1 == 0:
    print("O número é inteiro.")
else:
    print("O número é decimal.")

''' 8. Crie um programa que leia dois números. Exiba na tela uma mensagem que mostre
os números informados e se são menores, iguais ou maiores do que 150. Verifique
se a soma dos dois números é maior que 300 e exiba mensagem na tela
informando o ocorrido.'''  
   
#Resposta   
    
NUM1 = float(input("Digite o primeiro número: "))
NUM2 = float(input("Digite o segundo número: "))

NUMEROS = (NUM1, NUM2)  # constante como tupla

print(f"Números informados: {NUM1} e {NUM2}")

# verificando cada número com if
if NUM1 < 150:
    print(f"O primeiro número ({NUM1}) é menor que 150.")
elif NUM1 == 150:
    print(f"O primeiro número ({NUM1}) é igual a 150.")
else:
    print(f"O primeiro número ({NUM1}) é maior que 150.")

if NUM2 < 150:
    print(f"O segundo número ({NUM2}) é menor que 150.")
elif NUM2 == 150:
    print(f"O segundo número ({NUM2}) é igual a 150.")
else:
    print(f"O segundo número ({NUM2}) é maior que 150.")

soma = NUM1 + NUM2
if soma > 300:
    print("A soma dos dois números é maior que 300.")
else:
    print("A soma dos dois números NÃO é maior que 300.")


    
'''9. Crie um programa que exiba na tela os dias da semana. Defina os dias da semana
como constantes do tipo String. Solicite ao usuário que digite um número entre 1 e 7,
onde 1 = segunda-feira e 7 = domingo. De acordo com o número digitado exiba o dia
da semana. Caso um valor inválido seja informado, exiba uma mensagem de erro
para o usuário.'''
 
#Resposta
 
# Constantes para os dias da semana
DIA1 = "domingo"
DIA2 = "segunda-feira"
DIA3 = "terça-feira"
DIA4 = "quarta-feira"
DIA5 = "quinta-feira"
DIA6 = "sexta-feira"
DIA7 = "sábado"

numero = int(input("Digite um número de 1 a 7: "))

if numero == 1:
    print("Dia da semana:", DIA1)
elif numero == 2:
    print("Dia da semana:", DIA2)
elif numero == 3:
    print("Dia da semana:", DIA3)
elif numero == 4:
    print("Dia da semana:", DIA4)
elif numero == 5:
    print("Dia da semana:", DIA5)
elif numero == 6:
    print("Dia da semana:", DIA6)
elif numero == 7:
    print("Dia da semana:", DIA7)
else:
    print("Erro: número inválido. Digite um número entre 1 e 7.")


'''10. Crie um programa que exiba na tela os meses do ano por extenso. Defina os meses
como constantes do tipo String. Solicite ao usuário que digite um número entre 1 e
12, onde 1 = janeiro e 12 = dezembro. De acordo com o número digitado, exiba o
mês do ano. Juntamente com o nome do mês do ano, informe a quantidade de dias
do mês (desconsiderar ano bissexto). Caso um valor inválido seja informado, exiba
uma mensagem de erro para o usuário.'''

#Resposta

# Constantes para os meses do ano e seus dias
MES1 = "Janeiro"; DIAS1 = 31
MES2 = "Fevereiro"; DIAS2 = 28
MES3 = "Março"; DIAS3 = 31
MES4 = "Abril"; DIAS4 = 30
MES5 = "Maio"; DIAS5 = 31
MES6 = "Junho"; DIAS6 = 30
MES7 = "Julho"; DIAS7 = 31
MES8 = "Agosto"; DIAS8 = 31
MES9 = "Setembro"; DIAS9 = 30
MES10 = "Outubro"; DIAS10 = 31
MES11 = "Novembro"; DIAS11 = 30
MES12 = "Dezembro"; DIAS12 = 31

numero = int(input("Digite um número de 1 a 12: "))

if numero == 1:
    print(f"Mês: {MES1}, Dias: {DIAS1}")
elif numero == 2:
    print(f"Mês: {MES2}, Dias: {DIAS2}")
elif numero == 3:
    print(f"Mês: {MES3}, Dias: {DIAS3}")
elif numero == 4:
    print(f"Mês: {MES4}, Dias: {DIAS4}")
elif numero == 5:
    print(f"Mês: {MES5}, Dias: {DIAS5}")
elif numero == 6:
    print(f"Mês: {MES6}, Dias: {DIAS6}")
elif numero == 7:
    print(f"Mês: {MES7}, Dias: {DIAS7}")
elif numero == 8:
    print(f"Mês: {MES8}, Dias: {DIAS8}")
elif numero == 9:
    print(f"Mês: {MES9}, Dias: {DIAS9}")
elif numero == 10:
    print(f"Mês: {MES10}, Dias: {DIAS10}")
elif numero == 11:
    print(f"Mês: {MES11}, Dias: {DIAS11}")
elif numero == 12:
    print(f"Mês: {MES12}, Dias: {DIAS12}")
else:
    print("Erro: número inválido. Digite um número entre 1 e 12.")

    
'''11. Peça que o usuário informe três valores inteiros positivos que representam os lados
de um triângulo. Verifique se os valores informados podem formar um triângulo. Se
sim, informe se é um triângulo: equilátero, isósceles ou escaleno. Se não, exiba
uma mensagem dizendo que as medidas dos lados informados não representam um
triângulo. Lembrando que:
➢ Na geometria euclidiana, um triângulo é formado por três segmentos de reta
que podem ser conectados extremidade a extremidade.
➢ Para que isso seja possível, nenhum lado pode ser maior ou igual à soma
dos outros dois. Se fosse igual, teríamos uma linha reta (triângulo
degenerado). Se fosse maior, não haveria como fechar a figura.'''    
    
#Resposta

a = int(input("Digite o lado A: "))
b = int(input("Digite o lado B: "))
c = int(input("Digite o lado C: "))

if a + b > c and a + c > b and b + c > a:
    if a == b == c:
        print("Triângulo equilátero.")
    elif a == b or a == c or b == c:
        print("Triângulo isósceles.")
    else:
        print("Triângulo escaleno.")
else:
    print("Os valores informados NÃO formam um triângulo.")

'''12. Solicite ao usuário que informe três números inteiros e exiba na tela o maior deles.
Não utilize funções built-in do Python. Se não forem informados valores numéricos,
exiba mensagem de erro ao usuário.'''

#Resposta

try:
    n1 = int(input("Digite o primeiro número: "))
    n2 = int(input("Digite o segundo número: "))
    n3 = int(input("Digite o terceiro número: "))

    maior = n1
    if n2 > maior:
        maior = n2
    if n3 > maior:
        maior = n3

    print("O maior número é:", maior)

except ValueError:
    print("Erro: Por favor, digite apenas números inteiros.")

#feita pela professor uso para melhor entendimento
#Questões01

try:
    numero1 = int(input("Digite o primeiro número inteiro: "))
    numero2 = int(input("Digite o segundo número inteiro: "))

    if numero1 > numero2:
       print(f"{numero1}  é maior do que {numero2}") 
       
    elif numero2 > numero1:
         print(f"{numero2}  é maior do que {numero1}")   
         
    else:
        print("Os valores informdos são iguais.")
        
    if (numero1 % 2 == 0) and (numero2 % 2 == 0):
        print(f"{numero1} e o número {numero2} são números pares.")
        
    else:
        print("Um ou ambos os números são pares.")
        
    if (numero1 % 5 == 0) or (numero2 % 5 == 0):
        print("Pelo menos um dos números é multiplo de 5")
        
    else:
        print("Os números informados não são multiplos de 5")                       

except ValueError:
    print(f"Número inválido. O valor informado não é um inteiro válido. Erro do compilador {e}")
