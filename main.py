from colmenero import Colmenero


def suma(value, *args):
    return value + 1


def decir_algo(text, *args):
    print(text + str(*args))


if __name__ == '__main__':
    colmena1 = Colmenero(1)
    colmena1.start()
    colmena1.create_bee("abeja1", "alza1", suma, 1)
    colmena1.create_bee("abeja2", "alza2", suma, 5)
    colmena1.create_bee("abeja3", "alza3", decir_algo, "hola")

