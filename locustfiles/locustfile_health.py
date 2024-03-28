from locust import between, task, HttpUser, tag
import os
from dotenv import load_dotenv
from helpers.rules import rules_get_health

failureMessage = "Health check, falhou"
load_dotenv()


class CargaHealthCheckOrders(HttpUser):
    host = os.environ["DNS_ORDERS_DEV"]
    wait_time = between(1.0, 3.0)
    prefix_health_check = os.environ["PREFIX_HEALTH_CHECK"]

    @task
    def health_check(self):
        consult_orders_health_check = f"{self.prefix_health_check}"
        rules_get_health(self.client, consult_orders_health_check, "Health")

