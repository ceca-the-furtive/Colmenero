import multiprocessing
import threading
import time

from abeja import Abeja


class Colmenero(multiprocessing.Process):
    id = 0
    process_tail = []
    targets = []

    def __init__(self, **kwargs):
        super(Colmenero, self).__init__()

    def run(self):
        try:
            time.sleep(1)
            print(self.targets)
        except Exception as error:
            print(error)

    def add_bee_kw(self, **kwargs):
        abeja = Abeja()
        counter = 0
        if len(kwargs.items()) > 1:
            for key, value in kwargs.items():
                if key[:6] == "target":
                    abeja.add_name("Abeja " + str(value))
                    abeja.add_target(value)
                if key[:6] == "params":
                    abeja.add_argument_list(value)
                counter += 1
                if counter >= 2:
                    self.targets.append(abeja)
                    abeja = None
                    counter = 0
        else:
            abeja = Abeja()
            for key, value in kwargs.items():
                if key[:6] == "target":
                    abeja.add_name("Abeja " + str(value))
                    abeja.add_target(value)
                if key[:6] == "params":
                    abeja.add_argument_list(value)
                self.targets.append(abeja)
                abeja = None

    def add_bee(self, target, params: tuple):
        abeja = Abeja()
        abeja.add_target(target)
        abeja.add_argument_list(params)

    def charge_process_list(self):
        for abeja in self.targets:
            if len(abeja.arguments) >= 1:
                p = multiprocessing.Process(target=abeja.target, args=abeja.arguments)
            else:
                p = multiprocessing.Process(target=abeja.target)
            self.process_tail.append(p)

    def run_process_list(self):
        for proceso in self.process_tail:
            proceso.start()

    def seeall(self):
        print("\n")
        print("Process List Line -> ", self.process_tail)
        print("Targets List line-> ", self.targets)
        print("Target List:")
        for target in self.targets:
            print(target)
