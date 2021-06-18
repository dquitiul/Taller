class Aves:
    def volar(self):
        print('La mayoria de las aves pueden volar pero algunas no')

class Aguila(Aves):
    def volar(self):
        print('Las aguilas pueden volar')

class Gallina(Aves):
    def volar(self):
        print('La gallina no puede volar')
        

ave_tipo = Aves()
ave_aguila = Aguila()
ave_gallina = Gallina()
ave_tipo.volar()
ave_aguila.volar()
ave_gallina.volar()
