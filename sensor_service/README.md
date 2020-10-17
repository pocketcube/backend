# sensor-service

Microsserviço para receber os dados vindos da fila do RabbitMQ e transmitir via WebSockets.

## Configurando e instalando

**ATENÇÃO: Código configurado para rodar em ambientes UNIX**

Primeiro, para instalar os containers Docker, execute:

`docker-compose up`

Depois, execute os scripts de simulação em:

* Simulador dos dados sendo recebidos pelo cliente websocket 

`python scripts/wsclient.py`

* Simulador de sensores emitindo dados para a fila:

`python scripts/send.py`

