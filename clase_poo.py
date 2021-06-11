
#! Programación orientada a objetos

#! Componentes: Clases, Objetos y Mensajes

#! Caracteristicas: Encapsulamiento, Herencia, Polimorfismo

#! Sobrecarga, Constructor, Ocultamiento de la informacíon


class Persona(object):
    """Clase que representa a una persona."""

    def __init__(self, apellido, nombre, edad=None, email=None, n_cuenta=None):
        self.__apellido = apellido
        self.__nombre = nombre
        self.__edad = edad
        self.__email = email
        self.__n_cuenta = n_cuenta

    def apellido(self):
        return self.__apellido

    def email(self):
        return self.__email

    def set_email(self, mail):
        """Cambia el valor del atributo mail."""
        self.__email = mail

    @property
    def edad(self):
        return self.__edad
    
    @edad.setter
    def edad(self, edad):
        """Cambia el valor del atributo mail."""
        if(type(edad) is int):
            self.__edad = edad
        else:
            print('la edad debe ser entero')

    def mostrar_datos(self):
        """Muestra los datos de cada persona."""
        print(self.__apellido, self.__nombre, self.__email)
    

# from consumo_api import get_charter_by_id

# per1 = get_charter_by_id(20)

# persona0 = Persona(per1['name'], per1['height'])

persona1 = Persona('Perez', 'Maria', email='asdasd@asda.com')
# persona2 = Persona('Gonzalez', 'Maria', 23)
# persona3 = Persona('Caseres', 'Julieta')

# persona3.set_email("123@123.com")

# persona1.mostrar_datos()
# persona2.mostrar_datos()
# persona3.mostrar_datos()

# persona2.edad = 45

# print(persona2.edad)


# print(persona1.apellido, persona1.nombre)
# print(persona2.apellido, persona2.nombre)
# print(persona3.apellido, persona3.nombre)
# print(persona1)
# print(persona2)
# print(persona3)
# print(persona1.apellido == persona3.apellido)


#! Herencia: agrupar objetos de distinta clase
#! que se comportan de manera similar

# class Animal():

#     def __init__(self, nombre, especie, cantidad_patas):
#         self.nombre = nombre
#         self.especie = especie
#         self.cantidad_patas = cantidad_patas


# a1 = Animal('caballo', 'mamifero', 4)
# a2 = Animal('pinguino', 'mamifero', 2)
# a3 = Animal('serpiente', 'reptil', 0)



# class Alumno(Persona):

#     def __init__(self, fecha_inscripcion, apellido, nombre, edad=None, email=None, n_cuenta=None):
#         self.__fecha_inscripcion = fecha_inscripcion
#         Persona.__init__(self, apellido, nombre, edad, email, n_cuenta)
    
#     def inscribirse(self):
#         print('el alumno se esta inscribiendo a una materia')

#     def mostrar_datos(self):
#         print(self.apellido(), 'se incribio a cursar en:', self.__fecha_inscripcion)

# class Docente(Persona):

#     def __init__(self, cantidad_materias, apellido, nombre, edad=None, email=None, n_cuenta=None):
#         self.__cantidad_materia = cantidad_materias
#         Persona.__init__(self, apellido, nombre, edad, email, n_cuenta)

#     def mostrar_datos(self):
#         print(self.apellido(), self.__cantidad_materia)
    
#     def dictar_clase(self):
#         print('el docente esta dictanto una cátedra...')

# a = Alumno('01-03-2021', 'perez', 'juan')
# d = Docente(4, 'alvarez', 'maria')

# personas = [a, persona1, d]

# for elemento in personas:
#     elemento.mostrar_datos()


class FormaGeometrica():

    def __init__(self, nombre, x, y, color):
        self.nombre = nombre
        self.x = x
        self.y = y
        self.color = color
    
    def area(self):
        print('metodo para calcular el area')
    
    def perimetro(self):
        print('metodo para calcular el perimetro')
    
    def info(self):
        print(self.nombre, self.color)


class Reactangulo(FormaGeometrica):

    def __init__(self, base, altura, nombre, x, y, color):
        self.base = base
        self.altura = altura
        FormaGeometrica.__init__(self, nombre, x, y, color)

    def area(self):
        return self.base * self.altura

    def perimetro(self):
        return 2 * self.altura + 2 * self.base

from math import pi

class Circulo(FormaGeometrica):

    def __init__(self, radio, nombre, x, y, color):
        self.radio = radio
        FormaGeometrica.__init__(self, nombre, x, y, color)

    def area(self):
        return pi * self.radio ** 2

    def perimetro(self):
        return 2 * pi * self.radio


class Triangulo(FormaGeometrica):

    def __init__(self, base, altura, altura2, nombre, x, y, color):
        self.base = base
        self.altura = altura
        self.altura2 = altura2
        FormaGeometrica.__init__(self, nombre, x, y, color)
    
    def area(self):
        return self.base * self.altura / 2
    
    def perimetro(self):
        return self.base + self.altura + self.altura2

formas = []

r1 = Reactangulo(3, 6, 'rectangulo 1', 5, 7, 'rojo')
formas.append(r1)
r2 = Reactangulo(5, 4, 'rectangulo 2', 15, 70, 'azul')
formas.append(r2)
c1 = Circulo(9, 'circulo 1', -6, 21, 'negro')
formas.append(c1)
c2 = Circulo(2, 'circulo 2', -16, 2, 'violeta')
formas.append(c2)
t1 = Triangulo(3, 1, 4, 'triangulo 1', 4, 0, 'amarillo')
formas.append(t1)


for elemento in formas:
    elemento.info()
    print('area:', elemento.area())
    print('perimetro:', elemento.perimetro())