
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

# monto = float(input("ingrese el monto "))
# tarjeta = input("ingrese tarjeta ")
# coutas = int(input('ingrese el numero de cuotas '))

# if(coutas == 3):
#     monto = monto * 1.03  # 3 * monto / 100     (monto * 0.3) + monto
# elif(coutas == 8):
#     monto = monto * 1.17
# elif(coutas == 12):
#     monto = monto * 1.32


# if(tarjeta == 'visa'):
#     recargo_visa = monto * 1.07
#     print('monto total:', recargo_visa)
# elif(tarjeta == 'mastercard'):
#     recargo_master = monto * 1.11
#     print('monto total:', recargo_master)
# else:
#     print('monto total:', monto)

# dia = int(input('ingrese el numero del dia '))
# mes = int(input('ingrese el numero del mes '))
# anio = int(input('ingrese el año '))



# if(mes >= 1 and mes <= 12):
#     if(mes == 2):
#         # print('el tiempo tiene 28 dias')
#         if(dia >=1 and dia <= 28):
#             if(dia == 28):
#                 dia = 1
#                 mes += 1
#             else:
#                 dia += 1
#             # print('fecha correcta')
#     elif(mes == 4 or mes == 6 or mes == 9 or mes == 11):
#         # print('el mes tiene 30 dias')
#         if(dia >=1 and dia <= 30):
#             if(dia == 30):
#                 dia = 1
#                 mes += 1
#             else:
#                 dia += 1
#     else:
#         # print('el mes tiene 31')
#         if(dia >=1 and dia <= 31):

#             if(dia == 31):
#                 dia = 1
#                 mes += 1
#             else:
#                 dia += 1

#             if(mes == 13):
#                 mes = 1
#                 anio += 1 # anio = anio + 1
    
#     print(dia,'/',mes,"/",anio)
# else:
#     print('numero de mes incorrecto')


# temperatura = float(input('ingrese el valor de la temperatura '))
# escala = input('ingrese la escala C|F ')

# if(escala == 'C'):
#     print('la temperatura el grados farenheit es', (temperatura * 9/5) + 32)
# elif(escala == 'F'):
#     print('la temperatura el grados celsius es', (temperatura - 32) * 5/9)
# else:
#     print('la escala ingresada es incorrecta')

# num1 = int(input('ingrese valor de la carta 1 '))
# palo1 = input('ingrese palo de la carta 1 ')
# num2 = int(input('ingrese valor de la carta 2 '))
# palo2 = input('ingrese palo de la carta 2 ')
# num3 = int(input('ingrese valor de la carta 3 '))
# palo3 = input('ingrese palo de la carta 3 ')

# if(palo1 == palo2 and palo1 == palo3):
#     puntos = 20
#     if(num1 <=7):
#         puntos += num1
#     if(num2 <=7):
#         puntos += num2
#     if(num3 <=7):
#         puntos += num3
#     print('flor ', puntos)
# elif(palo1 == palo2 or palo1 == palo3 or palo2 == palo3):
#     puntos = 20
#     if(palo1 == palo2):
#         if(num1 <=7):
#             puntos += num1
#         if(num2 <=7):
#             puntos += num2
#     elif(palo1 == palo3):
#         if(num1 <=7):
#             puntos += num1
#         if(num3 <=7):
#             puntos += num3
#     elif(palo2 == palo3):
#         if(num2 <=7):
#             puntos += num2
#         if(num3 <=7):
#             puntos += num3
#     print('envido', puntos)

num1 = int(input('ingrese un numero '))
num2 = int(input('ingrese un numero '))
num3 = int(input('ingrese un numero '))
num4 = int(input('ingrese un numero '))
num5 = int(input('ingrese un numero '))


cantidad_multiplos_3 = 0 #! contador

if(num1 % 3 == 0):
    cantidad_multiplos_3 += 1
    
if(num2 % 3 == 0):
    cantidad_multiplos_3 += 1

if(num3 % 3 == 0):
    cantidad_multiplos_3 += 1

if(num4 % 3 == 0):
    cantidad_multiplos_3 += 1

if(num5 % 3 == 0):
    cantidad_multiplos_3 += 1

print('cantidad de multiplos de 3', cantidad_multiplos_3)

