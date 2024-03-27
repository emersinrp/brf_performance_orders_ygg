from locust import between, task, HttpUser, tag
import os
from dotenv import load_dotenv
from helpers.bodycreator_post_orders import create_central_post_orders, create_bees_post_orders
from helpers.auth import get_authentication

failureMessage = "Order não criada"
print("Key 1:")
load_dotenv()


class CargaOrders(HttpUser):
    host = os.environ["KONG_ORDERS_QAS"]
    wait_time = between(1.0, 3.0)
    prefix_orders = os.environ["PREFIX_OPERATION_ORDER"]

    def on_start(self):
        self.authorization_qas = get_authentication()

    @task
    def create_order_bees(self):
        post_orders = f"{self.prefix_orders}"
        body = create_bees_post_orders()

        # Authorization/Headers Keys QAs:
        self.client.headers['Authorization'] = f'{self.authorization_qas}'
        print(self.authorization_qas)
        self.rules_post_order(body, post_orders)

    @tag('test1')
    @task
    def create_order_central(self):
        post_orders = f"{self.prefix_orders}"
        body = create_central_post_orders()

        # Authorization/Headers Keys QAs:
        self.client.headers['Authorization'] = f'{self.authorization_qas}'
        print(self.authorization_qas)
        self.rules_post_order(body, post_orders)

    def rules_post_order(self, body, post_orders):
        with self.client.post(url=post_orders,
                              name="Post Orders Central|Bees|Mercato|Souk",
                              catch_response=True, json=body) as response:

            if response.status_code == 202:
                resposta = response.json()

                if resposta['message'] == "Order successfully integrated!":
                    print(
                        f"---- SUCESSO NA REQUISICAO ----\n"
                        f"Response: {resposta['message']} \n"
                        f"Order id: {resposta['order_id']} \n"
                        f"Order number enviado: {body['order']['customer']['order_number']} \n"
                        f"STATUS CODE: {response.status_code} \n"

                    )

                else:
                    print(
                        f"---- FALHA NA REQUISICAO ----\n {response.text} \n "
                        f"STATUS CODE: {response.status_code} \n {body}")
                    response.failure(
                        failureMessage + f" Status CODE: {response.status_code}"
                    )

            elif response.status_code == 401:
                self.authorization_qas = get_authentication()
                self.rules_post_order(body, post_orders)

            else:
                print(
                    f"---- FALHA NA REQUISICAO ----\n "
                    f"{response.text} \n "
                    f"STATUS CODE: {response.status_code} \n"
                    f"Body enviado: {body} \n")
                response.failure(
                    failureMessage + f" Status CODE: {response.status_code}"
                )
