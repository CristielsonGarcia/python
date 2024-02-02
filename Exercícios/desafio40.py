print('Calculando a Média')
m1 = float(input('Nota 1: '))
m2 = float(input('Nota 2: '))
m3 = float(input('Nota 3: '))
m4 = float(input('Nota 4: '))
media = (m1 + m2 + m3 + m4)/4
print(f'Sua média foi {media:.1f}')
if media >= 7:
    print('Aprovado! Parabéns.')
elif media >= 6 and media < 7:
    print('Recuperação! Não desista!')
else:
    print('Reprovado! Estude mais e não desista!')