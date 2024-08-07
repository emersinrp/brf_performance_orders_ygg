# BRF Performance Orders YGG

Este projeto é uma aplicação para gerenciamento e teste de performance de pedidos na plataforma YGG da BRF. O objetivo é criar, enviar e monitorar pedidos através de várias interfaces de API, garantindo a robustez e eficiência do sistema.

## Estrutura do Projeto

```plaintext
brf_performance_orders_ygg/
├── .env
├── .gitignore
├── README.md
├── requirements.txt
├── helpers/
│   ├── __init__.py
│   ├── auth.py
│   ├── bodycreator_post_orders.py
│   ├── rules.py
│   ├── order_creator.py
├── locustfiles/
│   ├── __init__.py
│   ├── locustfile_health.py
│   ├── locustfile_operation_order.py
├── logs/
│   ├── order_success.log
│   └── order_error.log
└── .idea/
```

## Configuração:
**Pré-requisitos:**
    
    Python 3.8+
    pip (Python package installer)

## Instalação:

1. Clone o repositório:
    ```bash
    git clone https://github.com/seu_usuario/brf_performance_orders_ygg.git
    cd brf_performance_orders_ygg
    ```

2. Crie um ambiente virtual e ative-o:
    ```bash
    python -m venv venv
    source venv/bin/activate  # No Windows, use `venv\Scripts\activate`
    ```

3. Instale as dependências:
    ```bash
    pip install -r requirements.txt
    ```

4. Configure o arquivo .env com suas credenciais e URLs apropriadas. Um exemplo de configuração está disponível abaixo.

```plaintext
# URLs
AUTH_URL="https://ygg-qas.brf.cloud/token"
KONG_ORDERS_QAS="https://ygg-qas.brf.cloud/operation-order"
DNS_ORDERS_QAS="https://operation-order-qas.brf.cloud"
DNS_ORDERS_DEV="https://operation-order-dev.brf.cloud"
URL_CALLBACK_DEV="https://ygg-dev.brf.cloud/api-post-order-ygg/api/ok"

# Prefixos
PREFIX_HEALTH_CHECK="/health/"
PREFIX_OPERATION_ORDER="/order/"
PREFIX_PUT_OPERATION_ORDER="/order/operation-order/{{identifier}}"
PREFIX_GET_OPERATION_ORDER="/order/operation-order/{{identifier}}"

# Credenciais
CLIENT_ID="financial"
CLIENT_SECRET_HEADER_AUTH="your_client_secret_header_here"
CLIENT_SECRET_PAYLOAD_AUTH="your_client_secret_payload_here"
AUTH_COOKIE="your_auth_cookie_here"

# Outros
IP_ORDERS_QAS="ip_application"
```

## Estrutura dos Módulos

**helpers/auth.py:**
Este módulo contém a função get_authentication que obtém o token de autenticação necessário para interagir com a API YGG.

**helpers/bodycreator_post_orders.py:**
Este módulo contém funções que geram os corpos das requisições de pedidos para diferentes parceiros como BEES, CENTRAL, MEX, MER e SOUK.

**helpers/rules.py:**
Este módulo contém funções que lidam com as regras de envio e recebimento de pedidos, incluindo a lógica para tratamento de sucesso e falha nas requisições e o registro de logs.

**helpers/order_creator.py:**
Este módulo abstrai a criação e envio de pedidos, organizando as chamadas para diferentes parceiros e unificando a lógica de autorização e envio.

**locustfiles/locustfile_health.py:**
Este módulo usa Locust para testar a saúde da API de pedidos, enviando requisições periódicas para garantir que o serviço esteja funcionando corretamente.

**locustfiles/locustfile_operation_order.py:**
Este módulo usa Locust para testar a criação de pedidos na API de pedidos, utilizando as funções definidas em order_creator.py para enviar pedidos reais.

## Execução
**Testando a Saúde da API:**
Para executar o teste de saúde da API, use o Locust:
```bash
locust -f locustfiles/locustfile_health.py
```

**Testando a Criação de Pedidos:**
Para executar o teste de criação de pedidos, use o Locust:
```bash
locust -f locustfiles/locustfile_operation_order.py
locust --headless -f locustfiles/locustfile_operation_order.py --users 1 --spawn-rate 1
locust --headless -f locustfiles/locustfile_operation_order.py --tags test1 --users 1 --spawn-rate 1
locust -f .\locustfiles\locustfile_operation_order.py
locust -f locustfiles/ --users 10 --spawn-rate 1
```

**Logs:**
Os logs de sucesso e erro das requisições são armazenados nos arquivos "logs/order_success.log" e "logs/order_error.log", respectivamente.

## Contribuição:
    Faça um fork do projeto.
    Crie uma branch para sua feature (git checkout -b feature/AmazingFeature).
    Commit suas mudanças (git commit -m 'Add some AmazingFeature').
    Faça um push para a branch (git push origin feature/AmazingFeature).
    Abra um Pull Request.

## Contato:
Emerson Rodrigues - el.silvarodrigues@gmail.com

Link do Projeto: https://github.com/emersinrp/brf_performance_orders_ygg