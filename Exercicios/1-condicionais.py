import sys


def pegar_numero(msg, positivo=True, decimal=False):
    """
    Solicita e valida entrada numérica do usuário.

    Args:
        msg (str): Mensagem de prompt para o usuário
        positivo (bool): Se True, aceita apenas números positivos
        decimal (bool): Se True, aceita números decimais, senão apenas inteiros

    Returns:
        float|int: Número validado de acordo com os parâmetros
    """
    while True:
        try:
            num = float(input(msg)) if decimal else int(input(msg))
            if positivo and num < 0:
                print('Valor não pode ser negativo')
                continue
            return num
        except ValueError:
            print('Digite um número válido')
            input('Pressione Enter para continuar...')

def comparar_vendas():
    """
    Compara a quantidade de maçãs e bananas vendidas e indica qual vendeu mais.
    """
    macas = pegar_numero('Quantidade de maçãs: ', positivo=True)
    bananas = pegar_numero('Quantidade de bananas: ', positivo=True)

    if bananas > macas:
        print('Mais bananas vendidas')
    elif macas > bananas:
        print('Mais maçãs vendidas')
    else:
        print('Quantidades iguais')


def calcular_tempo():
    """
    Calcula o tempo total de três atividades em dias.
    Valida que os tempos não sejam negativos.
    """
    while True:
        tempos = [
            pegar_numero('Dias atividade A: '),
            pegar_numero('Dias atividade B: '),
            pegar_numero('Dias atividade C: ')
        ]
        if any(t < 0 for t in tempos):
            print('Tempo não pode ser negativo')
            continue
        print(f'Total: {sum(tempos)} dias')
        break


def controlar_temp():
    """
    Avalia uma temperatura em Celsius e indica se deve aquecer (<5°C),
    resfriar (>25°C) ou manter a temperatura.
    """
    temp = pegar_numero('Temperatura (°C): ', decimal=True)
    if temp < 5:
        print('Aquecer')
    elif temp > 25:
        print('Resfriar')
    else:
        print('Temperatura OK')

def calcular_imc():
    """
    Calcula o IMC (Índice de Massa Corporal) e classifica em:
    - Abaixo do peso: < 18.5
    - Peso normal: 18.5-24.9
    - Sobrepeso: >= 25
    """
    peso = pegar_numero('Peso (kg): ', positivo=True, decimal=True)
    altura = pegar_numero('Altura (m): ', positivo=True, decimal=True)
    imc = peso / altura ** 2
    print(f'IMC: {imc:.1f}')
    if imc < 18.5:
        print('Abaixo do peso')
    elif imc >= 25:
        print('Sobrepeso')
    else:
        print('Peso normal')

def verificar_orcamento():
    """
    Verifica se os gastos excedem o limite de R$ 3000.
    """
    gastos = pegar_numero('Gastos R$: ', positivo=True, decimal=True)
    if gastos > 3000:
        print('Orçamento excedido')
    else:
        print('Dentro do orçamento')

def verificar_horario():
    """
    Verifica se um estabelecimento está aberto com base no horário (0-23).
    Horário de funcionamento: 8h às 18h.
    """
    while True:
        hora = pegar_numero('Hora (0-23): ')
        if not 0 <= hora <= 23:
            print('Hora inválida')
            continue
        print('Aberto' if 8 <= hora <= 18 else 'Fechado')
        break

def calcular_media():
    """
    Calcula a média de três notas e classifica em:
    - Reprovado: < 5
    - Recuperação: 5-6.9
    - Aprovado: 7-8.9
    - Aprovado com louvor: >= 9
    """
    while True:
        notas = [pegar_numero(f'Nota {i + 1}: ', positivo=True, decimal=True) for i in range(3)]
        media = sum(notas) / 3
        if media > 10:
            print('Notas inválidas')
            continue
        print(f'Média: {media:.1f}')
        if media < 5:
            print('Reprovado')
        elif media < 7:
            print('Recuperação')
        elif media < 9:
            print('Aprovado')
        else:
            print('Aprovado com louvor')
        break

def calcular_pedagio():
    """
    Calcula o valor do pedágio baseado na distância:
    - Até 100km: R$ 10
    - 101-200km: R$ 20
    - Acima de 200km: R$ 30
    """
    km = pegar_numero('Distância (km): ', positivo=True, decimal=True)
    if km <= 100:
        valor = 10
    elif km <= 200:
        valor = 20
    else:
        valor = 30
    print(f'Pedágio: R$ {valor:.2f}')


def par_impar():
    """
    Determina se um número é par ou ímpar.
    """
    num = pegar_numero('Número: ', positivo=True)
    print('Par' if num % 2 == 0 else 'Ímpar')

def analisar_emprestimo():
    """
    Analisa aprovação de empréstimo baseado em:
    - Renda mínima: R$ 2000
    - Parcela máxima: 30% da renda
    """
    renda = pegar_numero('Renda R$: ', positivo=True, decimal=True)
    parcela = pegar_numero('Parcela R$: ', positivo=True, decimal=True)
    if renda > 2000 and parcela <= renda * 0.3:
        print('Aprovado')
    else:
        print('Negado')


def menu():
    """
    Exibe menu interativo com opções de operações.
    Permite sair com opção 0 ou Ctrl+C.
    """
    opcoes = {
        1: ('Comparar vendas', comparar_vendas),
        2: ('Calcular tempo', calcular_tempo),
        3: ('Controlar temperatura', controlar_temp),
        4: ('Calcular IMC', calcular_imc),
        5: ('Verificar orçamento', verificar_orcamento),
        6: ('Verificar horário', verificar_horario),
        7: ('Calcular média', calcular_media),
        8: ('Calcular pedágio', calcular_pedagio),
        9: ('Par ou ímpar', par_impar),
        10: ('Analisar empréstimo', analisar_emprestimo),
        0: ('Sair', sys.exit)
    }

    while True:
        print('\n=== MENU ===')
        for num, (desc, _) in opcoes.items():
            print(f'{num}. {desc}')
        try:
            op = pegar_numero('Opção: ')
            if op in opcoes:
                opcoes[op][1]()
            else:
                print('Opção inválida')
        except KeyboardInterrupt:
            print('\nPrograma encerrado')
            sys.exit()

if __name__ == '__main__':
    menu()