import socket


def servidor(host = 'localhost', port=8031):
    """
    Método para iniciar o servidor. O parâmetro host/port definem o ip/nome da máquina
    servidora e a porta onde o serviço será provido.
    """

    #Define a quantidade máxima de dados que podem ser recebido de uma única vez
    data_payload = 2048 
    
    #Cria um socket TCP
    with socket.ssocket(socket.AF_INET, socket.SOCK_STREAM) as s:

        #Associa o socket a uma porta
        endereco_servidor = (host, port)
        s.bind(endereco_servidor)

        #Escuta os clientes e define o número máximo de clientes na fila
        s.listen(5)

        while True: 
            print ("Aguardando para Recever Mensagens do Cliente")
            client, address = s.accept() 
            with client:
                print(f"Connected by {address}")
  
                while True:
                    data = client.recv(1024)
                    if not data:
                        client.close()
                        break
                    else:
                        print(f"Mensagem Recebida {data}")
                    client.sendall(data)



if __name__ == '__main__':
    servidor()