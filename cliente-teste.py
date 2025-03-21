import socket
import threading

def cliente(host, porta, operacao):
    """Conecta-se ao servidor, envia a operação e recebe o resultado."""
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as cliente_socket:
        cliente_socket.connect((host, porta))
        cliente_socket.sendall(operacao.encode())
        dados = cliente_socket.recv(1024)
    print(f"Operação: {operacao}, Resultado: {dados.decode()}")

def testar_conexoes_multiplas(host, porta, operacoes):
    """Cria várias threads para enviar cálculos diferentes ao servidor."""
    threads = []
    for operacao in operacoes:
        thread = threading.Thread(target=cliente, args=(host, porta, operacao))
        threads.append(thread)
        thread.start()

    # Aguarda todas as threads terminarem
    for thread in threads:
        thread.join()

if __name__ == "__main__":
    HOST = input("Digite o endereço do servidor: ")
    PORTA = 65432
    operacoes = [
        "2 + 3",
        "10 / 2",
        "5 * 4",
        "10 - 7",
        "2 ** 3",
        "15 % 4",
        "1 + 2 * 3",
        "(10 + 5) / 3",
    ]

    testar_conexoes_multiplas(HOST, PORTA, operacoes)
    print("Todos os cálculos foram enviados.")