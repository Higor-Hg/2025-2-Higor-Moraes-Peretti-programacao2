'''
1. Crie uma função que leia e exiba o conteúdo de um arquivo passado por
parâmetro. Caso o arquivo não exista, capture a exceção e exiba uma
mensagem de erro na tela. Teste a implementação, inclusive, fornecendo
arquivos que não existem.
'''

def ler_e_exibir_arquivo(nome_arquivo: str):
    """
    Lê e exibe o conteúdo de um arquivo.

    Args:
        nome_arquivo: O caminho para o arquivo a ser lido.
    """
    try:
        # Abre o arquivo em modo de leitura ('r') com codificação UTF-8
        with open(nome_arquivo, 'r', encoding='utf-8') as arquivo:
            conteudo = arquivo.read()
            print(f"\n--- Conteúdo do arquivo '{nome_arquivo}' ---")
            print(conteudo)
            print(f"--- Fim do conteúdo do arquivo '{nome_arquivo}' ---\n")
    except FileNotFoundError:
        # Captura a exceção se o arquivo não for encontrado
        print(f"\nERRO: O arquivo '{nome_arquivo}' não foi encontrado.\n")
    except Exception as e:
        # Captura outras possíveis exceções (permissão, etc.)
        print(f"\nOcorreu um erro inesperado ao tentar ler o arquivo '{nome_arquivo}': {e}\n")




















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






# --- Programa Principal ---



    

