class Abeja():
    name = None
    arguments = []

    def __init__(self, nombre, *args, **kwargs):
        print("Hola soy ", nombre)
        self.name = nombre
        self.arguments = args
        for key, value in kwargs.values():
            print(key, "=", value)
