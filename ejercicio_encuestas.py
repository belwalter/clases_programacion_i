

red_social = input('ingrese red social preferida Twitter, Instagram, Facebook, otras ')

cont_tw = 0
cont_in = 0
cont_fa = 0
cont_ot = 0


while(red_social != ''):
    if(red_social == 'Twitter'):
        cont_tw += 1
    elif(red_social == 'Instagram'):
        cont_in += 1
    elif(red_social == 'Facebook'):
        cont_fa += 1
    else:
        cont_ot += 1
    red_social = input('ingrese red social preferida Twitter, Instagram, Facebook, otras ')

red_mayor = 'Tiwtter'
mayor = cont_tw

if(cont_in > mayor):
    mayor = cont_in
    red_mayor = 'Instagram'
if(cont_fa > mayor):
    mayor = cont_fa
    red_mayor = 'Facebook'
if(cont_ot > mayor):
    mayor = cont_ot
    red_mayor = 'otro'

red_menor = 'Tiwtter'
menor = cont_tw

if(cont_in < menor):
    menor = cont_in
    red_menor = 'Instagram'
if(cont_fa < menor):
    menor = cont_fa
    red_menor = 'Facebook'
if(cont_ot < menor):
    menor = cont_ot
    red_menor = 'otro'


print('la red de mayor preferencia es:', red_mayor, mayor)
print('la red de menor preferencia es:', red_menor, menor)



multiplo2 = 0
multiplo3 = 0
multiplo4 = 0

for i in range(6,61):
    if(i % 2 == 0):
        multiplo2 += i
    if(i % 3 == 0):
        multiplo3 += i
    if(i % 4 == 0):
        multiplo4 += i


print('2', multiplo2)
print('3', multiplo3)
print('4', multiplo4)

print(multiplo2 + multiplo3 - multiplo4)


# mayor = int(input('ingrese un numero '))

# for i in range(1, 15):
#     numero = int(input('ingrese un numero '))
#     if(numero > mayor):
#         mayor = numero

# print('el mayor es', mayor)



cantidad = 0

while(True):
    numero = int(input('ingrese el numero de la carta '))
    palo = input('ingrese el palo ')
    cantidad += 1
    if(palo == 'copa' and numero == 7):
        break

print('cantidad de cartas', cantidad)