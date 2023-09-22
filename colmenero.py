import multiprocessing
import threading
import time

from abeja import Abeja


class Colmenero(multiprocessing.Process):
    id = 0
    process_tail = []
    targets = []
    counter= 0

    def __init__(self, **kwargs):
        super(Colmenero, self).__init__()
        for key, value in kwargs.items():
            if key == "id":
                self.id = id
            if key == "targets":
                self.targets = value

    def run(self):
        while True:
            try:
                for target in self.targets:
                    self.process_tail.append(Abeja("abeja1", "alza1", target, 1))
                self.thread_manager()
            except Exception as error:
                print(error)

    def thread_manager(self):
        if len(self.process_tail) > 0:
            for abeja in self.process_tail:
                retValue = media_alza("Media_alza " + abeja.name +" "+ str(self.counter), argumentos=abeja.arguments)
                time.sleep(1)
                self.counter +=1
                if retValue:
                    self.process_tail.remove(abeja)

    # def addbee(self, *abejas):
    #    for abeja in abejas:
    #        self.process_tail.append(abeja)
    #        print("Proces tail -> ", len(self.process_tail))

    # def delbee(self, abeja_name):
    #    for abeja in self.process_tail:
    #        if abeja.name == abeja_name:
    #            self.process_tail.pop(abeja)

    # def create_bee(self, name, alza, metodo, *args):
    #    self.addbee(Abeja(name, alza, metodo, args))


def media_alza(name, argumentos):
    try:
        i=0
        for arg in argumentos:
            if i==0:
                nombre= arg
            elif i==1:
                objetivo= arg
            else:
                arguments= arg
            i+=1
        threading.Thread(name=nombre, target=objetivo, args=[arguments]).start()
    except Exception as error:
        print(error)
