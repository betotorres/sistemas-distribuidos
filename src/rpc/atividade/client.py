import rpyc
import sys
import random
import time


if len(sys.argv) < 3:
   exit("Usage {} SERVER NUMBER_ELEMENTS".format(sys.argv[0]))

#captura o servidor
server = sys.argv[1]

#captura a quantidade de elementos do array
n_elements = int(sys.argv[2])

#gera numeros aleatorios de 1 a 10 no array
array = [random.randint(1, 10) for i in range(0, n_elements)]

#conecta no servidor
conn = rpyc.connect(server,18080)

start_time = time.time()
result = conn.root.sumarray(array)
end_time = time.time()

print(result)
print(end_time-start_time)
   
