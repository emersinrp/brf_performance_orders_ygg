import os
from helpers.bodycreator_post_orders import (
    create_central_post_orders,
    create_bees_post_orders,
    create_mex_post_orders,
    create_mer_post_orders,
    create_souk_post_orders
)
from helpers.rules import rules_post_order

def create_order_bees(client, authorization, prefix_orders):
    post_orders = f"{prefix_orders}"
    body = create_bees_post_orders()
    client.headers['Authorization'] = authorization
    rules_post_order(client, body, post_orders, "Bees")

def create_order_central(client, authorization, prefix_orders):
    post_orders = f"{prefix_orders}"
    body = create_central_post_orders()
    client.headers['Authorization'] = authorization
    rules_post_order(client, body, post_orders, "Central")

def create_order_mex(client, authorization, prefix_orders):
    post_orders = f"{prefix_orders}"
    body = create_mex_post_orders()
    client.headers['Authorization'] = authorization
    rules_post_order(client, body, post_orders, "Mercado Ext")

def create_order_mer(client, authorization, prefix_orders):
    post_orders = f"{prefix_orders}"
    body = create_mer_post_orders()
    client.headers['Authorization'] = authorization
    rules_post_order(client, body, post_orders, "Mercato")

def create_order_souk(client, authorization, prefix_orders):
    post_orders = f"{prefix_orders}"
    body = create_souk_post_orders()
    client.headers['Authorization'] = authorization
    rules_post_order(client, body, post_orders, "Souk")
