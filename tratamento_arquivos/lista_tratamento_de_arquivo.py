
#1. Crie uma função que leia e exiba o conteúdo de um arquivo passado por
#parâmetro. Caso o arquivo não exista, capture a exceção e exiba uma
#mensagem de erro na tela. Teste a implementação, inclusive, fornecendo
#arquivos que não existem.

import os
def getDirectoryPath():
    diretorio_atual = os.path.dirname(os.path.abspath(__file__))
    diretorio_pai = os.path.dirname(diretorio_atual)
    
    return diretorio_pai

def ler_arquivo(nome_arquivo):
    print("\n===Exercícioi 1: Leitura de Arquivo===")
    try:
        # Abre o arquivo em modo de leitura ('r') com codificação UTF-8/Mapa de caractéres usado no IBGE
        with open(nome_arquivo, 'r', encoding="utf-8") as file:
            conteudo = file.read()
            print("\n--- Conteúdo do arquivo ---")
            print(conteudo) 
            
    except FileNotFoundError as e:
        # Captura a exceção se o arquivo não for encontrado
        return f"ERRO: O arquivo {nome_arquivo} não foi encontrado. {e}"
    


# 2. Crie uma função que receba uma lista de strings e escreva cada item em
# uma nova linha de um arquivo chamado conteudo_lista.txt.

def escrever_em_arquivo(lista, local_nome_do_arquivo):
    print("\nExercício 2: Escrita em arquivo")
    
    try:
            with open (local_nome_do_arquivo, "w", encoding="Utf-8") as arquivo:
                for linha in lista:
                    arquivo.write(linha + "\n")
                    
                print(f"Dados gravados com sucesso no arquivo {local_nome_do_arquivo}")
                
        
    except FileNotFoundError as e:
        print(f"Erro, o arquivo {local_arquivo} não pode ser criado:  {e}")
    

# 3. Crie uma função “contarLinhasArquivo”, que receba como parâmetro um
# arquivo. Leia o arquivo e retorne o número total de linhas.

def contar_linhas_arquivo(local_nome_do_arquivo):
    total_linhas_arquivo = 0
    
    try:
        with open(local_nome_do_arquivo, "r", encoding= "UTF-8") as arquivo:
            for _ in arquivo:
                
                 total_linhas_arquivo += 1
                
            return total_linhas_arquivo
        
    except FileNotFoundError as e:
        print(f"O arquivo \"{local_nome_do_arquivo}\"não foi encontrado")
        

# 4. Crie uma função que copie o conteúdo de um arquivo para outro. Ambos os
# nomes dos arquivos devem ser passados como parâmetros.

def copiar_arquivo(origem, destino):
    print("Exercício 4")

    try:
        with open(origem, "r", encoding= "UTF-8") as arquivo_origem:
            conteudo_arquivo_origem = arquivo_origem.read()
            
            
        with open(destino, "w", encoding= "UTF-8") as arquivo_destino:
            arquivo_destino.write(conteudo_arquivo_origem)
            
        print()
        
        
    except FileNotFoundError as e:
        print(f"O arquivo de origem {origem} não foi encontrado")
        
    except Exception as error:
        print(f"Erro ao copiar o arquivo {error}")
        
        
# 5. Crie uma função que abra um arquivo, leia o conteúdo do mesmo e conte
# quantas palavras ele possui.

def contar_palavras_em_arquivo(local_nome_do_arquivo):
    print("\nExercício 6")
    
    try:
        with open(local_nome_do_arquivo, "r", encoding= "UTF-8") as arquivo:
            conteudo_arquivo= arquivo.read()
            
            palavras = conteudo_arquivo.split()
            print(f"O arquivo {local_nome_do_arquivo} tem: {len(palavras) }")
        
        
    except FileNotFoundError as e:
        print(f" O arquivo de origem {local_nome_do_arquivo} não foi encontrado")
        

#==============================
# --- Programa Principal --- 
#==============================

#Exercício 1:

local_arquivo = getDirectoryPath() + r"\tratamento_arquivos\arquivo\Dados_IBGE.txt"
ler_arquivo(local_arquivo)
print(f"Caminho ao diretoriio atual: {getDirectoryPath()}")

#Exercício 2:

pathfile = getDirectoryPath() + r"\tratamento_arquivos\arquivo\saida.txt"
escrever_em_arquivo(("Python", "Java", "Javascript", "C", "C++"), pathfile)
print("Linguagens de programação gravadas")


#Exercício 3:
print("\n Exercício 3")
pathfile = getDirectoryPath() + r"\tratamento_arquivos\arquivo\Dados_IBGE.txt"
contador = contar_linhas_arquivo(pathfile)
print(f"Número de linhas do arquivo Dados_IBGE.txt ")(contar_linhas_arquivo(pathfile))

#Exercício 4:
arquivo_origem = getDirectoryPath() + r"\tratamento_arquivos\arquivo\Dados_IBGE.txt"
arquivo_copia = getDirectoryPath() + r"\tratamento_arquivos\arquivo\Dados_IBGE copy.txt"

#Exercício 5:
arquivo_origem = getDirectoryPath() + r"\tratamento_arquivos\arquivo\Dados_IBGE.txt"
contar_palavras_em_arquivo(arquivo_origem)