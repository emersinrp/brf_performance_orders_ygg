from locust import between, task, HttpUser, tag
import os
from dotenv import load_dotenv
from helpers.bodycreator_post_orders import create_central_post_orders, create_bees_post_orders, \
    create_mex_post_orders, create_mer_post_orders, create_souk_post_orders
from helpers.auth import get_authentication
from helpers.rules import rules_post_order
from datetime import datetime, timedelta

failureMessage = "Order não criada"
load_dotenv()
token_authorization = get_authentication()
nomeOrder = ""


class CargaOrdersBees(HttpUser):
    host = os.environ["KONG_ORDERS_QAS"]
    wait_time = between(1.0, 3.0)
    prefix_orders = os.environ["PREFIX_OPERATION_ORDER"]
    token_authorization = ""
    expires_date = None

    def on_start(self):
        self.token_authorization, self.expires_date = get_authentication()
        self.client.headers['Authorization'] = f'{self.token_authorization}'

    def reauth_method(self, body, post_orders, metodo):
        if datetime.now() - timedelta(seconds=-10) >= self.expires_date:
            self.client.headers['Authorization'], self.expires_date = get_authentication()
            rules_post_order(self.client, body, post_orders, metodo)

    # Post de orders BEES
    @task
    def create_order_bees(self):
        post_orders = f"{self.prefix_orders}"
        body = create_bees_post_orders()

        metodo_name = "Bess"
        sucess = rules_post_order(self.client, body, post_orders, metodo_name)
        self.reauth_method(body, post_orders, metodo_name)

    # Post de orders CENTRAL
    @task
    def create_order_central(self):
        post_orders = f"{self.prefix_orders}"
        body = create_central_post_orders()

        metodo_name = "Central"
        sucess = rules_post_order(self.client, body, post_orders, metodo_name)
        self.reauth_method(body, post_orders, metodo_name)

    # Post de orders MERCADO EXTERNO
    @tag('test1')
    @task
    def create_order_mex(self):
        post_orders = f"{self.prefix_orders}"
        body = create_mex_post_orders()

        metodo_name = "Mercado Ext"
        sucess = rules_post_order(self.client, body, post_orders, metodo_name)
        self.reauth_method(body, post_orders, metodo_name)

    # Post de orders MERCATO
    @task
    def create_order_mer(self):
        post_orders = f"{self.prefix_orders}"
        body = create_mer_post_orders()

        metodo_name = "Mercato"
        sucess = rules_post_order(self.client, body, post_orders, metodo_name)
        self.reauth_method(body, post_orders, metodo_name)

    # Post de orders SOUK
    @task
    def create_order_souk(self):
        post_orders = f"{self.prefix_orders}"
        body = create_souk_post_orders()

        metodo_name = "Souk"
        sucess = rules_post_order(self.client, body, post_orders, metodo_name)
        self.reauth_method(body, post_orders, metodo_name)
