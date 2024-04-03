from locust import between, task, HttpUser, tag
import os
from dotenv import load_dotenv
from helpers.rules import rules_get_health
from helpers.auth import get_authentication

failureMessage = "Health check, falhou"
load_dotenv()


class CargaHealthCheckOrders(HttpUser):
    host = os.environ["KONG_ORDERS_QAS"]
    wait_time = between(1.0, 3.0)
    prefix_health_check = os.environ["PREFIX_HEALTH_CHECK"]

    def on_start(self):
        self.authorization_qas = get_authentication()

    @task
    def health_check(self):
        consult_orders_health_check = f"{self.prefix_health_check}"

        # Authorization/Headers Keys QAs: -> Comentado para utilizar em ambiente de DEV
        self.client.headers['Authorization'] = f'{self.authorization_qas}'
        print(self.authorization_qas)
        rules_get_health(self.client, consult_orders_health_check, "Health")

