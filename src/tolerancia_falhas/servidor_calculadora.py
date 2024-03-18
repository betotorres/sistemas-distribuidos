import socket


def servidor(host = 'localhost', port=8032):
    """
    Método para iniciar o servidor. O parâmetro host/port definem o ip/nome da máquina
    servidora e a porta onde o serviço será provido.
    """

    #Define a quantidade máxima de dados que podem ser recebido de uma única vez
    data_payload = 2048 
    
    #Cria um socket TCP
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:

        #Associa o socket a uma porta
        endereco_servidor = (host, port)
        s.bind(endereco_servidor)

        #Escuta os clientes e define o número máximo de clientes na fila
        s.listen(5)



        while True: 
            print (f"Aguardando para Recever Mensagens do Cliente em {host}:{port}")
            client, address = s.accept() 
            with client:
                print(f"Connected by {address}")
          
                try:
                    while True:
                        data = client.recv(data_payload)
                        print(data)

                        retorno = encontra_operador(data)
                        if retorno:
                            retorno = str(retorno).encode()
                            client.sendall(retorno)
                        else:
                            client.sendall(b'Informe uma Operacao Valida' )
                except Exception as e:
                    print(f'Conexao Finalizada com {address}')


def calcula(num1, num2, operacao):
    num1 = int(num1)
    num2 = int(num2)
    if operacao == '+':
        return num1 + num2
    elif operacao == '-':
        return num1 - num2
    elif operacao == '/':
        return num1 / num2
    elif operacao == '*':
        return num1 * num2


def encontra_operador(data):
    data = data.decode('utf-8').strip()
    array_resultados = [data.find('+'), data.find('-'), data.find('*'), data.find('/')]
    posicao = max(array_resultados)

    if posicao > 0:
        return calcula(data[:posicao], data[posicao+1:], data[posicao: posicao+1])
    else:
        return None



if __name__ == '__main__':
    servidor()