from locust import between, task, HttpUser
import os
from dotenv import load_dotenv
from helpers.rules import rules_get_health
from helpers.auth import get_authentication

load_dotenv()

class CargaHealthCheckOrders(HttpUser):
    host = os.getenv("KONG_ORDERS_QAS")
    wait_time = between(1.0, 3.0)
    prefix_health_check = os.getenv("PREFIX_HEALTH_CHECK")

    def on_start(self):
        self.authorization_qas = get_authentication()
        self.client.headers['Authorization'] = self.authorization_qas

    @task
    def health_check(self):
        consult_orders_health_check = f"{self.prefix_health_check}"
        rules_get_health(self.client, consult_orders_health_check, "Health")
