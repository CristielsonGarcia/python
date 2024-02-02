print('Bem Vindo(a) ao banco do Brasil')
print('Quer comprar uma casa? Podemos tornar seu sonho realidade!')
print('Mas para isso precisamos de algumas informações antes.')
v_casa = float(input('Nos informe o valor da casa: '))
salario = float(input('Agora nos informe o seu salário: '))
tempo = int(input('Você pretende parcelar o valor em quantos anos? '))
v_mensal = v_casa / (tempo*12)
if v_mensal <= (salario*0.3):
    print('Parabéns, seu empréstimo foi aprovado!')
elif v_mensal > (salario*0.3):
    print('Infelizmente seu empréstimo não foi aprovado!')
    print('Recomendamos que aumente o tempo de pagamento.')
