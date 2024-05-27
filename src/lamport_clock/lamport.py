from multiprocessing import Process, Pipe
from os import getpid
from datetime import datetime



def local_time(counter):
    """"
   Imprime a data/hora local do Lamport e a hora real na máquina que executa os processos. 

    """
    return ' (LAMPORT_TIME={}, LOCAL_TIME={})'.format(counter,
                                                     datetime.now())


def calc_recv_timestamp(recv_time_stamp, counter):
    """
    Calcula o novo valor de data/hora quando um processo recebe uma mensagem. 
    A função pega o máximo de data/hora recebido e seu contador local e o incrementa em um.
    """
    return max(recv_time_stamp, counter) + 1


def event(pid, counter):
    """
    Função para cada evento que possa ocorrer. 
    No exemplo são três eventos: evento (qualquer evento local), mensagem enviada e mensagem recebida. 
    Para facilitar a leitura do código, as funções de evento retornarão a data/hora atualizado do processo onde 
    o evento ocorre.
    O evento event pega o contador local e o id do processo (pid), incrementa o contador em um, 
    imprime uma linha para saber que o evento ocorreu e retorna o contador incrementado.
    """
    counter += 1
    print('Alguma coisa aconteceu em {} !'.\
          format(pid) + local_time(counter))
    return counter


"""
O evento send_message também usa o pid e o contador como entrada, mas requer adicionalmente um canal.
Um Pipe é um objeto da biblioteca de multiprocessamento que representa uma conexão bidirecional entre dois 
processos. Cada pipe consiste em dois objetos de conexão, um em cada direção. Para enviar ou receber uma mensagem,
precisamos chamar a função send ou recv nesses objetos de conexão.
No exemplo, precisamos de apenas de dois canais de mensagens. Um entre o processo 1 e o processo 2, e outro entre
o processo 2 e o processo 3. 
Portanto, este exemplo terá quatro objetos de conexão: pipe12, pipe21, pipe23 e pipe32.
"""

def send_message(pipe, pid, counter):
    """
    O evento send_message primeiro incrementa o contador em um, depois envia uma mensagem real 
    (o conteúdo não é importante aqui) e seu valor de data/hora incrementado e imprime uma declaração
    curta incluindo o novo horário local de Lamport e o horário real na máquina. 
    Assim como todas as  funções de evento, ela retorna o valor de data/hora local.
    """
    counter += 1
    pipe.send(('Shell vazio', counter))
    print('Messagem enviada de ' + str(pid) + local_time(counter))
    return counter

def recv_message(pipe, pid, counter):
    """
    O evento recv_message usa os mesmos três argumentos que send_message. 
    Ele recebe a mensagem real e o valor de data/hora invocando a função recv no canal. 
    Em seguida, ele calcula o novo carimbo de data/hora com nossa função calc_recv_timestamp criada 
    anteriormente e imprime uma linha incluindo o contador atualizado e a hora real na máquina.
    """
    message, timestamp = pipe.recv()
    counter = calc_recv_timestamp(timestamp, counter)
    print('Message received at ' + str(pid)  + local_time(counter))
    return counter


"""
Cada processo começa obtendo seu ID de processo exclusivo (este é o ID real do processo em execução 
na  máquina) e definindo seu próprio contador como 0. Em seguida, o contador é atualizado invocando as 
diferentes funções de evento e passando o valor retornado para o contador.
"""

def process_one(pipe12):
    pid = getpid()
    counter = 0
    counter = event(pid, counter)
    counter = send_message(pipe12, pid, counter)
    counter  = event(pid, counter)
    counter = recv_message(pipe12, pid, counter)
    counter  = event(pid, counter)

def process_two(pipe21, pipe23):
    pid = getpid()
    counter = 0
    counter = recv_message(pipe21, pid, counter)
    counter = send_message(pipe21, pid, counter)
    counter = send_message(pipe23, pid, counter)
    counter = recv_message(pipe23, pid, counter)


def process_three(pipe32):
    pid = getpid()
    counter = 0
    counter = recv_message(pipe32, pid, counter)
    counter = send_message(pipe32, pid, counter)


if __name__ == '__main__':
    oneandtwo, twoandone = Pipe()
    twoandthree, threeandtwo = Pipe()

    process1 = Process(target=process_one, 
                       args=(oneandtwo,))
    process2 = Process(target=process_two, 
                       args=(twoandone, twoandthree))
    process3 = Process(target=process_three, 
                       args=(threeandtwo,))

    process1.start()
    process2.start()
    process3.start()

    process1.join()
    process2.join()
    process3.join()