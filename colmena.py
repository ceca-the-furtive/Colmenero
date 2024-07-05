import multiprocessing
import threading
import time


class Hive_type():
    queens = []
    bees = []

    def exec(self):
        while True:
            self.decelerate_cond = False
            if len(self.bees) < 1 and len(self.queens) < 1:
                self.decelerate_cond = True
            if self.decelerate_cond:
                time.sleep(1)
            if len(self.bees) > 0:
                for bee in self.bees:
                    try:
                        Bee(str(bee.beename), bee.target).start()
                        self.bees.pop(0)
                    except Exception as error:
                        print(error)
                        try:
                            self.bees.pop(0)
                        except Exception as error:
                            print(error)
            if len(self.queens) > 0:
                for queen in self.queens:
                    try:
                        Queen(str(queen.beename), queen.target, queen.args).start()
                        self.queens.pop(0)
                    except Exception as error:
                        print(error)
                        try:
                            self.queens.pop(0)
                        except Exception as error:
                            print(error)

    def addqueen(self, name, target, args):
        self.queens.append(Queen(name, target, args))

    def addqueenObject(self, queenObject):
        self.queens.append(queenObject)

    def addbee(self, name, target):
        self.bees.append(Bee(name, target))

    def addbeeObject(self, beeObject):
        self.bees.append(beeObject)

    def printbeelist(self):
        if len(self.bees) > 0:
            print("bees list -> ", self.bees)

    def printqueenlist(self):
        if len(self.queens) > 0:
            print("bees list -> ", self.queens)

    def printlists(self):
        self.printqueenlist()
        self.printbeelist()


class Queen(multiprocessing.Process, Hive_type):
    name = "Queen"
    beename = None

    def __init__(self, nam: str, target, args: []):
        super().__init__(name=nam, target=target, args=args)
        Hive_type().__init__()
        self.beename = nam
        self.queens = []
        self.bees = []

    def run(self):
        self.ex()
        self.exec()

    def ex(self):
        print("Queen " + self.beename)

    def printbeelist(self):
        if len(self.bees) > 0:
            print(self.beename + " bees list -> ", self.bees)

    def printqueenlist(self):
        if len(self.queens) > 0:
            print(self.beename + " queens list -> ", self.queens)


class Bee(threading.Thread):
    beename = None

    def __init__(self, nam: str, target):
        super().__init__(target=target)
        self.beename = nam

    def run(self) -> None:
        print(self.beename)
        super().run()


class Honey(multiprocessing.Process, Hive_type):

    def __init__(self):
        super().__init__()
        Hive_type().__init__()
        self.queens = []
        self.bees = []

    def run(self):
        self.exec()


class Coche(Honey):

    def __init__(self):
        super().__init__()
        self.ruedas = []

    def exec(self):
        i = 1
        while i <= 4:
            Rueda("rueda" + str(i)).start()
            i += 1


class Rueda(Bee):
    def __init__(self, nam: str):
        super().__init__(nam)

    def run(self) -> None:
        while True:
            print("velocidad")


if __name__ == '__main__':
    colmena = Honey()
    colmena.addqueen("1")
    colmena.addqueen("2")
    colmena.addbee("1")
    colmena.start()