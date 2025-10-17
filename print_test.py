print('Python na Escola de Programação do Alura')

nome = 'Kevin'
idade = 25

print('----------------------------------')
print('\tImprimindo nome e idade')
print('----------------------------------', end='\n\n')

print('Abordagem Simples:', end='\t')
print('Meu nome é ', nome, ' e tenho ', idade, ' anos.')
print('----------------------------------', end='\n\n')


print('Abordagem f-string:', end='\t')
print(f'Meu nome é {nome} e tenho {idade} anos.')
print('----------------------------------', end='\n\n')

print('Abordagem .format():', end='\t')
print('Meu nome é {} e tenho {} anos.'.format(nome, idade))
print('----------------------------------', end='\n\n')


print('Abordagem da % (Formatação de String Antiga - Python 2)', end='\t')
print('Meu nome é %s e tenho %i anos.'%(nome, idade))
print('----------------------------------', end='\n\n')


print('Nome na vertical ... ')
print('K', 'E', 'V', 'I', 'N', sep='\n')


print('----------------------------------')
print('\tFormatando valor de PI')
print('----------------------------------', end='\n\n')
pi = 3.14159

print('Abordagem f-string:', end='\t')
print(f'O valor arredondado de pi é {pi:.2f}')
print('----------------------------------', end='\n\n')

print('Abordagem .format():', end='\t')
print('O valor arredondado de pi é: {:.2f}'.format(pi))
print('----------------------------------', end='\n\n')


print('# Utilizando a função round():', end='\t')
print('O valor arredondado de pi é:', round(pi, 2))
print('----------------------------------', end='\n\n')