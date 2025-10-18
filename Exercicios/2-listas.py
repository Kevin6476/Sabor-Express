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

# Gera um range de 1 a 10 (valor final não incluído em range, por isso 11)
numeros = range(1, 11)
print('\n--------------------------')
print('Numeros de 1 á 10: ')
# Usa enumerate para obter o índice e decidir o separador (barra vertical) até o último elemento
for idx, num in enumerate(numeros, start=1):
    print(num, '|' if idx < len(numeros) else '', end=' ')


print('\n--------------------------')
# Lista com quatro nomes
quatro_nomes = ['Kevin', 'João', 'Maria', 'Zezinho']
print('Quatro nomes: ')
# Imprime cada nome separado por vírgula, sem adicionar vírgula após o último elemento
for idx, nome in enumerate(quatro_nomes, start=1):
    print(nome, ',' if idx < len(quatro_nomes) else '', end=' ')


print('\n--------------------------')
# Lista com alguns anos
lista_datas_anuais = [2000, 2010, 2020, 2025]
print('Lista com alguns anos: ')
# Imprime os anos separados por '->' até o último elemento
for idx, ano in enumerate(lista_datas_anuais, start=1):
    print(ano, '->' if idx < len(lista_datas_anuais) else '', end=' ')


print('\n--------------------------')
print('Calculando soma de numeros impares de 1 á 10 ... ')
# Gera uma lista com os números ímpares entre 1 e 10 usando list comprehension
lista_impares = [impar for impar in range(1, 11) if impar % 2 != 0]
# Cria uma expressão textual do tipo "1 + 3 + 5 + ..."
expressao = ' + '.join(map(str, lista_impares))
# Imprime a expressão e o resultado da soma
print(f'{ expressao } = { sum(lista_impares) }')


print('\n--------------------------')
print('Imprimindo números de 1 á 10 em ordem decresente ... ')
# Gera lista em ordem decrescente de 10 até 1
numeros_cresente = [n for n in range(10, 0, -1)]
# Junta os valores usando ' > ' como separador
print(' > '.join(map(str, numeros_cresente)))


print('\n--------------------------')
print('Fazendo soma de uma lista com 15 números aleatórios de 1 a 100.')
import random
# Gera uma lista de números aleatórios entre 1 e 100. Note: o código original usa 16 elementos.
numeros_aleatorios = [random.randint(1, 100) for _ in range(16)]
# Ordena a lista antes de imprimir
numeros_aleatorios.sort()
# Imprime todos os números separados por ' + ' e a soma total
print(' + '.join(map(str, numeros_aleatorios)), ' = ', sum(numeros_aleatorios))

print('\n--------------------------')
print('Calculando a média dos valores de uma lista com 10 números aleatóros de 1 a 1000.')
# Gera 10 números aleatórios entre 1 e 1000
num_aleatorios = [random.randint(1, 1000) for _ in range(10) ]
# Imprime a lista no formato {a,b,c,...}
print('{', ','.join(map(str, num_aleatorios)), '}')
# Calcula e imprime a média com duas casas decimais
print('A média dos números acima é: {:.2f}'.format(sum(num_aleatorios) / len(num_aleatorios)))



print('\n--------------------------')
print('Pegando um numero com o usuário e fazendo a tabuada do 1 ao 10 do numero ... ')
# Variável que receberá o número informado pelo usuário para a tabuada
tabudada = None  # nota: nome da variável segue o original (possível typo: "tabudada" em vez de "tabuada")
# Loop que solicita a entrada do usuário até receber um inteiro válido
while True:
    try:
        tabudada = int(input('Informe um número para imprimir a tabuada: '))
        break
    except (ValueError, KeyboardInterrupt, EOFError):
        # Em caso de entrada inválida, aguarda que o usuário pressione Enter e tenta novamente
        input('Número inválido! Pressione <enter> para continuar.')
        continue
    except Exception as e:
        # Captura qualquer outro erro inesperado e informa ao usuário
        print('Ocorreu um erro inesperado!')

# Imprime a tabuada de 1 a 10 usando enumerate apenas para contar (poderia usar range também)
for i, _ in enumerate(range(10), start=1):
    print('{} x {} = {}'.format(tabudada, i, tabudada * i))