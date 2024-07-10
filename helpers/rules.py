from helpers.auth import get_authentication

failureMessage = "Order não criada"


def rules_post_order(client, body, post_orders, function_name):
    with client.post(url=post_orders,
                     name=f"Post Orders {function_name}",
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

            return False



        else:
            print(
                f"---- FALHA NA REQUISICAO ----\n "
                f"{response.text} \n "
                f"STATUS CODE: {response.status_code} \n"
                f"Body enviado: {body} \n")
            response.failure(
                failureMessage + f" Status CODE: {response.status_code}"
            )

    return True


def rules_get_health(client, consult_orders_health_check, function_name):
    with client.get(url=consult_orders_health_check,
                    name=f"Get {function_name}",
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
