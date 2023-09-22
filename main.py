import threading
import time

from colmenero import Colmenero
from abeja import Abeja


def suma(*args):
    try:
        while True:
            print("SUMA -> ",str(args))
            time.sleep(1)
    except Exception as error:
        print(error)


def decir_algo(*args):
    print("decir algo -> ", str(*args))


if __name__ == '__main__':
    colmena1 = Colmenero(id=1, targets=[suma])
    colmena2 = Colmenero(id=2, targets=[decir_algo])
    colmena1.start()
    colmena2.start()
    colmena2.join()