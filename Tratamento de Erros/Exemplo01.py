try:        #Nesse bloco o programa vai executar uma operação, nesse caso ele vai receber dois valores e atribuir a divisão desses valores a uma variável
    a = int(input('Numerador: '))
    b = int(input('Denominador: '))
    r = a / b
except:     #Esse bloco vai ser executado caso dê algum problema na execução do bloco Try, um exemplo seria uma divisão por 0 ou uma divisão com strings
    print('Infelizmente tivemos um problema')
else:       #Esse bloco vai ser executado se tudo ocorrer bem no bloco Try.
    print(f'O resultado é {r}')
finally:    #Esse bloco vai ser executado independente se houver erros ou não no bloco Try, ele sempre será executado.    
    print('Volte sempre! Muito obrigado!')

#Detalhes importantes, os bloco else e finally são opcionais 
#O bloco except pode ser utilizado mais de uma vez 