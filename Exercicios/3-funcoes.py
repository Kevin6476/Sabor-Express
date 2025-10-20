"""
Módulo: Exercicios/3-funcoes.py

Coleção de funções utilitárias e pequenos exercícios interativos em Python.
Cada função lê entradas do usuário, processa dados simples e imprime resultados.
Projetado para rodar em Windows (usa `cls` para limpar a tela via `os.system`).

Observações:
- Usa `pegar_numero` importado de `utils` para entradas numéricas seguras.
- Funções são independentes e chamadas via `menu_principal`.
"""
# imports padrão
import os
import random
import string
import unicodedata

from utils import pegar_numero


def limpar_tela():
    """
    Limpa a tela do terminal no Windows usando `cls`.
    Não possui parâmetros nem retorno.
    """
    os.system('cls')


def calcular_idade():
    """
    Calcula e imprime a idade baseada no ano de nascimento e ano atual.

    Fluxo:
    - Solicita `ano_nascimento` e `ano_atual` via `pegar_numero`.
    - Calcula a diferença e imprime a idade ou uma mensagem caso `ano_atual` < `ano_nascimento`.
    """
    subtrair = lambda x, y: x - y

    ano_nascimento = pegar_numero('Digite o ano de nascimento: ')
    ano_atual = pegar_numero('Digite o ano atual: ')

    if ano_atual >= ano_nascimento:
        idade = subtrair(ano_atual, ano_nascimento)
        print(f'A idade é de {idade} anos.')
    else:
        print('Você ainda não nasceu :o')


def contar_caracteres():
    """
    Lê uma palavra do usuário e imprime a quantidade de caracteres.

    Exemplo:
    Entrada: 'Python' -> Saída: 'Essa palavra tem 6 caracteres.'
    """
    contar = lambda c: len(c)

    texto = input('Digite uma palavra: ')
    print(f'Essa palavra tem {contar(texto)} caracteres.')


def saudacao():
    """
    Pergunta a hora atual (0-23) e imprime uma saudação apropriada:
    - 'Bom dia!' para <12
    - 'Boa tarde!' para 12-17
    - 'Boa noite!' para >=18
    """
    horario = pegar_numero('Digite a hora atual (0-23): ')

    if horario < 12:
        msg = 'Bom dia!'
    elif horario < 18:
        msg = 'Boa tarde!'
    else:
        msg = 'Boa noite!'

    print(msg)


def conversor_telefones():
    """
    Demonstra conversão de strings de telefones para inteiros.
    - Converte uma lista fixa de strings para inteiros.
    - Valida se houve algum erro na conversão (lista `invalidos`).
    Imprime mensagem de sucesso ou erro.
    """
    convert = lambda telefones: [int(tel) for tel in telefones]
    validar = lambda telefones: [tel for tel in telefones if not isinstance(tel, int)]
    numeros = convert(["11987654321", "21912345678", "31987654321", "11911223344"])
    invalidos = validar(numeros)
    print('Erro na conversão' if invalidos else 'Todos os números foram convertidos corretamente!')


def soma_diversos_valores():
    """
    Soma valores de vendas informados pelo usuário (separados por espaços)
    e imprime o total formatado com duas casas decimais.
    """
    somar_tudo = lambda values: sum(map(float, values))
    valores = input("Digite os valores das vendas: ").split()
    print(f"O total de vendas foi: {somar_tudo(valores):.2f}")


def extrair_numeros_pares():
    """
    Lê números separados por espaço, filtra os pares e imprime-os.
    Se não houver pares, informa que nenhum foi encontrado.
    """
    numbers = [int(n) for n in input("Digite os números separados por espaço: ").split()]
    pares = [str(n) for n in numbers if n % 2 == 0]
    print("Números pares:", " ".join(pares) if pares else "Nenhum número par encontrado")


def juntar_listas():
    """
    Lê produtos e preços separados por vírgula e imprime cada produto com seu preço.
    - Remove espaços extras usando `strip`.
    """
    produtos = input("Digite os produtos separados por vírgula: ").split(",")
    precos = input("Digite os preços separados por vírgula: ").split(",")
    for produto, preco in zip(produtos, precos):
        print(f"{produto.strip()}: {preco.strip()}")


def maquina_descontos():
    """
    Calcula preço final aplicando uma porcentagem de desconto.
    - Solicita `porcentagem` (decimal=True) e `total_compra` (decimal=True).
    - Usa uma função closure `criar_desconto` que retorna uma função que aplica o desconto.
    """
    criar_desconto = lambda desconto: lambda valor: valor - (valor * (desconto / 100))

    porcentagem = pegar_numero('Digite a porcentagem de desconto: ', decimal=True)
    total_compra = pegar_numero('Digite o total de compra: ', decimal=True)
    preco_desconto = criar_desconto(porcentagem)
    print(f"Preço final com desconto: {preco_desconto(total_compra):.2f}")


def somar_recursivamente():
    """
    Soma recursivamente os inteiros de 1 até `numero` informado pelo usuário.
    - Exemplo: entrada 4 -> 1+2+3+4 = 10.
    """

    def soma_recursiva(num):
        if num <= 1:
            return 1
        return num + soma_recursiva(num - 1)

    numero = pegar_numero("Digite um número: ")
    print(f"A soma de 1 a {numero} é: {soma_recursiva(numero)}")


def lista_voluntarios():
    """
    Permite cadastrar nomes de voluntários até o usuário digitar 'sair'.
    Imprime a lista de voluntários cadastrados.
    """
    voluntarios = []
    while True:
        voluntario = input('Digite o nome do voluntário ou "sair" para encerrar: ')
        if voluntario.lower() == 'sair':
            break
        voluntarios.append(voluntario)

    print('Os voluntarios cadastrados são: ', '\n\t'.join(voluntarios), sep='\n\t')


def atualizar_lista_convidados():
    """
    Exibe uma lista inicial de convidados e permite inserir um novo convidado
    em uma posição informada pelo usuário (base 1).
    """
    convidados = ['Ana', 'Pedro', 'Carlos']
    print('Lista atual de convidados: ', convidados)

    convidado = input('Digite o nome do novo convidado: ')
    posicao = pegar_numero('Informe a posição em que deseja colocar o convidado: ')

    convidados.insert(posicao - 1, convidado)
    print(f'Lista atualizada de convidados: {convidados}')


def reordenar_eventos():
    """
    Mostra uma lista de eventos com ordem invertida e corrige invertendo a lista.
    """
    eventos_registrados = ['Encerramento', 'Palestra 3', 'Palestra 2', 'Abertura']
    print(f"Ordem atual: {eventos_registrados}")
    eventos_registrados.reverse()
    print(f"Ordem corrigida: {eventos_registrados}")


def trocar_nome_na_lista():
    """
    Substitui um nome incorreto por um correto em uma lista predefinida.
    - Solicita `nome_errado` e, se presente, pede `nome_correto` para substituir mantendo posição.
    """
    resultados = ['Ana', 'Carlos', 'Pedro']
    print('Lista original', resultados)

    nome_errado = input('Informe o nome incorreto: ')
    if nome_errado in resultados:
        nome_correto = input('Informe o nome correto: ')
        posicao = resultados.index(nome_errado)
        resultados.remove(nome_errado)
        resultados.insert(posicao, nome_correto)

        print(f'O nome {nome_errado} foi substituído por {nome_correto}.')
        print('Lista atualizada ', resultados)

    else:
        print('Nome não está presente na lista')


def remove_ultimo_item_pedido():
    """
    Remove o último item de uma lista de pedidos informada pelo usuário (separada por vírgula).
    Imprime a lista resultante.
    """
    pedidos = input('Informe os pedidos separados por vírgula: ').split(', ')
    if pedidos:
        pedidos.pop()
    print(f'Pedidos finais: {pedidos}')


def calcular_media_alunos():
    """
    Calcula e imprime a média de turma a partir de notas fornecidas separadas por vírgula.
    - Converte valores para float antes de calcular.
    """
    notas = input('Informe a media de cada aluno separadas por vírugula: ').split(', ')
    notas = [float(x) for x in notas]
    media = sum(notas) / len(notas)
    print(f'A media da turma é {media:.2f}')


def exibir_dados_alunos():
    """
    Exibe dados de alunos informados em sequência no formato:
    Nome, Idade, Nota, Nome, Idade, Nota, ...
    - Percorre a lista de entrada em passos de 3 e imprime cada aluno.
    """
    dados = input('Digite os dados do aluno no formato Nome, Idade, Nota serparados por virgula: ').split(', ')

    for i in range(0, len(dados), 3):
        nome, idade, nota = dados[i], int(dados[i + 1]), float(dados[i + 2])
        print(' -----------------------')
        print(f"Aluno: {nome}")
        print(f"Idade: {idade}")
        print(f"Nota: {nota}")
        print(' -----------------------\n')


def calcular_conta_restaurante():
    """
    Calcula o total a pagar em uma conta de restaurante incluindo gorjeta.

    Fluxo:
    - Função interna `calcular_conta(valor_conta, gorjeta)` retorna (total, valor_gorjeta).
    - Solicita `conta` (decimal) e `gorjeta_porc` (% inteiro).
    - Imprime valor da gorjeta e total a pagar.
    """

    def calcular_conta(valor_conta, gorjeta):
        """
        Retorna (pagamento_total, valor_gorjeta).
        - `valor_conta`: float
        - `gorjeta`: percentual (ex.: 10 para 10%)
        """
        valor_gorjeta = (gorjeta / 100) * valor_conta
        pagamento_total = valor_conta + valor_gorjeta
        return pagamento_total, valor_gorjeta

    conta = pegar_numero('Digite o valor da conta: ', decimal=True)
    gorjeta_porc = pegar_numero('Digite o valor da gorjeta em %: ')

    total, gorjeta = calcular_conta(conta, gorjeta_porc)
    print(f'Valor da gorjeta: {gorjeta:.2f}\nTotal a pagar: {total:.2f}')


def validar_cpf():
    """
    Valida se o CPF informado contém apenas dígitos e tem exatamente 11 caracteres.
    - Lê `cpf_input` e usa função interna `validar` que retorna (cpf, valido_bool, mensagem).
    - Imprime a mensagem de validação.
    """

    def validar(cpf):
        """
        Valida regras básicas de formatação do CPF.
        Retorna: (cpf, bool_valido, mensagem_str)
        """
        if not cpf.isdigit():
            return cpf, False, 'CPF deve conter apenas números'
        if len(cpf) != 11:
            return cpf, False, 'CPF deve conter extamanete 11 dígitos'
        return cpf, True, f'O CPF {cpf} é válido'

    cpf_input = input('Informe seu CPF apenas em digitos: ')
    _, valido, msg = validar(cpf_input)
    print(msg)


def somar_vogais():
    """
    Conta vogais em um texto ignorando acentuação.
    - Normaliza usando `unicodedata.normalize('NFD', ...)` e descarta marcas (`Mn`).
    - Retorna a contagem de vogais (a, e, i, o, u).
    """

    def somar(frase):
        frase_normalizada = ''.join(c for c in unicodedata.normalize('NFD', frase.lower())
                                    if unicodedata.category(c) != 'Mn')
        return sum(c in 'aeiou' for c in frase_normalizada)

    frase = input('Digite um texto: ')
    print(f'O texto digitado tem {somar(frase)} vogais')


def pegar_palavras_grande():
    """
    Retorna palavras com comprimento maior que `tamanho` (padrão 10) do texto informado.
    - Imprime as palavras encontradas ou mensagem caso não haja.
    """
    palavras_grande = lambda frase, tamanho=10: [x for x in frase.split() if len(x) > tamanho]
    palavras = palavras_grande(input('Digite um texto: '))
    print(f'Palavras longas encontradas: {palavras}' if palavras else 'Nenhuma palavra longa foi encontrada no texto')


def gerador_de_senha():
    """
    Gera uma senha aleatória contendo pelo menos 1 maiúscula, 1 minúscula, 1 número e 1 caractere especial.
    - `gerar_senha(tamanho=12)` retorna a senha como string.
    - A função imprime uma senha com comprimento 50 (no código atual).
    """

    def gerar_senha(tamanho=12):
        # Define os conjuntos de caracteres
        letras_maiusculas = string.ascii_uppercase
        letras_minusculas = string.ascii_lowercase
        numeros = string.digits
        especiais = string.punctuation

        # Garante pelo menos um de cada tipo
        senha = [
            random.choice(letras_maiusculas),
            random.choice(letras_minusculas),
            random.choice(numeros),
            random.choice(especiais)
        ]
        todos_caracteres = letras_maiusculas + letras_minusculas + numeros + especiais
        senha += random.choices(todos_caracteres, k=tamanho - len(senha))
        random.shuffle(senha)  # embaralha
        return ''.join(senha)

    print("Senha gerada:", gerar_senha(50))


def pedra_papel_tesoura():
    """
    Jogo simples de Pedra, Papel e Tesoura entre usuário e computador.
    - Lê a jogada do usuário (aceita variações de caixa) e gera jogada aleatória.
    - Imprime resultado (Empate, Você Venceu! ou Você Perdeu!).
    """
    PE = 'pedra'
    PA = 'papel'
    TE = 'tesoura'

    jogadas = PE, PA, TE
    jogada_competidor = input('Escolha:\nPedra, Papel ou Tesoura? ').strip().lower()
    jogada_maquina = random.choice(jogadas)

    if jogada_competidor not in jogadas:
        print(f'\nOpção inválida! Você escolheu: {jogada_competidor}')
        return

    print(f'\nO computador escolheu {jogada_maquina}. ', end='')
    if jogada_competidor == jogada_maquina:
        print(f'Empatou!')

    venceu = (jogada_competidor == PE and jogada_maquina == TE) or \
             (jogada_competidor == PA and jogada_maquina == PE) or \
             (jogada_competidor == TE and jogada_maquina == PA)
    print('Você Venceu!' if venceu else 'Você Perdeu!')


def jogo_numero_aleatorio(limite=100):
    """
    Jogo de adivinhar um número aleatório entre 1 e `limite`.
    - Repetir até o usuário acertar.
    - Trata entradas inválidas com exceção `ValueError`.
    """
    numero_aleatorio = random.randint(1, limite)
    tentativas = 0
    while True:
        try:
            chute = int(input(f'Chute um número aleatório entre 1 e {limite}: '))
            tentativas += 1
            if chute < numero_aleatorio:
                print('O número aleatório é maior')
            elif chute > numero_aleatorio:
                print('O número aleatório é menor')
            else:
                print(f'\nVocê acertou! O número secreto é {numero_aleatorio}')
                break

        except ValueError:
            input('Valor fornecido inválido! Informe um numero válido\nPressione <enter> para continuar.')
            continue


def caucular_expressoes_simples():
    """
    Calculadora simples que recebe uma expressão no formato: 'a <op> b'
    - Operadores suportados: +, -, *, /
    - Converte `a` e `b` para float antes de executar a operação.
    - Imprime resultado ou mensagem de operador não suportado.
    """
    somar = lambda a, b: f'A soma de {a} + {b} é igual á {a + b}'
    subtrair = lambda a, b: f'A Subtração de {a} - {b} é igual á {a - b}'
    multiplicar = lambda a, b: f'A Multiplicação de {a} * {b} é igual á {a * b}'
    dividir = lambda a, b: f'A Divisão de {a} / {b} é igual á {a / b}' if b != 0 else 'Divisão por zero não permitida!'

    expressoes = {
        '+': (somar, 'Soma'),
        '-': (subtrair, 'Subtração'),
        '*': (multiplicar, 'Multiplicação'),
        '/': (dividir, 'Divisão')
    }

    ops_text = '\n'.join(f'{chave} -> {desc}' for chave, (_, desc) in expressoes.items())
    print(f'Operações <op>:\n{ops_text}\n')
    a, op, b = input('Informe a operação no seguinte formato "a <op> b": ').split(' ')

    if op not in expressoes:
        print(f'Expressão matemática "{op}" não suportada!')
        return

    operacao, desc = expressoes.get(op)
    print(operacao(float(a), float(b)))


def gerenciador_tarefas():
    """
    Gerenciador de tarefas em modo texto:
    - Adicionar tarefa
    - Visualizar tarefas
    - Remover tarefa por índice
    - Sair
    """
    tarefas = []

    while True:
        print("\n1. Adicionar tarefa")
        print("2. Visualizar tarefas")
        print("3. Remover tarefa")
        print("4. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            tarefa = input("Digite a tarefa: ").strip()
            if tarefa:  # Verifica se a string não está vazia
                tarefas.append(tarefa)
                print("Tarefa adicionada!")
            else:
                print("Erro: A tarefa não pode estar vazia.")

        elif opcao == "2":
            if tarefas:
                print("\nTarefas:")
                for i, tarefa in enumerate(tarefas, 1):
                    print(f"{i}. {tarefa}")
            else:
                print("Nenhuma tarefa cadastrada.")

        elif opcao == "3":
            if not tarefas:
                print("Erro: Nenhuma tarefa para remover.")
                continue

            try:
                indice = int(input("Digite o número da tarefa a ser removida: ")) - 1
                if 0 <= indice < len(tarefas):
                    removida = tarefas.pop(indice)
                    print(f"Tarefa '{removida}' removida!")
                else:
                    print("Erro: Índice inválido! Digite um número válido.")
            except ValueError:
                print("Erro: Entrada inválida! Digite um número.")

        elif opcao == "4":
            print("Saindo do gerenciador de tarefas. Até mais!")
            break

        else:
            print("Erro: Opção inválida! Escolha uma opção entre 1 e 4.")


def menu_principal():
    """
    Exibe um menu com todas as funções disponíveis neste módulo.
    - O usuário escolhe uma opção numérica para executar a função correspondente.
    - Pressionar 0 encerra o programa.
    - Após execução de cada função, aguarda ENTER para retornar ao menu.
    """
    funcoes = {
        1: ('Calcular Idade', calcular_idade),
        2: ('Contar Caracteres', contar_caracteres),
        3: ('Saudação', saudacao),
        4: ('Conversor de Telefones', conversor_telefones),
        5: ('Soma de Diversos Valores', soma_diversos_valores),
        6: ('Extrair Números Pares', extrair_numeros_pares),
        7: ('Juntar Listas', juntar_listas),
        8: ('Máquina de Descontos', maquina_descontos),
        9: ('Somar Recursivamente', somar_recursivamente),
        10: ('Lista de Voluntários', lista_voluntarios),
        11: ('Atualizar Lista de Convidados', atualizar_lista_convidados),
        12: ('Reordenar Eventos', reordenar_eventos),
        13: ('Trocar Nome na Lista', trocar_nome_na_lista),
        14: ('Remover Último Item do Pedido', remove_ultimo_item_pedido),
        15: ('Calcular Média dos Alunos', calcular_media_alunos),
        16: ('Exibir Dados dos Alunos', exibir_dados_alunos),
        17: ('Calcular Conta Restaurante', calcular_conta_restaurante),
        18: ('Validar CPF', validar_cpf),
        19: ('Somar Vogais', somar_vogais),
        20: ('Pegar Palavras Grandes', pegar_palavras_grande),
        21: ('Gerador de Senha', gerador_de_senha),
        22: ('Pedra, Papel e Tesoura', pedra_papel_tesoura),
        23: ('Jogo do Número Aleatorio', jogo_numero_aleatorio),
        24: ('Calcular Expressões Simples', caucular_expressoes_simples),
        25: ('Gerenciador de Tarefas', gerenciador_tarefas)
    }

    while True:
        limpar_tela()
        print('\n=== Menu Principal ===')
        for num, (nome, _) in funcoes.items():
            print(f'{num}. {nome}')
        print('0. Sair')

        try:
            opcao = int(input('\nEscolha uma opção: '))
            if opcao == 0:
                print('Programa encerrado!')
                break

            if opcao in funcoes:
                limpar_tela()
                print(f'\n=== {funcoes[opcao][0]} ===\n')
                funcoes[opcao][1]()
                input('\nPressione ENTER para continuar...')
            else:
                print('Opção inválida!')
                input('\nPressione ENTER para continuar...')

        except ValueError:
            print('Por favor, digite um número válido!')
            input('\nPressione ENTER para continuar...')


if __name__ == '__main__':
    menu_principal()
