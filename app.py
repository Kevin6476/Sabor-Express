# python
"""
Módulo `app.py`
Aplicação de console para gerenciar uma lista simples de restaurantes:
- exibe título e opções de menu
- permite cadastrar, listar e trocar status de restaurantes
- usa um dicionário `global_vars` como armazenamento global temporário

Observações:
- Funções utilitárias `pegar_*` encapsulam o acesso a `global_vars`.
- Interações com o usuário são feitas via `input()` e saídas via `print()`.
"""

import os
import sys
from typing import Final

# --- Constantes usadas como chaves e configurações de exibição ---
ID: Final = 'Id'
DESC: Final = 'Desc'
CATEGORIA: Final = 'Categoria'
STATUS: Final = 'Status'
TAMANHO_LINHA: Final = 68
ESPACO_COLUNAS: Final = 25

# Armazenamento global simulado (lista de restaurantes e opções de menu)
# - usado apenas em memória durante a execução do programa
global_vars = {
    'separador': TAMANHO_LINHA,
    'restaurantes': sorted([
        { ID: 1, DESC: 'Italiana', CATEGORIA: 'Pizzaria', STATUS: True },
        { ID: 2, DESC: 'Outback', CATEGORIA: 'Restaurante', STATUS: True },
        { ID: 3, DESC: 'Mc Donalds', CATEGORIA: 'Fast Food', STATUS: False },
        { ID: 4, DESC: 'Coco Bambu', CATEGORIA: 'Restaurante', STATUS: True },
        { ID: 5, DESC: 'Mineiro', CATEGORIA: 'Restaurante', STATUS: False },
        { ID: 6, DESC: 'Churrascaria', CATEGORIA: 'Rodizío', STATUS: False },
        { ID: 7, DESC: 'Shell Café', CATEGORIA: 'Conveniência', STATUS: False },
    ], key=lambda x: x[DESC]),
    'opcoes_menu_princ': (
        {ID: 1, DESC: 'Cadastrar Restaurantes'},
        {ID: 2, DESC: 'Listar restaurantes'},
        {ID: 3, DESC: 'Trocar Status do restaurante'},
        # { ID: 4, DESC: 'Sair' }
    )
}


def pegar_linha():
    """
    Retorna uma linha repetida (string) usada como separador visual.
    Usa o valor em `global_vars['separador']` se presente, caso contrário `TAMANHO_LINHA`.
    """
    return '*' * global_vars.get('separador', TAMANHO_LINHA)


def pegar_restaurantes():
    """
    Retorna a lista de restaurantes do armazenamento global.
    Retorna lista vazia se a chave não existir.
    """
    return global_vars.get('restaurantes', [])


def pegar_opcoes_menu_princ():
    """
    Retorna a sequência de opções do menu principal.
    Retorna lista/tupla vazia se a chave não existir.
    """
    return global_vars.get('opcoes_menu_princ', [])


def main():
    """
    Ponto de entrada principal da aplicação.
    Exibe título, lista de opções e inicia o loop de seleção.
    """
    exibir_titulo_aplicacao()
    listar_opcoes_menu()
    escolher_opcoes()


def exibir_titulo_aplicacao():
    """
    Limpa a tela (CMD/PowerShell via `cls`) e imprime o cabeçalho da aplicação.
    Usa `pegar_linha()` para gerar bordas visuais.
    """
    os.system('cls')  # limpa o console no Windows
    linha = pegar_linha()
    print(linha)
    # Arte ASCII do título (mantida conforme original)
    print('\t █▀ ▄▀█ █▄▄ █▀█ █▀█   █▀▀ ▀▄▀ █▀█ █▀█ █▀▀ █▀ █▀')
    print('\t ▄█ █▀█ █▄█ █▄█ █▀▄   ██▄ █░█ █▀▀ █▀▄ ██▄ ▄█ ▄█')
    print(linha)


def exibir_subtitulo(acao_atual):
    """
    Exibe um subtítulo com a ação atual seguido de uma linha separadora.
    Parâmetros:
    - acao_atual (str): texto descritivo do contexto atual.
    """
    print(f'# {acao_atual}')
    linha = pegar_linha()
    print(linha + '\n')


def listar_opcoes_menu():
    """
    Exibe as opções do menu principal.
    - Obtém as opções via `pegar_opcoes_menu_princ()`.
    - Exibe uma mensagem alternativa caso não haja opções.
    """
    opcoes = pegar_opcoes_menu_princ()
    qtd_opcoes = len(opcoes)
    exibir_subtitulo('Selecione alguma opção abaixo:' if qtd_opcoes >= 1 else 'Nenhuma opção disponivel para escolha')
    # Constrói e imprime a lista de opções no formato "Id - Descrição"
    print('\n'.join(f'{op.get(ID)} - {op.get(DESC)}' for op in opcoes), end='\n\n')


def voltar_menu_principal(msg=''):
    """
    Aguarda uma entrada do usuário e retorna ao menu principal.
    - msg: mensagem exibida no `input()` antes de voltar.
    """
    input(msg if len(msg) > 0 else 'Pressione uma tecla para retornar ao menu principal...')
    exibir_titulo_aplicacao()
    listar_opcoes_menu()


def escolher_opcoes():
    """
    Loop principal de leitura da opção escolhida pelo usuário.
    - Valida se a opção existe nas `opcoes_menu_princ`.
    - Chama a função correspondente (cadastrar, listar, trocar status, encerrar).
    - Em caso de erro de entrada, exibe mensagem de erro e volta ao menu.
    """
    opcoes = pegar_opcoes_menu_princ()
    qtd_opcoes = len(opcoes)

    if not qtd_opcoes:
        return

    msg_err: str = f'\nOpção inválida! Selecione um número entre 1 e {qtd_opcoes}.'
    while True:
        try:
            opcao_menu = int(input('Escolha uma opção de menu: ').strip())
            # Verifica existência da opção selecionada
            existe_opcao = next((opcao for opcao in opcoes if opcao.get(ID) == opcao_menu), None)

            if not existe_opcao:
                voltar_menu_principal(msg_err)
                continue

            # Roteamento simples por número de opção
            match opcao_menu:
                case 1:
                    cadastrar_restaurante()
                case 2:
                    listar_restaurantes()
                case 3:
                    trocar_status_restaurante()
                case 4:
                    encerrar_aplicacao()
                case _:
                    voltar_menu_principal(msg_err)
        except (ValueError, EOFError):
            # Entrada inválida: retorna ao menu com mensagem de erro
            voltar_menu_principal(msg_err)
        except KeyboardInterrupt:
            # Interrupção pelo usuário (Ctrl+C): exibe título e mensagem e sai do loop
            exibir_escolha_menu('Operação cancelada pelo usuário!')
            break


def cadastrar_restaurante():
    """
    Processo interativo para cadastrar um novo restaurante.
    - Solicita nome e categoria (validação de não vazio).
    - Atribui novo ID baseado no maior ID existente ou 1 se lista vazia.
    - Insere e ordena a lista de restaurantes por nome.
    - Retorna ao menu principal após concluir.
    """
    exibir_escolha_menu('Cadastrar novo restaurante')

    nome = None
    categoria = None
    try:
        # Solicita nome (com validação de não vazio)
        while True:
            nome = input('Informe o nome do novo restaurante: ').strip().title()
            print()
            if not nome:
                exibir_escolha_menu('Cadastrar novo restaurante', 'Nome de restaurante inválido!')
            else:
                break

        # Solicita categoria (com validação de não vazio)
        while True:
            categoria = input(f'Informe a categoria do restaurante {nome}: ').strip().title()
            print()
            if not categoria:
                exibir_escolha_menu('Cadastrar novo restaurante', 'Categoria não permitida!')
            else:
                break
    except KeyboardInterrupt:
        # Permite cancelar o cadastro com Ctrl+C sem encerrar a aplicação
        voltar_menu_principal('\nOperação cancelada! Aperte uma tecla para voltar ao menu principal.')
        return

    l_restaurantes = pegar_restaurantes()

    # Gera novo ID de forma segura (1 se lista vazia)
    novo_id = 1
    if l_restaurantes:
        novo_id = max(l_restaurantes, key=lambda res: res.get(ID)).get(ID) + 1

    # Insere novo registro (mantém estrutura de chaves usadas no projeto)
    l_restaurantes.append({
        ID: novo_id,
        DESC: nome,
        CATEGORIA: categoria
    })
    # Ordena por nome (campo `Desc`)
    l_restaurantes.sort(key=lambda r: r.get(DESC))
    print(f'{categoria} {nome} cadastrado com sucesso!')
    voltar_menu_principal()


def listar_restaurantes():
    """
    Exibe a listagem formatada de restaurantes:
    - Cabeçalho com colunas: Nome Restaurante, Categoria, Status, Identificador
    - Para cada restaurante imprime uma linha com os campos formatados.
    - Se não houver restaurantes, exibe mensagem apropriada.
    Ao final, volta ao menu principal.
    """
    exibir_escolha_menu('Listar restaurantes')
    l_restaurantes = pegar_restaurantes()

    if not l_restaurantes:
        # Mensagem quando a lista está vazia
        print('Nenhum restaurante cadastrado até o momento.\n')
    else:
        # Constroi cabeçalho com alinhamento baseado em `ESPACO_COLUNAS`
        header = (
                "Nome Restaurante".ljust(ESPACO_COLUNAS) + "| " +
                "Categoria".ljust(ESPACO_COLUNAS) + "| " +
                "Status".ljust(ESPACO_COLUNAS) + "| " +
                "Identificador".ljust(ESPACO_COLUNAS) + "|"
        )
        linha = '-' * len(header)
        print(linha)
        print(header)
        print(linha)
        # Imprime cada restaurante formatado em colunas
        for idx, restaurante in enumerate(l_restaurantes, start=1):
            nome = restaurante.get(DESC).ljust(ESPACO_COLUNAS)
            categoria = restaurante.get(CATEGORIA).ljust(ESPACO_COLUNAS)
            status = 'Ativo' if restaurante.get(STATUS) else 'Inativo'
            print(
                f'{nome}| {categoria}| {status.ljust(ESPACO_COLUNAS)}| {str(restaurante.get(ID)).ljust(ESPACO_COLUNAS)}|')
        print(linha)

    print()
    voltar_menu_principal()


def trocar_status_restaurante():
    """
    Solicita ao usuário o identificador do restaurante e alterna seu STATUS booleano.
    - Valida entrada inteira e existência do ID na lista.
    - Em caso de erro, exibe mensagem e permite nova tentativa.
    """
    exibir_escolha_menu('Ativar restaurante')
    restaurante = None

    # Loop para validar o identificador informado
    while True:
        try:
            id = int(input('Informe identificador do restaurante: '))
            restaurante = next((res for res in pegar_restaurantes() if res.get(ID) == id), None)
            if not restaurante:
                exibir_escolha_menu('Ativar restaurante', f'Restaurante com o Identificador {id} não encontrado!')
                continue
            break
        except ValueError:
            # Entrada não é um inteiro válido
            exibir_escolha_menu('Ativar restaurante', f'Identificador não permitido, passe um numero inteiro!')
            continue
        except KeyboardInterrupt:
            # Permite cancelar e voltar ao menu sem encerrar a aplicação
            voltar_menu_principal('\nOperação cancelada! Aperte uma tecla para voltar ao menu principal.')
            return

    # Alterna o status booleano do restaurante
    restaurante[STATUS] = not restaurante.get(STATUS)
    # Para evitar f-string inválida, precomputamos a string do status
    status_str = 'Ativo' if restaurante.get(STATUS) else 'Inativo'
    # Mensagem de confirmação para o usuário
    print(f"{restaurante.get(CATEGORIA)} {restaurante.get(DESC)} teve o status alterado para {status_str} com sucesso!")
    voltar_menu_principal()


def encerrar_aplicacao():
    """
    Exibe título de encerramento e finaliza o processo com `sys.exit()`.
    """
    exibir_escolha_menu('Encerrando o programa')
    sys.exit()


def exibir_escolha_menu(title, info=None):
    """
    Helper para exibir o título da aplicação seguido do subtítulo de uma ação específica.
    - title: texto do subtítulo a ser exibido.
    - info: mensagem opcional que será exibida antes do título (útil para erros/avisos).
    """
    # Exibe mensagem auxiliar (se fornecida) e o menu correspondente
    exibir_mensagem(info) if info else None
    exibir_titulo_aplicacao()
    exibir_subtitulo(title)


def exibir_mensagem(msg):
    """
    Exibe uma mensagem e aguarda que o usuário pressione uma tecla para continuar.
    - msg: texto a ser exibido (geralmente uma mensagem de erro ou confirmação).
    """
    print(msg)
    input('Pressione alguma tecla para continuar ...\n')


if __name__ == '__main__':
    main()
