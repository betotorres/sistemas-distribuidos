import socket

def client(host = 'localhost', port=8031, mensagem='Mensagem de Teste'): 
       
    try: 

        # Cria um socket TCP/IP 
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            #Conecta no servidor
            s.connect((host, port))

            while mensagem != '':
                #envia a mensagem
                s.sendall(mensagem.encode('utf-8'))

                #Obtem o retorno
                dados_recebidos = s.recv(1024)

                #Imprime os dados Recebidos
                print(f'Recebido: {dados_recebidos}')

                mensagem = input()
    
        
    except socket.error as e: 
        print (f"Erro na conexão com o Servidor: {e}") 
    except Exception as e: 
        print (f"Erro Geral: {e}") 
    finally: 
        print ("Encerrando conexão com o Servidor") 


if __name__ == "__main__":
    client()