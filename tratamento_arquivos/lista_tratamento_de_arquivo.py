'''
1. Crie uma função que leia e exiba o conteúdo de um arquivo passado por
parâmetro. Caso o arquivo não exista, capture a exceção e exiba uma
mensagem de erro na tela. Teste a implementação, inclusive, fornecendo
arquivos que não existem.
'''
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
    


'''
2. Crie uma função que receba uma lista de strings e escreva cada item em
uma nova linha de um arquivo chamado conteudo_lista.txt.
'''






 

'''3. Crie uma função “contarLinhasArquivo”, que receba como parâmetro um
arquivo. Leia o arquivo e retorne o número total de linhas.'
'''



'''
4. Crie uma função que copie o conteúdo de um arquivo para outro. Ambos os
nomes dos arquivos devem ser passados como parâmetros.
'''



'''
5. Crie uma função que abra um arquivo, leia o conteúdo do mesmo e conte
quantas palavras ele possui.
'''





#==============================
# --- Programa Principal ---
#==============================

#Exercício 1:

local_arquivo = getDirectoryPath() + r"\tratamento_arquivos\arquivo\Dados_IBGE.txt"
ler_arquivo(local_arquivo)
print(f"Caminho ao diretoriio atual: {getDirectoryPath()}")

