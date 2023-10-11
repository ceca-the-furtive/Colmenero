import time

from colmenero import Colmenero

def suma(*args):
    try:
        while True:
            print("SUMA -> ",str(args))
            time.sleep(1)
    except Exception as error:
        print("ERROR suma ->", error)


def decir_algo(*args):
    print("decir algo -> ", str(*args))


if __name__ == '__main__':
    colmena1 = Colmenero()
    colmena1.start()
    colmena1.join()
    colmena1.add_bee_kw(target1=suma, params=[4,4])
    colmena1.charge_process_list()
    colmena1.seeall()
    colmena1.run_process_list()

