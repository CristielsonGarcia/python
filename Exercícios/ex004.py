algo = input('Digite algo: ')
print(f'Você digitou uma informação do tipo {type(algo)}')
print(f'Na informação que você digitou contém letras e números: {algo.isalnum()}')
print(f'Na informação que você digitou contém espaços: {algo.isspace()}')
print(f'A informação que você digitou está totalmente em maiusculo: {algo.isupper()}')
