from faker import Faker
from datetime import datetime, timedelta
import pytz


def create_bees_post_orders(null=None):
    order_number, fuso_horario, current_datetime, future_data = rules_body()
    body_orders = {
        "order": {
            "partner": "BEES",
            "type": "YB2B",
            "channel": "BEES",
            "sales_organization": "1714",
            "delivery_date": f"{future_data.strftime('%Y-%m-%dT%H:%M:%S.388Z')}",
            "created_date": f"{future_data.strftime('%Y-%m-%dT%H:%M:%S.388Z')}",
            "customer": {
                "document_number": "11178500000134",
                "payment_method": "R007",
                "order_number": f"EMEB{order_number}"
            },
            "items": [
                {
                    "sku": "000000000000044644",
                    "quantity": 2.000,
                    "fifo_category": "GREEN",
                    "price": {
                        "value": 24.497398,
                        "unit": "KG",
                        "currency": "BRL"
                    }
                }
            ]
        }
    }

    return body_orders


def create_central_post_orders(null=None):
    order_number, fuso_horario, current_datetime, future_data = rules_body()
    body_orders_central = {
        "order": {
            "partner": "CENTRAL",
            "type": "YB2B",
            "channel": "B2BB",
            "sales_organization": "1625",
            "delivery_date": f"{future_data.strftime('%Y-%m-%dT%H:%M:%S.388Z')}",
            "created_date": f"{current_datetime.strftime('%Y-%m-%dT%H:%M:%S.388Z')}",
            "customer": {
                "document_number": "04142833000148",
                "payment_method": "R007",
                "receiving_customer_code": "0000212026",
                "order_number": f"EMEC{order_number}"
            },
            "items": [
                {
                    "sku": "000000000000500744",
                    "quantity": 22.0,
                    "fifo_category": "GREEN",
                    "price": {
                        "value": 21.91,
                        "unit": "KG",
                        "currency": "BRL"
                    },
                    "additional_info": {}
                }
            ],
            "additional_info": {
                "campaign_year": "2024",
                "origin_plant": "1625",
                "unloading_point": "BRF CARNES",
                "customer_activity": "C",
                "customer_user": "SRV_IFCKITS",
                "payment_method": "D",
                "installment_value_01": "4793.8",
                "installment_date_01": "20240308"
            }
        }
    }

    return body_orders_central


def rules_body():
    fake = Faker()

    order_number = fake.random_number(digits=6)
    fuso_horario = pytz.timezone('America/Los_Angeles')
    current_datetime = datetime.now(fuso_horario)
    future_data = current_datetime + timedelta(days=3)

    return order_number, fuso_horario, current_datetime, future_data
