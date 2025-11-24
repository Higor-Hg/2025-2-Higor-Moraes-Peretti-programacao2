
'Modos de abertura de arquivo'

'--Modo Descrição--'

'r' #Leitura (padrão)
'w' #Escrita (sobrescreve)
'a' #Acrescentar ao Final   
'b' #Binário         
'x' #Cria novo Arquivo         
'+' #Leitura e escrita 

'--Métodos de leitura--'
 

with open('exemplo.txt', 'r', encoding='utf-8') as f:
    conteudo = f.read() #Lê todo conteùdo
    
with open('exemplo.txt', 'r', encoding='utf-8') as f:
    linhas = f.readlines() #Lê linha por linha em lista 
    
f.seek(0)#Move o cursor para o início
    
with open('exemplo.txt', 'r', encoding='utf-8') as f:
    linhas = f.readline() #Lê uma linha por vez, usra laço de repetição
    
#Escreva um texto

#O modo de abretura "w" trunca o arquivo, ou seja, apaga o arquivo, caso ele 
#exista, senão cria um novo arquivo e insere o conteúdo.

with open('exemplo.txt', 'r', encoding='utf-8') as f:
    
    f.write("Primeira linha.\n")
        
    f.write("Segunda linha.\n")
    
'Métodos de Escrita'    

#Acrescentando o conteúdo

#O modo de abertura "a" adiciona o conteúdo no final do arquivo, caso ele
#exista, senão cria um novo arquivo e insere o conteúdo.

with open('saída.txt', 'a' ,enconding='utf-8') as f:
    
   f.write("Nova linha adicionada.\n") 
   
'Arquivos- estrutura de repetição'

with open('log.txt', 'r' ,enconding='utf-8') as f:

    for linha in f:
        
        print(linha.strip()) # strip remove\n
        
'Tratamento de Excecões - try-except'      
    
try:
  with open('log.txt', 'r' ,enconding='utf-8') as f:
      conteudo = f.read()
      
except FileNotFoundError:
    print("Arquivo não encontrado") 
    
except PermissionError:
    print("Permissão negada para abrir  arquivo.")
    
except Exception as e:
    print(f"Ocorreu um erro inesperado: {e}")               
    
          

       