# -*- coding: utf-8 -*-
"""
Exemplos de operações com listas e ranges.

Este script demonstra:
- Impressão formatada de ranges e listas com separadores condicionais.
- Criação de listas por compreensão (list comprehensions).
- Cálculo de soma e média de listas de números aleatórios.
- Loop de entrada do usuário para imprimir a tabuada de um número.

Observações:
- Mantida a lógica original do arquivo; foram adicionados comentários e docstrings para documentação.
"""

import random
import os
os.system('cls')

def imprimir_numeros(init=1, end=10):
    """Imprime números de 1 a 10 com separador."""
    numeros = range(init, end+1)
    print('\nNumeros de 1 á 10: ')
    for idx, num in enumerate(numeros, start=1):
        print(num, '|' if idx < len(numeros) else '', end=' ')
    print()

def imprimir_quatro_nomes():
    """Imprime uma lista de quatro nomes com separador."""
    quatro_nomes = ['Kevin', 'João', 'Maria', 'Zezinho']
    print('\nQuatro nomes: ')
    for idx, nome in enumerate(quatro_nomes, start=1):
        print(nome, ',' if idx < len(quatro_nomes) else '', end=' ')
    print()

def imprimir_anos():
    """Imprime uma lista de anos com separador."""
    lista_datas_anuais = [2000, 2010, 2020, 2025]
    print('\nLista com alguns anos: ')
    for idx, ano in enumerate(lista_datas_anuais, start=1):
        print(ano, '->' if idx < len(lista_datas_anuais) else '', end=' ')
    print()

def calcular_soma_impares():
    """Calcula e exibe a soma dos números ímpares de 1 a 10."""
    lista_impares = [impar for impar in range(1, 11) if impar % 2 != 0]
    expressao = ' + '.join(map(str, lista_impares))
    print(f'\n{expressao} = {sum(lista_impares)}')

def imprimir_numeros_decrescente():
    """Imprime números de 10 a 1 em ordem decrescente."""
    numeros_cresente = [n for n in range(10, 0, -1)]
    print('\n' + ' > '.join(map(str, numeros_cresente)))

def somar_numeros_aleatorios():
    """Soma 16 números aleatórios entre 1 e 100."""
    numeros_aleatorios = [random.randint(1, 100) for _ in range(16)]
    numeros_aleatorios.sort()
    print(f'\n{" + ".join(map(str, numeros_aleatorios))} = {sum(numeros_aleatorios)}')

def calcular_media_aleatorios():
    """Calcula a média de 10 números aleatórios entre 1 e 1000."""
    num_aleatorios = [random.randint(1, 1000) for _ in range(10)]
    print('\n{', ','.join(map(str, num_aleatorios)), '}')
    print(f'A média dos números acima é: {sum(num_aleatorios) / len(num_aleatorios):.2f}')

def fazer_tabuada():
    """Gera a tabuada de um número informado pelo usuário."""
    while True:
        try:
            tabuada = int(input('\nInforme um número para imprimir a tabuada: '))
            print()
            for i in range(1, 11):
                print(f'{tabuada} x {i} = {tabuada * i}')
            break
        except (ValueError, KeyboardInterrupt, EOFError):
            input('Número inválido! Pressione <enter> para continuar.')
        except Exception:
            print('Ocorreu um erro inesperado!')
            break

def menu():
    """Exibe o menu principal e gerencia as escolhas do usuário."""
    opcoes = {
        1: ('Imprimir números de 1 a 10', imprimir_numeros),
        2: ('Imprimir quatro nomes', imprimir_quatro_nomes),
        3: ('Imprimir anos', imprimir_anos),
        4: ('Calcular soma dos ímpares', calcular_soma_impares),
        5: ('Imprimir números decrescentes', imprimir_numeros_decrescente),
        6: ('Somar números aleatórios', somar_numeros_aleatorios),
        7: ('Calcular média de aleatórios', calcular_media_aleatorios),
        8: ('Fazer tabuada', fazer_tabuada),
        0: ('Sair', None)
    }

    while True:
        print('\n=== Menu de Operações ===')
        for key, (descricao, _) in opcoes.items():
            print(f'{key}. {descricao}')

        try:
            escolha = int(input('\nEscolha uma opção: '))
            if escolha == 0:
                print('Programa encerrado!')
                break
            elif escolha in opcoes:
                opcoes[escolha][1]()
            else:
                print('Opção inválida!')
        except ValueError:
            print('Por favor, digite um número válido!')
        input('\nPressione Enter para continuar...')

if __name__ == '__main__':
    menu()