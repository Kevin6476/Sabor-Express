import os

def exibir_nome_do_programa():
    print('==============================================================')
    print('\t█▀ ▄▀█ █▄▄ █▀█ █▀█   █▀▀ ▀▄▀ █▀█ █▀█ █▀▀ █▀ █▀')
    print('\t▄█ █▀█ █▄█ █▄█ █▀▄   ██▄ █░█ █▀▀ █▀▄ ██▄ ▄█ ▄█')
    print('==============================================================')

def listar_opcoes_menu():
    print('1. Cadastrar restaurante')
    print('2. Listar restaurantes')
    print('3. Ativar restaurante')
    print('4. Sair', end='\n\n')

def exit_application():
    os.system('cls')
    print('#Encerrando o programa...', end='\n\n')

def opcao_invalida():
    print('Opção inválida!', end='\n\n')
    input('Pressione uma tecla para continuar...')
    main()

def escolher_opcoes():
    try:
        opcao_escolhida = int(input('Escolha uma opção: '))

        if opcao_escolhida == 1:
            print('# Cadastro de restaurante.')
        elif opcao_escolhida == 2:
            print('# Listar restaurantes.')
        elif opcao_escolhida == 3:
            print('# Ativar restaurante.')
        elif opcao_escolhida == 4:
            exit_application()
        else:
            opcao_invalida()
    except:
        opcao_invalida()


def main():
    os.system('cls')
    exibir_nome_do_programa()
    listar_opcoes_menu()
    escolher_opcoes()


if __name__ == '__main__':
    main()