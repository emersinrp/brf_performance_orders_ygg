from locust import between, task, HttpUser
import os
import time
import threading
from dotenv import load_dotenv
from helpers.auth import get_authentication
from helpers.order_creator import (
    create_order_bees,
    create_order_central,
    create_order_mex,
    create_order_mer,
    create_order_souk
)

load_dotenv()
token_authorization = get_authentication()
nomeOrder = ""

class CargaOrders(HttpUser):
    host = os.getenv("KONG_ORDERS_QAS")
    wait_time = between(1.0, 3.0)
    prefix_orders = os.getenv("PREFIX_OPERATION_ORDER")

    def on_start(self):
        self.authorization_qas = get_authentication()
        self.client.headers['Authorization'] = self.authorization_qas
        self.start_token_renewal()

    def start_token_renewal(self):
        def renew_token():
            while True:
                time.sleep(250)  # Renova o token a cada 250 segundos
                self.authorization_qas = get_authentication()
                self.client.headers['Authorization'] = self.authorization_qas
                print("Token renovado.")

        token_thread = threading.Thread(target=renew_token)
        token_thread.daemon = True
        token_thread.start()

    @task
    def create_order_bees(self):
        create_order_bees(self.client, self.authorization_qas, self.prefix_orders)

    @task
    def create_order_central(self):
        create_order_central(self.client, self.authorization_qas, self.prefix_orders)

    @task
    def create_order_mex(self):
        create_order_mex(self.client, self.authorization_qas, self.prefix_orders)

    @task
    def create_order_mer(self):
        create_order_mer(self.client, self.authorization_qas, self.prefix_orders)

    @task
    def create_order_souk(self):
        create_order_souk(self.client, self.authorization_qas, self.prefix_orders)
