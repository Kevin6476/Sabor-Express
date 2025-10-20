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

if __name__ == "__main__":
    print('Arquivo utilitarios/utils.py executado diretamente.')