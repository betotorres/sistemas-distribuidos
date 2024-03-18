import socket

def client(host = 'localhost', port=8032, mensagem=''): 
       
    try: 

        # Cria um socket TCP/IP 
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            #Conecta no servidor
            s.connect((host, port))

            #envia a mensagem
            s.sendall(mensagem.encode('utf-8'))

            #Obtem o retorno
            dados_recebidos = s.recv(2048)
            if len(dados_recebidos) == 0:
                raise socket.error

            #Imprime os dados Recebidos
            dados_recebidos = dados_recebidos.decode("utf-8")
            print(f'O resultado é : {dados_recebidos}')


        
    except socket.error as e: 
        raise Exception(f"Erro na conexão com o Servidor: {e}") 
    except Exception as e: 
        raise Exception(f"Erro Geral: {e}") 




if __name__ == "__main__":

    while True:
        mensagem = input('Digite a operacao matematica no formato Num1 Operador Num2 ou SAIR: \n')
        if mensagem == 'SAIR':
            break
        try:
            client('localhost', 8031, mensagem)
        except:
            try:
                client('localhost', 8033, mensagem)
            except:
                 pass
    