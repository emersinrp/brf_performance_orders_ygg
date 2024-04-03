from locust import between, task, HttpUser, tag
import os
from dotenv import load_dotenv
from helpers.bodycreator_post_orders import create_central_post_orders, create_bees_post_orders, \
    create_mex_post_orders, create_mer_post_orders, create_souk_post_orders
from helpers.auth import get_authentication
from helpers.rules import rules_post_order

failureMessage = "Order não criada"
print("Key 1:")
load_dotenv()


class CargaOrdersBees(HttpUser):
    host = os.environ["KONG_ORDERS_QAS"]
    wait_time = between(1.0, 3.0)
    prefix_orders = os.environ["PREFIX_OPERATION_ORDER"]

    def on_start(self):
        self.authorization_qas = get_authentication()

    # Post de orders BEES
    @task
    def create_order_bees(self):
        post_orders = f"{self.prefix_orders}"
        body = create_bees_post_orders()

        # Authorization/Headers Keys QAs: -> Comentado para utilizar em ambiente de DEV
        self.client.headers['Authorization'] = f'{self.authorization_qas}'
        print(self.authorization_qas)
        rules_post_order(self.client, body, post_orders, "Bees")

    # Post de orders CENTRAL
    @task
    def create_order_central(self):
        post_orders = f"{self.prefix_orders}"
        body = create_central_post_orders()

        # Authorization/Headers Keys QAs: -> Comentado para utilizar em ambiente de DEV
        self.client.headers['Authorization'] = f'{self.authorization_qas}'
        print(self.authorization_qas)
        rules_post_order(self.client, body, post_orders, "Central")

    # Post de orders MERCADO EXTERNO
    @task
    def create_order_mex(self):
        post_orders = f"{self.prefix_orders}"
        body = create_mex_post_orders()

        # Authorization/Headers Keys QAs: -> Comentado para utilizar em ambiente de DEV
        self.client.headers['Authorization'] = f'{self.authorization_qas}'
        print(self.authorization_qas)
        rules_post_order(self.client, body, post_orders, "Mercado Ext")

    # Post de orders MERCATO
    @task
    def create_order_mer(self):
        post_orders = f"{self.prefix_orders}"
        body = create_mer_post_orders()

        # Authorization/Headers Keys QAs: -> Comentado para utilizar em ambiente de DEV
        self.client.headers['Authorization'] = f'{self.authorization_qas}'
        print(self.authorization_qas)
        rules_post_order(self.client, body, post_orders, "Mercato")

    # Post de orders SOUK
    @task
    def create_order_souk(self):
        post_orders = f"{self.prefix_orders}"
        body = create_souk_post_orders()

        # Authorization/Headers Keys QAs: -> Comentado para utilizar em ambiente de DEV
        self.client.headers['Authorization'] = f'{self.authorization_qas}'
        print(self.authorization_qas)
        rules_post_order(self.client, body, post_orders, "Souk")
