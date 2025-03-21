# Calculadora Distribuída - Sistema Paralelo e Distribuído

Este projeto implementa um servidor de cálculo distribuído, no qual múltiplos clientes podem enviar operações matemáticas para um servidor, que processa as requisições e retorna os resultados. A solução usa **Sockets** para comunicação entre cliente e servidor e **Multithreading** para lidar com múltiplos clientes simultaneamente.

## Objetivo

Desenvolver um **servidor** capaz de processar requisições de operações matemáticas enviadas por **múltiplos clientes**. O servidor deve ser capaz de lidar com várias requisições simultâneas utilizando threads para garantir um processamento eficiente e escalável.

### Funcionalidades do Sistema:

- O **servidor** aceita conexões de múltiplos clientes ao mesmo tempo.
- Cada **cliente** envia uma operação matemática para o servidor.
- O **servidor** processa a operação em uma **thread separada** para cada cliente.
- O **servidor** retorna o resultado da operação matemática ao cliente.
- O **cliente** exibe o resultado recebido do servidor.

## Requisitos

### Servidor

- O servidor deve aceitar conexões simultâneas de múltiplos clientes.
- Cada cliente é tratado por uma **thread separada**, garantindo o processamento paralelo.
- O servidor escuta em uma porta específica (porta **65432**).
- O servidor recebe operações matemáticas (exemplo: "2 + 3", "10 / 2", "5 * 6").
- Após o processamento da operação, o servidor envia o **resultado** de volta ao cliente.
- O servidor deve ser capaz de lidar com operações de soma, subtração, multiplicação e divisão.

### Cliente

- O cliente se conecta ao servidor via **socket**.
- O cliente envia a operação matemática para o servidor em formato textual.
- O cliente recebe o **resultado** da operação e exibe na tela.

## Funcionamento

1. **Servidor**:
   - O servidor fica ouvindo na porta **65432** esperando conexões de clientes.
   - Para cada cliente conectado, o servidor cria uma nova **thread**.
   - A thread recebe a operação matemática do cliente, processa e envia o resultado de volta.
   
2. **Cliente**:
   - O cliente solicita a operação matemática ao servidor.
   - O cliente exibe o resultado retornado pelo servidor.

## Tecnologias Utilizadas

- **Sockets**: Para comunicação entre o servidor e os clientes.
- **Multithreading**: Para garantir que o servidor consiga processar várias requisições simultaneamente sem bloquear.
- **Python** (ou outra linguagem de sua preferência): Para implementação do servidor e cliente.

## Como Rodar o Projeto

### 1. Inicie o servidor:
Execute o código do servidor. O servidor ficará ouvindo por novas conexões na porta 65432.

```bash
python servidor.py
