# Calculadora-Distribuida
Atividade da materia de Sistemas paralelos e distribuidos

##Sockets e multithreading

Foi solicitada a criação de um servidor de cálculo distribuído, onde clientes enviam operações matemáticas para o servidor, e ele retorna o resultado. O servidor deve ser capaz de lidar com múltiplos clientes simultaneamente usando threads.

###Objetivo:
Implementar um servidor que recebe operações matemáticas de múltiplos clientes, processa-as e retorna o resultado. O servidor deve usar multithreading para lidar com várias requisições ao mesmo tempo.

##Requisitos:
###Servidor:

Aceita conexões de múltiplos clientes.

Cada cliente é tratado em uma thread separada.

Recebe operações matemáticas (ex: 2 + 3 ou 10/2) dos clientes.

Processa a operação e envia o resultado de volta ao cliente.

###Cliente:

Conecta-se ao servidor.

Envia operações matemáticas para o servidor.

Recebe e exibe o resultado.

 

##Informações úteis 
O servidor escuta em uma porta específica (65432)

Para cada cliente conectado, uma nova thread é criada.

A thread processa as operações enviadas pelo cliente e retorna o resultado.

 
