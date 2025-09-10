#Forma direta (melhor performance)
soma_par = 0
for numero_ in range(2, 101, 2):
    soma_par += numero_par
#Forma mais explícita
soma_par = 0
for numero in range(1, 101):
    if numero % 2 == 0:
        soma_par += numero