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

    def exposed_fib(self,n):
        seq = []
        a, b = 0,1
        while a < n:
            seq.append(a)
            a, b = b, a+b
        return seq
    
    def get_question(self):  
        # este método não é exposto
        return "Em que ano Nasceu Albert Einstein?"
    
    def exposed_get_question(self):
        return self.get_question()
    
    
if __name__ == '__main__':
    ts = ThreadedServer(MathService,port=18080)
    print('Service started on port 18080')
    ts.start()