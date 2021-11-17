# # Modelar auto

# class Automovil:

#     def __init__(self, modelo, marca, color):
#         self.modelo = modelo
#         self.marca = marca
#         self.color = color
#         self._estado = "en_reposo"
#         self._motor = Motor(cilindros=4)

#     def acelerar(self, tipo="despacio"):
#         if tipo == "rapida":
#             self._motor.inyecta_gasolina(10)
#         else:
#             self._motor.inyecta_gasolina(3)
        
#         self._estado = "en_movimiento"


# class Motor:

#     def __init__(self, cilindros, tipo="gasolina"):
#         self.cilindros = cilindros
#         self.tipo = tipo
#         self._temperatura = 0
    
#     def inyecta_gasolina(self, cantidad):
#         pass

###############################################

class Computadora:

    def __init__(self, marca, tipo ,modelo, color):
        self.marca = marca
        self.tipo = tipo
        self.modelo = modelo
        self.color = color
        self._temperatura = 0
        self._config_teclado = 'American'


    def encender(self, estado=False):
        if estado:
            self._temperatura += 20
            print(f'La pc esta encencida, su temperatura es {self._temperatura}º!')
        else:
            print(f'La pc esta apagada, su temperatura es {self._temperatura}º')

    def sistema(self, sistema_operativo):
        if sistema_operativo == 'linux':
            print('Tu si que eres un verdadero cientifico computacional!')
        elif sistema_operativo == 'mac os':
            print('Eres un ingeniero de software que invierte en sus equipos para optimizar su tiempo')
        elif sistema_operativo == 'windows':
            print('Meeeeh esa excusa de los juegos ya no sirve, hay muchisimos juegos ya para Linux. Estudia e invierte en ti!')
        else:
            print('Eres una persona rara!')

# class Procesador:

#     def __init__(self, fabricante, modelo, frecuencia, nucleos, hilos, funciona=True):
#         self.fabricante = fabricante
#         self.modelo = modelo
#         self.frecuencia = frecuencia
#         self.nucleos = nucleos
#         self.hilos = hilos
#         self.funciona = funciona

# class MemoriaRam():

#     def __init__(self, fabricante, capacidad, funciona=True):
#         self.fabricante = fabricante
#         self.capacidad = capacidad
#         self.funciona = funciona

if __name__ == '__main__':
    pc1 = Computadora('HP', 'Laptop','Notebook pro 15', 'Negra')
    print(pc1.encender(True))
    print(pc1.sistema('linux'))

    # pc1_procesador = Procesador('AMD', 'Ryzen 3 1200', '3.7', '4', '4', True)
    # IDK Why print None!!!