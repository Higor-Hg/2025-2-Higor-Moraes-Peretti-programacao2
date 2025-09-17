#Função que calcula o triplo de um número
def triplo(calcular_triplo):
    return calcular_triplo * 3 #Implementação da função

#Função que possui 2 parâmetros e nenhum retorno
def imprime_info(nome, idade) :
    print("Nome: ", nome)
    print("Idade: ", idade)

''''
#Código principal
calcular_triplo = 3
num = triplo(calcular_triplo) #chamda da funções
print("O triplo de 3 é: ",num) #num nesse caso vai valer 9, pois 3 * 3 = 9

calcular_triplo = 6
num = triplo(calcular_triplo) #chamada da função
print("O triplo de 6 é: ",num) #num nesse caso vai valer 18, pois 6 * 3 = 18
'''



#Código principal    
nome = 'Jhon Travolta'
i = 52
imprime_info(nome, i) #Chamada da função