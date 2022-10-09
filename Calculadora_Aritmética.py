# TESTE - Calculadora aritmética basica

import sys
import os

def restart_program():
  python = sys.executable
  os.execl(python, python, * sys.argv)

print('\n## CALCULADORA ARITMÉTICA ##')
print('')
print('INSTRUÇÕES: UTILIZAR O ''.(PONTO)'' CASO FOR UTILIZAR NUMEROS DECIMAIS \n')
n1 = float(input("Digite o primeiro numero: "))
n2 = float(input("Digite o segundo numero: "))
opção = int(input("Digite o calculo desejado( 1 soma ; 2 subtração ; 3 multiplicação ; 4 divisão ; 5 potencia ; 6 divisão inteira ; 7 resto da divisão): \n"))
if opção == 1:
   print('O resultado é: ', n1+n2)
elif opção == 2:
   print('O resultado é: ', n1-n2)
elif opção == 3:
   print('O resultado é:{:.2f} ', n1*n2)
elif opção == 4:
   print('O resultado é:{:.2f} ', n1/n2)
elif opção == 5:
   print('O resultado é:{:.2f} ', n1**n2)
elif opção == 6:
   print('O resultado é:{:.2f} ', n1//n2)
elif opção == 7:
   print('O resultado é:{:.2f} ', n1%n2)

reset = int(input('\nDeseja realizar uma nova operação? \n1 - SIM \n2 - NÃO \n'))
while True:
 if int(reset) == 1:
  print('\nPrograma será reinicializado...\n')
  restart_program()
  #os.execl(sys.executable, os.path.abspath(__file__),*sys.argv) 
 elif int(reset) == 2:
  print('\nPrograma será finalizado...\n')
  sys.exit
 break
