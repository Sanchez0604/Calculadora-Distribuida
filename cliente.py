import socket

def cliente(host, porta, operacao):
    """Conecta-se ao servidor, envia a operação e recebe o resultado."""
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as cliente_socket:
        cliente_socket.connect((host, porta))
        cliente_socket.sendall(operacao.encode())
        dados = cliente_socket.recv(1024)
    return dados.decode()

if __name__ == "__main__":
    HOST = input("Digite o endereço do servidor: ")
    PORTA = 65432

    while True:
        print("\nEscolha uma opção:")
        print("1. Realizar operação")
        print("2. Sair")

        opcao = input("Digite o número da opção: ")

        if opcao == "1":
            operacao = input("Digite a operação: ")
            resultado = cliente(HOST, PORTA, operacao)
            print(f"Resultado: {resultado}")
        elif opcao == "2":
            print("Encerrando o cliente.")
            break
        else:
            print("Opção inválida. Tente novamente.")