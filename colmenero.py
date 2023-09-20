import threading
import time
from multiprocessing import Process

from abeja import Abeja


class Colmenero(threading.Thread):
    id = 0
    process_tail = []
    process_executor = None

    def __init__(self, id, *args, **kwargs, ):
        super(Colmenero, self).__init__(*args, **kwargs)
        self.id = id
        # self.process_executor = concurrent.futures.ProcessPoolExecutor()

    def run(self):
        while True:
            try:
                time.sleep(1)
                self.process_manager()
                time.sleep(1)
                print("Colmena", self.id)
                # self.process_tail.append(Abeja(suma,2))
                # print(len(self.process_tail))
            except Exception as error:
                print(error)
            # self.gestor2()
            if len(self.process_tail) > 0:
                None

    def process_manager(self):
        process_list = []
        if len(self.process_tail) > 0:
            for abeja in self.process_tail:
                time.sleep(1)
                p = Process(name="Alza " + abeja.name, target=alza, args=abeja.arguments)
                process_list.append(p)
                self.process_tail.remove(abeja)

            for p in process_list:
                p.start()
                time.sleep(1)

    def addbee(self, *abejas):
        for abeja in abejas:
            self.process_tail.append(abeja)

    def delbee(self, abeja_name):
        for abeja in self.process_tail:
            if abeja.name == abeja_name:
                self.process_tail.pop(abeja)

    def create_bee(self, name, alza, metodo, *args):
        self.addbee(Abeja(name, alza, metodo, args))


def alza(*args):
    name = ""
    target = None
    argumentos = []

    i = 0
    for dato in args:
        if i == 0:
            name = dato
            i += 1
        elif i == 1:
            target = dato
            i += 1
        else:
            argumentos.append(dato)

    media_alza(name, target, argumentos)

    #


def media_alza(name, target, argumentos):
    print(name, target, argumentos)
    threading.Thread(name=name, target=target, args=argumentos)