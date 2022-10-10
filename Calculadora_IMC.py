# CALCULADORA DE IMC #

import sys
import os

def restart_program():
  python = sys.executable
  os.execl(python, python, * sys.argv)

print('\n## CALCULADORA DE IMC ## \n')
print('')
print('INSTRUÇÕES: NÃO É NECESSÁRIO UTILIZAR PONTO/VIRGULA, EX: 180 ( PARA 1.80 )\n')
altura = float(input('Digite sua altura em CM: '))
peso = float(input('Digite seu peso em KG: '))

imc = peso/(altura/100)**2

if imc <= 18.49:
    print(f'IMC:{imc:.2f} - Magreza')
elif imc >= 18.5 and imc <= 24.99:
    print(f'IMC:{imc:.2f} - Normal')
elif imc >= 25.0 and imc <= 29.99:
    print(f'IMC:{imc:.2f} - Sobrepeso')
elif imc >= 30.0 and imc <= 39.99:
    print(f'IMC:{imc:.2f} - Obesidade')
else:
    print(f'IMC:{imc:.2f} - Obesidade grave')

reset = int(input('\nDeseja realizar uma nova medição? \n1 - SIM \n2 - NÃO \n'))
while True:
 if int(reset) == 1:
  print('\nPrograma será reinicializado...\n')
  restart_program()
  #os.execl(sys.executable, os.path.abspath(__file__),*sys.argv) 
 elif int(reset) == 2:
  print('\nPrograma será finalizado...\n')
  sys.exit
 break