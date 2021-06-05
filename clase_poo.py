
#! Programación orientada a objetos

#! Componentes: Clases, Objetos y Mensajes

#! Caracteristicas: Encapsulamiento, Herencia, Polimorfismo

#! Sobrecarga, Constructor, Ocultamiento de la informacíon


class Persona(object):
    """Clase que representa a una persona."""

    def __init__(self, apellido, nombre, edad=None, email=None, n_cuenta=None):
        self.__apellido = apellido
        self.__nombre = nombre
        self.edad = edad
        self.__email = email
        self.__n_cuenta = n_cuenta

    def email(self):
        return self.__mail

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
persona2 = Persona('Gonzalez', 'Maria', 23)
persona3 = Persona('Caseres', 'Julieta')

persona3.set_email("123@123.com")

persona1.mostrar_datos()
persona2.mostrar_datos()
persona3.mostrar_datos()

persona2.edad = 45

print(persona2.edad)


# print(persona1.apellido, persona1.nombre)
# print(persona2.apellido, persona2.nombre)
# print(persona3.apellido, persona3.nombre)
# print(persona1)
# print(persona2)
# print(persona3)
# print(persona1.apellido == persona3.apellido)