print('Calcule seu IMC')
massa = float(input('Informe seu peso [kg]: '))
altura = float(input('Informe sua altura [m]: '))
imc = massa/(altura*altura)
print(f'Seu IMC é {imc:.1f} ')
if imc < 18.5:
    print('Você está abaixo do peso.')
elif imc >= 18.5 and imc <= 25:
    print('Parabéns, você está com o peso ideal.')
elif imc > 25 and imc <= 30:
    print('Você esta sobrepeso.')
elif imc > 30 and imc <= 40:
    print('Você está com obesidade.')
else:
    print('Você está com obesidade mórbida.')