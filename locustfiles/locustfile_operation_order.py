from locust import between, task, HttpUser, tag
import os
from dotenv import load_dotenv
from helpers.bodycreator_post_orders import create_central_post_orders, create_bees_post_orders
from helpers.auth import get_authentication
from helpers.rules import rules_post_order

failureMessage = "Order não criada"
print("Key 1:")
load_dotenv()


class CargaOrdersBees(HttpUser):
    host = os.environ["DNS_ORDERS_DEV"]
    wait_time = between(1.0, 3.0)
    prefix_orders = os.environ["PREFIX_OPERATION_ORDER"]

    def on_start(self):
        self.authorization_qas = get_authentication()

    @tag('test1')
    @task
    def create_order_bees(self):
        post_orders = f"{self.prefix_orders}"
        body = create_bees_post_orders()

        # Authorization/Headers Keys QAs: -> Comentado para utilizar em ambiente de DEV
        #self.client.headers['Authorization'] = f'{self.authorization_qas}'
        #print(self.authorization_qas)
        rules_post_order(self.client, body, post_orders, "Bees")

    @task
    def create_order_central(self):
        post_orders = f"{self.prefix_orders}"
        body = create_central_post_orders()

        # Authorization/Headers Keys QAs: -> Comentado para utilizar em ambiente de DEV
        #self.client.headers['Authorization'] = f'{self.authorization_qas}'
        #print(self.authorization_qas)
        rules_post_order(self.client, body, post_orders, "Central")

