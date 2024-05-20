#pip install rpyc

import rpyc
from rpyc.utils.server import ThreadedServer

class MathService(rpyc.Service):
    def on_connect(self,conn):
        # código que é executado quando uma conexão é iniciada, caso seja necessário
        pass
    def on_disconnect(self,conn):
        #  código que é executado quando uma conexão é finalizada, caso seja necessário
        pass

    def exposed_sumarray(self,n:list):
        return sum(n)
    
    
    
if __name__ == '__main__':
    ts = ThreadedServer(MathService,port=18080)
    print('Service started on port 18080')
    ts.start()