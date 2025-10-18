
numeros = range(1, 11)
print('\n--------------------------')
print('Numeros de 1 á 10: ')
for idx, num in enumerate(numeros, start=1):
    print(num, '|' if idx < len(numeros) else '', end=' ')

print('\n--------------------------')
quatro_nomes = ['Kevin', 'João', 'Maria', 'Zezinho']
print('Quatro nomes: ')
for idx, nome in enumerate(quatro_nomes, start=1):
    print(nome, ',' if idx < len(quatro_nomes) else '', end=' ')


print('\n--------------------------')
lista_datas_anuais = [2000, 2010, 2020, 2025]
print('Lista com alguns anos: ')
for idx, ano in enumerate(lista_datas_anuais, start=1):
    print(ano, '->' if idx < len(lista_datas_anuais) else '', end=' ')


print('\n--------------------------')
print('Calculando soma de numeros impares de 1 á 10 ... ')
lista_impares = [impar for impar in range(1, 11) if impar % 2 != 0]
expressao = ' + '.join(map(str, lista_impares))
print(f'{ expressao } = { sum(lista_impares) }')


print('\n--------------------------')
print('Imprimindo números de 1 á 10 em ordem decresente ... ')
numeros_cresente = [n for n in range(10, 0, -1)]
print(' > '.join(map(str, numeros_cresente)))


print('\n--------------------------')
print('Fazendo soma de uma lista com 15 números aleatórios de 1 a 100.')
import random
numeros_aleatorios = [random.randint(1, 100) for _ in range(16)]
numeros_aleatorios.sort()
print(' + '.join(map(str, numeros_aleatorios)), ' = ', sum(numeros_aleatorios))





print('\n--------------------------')
print('Calculando a média dos valores de uma lista com 10 números aleatóros de 1 a 1000.')
num_aleatorios = [random.randint(1, 1000) for _ in range(10) ]
print('{', ','.join(map(str, num_aleatorios)), '}')
print('A média dos números acima é: {:.2f}'.format(sum(num_aleatorios) / len(num_aleatorios)))



print('\n--------------------------')
print('Pegando um numero com o usuário e fazendo a tabuada do 1 ao 10 do numero ... ')
tabudada = None
while True:
    try:
        tabudada = int(input('Informe um número para imprimir a tabuada: '))
        break
    except (ValueError, KeyboardInterrupt, EOFError):
        input('Número inválido! Pressione <enter> para continuar.')
        continue
    except Exception as e:
        print('Ocorreu um erro inesperado!')

for i, _ in enumerate(range(10), start=1):
    print('{} x {} = {}'.format(tabudada, i, tabudada * i))
