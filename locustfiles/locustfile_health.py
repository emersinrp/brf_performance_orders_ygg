from locust import between, task, HttpUser, tag
import os
from dotenv import load_dotenv

failureMessage = "Health check, falhou"
load_dotenv()


class CargaHealthCheckOrders(HttpUser):
    host = os.environ["DNS_ORDERS_QAS"]
    wait_time = between(1.0, 3.0)
    prefix_health_check = os.environ["PREFIX_HEALTH_CHECK"]

    @tag('test1')
    @task
    def health_check(self):
        consult_orders_health_check = f"{self.prefix_health_check}"

        with self.client.get(url=consult_orders_health_check,
                             name="Carga Orders - Get Health",
                             catch_response=True) as response:

            if response.status_code == 200:
                resposta = response.json()

                if resposta['aplication_message'] == "May the Orders be with YOU!":
                    print(
                        f"---- SUCESSO NA CONSULTA ----\n"
                        f"Response: {resposta['aplication_message']} \n"
                        f"STATUS CODE: {response.status_code} \n")

                else:
                    print(
                        f"---- FALHA NA CONSULTA ----\n {response.text} \n "
                        f"STATUS CODE: {response.status_code} \n")
                    response.failure(
                        failureMessage + f" Status CODE: {response.status_code}"
                    )
            else:
                print(
                    f"---- FALHA NA CONSULTA ----\n {response.text} \n STATUS CODE: {response.status_code}")
                response.failure(
                    failureMessage + f" Status CODE: {response.status_code}"
                )
