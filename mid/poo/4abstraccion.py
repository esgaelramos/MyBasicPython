class Lavadora:

    def __init__(self):
        pass

    def lavar(self, temperatura=30):
        self._llenar_tanque_agua(temperatura)
        self._anadir_jabon()
        self._lavar()
        self._centrifugar()

    def _llenar_tanque_agua(self, temperatura):
        print(f'Llenando tanque de agua a {temperatura} grados celsius.')

    def _anadir_jabon(self):
        print('Anadiendo jabon para la ropa:)')
    
    def _lavar(self):
        print('¡Lavando ropa!')
    
    def _centrifugar(self):
        print('¡Centrifugando ropa!')

if __name__ == "__main__":
    lavadora = Lavadora()
    lavadora.lavar()