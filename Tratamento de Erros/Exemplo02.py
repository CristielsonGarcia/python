#No except você pode mostrar uma mensagem em função do tipo de erro que aconteceu na execução do programa!

try:        #Nesse bloco o programa vai executar uma operação, nesse caso ele vai receber dois valores e atribuir a divisão desses valores a uma variável
    a = int(input('Numerador: '))
    b = int(input('Denominador: '))
    r = a / b
except (ValueError, TypeError):     #Esse bloco vai ser executado caso dê algum problema na execução do bloco Try, um exemplo seria uma divisão por 0 ou uma divisão com strings
    print('Tivemos um problema com os tipos de dados que você digitou.')
except ZeroDivisionError:           #Esse bloco vai ser executado sempre que a variável b receber o número 0
    print('Não é possível dividir um número por zero!')
except KeyboardInterrupt:           #Esse bloco vai ser executado sempre que nenhuma informação for digitada, ou seja, você abriu o programa e simplesmente deu enter sem digitar nenhum valor
    print('O usuário preferiu não informar os dados!')
except Exception as erro:
    print(f'O erro encontrado foi {erro.__cause__}')
else:       #Esse bloco vai ser executado se tudo ocorrer bem no bloco Try.
    print(f'O resultado é {r}')
finally:    #Esse bloco vai ser executado independente se houver erros ou não no bloco Try, ele sempre será executado.    
    print('Volte sempre! Muito obrigado!')

#Detalhes importantes, os bloco else e finally são opcionais 
#O bloco except pode ser utilizado mais de uma vez 