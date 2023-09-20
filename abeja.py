class Abeja():
    name = None
    arguments = []

    def __init__(self, nombre, *args):
        print("Hola soy abeja de ", nombre)
        self.name = nombre
        self.arguments = args