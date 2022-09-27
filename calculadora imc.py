altura = float(input('Digite sua altura em CM: '))
peso = float(input('Digite seu peso em KG: '))

imc = peso/(altura/100)**2

if imc <= 18.49:
    print(f'IMC:{imc} - Magreza')
elif imc >= 18.5 and imc <= 24.99:
    print(f'IMC:{imc} - Normal')
elif imc >= 25.0 and imc <= 29.99:
    print(f'IMC:{imc} - Sobrepeso')
elif imc >= 30.0 and imc <= 39.99:
    print(f'IMC:{imc} - Obesidade')
else:
    print(f'IMC:{imc} - Obesidade grave')
 