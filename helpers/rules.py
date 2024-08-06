import os
import json
from datetime import datetime
from unittest.mock import MagicMock
from helpers.auth import get_authentication

failureMessage = "Order não criada"
MAX_RETRIES = 3  # Limite de tentativas de reenvio

def ensure_log_directories():
    os.makedirs("logs", exist_ok=True)

def log_success(response_time, status_code, function_name):
    log_entry = {
        "timestamp": datetime.now().isoformat(),
        "response_time": response_time,
        "status_code": status_code,
        "function_name": function_name
    }
    log_file_path = "logs/order_success.log"
    with open(log_file_path, 'a') as log_file:
        log_file.write(json.dumps(log_entry) + '\n')

def log_error(response_time, function_name, body, response):
    log_entry = {
        "timestamp": datetime.now().isoformat(),
        "response_time": response_time,
        "status_code": response.status_code,  # Inclui o código de status no log
        "function_name": function_name,
        "body_sent": clean_for_logging(body),
        "response_received": clean_for_logging(response.text)
    }
    log_file_path = "logs/order_error.log"
    with open(log_file_path, 'a') as log_file:
        log_file.write(json.dumps(log_entry) + '\n')

def clean_for_logging(obj):
    if isinstance(obj, MagicMock):
        return "<MagicMock>"
    if isinstance(obj, dict):
        return {k: clean_for_logging(v) for k, v in obj.items()}
    if isinstance(obj, list):
        return [clean_for_logging(i) for i in obj]
    return obj

def rules_post_order(client, body, post_orders, function_name, retry_count=0):
    ensure_log_directories()
    with client.post(url=post_orders, name=f"Post Orders {function_name}", catch_response=True, json=body) as response:
        response_time = response.elapsed.total_seconds()
        if response.status_code == 202:
            resposta = response.json()
            if resposta.get('message') == "Order successfully integrated!":
                log_success(response_time, response.status_code, function_name)
                print(f"---- SUCESSO NA REQUISICAO ----\nResponse: {resposta['message']} \nOrder id: {resposta['order_id']} \nOrder number enviado: {body['order']['customer']['order_number']} \nSTATUS CODE: {response.status_code} \n")
            else:
                log_error(response_time, function_name, body, response)
                handle_failure(response, body)
        elif response.status_code == 401 and retry_count < MAX_RETRIES:
            print("Token expirado, renovando token...")
            client.headers['Authorization'] = get_authentication()
            rules_post_order(client, body, post_orders, function_name, retry_count + 1)
        else:
            log_error(response_time, function_name, body, response)
            handle_failure(response, body)

def handle_failure(response, body):
    print(f"---- FALHA NA REQUISICAO ----\n {response.text} \n STATUS CODE: {response.status_code} \n {body}")
    response.failure(failureMessage + f" Status CODE: {response.status_code}")

def rules_get_health(client, consult_orders_health_check, function_name):
    ensure_log_directories()
    with client.get(url=consult_orders_health_check, name=f"Get {function_name}", catch_response=True) as response:
        response_time = response.elapsed.total_seconds()
        if response.status_code == 200:
            resposta = response.json()
            if resposta.get('aplication_message') == "May the Orders be with YOU!":
                log_success(response_time, response.status_code, function_name)
                print(f"---- SUCESSO NA CONSULTA ----\nResponse: {resposta['aplication_message']} \nSTATUS CODE: {response.status_code} \n")
            else:
                log_error(response_time, function_name, {}, response)
                handle_failure(response, {})
        else:
            log_error(response_time, function_name, {}, response)
            handle_failure(response, {})
