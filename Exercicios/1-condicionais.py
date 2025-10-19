# python
"""
Módulo `Exercicios/1-condicionais.py`

Coleção de pequenas funções demonstrando condicionais e interações com o usuário.
Cada função implementa uma tarefa específica (comparação de vendas, cálculo de IMC,
verificação de horário, etc.). Há uma função `menu_principal` que expõe essas
funcionalidades via um menu interativo no terminal.

Observações:
- As entradas são obtidas via `input` e validadas por `pegar_numero`.
- O programa trata `KeyboardInterrupt` para encerrar com segurança.
"""

import sys

def pegar_numero(questao, aceita_negativo=True, decimal=False):
    """
    Lê um número do usuário com repetição até obter um valor válido.

    Parâmetros:
    - questao (str): Texto exibido para solicitar a entrada ao usuário.
    - aceita_negativo (bool): Se False, não permite números negativos.
    - decimal (bool): Se True, interpreta a entrada como float; caso contrário como int.

    Retorno:
    - int | float: Valor numérico inserido pelo usuário (tipo depende de `decimal`).

    Comportamento:
    - Em caso de entrada inválida, exibe mensagem e solicita novamente.
    - Não trata explicitamente `KeyboardInterrupt`; este é propagado para o chamador.
    """
    while True:
        try:
            qtd = int(input(questao)) if not decimal else float(input(questao))
            if not aceita_negativo and qtd < 0:
                print('A quantidade não pode ser negativa. Tente novamente.')
                continue
            return qtd
        except ValueError:
            print(f'Por favor, insira um número {"Decimal" if decimal else "Inteiro"} válido!')
            input('Pressione Enter para tentar novamente...\n')
            continue


def comparar_vendas():
    """
    Compara quantidades vendidas de maçãs e bananas e exibe qual foi vendida em maior quantidade
    ou se houve empate.

    Usa `pegar_numero` para leitura das quantidades (inteiras, não negativas).
    """
    try:
        macas_qtd = pegar_numero('Digite a quantidade de maçãs vendidas: ', aceita_negativo=False)
        bananas_qtd = pegar_numero('Digite a quantidade de bananas vendidas: ', aceita_negativo=False)

        if bananas_qtd > macas_qtd:
            print('Mais bananas foram vendidas.')
        elif macas_qtd > bananas_qtd:
            print('Mais maçãs foram vendidas.')
        else:
            print('A quantidade de maçãs e bananas vendidas foi igual.')
    except KeyboardInterrupt:
        raise


def calcular_tempo_atividades():
    """
    Solicita a quantidade de dias de três atividades e exibe o tempo total.

    Valida que nenhuma quantidade seja negativa; em caso de erro solicita reentrada.
    """
    while True:
        atividade_a = pegar_numero('Digite a quantidade de dias para a atividade A: ')
        atividade_b = pegar_numero('Digite a quantidade de dias para a atividade B: ')
        atividade_c = pegar_numero('Digite a quantidade de dias para a atividade C: ')

        if atividade_a < 0 or atividade_b < 0 or atividade_c < 0:
            input('A quantidade de dias não pode ser negativa. Pressione Enter para tentar novamente...\n')
            continue
        print(f'O tempo total gasto nas atividades foi de {atividade_a + atividade_b + atividade_c} dias.')
        break


def controlar_temperatura():
    """
    Sugere ajuste do ar-condicionado com base na temperatura em Celsius.

    Regras:
    - < 5: aquecer
    - > 25: resfriar
    - caso contrário: desligado / agradável
    """
    temperatura = pegar_numero('Digite a temperatura atual em Celsius: ', decimal=True)
    if temperatura < 5:
        print('Ajuste o ar-condicionado para aquecer.')
    elif temperatura > 25:
        print('Ajuste o ar-condicionado para resfriar.')
    else:
        print('A temperatura está agradável. Mantenha o ar-condicionado desligado.')


def calcular_imc():
    """
    Calcula o Índice de Massa Corporal (IMC) com base em peso (kg) e altura (m)
    e exibe a classificação correspondente.

    - peso: float, não negativo
    - altura: float, não negativo (não há validação explícita para altura zero)
    """
    peso = pegar_numero('Digite seu peso (kg): ', decimal=True, aceita_negativo=False)
    altura = pegar_numero('Digite sua altura (m): ', decimal=True, aceita_negativo=False)
    imc = peso / (altura ** 2)
    print(f'Seu IMC é {imc:.2f}. ', end='')

    if imc < 18.5:
        print('Você está abaixo do peso.')
    elif imc >= 25:
        print('Você está com sobrepeso.')
    else:
        print('Você está com o peso normal.')


def verificar_orcamento():
    """
    Compara as despesas mensais com um orçamento fixo e informa se o orçamento foi excedido.

    - orcamento é fixo em 3000.0
    - gastos lidos como float não-negativo
    """
    orcamento = 3000.0
    gastos = pegar_numero('Digite o total de despesas do mês: R$ ', decimal=True, aceita_negativo=False)

    if gastos > orcamento:
        print('Atenção! Você excedeu o orçamento deste mês.')
    else:
        print('Parabéns! Você está dentro do orçamento deste mês.')


def verificar_horario():
    """
    Verifica se o horário informado (hora inteira no formato 24h) está dentro do
    horário de funcionamento (8 às 18 horas) e informa se está aberto ou fechado.

    Valida que a hora esteja entre 0 e 23.
    """
    while True:
        hora = pegar_numero('Digite a hora atual (Formato 24 horas): ')
        if hora < 0 or hora > 23:
            input('Hora inválida. Por favor, insira uma hora entre 0 e 23.\nPressione Enter para tentar novamente...\n')
            continue

        if 8 <= hora <= 18:
            print('Estamos abertos! Bem-vindo ao nosso sistema de vendas.')
        else:
            print('Desculpe, estamos fechados no momento. Nosso horário de funcionamento é das 8h às 18h.')
        break


def calcular_media():
    """
    Calcula a média de três notas fornecidas e imprime o resultado com a respectiva classificação.

    Classes:
    - 0 <= média < 5: reprovado
    - 5 <= média < 7: recuperação
    - 7 <= média < 9: aprovado
    - 9 <= média <= 10: aprovado com louvor

    Observação: Se a média for maior que 10, considera-se inválida e solicita nova entrada.
    """
    while True:
        notas = [
            pegar_numero('Digite sua primeira nota: ', decimal=True, aceita_negativo=False),
            pegar_numero('Digite sua segunda nota: ', decimal=True, aceita_negativo=False),
            pegar_numero('Digite sua terceira nota: ', decimal=True, aceita_negativo=False)
        ]
        media = round(sum(notas) / len(notas), 2)
        print(f'\nSua média final é {media:.2f}. ', end='')

        if 0 <= media < 5:
            print('Infelizmente, você foi reprovado.')
        elif 5 <= media < 7:
            print('Você está de recuperação.')
        elif 7 <= media < 9:
            print('Parabéns! Você foi aprovado.')
        elif 9 <= media <= 10:
            print('Parabéns! Você foi aprovado com louvor.')
        elif 10 < media:
            print('\nMédia inválida. As notas devem estar entre 0 e 10.')
            input('Pressione Enter para tentar novamente...\n')
            continue
        break


def calcular_pedagio():
    """
    Calcula o valor do pedágio com base na distância percorrida (em km).
    Faixas:
    - até 100 km: R$ 10,00
    - entre 100 e 200 km: R$ 20,00
    - acima de 200 km: R$ 30,00

    Distância lida como float não-negativo.
    """
    quilometros = pegar_numero('Digite a distancia percorrida em km: ', decimal=True, aceita_negativo=False)
    if quilometros <= 100:
        print(f'O valor do pedágio para a distância de {quilometros:.2f} km é R$ 10,00')
    elif 100 < quilometros <= 200:
        print(f'O valor do pedágio para a distância de {quilometros:.2f} km é R$ 20,00')
    else:
        print(f'O valor do pedágio para a distância de {quilometros:.2f} km é R$ 30,00')


def verificar_par_impar():
    """
    Verifica se um número inteiro informado é par ou ímpar.

    Lê número inteiro (não-negativo por padrão) e imprime o resultado.
    """
    numero = pegar_numero('Digite um número inteiro: ', aceita_negativo=False)
    if numero % 2 == 0:
        print(f'O número {numero} é par.')
    else:
        print(f'O número {numero} é ímpar.')


def analisar_emprestimo():
    """
    Analisa a possibilidade de aprovação de um empréstimo com base na renda mensal
    e no valor da parcela desejada.

    Regras:
    - Se a renda for maior que 2000 e a parcela for <= 30% da renda: aprovado.
    - Se a renda for <= 2000: negado por renda insuficiente.
    - Caso contrário: negado por parcela excedente.
    """
    renda = pegar_numero('Digite o valor da sua renda mensal (R$): ', decimal=True, aceita_negativo=False)
    parcela = pegar_numero('Digite o valor da parcela desejada: R$ ', decimal=True, aceita_negativo=False)

    if renda > 2000 and parcela <= renda * 0.3:
        print('Empréstimo aprovado!')
    elif renda <= 2000:
        print('Empréstimo negado! Renda insuficiente para o empréstimo solicitado.')
    else:
        print('Empréstimo negado! A parcela excede 30% da sua renda mensal.')


def menu_principal():
    """
    Exibe o menu principal com opções para executar as funcionalidades do módulo.

    - O dicionário `opcoes` mapeia números para descrições e funções.
    - A opção 0 encerra o programa via `sys.exit(0)`.
    - Trata `KeyboardInterrupt` para finalizar com mensagem amigável.
    """
    opcoes = {
        1: ("Comparar vendas de maçãs e bananas", comparar_vendas),
        2: ("Calcular tempo total de atividades", calcular_tempo_atividades),
        3: ("Controlar temperatura do ar-condicionado", controlar_temperatura),
        4: ("Calcular IMC", calcular_imc),
        5: ("Verificar orçamento", verificar_orcamento),
        6: ("Verificar horário de funcionamento", verificar_horario),
        7: ("Calcular média de notas", calcular_media),
        8: ("Calcular valor do pedágio", calcular_pedagio),
        9: ("Verificar se número é par ou ímpar", verificar_par_impar),
        10: ("Analisar empréstimo", analisar_emprestimo),
        0: ("Sair", lambda: sys.exit(0))
    }

    while True:
        print()
        print('*' * 40)
        print('=' * 10, 'Menu Principal', '=' * 10)
        print('*' * 40)

        for num, (desc, _) in opcoes.items():
            print(f'{num}. {desc}')

        try:
            escolha = pegar_numero('Selecione uma opção: ')
            if escolha in opcoes:
                print('-' * 40)
                opcoes[escolha][1]()
            else:
                print('Opção inválida. Tente novamente.')
                input('Pressione Enter para continuar...\n')
        except KeyboardInterrupt:
            print('\n\nPrograma encerrado pelo usuário.')
            sys.exit(0)

    sys.exit(0)


if __name__ == '__main__':
    menu_principal()
