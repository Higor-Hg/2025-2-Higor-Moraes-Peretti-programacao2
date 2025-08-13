menu = '''\nMenu de Opções:
            1- Cadastrar evento
            2- Excluir evento
            3- Cadastrar aluno
            4- Excluir aluno
            5- Matricular aluno
                        
            Digite Sair para finalizar o programa\n'''

def exibir_menu():
    print(menu)
    print("\n")


def escolha_do_menu(escolha):
    if escolha == '1':
        print("Foi selecionada a opção \"Cadastrar evento\" ")

    elif escolha == '2':
        print("Foi selecionada a opção \"Excluir evento\" ")

    elif escolha == '3':
        print("Foi selecionada a opção \"Cadastrar aluno\" ")

    elif escolha == '4':
        print("Foi selecionada a opção \"excluir evento\" ")

    elif escolha == '5':
        print("Foi selecionada a opção \"Matricular evento\" ")

    elif escolha.lower() == 'sair':
        print("Programa finalizado.")
    
    else:
        print("Opção Inválida.")


exibir_menu()

opcao = input('Digite uma opção do menu: ')

escolha_do_menu(opcao)