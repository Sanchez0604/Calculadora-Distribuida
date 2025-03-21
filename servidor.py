import socket
import threading
import logging

# Configuração do logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def processar_operacao(operacao):
    """Processa a operação matemática e retorna o resultado."""
    try:
        resultado = eval(operacao)
        return str(resultado)
    except Exception as e:
        return f"Erro: {e}"

def lidar_com_cliente(cliente_socket, endereco):
    """Lida com a comunicação com um cliente."""
    thread_id = threading.get_ident()
    logging.info(f"Thread {thread_id} iniciada para {endereco}")
    print(f"Conexão de {endereco} estabelecida.")
    while True:
        dados = cliente_socket.recv(1024).decode()
        if not dados:
            break
        resultado = processar_operacao(dados)
        cliente_socket.send(resultado.encode())
    print(f"Conexão de {endereco} encerrada.")
    logging.info(f"Thread {thread_id} encerrada para {endereco}")
    cliente_socket.close()

def iniciar_servidor(host, porta):
    """Inicia o servidor e aguarda conexões de clientes."""
    servidor_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    servidor_socket.bind((host, porta))
    servidor_socket.listen(5)
    print(f"Servidor ouvindo em {host}:{porta}")

    while True:
        cliente_socket, endereco = servidor_socket.accept()
        thread_cliente = threading.Thread(target=lidar_com_cliente, args=(cliente_socket, endereco))
        thread_cliente.start()

if __name__ == "__main__":
    HOST = '0.0.0.0'  # Aceita conexões de qualquer IP
    PORTA = 65432
    iniciar_servidor(HOST, PORTA)