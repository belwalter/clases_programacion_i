
#! ESTRUCTURAS DE CONTROL

#! CONDICIONAL SIMPLE - CONDICIONAL COMPUESTO - CONDICIONAL ANIDADO

#! CONDICION --> valor|variable  operador_control  valor|variable
#! OPERADORES DE CONTRO >, <, >=, <=, ==, !=

#! OPERADORES LOGICOS AND OR --> AGRUPAR DOS O MAS CONDICIONES
#! CONDICION1 AND CONDICION2  - CONDICION1 OR CONDICION2

# edad = 15

# if(edad >= 18 and edad <=50):
#     print('la persona es apta para el pueso')
# else:
#     print('no apta')

# titulo = 'secundario'
# nacionalidad = 'chile'

# if(titulo == 'tecnico' or nacionalidad == 'argentino' or edad >=18):
#     print('apto')
# else:
#     print('no apto')


# numero = int(input('ingrese un numero '))

# if(numero % 2 == 0):
#     print('el numero es par')
# else:
#     print('el numero es impar')


# print('fin del algoritmo')

# numero1 = int(input('ingrese un numero '))
# numero2 = int(input('ingrese un numero '))
# numero3 = int(input('ingrese un numero '))

# nota_final = round((numero1 + numero2 + numero3) / 3, 2)

# # round(valor a redondear, cantidad de digitos)

# print(nota_final)

# if(nombre == 'Visa'):

# anio_naciemieto = int(input("ingrese año de nacimiento "))
# anio_actual = int(input("ingrese fechaactual "))

# edad_de_postulantes = anio_actual - anio_naciemieto 

# if(edad_de_postulantes > 23):
#     print("el postulante es apto para el puesto")
# else:
#     print("el postulante no es apto para el puesto")

# numero = int(input('ingrese un numero '))

# if(numero > 0):
#     print('el numero es positivo')
# else:
#     if(numero < 0):
#         print('el numero es negativo')
#     else:
#         print('es neutro')

# numero1 = int(input('ingrese un numero '))
# numero2 = int(input('ingrese un numero '))

# if(numero1 == numero2):
#     print('son iguales')
# else:
#     if(numero1 > numero2):
#         print('el numero 1 es el mayor')
#     else:
#         print('el numero 2 es el mayor')

# if(numero1 == numero2):
#     print('son iguales')
# elif(numero1 > numero2):
#     print('el numero 1 es el mayor')
# else:
#     print('el numero 2 es el mayor')


# numero = int(input('ingrese un numero '))

# if(numero % 2 == 0 or numero % 5 == 0):
#     print(numero ** 3)
# else:
#     print('no es multiplo de 2 ni de 5')

monto = float(input("ingrese el monto "))
tarjeta = input("ingrese tarjeta ")
coutas = int(input('ingrese el numero de cuotas '))

if(coutas == 3):
    monto = monto * 1.03  # 3 * monto / 100     (monto * 0.3) + monto
elif(coutas == 8):
    monto = monto * 1.17
elif(coutas == 12):
    monto = monto * 1.32


if(tarjeta == 'visa'):
    recargo_visa = monto * 1.07
    print('monto total:', recargo_visa)
elif(tarjeta == 'mastercard'):
    recargo_master = monto * 1.11
    print('monto total:', recargo_master)
else:
    print('monto total:', monto)