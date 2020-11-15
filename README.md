# Backend

## Ambiente de Desenvolvimento
O ambiente de desenvolvimento está organizado basicamente em 3 partes:
- Servidor que faz o gerenciamento de mensagens e envio de dados para o front-end
- Script para simular os dados a serem enviados pela ESP32
- Script para simular a interface do front-end

Para a utilização da aplicação principal será necessário a instalação da ferramenta Docker, responsável pela conteinerização. Com o Docker instalado, será necessário navegar até a pasta **sensor_service** e digitar o comando abaixo:
    
    $ docker-compose up --build
    
Após isso, o servidor estará disponível e será indicada uma porta onde o gerenciador do RabbitMQ poderá ser visualizado. Como exemplo <http:/localhost:15672>

Os scripts criados poderão ser usados após a instalação de alguns pacotes. A instalação poderá ser feita pelo comando abaixo:
    
    $  pip3 install -r requirements.txt

Com os pacotes instalados e com o servidor disponível, os scripts deverão ser executados pelos comandos:
    
    $  python3 scripts/send.py
    $  python3 scripts/wsclient.py

Lembrando que ambos não são necessários para o funcionamento do projeto e devem ser executados de acordo com a necessidade do desenvolvedor.
