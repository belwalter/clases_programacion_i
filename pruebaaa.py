
from funciones import calculadora, es_vocal



# num1 = int(input('ingrese un numero '))
# operador = input('ingrese el operador ')
# num2 = int(input('ingrese un numero '))

# print(calculadora(num1, operador, num2))

palabra = input('ingrese una palabra ')

for letra in palabra:
    print(es_vocal(letra))
