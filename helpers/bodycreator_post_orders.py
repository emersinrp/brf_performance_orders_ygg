from faker import Faker
from datetime import datetime
import pytz

class BodyCreatorDefaultOrders:

    @staticmethod
    def create_default_post_orders(null=None):
        fake = Faker()

        order_number = fake.random_number(digits=5)
        fuso_horario = pytz.timezone('America/Los_Angeles')
        current_datetime = datetime.now(fuso_horario)

        body_orders = {
            "order": {
                "partner": "BEES",
                "type": "YB2B",
                "channel": "BEES",
                "sales_organization": "1714",
                "delivery_date": f"{current_datetime.strftime('%Y-%m-%dT%H:%M:%S.388Z')}",
                "created_date": f"{current_datetime.strftime('%Y-%m-%dT%H:%M:%S.388Z')}",
                "customer": {
                    "document_number": "11178500000134",
                    "payment_method": "R007",
                    "order_number": f"teste_order_{order_number}"
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
