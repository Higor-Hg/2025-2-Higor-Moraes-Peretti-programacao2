print("Lista 02 - Estruturas de Dados")

# 1
print("\nQuestão 1")
nomes = ("Higor", "Enzin", "Otávio", "Douglas", "Jackson")
print("Segundo nome:", nomes[1])

# 2
print("\nQuestão 2")
numeros = [1, 2, 3, 4, 5]
print("Soma:", sum(numeros))

# 3
print("\nQuestão 3")
aluno = {"nome": "Creito", "idade": 46, "curso": "TDS"}
print(aluno)

# 4
print("\nQuestão 4")
minha_lista = [1, 2, 3, 4, 5]
print("Tipo antes:", type(minha_lista))
print("Tipo depois:", type(tuple(minha_lista)))

# 5
print("\nQuestão 5")
frutas = ['Maçã', 'Banana', 'Laranja']
frutas.append('Uva')
print(frutas)

# 6
print("\nQuestão 6")
numeros_impares = [n for n in range(1, 11) if n % 2 != 0]
print(numeros_impares)

# 7
print("\nQuestão 7")
produtos = {'maçã': 7, 'feijão': 10, 'pão': 3, 'carne': 9}
print("Produto mais caro:", max(produtos, key=produtos.get))

# 8
print("\nQuestão 8")
nums = (1,2,3,4,5,6,7,8,9,10)
print("Maior:", max(nums), "Menor:", min(nums))

# 9
print("\nQuestão 9")
alunos = [
    {"nome": "João V.", "nota": 7.1},
    {"nome": "Cleiton", "nota": 4},
    {"nome": "Vitor", "nota": 6},
    {"nome": "João G.", "nota": 10},
    {"nome": "Maria", "nota": 9}
]
for aluno in alunos:
    if aluno["nota"] > 7:
        print(aluno["nome"])

# 10
print("\nQuestão 10")
palavras = ["Uva", "Pera", "Maçã", "Melancia"]
print(list(reversed(palavras)))

# 11
print("\nQuestão 11")
notas = {
    "Lucas": [9, 3, 10],
    "Maria": [5, 7, 1],
    "Vitor": [10, 10, 10]
}
for nome, n in notas.items():
    media = sum(n) / len(n)
    print(nome, "=", media)

# 12
print("\nQuestão 12")
clientes = [
    ("Claudio", [9.0, 32.5, 9.0]),
    ("Marcos", [45.0, 29.99, 30.0]),
    ("Lucas", [100.0, 99.99, 1.0])
]
for nome, valores in clientes:
    print(nome, "gastou R$", sum(valores))

# 13
print("\nQuestão 13")
def contar_letras(lista):
    contagem = {}
    for palavra in lista:
        for letra in palavra.lower():
            if letra in contagem:
                contagem[letra] += 1
            else:
                contagem[letra] = 1
    return contagem

print(contar_letras(["Maçã", "Vida", "Morte"]))

# 14
print("\nQuestão 14")
normal = {"Pessoas": 10, "Animais": 23, "Casas": 12}
invertido = {v: k for k, v in normal.items()}
print(invertido)

# 15
print("\nQuestão 15")
def contar_numeros(lista):
    contagem = {}
    for numero in lista:
        if numero in contagem:
            contagem[numero] += 1
        else:
            contagem[numero] = 1
    return contagem

print(contar_numeros([1234, 231, 1, 1234, 1, 1]))

