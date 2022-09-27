# TESTE - Calculadora aritmética basica

print('CALCULADORA ARITMÉTICA:')
print('')
n1 = int(input("Digite o primeiro numero: "))
n2 = int(input("Digite o segundo numero: "))
opção = float(input("Digite o calculo desejado( 1 soma ; 2 subtração ; 3 multiplicação ; 4 divisão ; 5 potencia ; 6 divisão inteira ; 7 resto da divisão): "))
if opção == 1:
   print('O resultado é: ', n1+n2)
elif opção == 2:
   print('O resultado é: ', n1-n2)
elif opção == 3:
   print('O resultado é: ', n1*n2)
elif opção == 4:
   print('O resultado é: ', n1/n2)
elif opção == 5:
   print('O resultado é: ', n1**n2)
elif opção == 6:
   print('O resultado é: ', n1//n2)
elif opção == 7:
   print('O resultado é: ', n1%n2)

