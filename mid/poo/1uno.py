# # Definción de clase
# class nombre_de_la_clase(super_clase):

#     def __init__(self, params):
#         pass

#     def nombre__del_método(self, params):_
#         pass

############################

# Definición
class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def saluda(self, otra_persona):
        return f'Hola {otra_persona.nombre}, me llamo {self.nombre}.'

# Uso
david = Persona('David', 35)
erika = Persona('Erika', 32)

david.saluda(erika)