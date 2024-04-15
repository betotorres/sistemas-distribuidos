from threading import Thread
from time import *
from random import *

def dorminhoco(nome: str):
    tempo_inicial = gmtime()
    tempo_sono = randint(1,10)

    print(f"""{nome} está indo dormir as {tempo_inicial.tm_hour}:\{tempo_inicial.tm_min}:{tempo_inicial.tm_sec} por {tempo_sono} segundos""")
    sleep(tempo_sono)

    tempo_final = gmtime()
    print(f"{nome} acordou as {tempo_final.tm_min}:{tempo_final.tm_sec}")


if __name__ == '__main__':

    #Cria as threads
    t1 = Thread(target=dorminhoco, args=('joao', ))
    t2 = Thread(target=dorminhoco, args=('maria', ))

    #Inicia as threads
    t1.start()
    t2.start()

    #Para interromper a execução do programa uma vez que que a thread se completa, utilizamos o método join()
    t1.join()
    t2.join()