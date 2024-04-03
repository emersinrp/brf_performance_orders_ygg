from faker import Faker
from datetime import datetime, timedelta
import pytz
import os


def create_bees_post_orders(null=None):
    order_number, fuso_horario, current_datetime, future_data = rules_body()
    body_orders = {
        "order": {
            "partner": "BEES",
            "type": "YB2B",
            "channel": "BEES",
            "sales_organization": "1714",
            "delivery_date": f"{future_data.strftime('%Y-%m-%dT%H:%M:%S.388Z')}",
            "created_date": f"{current_datetime.strftime('%Y-%m-%dT%H:%M:%S.388Z')}",
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
            ],
            "url_callback": os.environ["URL_CALLBACK_DEV"]
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
            },
            "url_callback": os.environ["URL_CALLBACK_DEV"]
        }
    }

    return body_orders_central


def create_mex_post_orders(null=None):
    order_number, fuso_horario, current_datetime, future_data = rules_body()
    body_orders_mex = {
        "order":
            {
                "partner": "MERCADO-EXTERNO",
                "type": "ZRME",
                "channel": "",
                "sales_organization": "2680",
                "shipping_type": "Z1",
                "delivery_date": f"{future_data.strftime('%Y-%m-%dT%H:%M:%S.388Z')}",
                "created_date": f"{current_datetime.strftime('%Y-%m-%dT%H:%M:%S.388Z')}",
                "total": 0.0,
                "sub_total": 0.0,
                "taxes": {},
                "customer": {
                    "document_number": "",
                    "payment_method": "EX97",
                    "receiving_customer_code": "",
                    "order_number": f"EMEX{order_number}"
                },
                "items": [
                    {
                        "sku": "346497",
                        "quantity": 1.0,
                        "fifo_category": "",
                        "price": {
                            "value": 5200.0,
                            "unit": "KG",
                            "currency": "USD",
                            "promotion": null
                        },
                        "status": "",
                        "unit_of_measurement": "",
                        "additional_info": {
                            "breackdown_freight": "",
                            "breackdown_freight_insurance": "",
                            "fresh_production": "",
                            "critical_stock": null,
                            "customer_item_number": "802U600000242WmIAI",
                            "preorder_block": null
                        }
                    },
                ],
                "salesman": {
                    "document_number": ""
                },
                "status_list": [
                    {}
                ],
                "url_callback": os.environ["URL_CALLBACK_DEV"],
                "additional_info": {
                    "company": "2500",
                    "origin_plant": "901",
                    "clients_code": "0000424581",
                    "buyer": "0000424581",
                    "tp_oper_comercial": "9",
                    "port_of_destination": "064",
                    "denomination_1": "03/2024.",
                    "shipment_type": "ZPAL",
                    "piv": "",
                    "nr_containers": "",
                    "region_number": "800820",
                    "one_sales_order_per_container": "",
                    "invisible_in_partial_shipment": "",
                    "global_desk": "",
                    "por_navio": "",
                    "por_container": "X",
                    "validacao_sif": "343;331;335;320;322;358;377;310;364;328;316;383;380;382;321;323;367;378;381"
                                     ";338;390;391;386;389;365;387;368;349;350;879;312;300;375;E03;E04;305;35;176",
                    "consignee_bl": "0000424581",
                    "notify_bl": "0000424581",
                    "notify_bl2": "",
                    "packing_list": "0000424581",
                    "certificate_of_origin": "0000424581",
                    "health_certificate": "0000424581",
                    "commercial_invoice": "0000424581",
                    "trader": "80100003",
                    "bank_details_in_case_of_cad": "501610",
                    "agent": "501608",
                    "bank_agent": "501610",
                    "part_lot": "",
                    "telex_release": "",
                    "sea_waybill": "",
                    "lc_cart_credito": "",
                    "sku_espelho": "",
                    "du": "",
                    "txt_du": "",
                    "pip": "",
                    "txt_pip": "",
                    "bietc": "",
                    "txt_bietc": "",
                    "moz": "",
                    "txt_moz": "",
                    "inspection": "",
                    "label": "X",
                    "check_photo_register": "",
                    "max_qty_of_cntr_on_bl": "1",
                    "min_qty_of_cntr_on_bl": "1",
                    "order_composition": "",
                    "clients_week": "10.2024",
                    "arrival_ship": "",
                    "resale": "",
                    "container": "",
                    "invoice": "",
                    "delivery": "",
                    "prioritized_week": "",
                    "global_accounts": "",
                    "order_mix": "",
                    "batch_shipment": "",
                    "advanced_order": "",
                    "mandatory_item": "",
                    "zregra_comp": "1",
                    "cod_mix_ordem": "",
                    "espelho": "",
                    "instructions": {
                        "invoice": "",
                        "packing_list": "",
                        "bill_of_lading": "",
                        "documentary": "1. Forma de Pagamento: Pagamento a 50 DIAS DO r o número de Pallets na "
                                       "fatura===8. Local de descarga: Não deve aparecer na fatura comercial",
                        "logistic": "Datos para Contramarca – Cliente Quickfood:SIFtDescripcióntN° "
                                    "RegistrotFechatVencimiento3681tCORTES DE CERDO - PERNILtI "
                                    "9186/110073/1t18/8/23t17/8/243681tCORTES DE CERDO - LOMOtI "
                                    "9186/110073/2t18/8/23t17/8/243681tCORTES DE CERDO - PALETAtI "
                                    "9186/110073/3t18/8/23t17/8/243681tCORTES DE CERDO - PANCETAtI "
                                    "9186/110073/4t18/8/23t17/8/243681tCORTES DE CERDO - BONDIOLA tI "
                                    "9186/110073/5t18/8/23t17/8/243681tCORTES DE CERDO - PANCETA CON CUEROtI "
                                    "9186/110073/6t18/8/23t17/8/24716tCORTES DE CERDO - JAMONtI "
                                    "9186/103041/1t18/8/23t17/8/24716tCORTES DE CERDO - PALETAtI "
                                    "9186/103041/2t18/8/23t17/8/24716tCORTES DE CERDO - BONDIOLA tI "
                                    "9186/103041/4t18/8/23t17/8/24716tCORTES DE CERDO - LOMOtI "
                                    "9186/103041/5t18/8/23t17/8/243515tCORTES DE CERDO CONG SIN HUESO - JAMONtI "
                                    "9186/113681/1t5/5/23t4/5/243515tCORTES DE CERDO CONG SIN HUESO - LOMOtI "
                                    "9186/113681/2t5/5/23t4/5/243515tCORTES DE CERDO CONG SIN HUESO - PALETAtI "
                                    "9186/113681/3t5/5/23t4/5/24-----------------------------------Carregamento "
                                    "PALETIZADO===Fronteira: São Borja===Peso total do veículo (carga + tara) não "
                                    "pode ultrapassar 45tons.Dúvidas contatar: "
                                    "felipe.pardo@brf.comcarlos.furlan@brf.com===Carga paletizada e todos os "
                                    "pallets devem ser fumigados.Os pallets da porta devem estar com o carimbo à "
                                    "vista (virados para aporta);Colocar próximo a porta traseira um pallet de "
                                    "cada produto (caso tenhamais de um);Esses pallets deverão estar com os "
                                    "números de lotes visíveis próximos aporta do Baú.===Enviar copia dos "
                                    "documentos "
                                    "para:marta.bucciarelli@marfrig.comdaniel.lines@marfrig.comhernan.canepa"
                                    "@marfrig.commh_serviciosinternacionales@cuf.com.brnyara.mesquita@marfrig"
                                    ".commonica.kombrink@marfrig.comPart Lot.: NÃOTelex Release.: NÃOSea "
                                    "Waybill.: NÃOL/C(Cart. Crédito).: NÃODU.: NÃOPIP.: NÃOMOZ.: NÃOL/C: NÃOTipo "
                                    "de Carregamento.: ZPAL - PaletizadoAgrupamento: NÃOIncoterms.: NÃOQuantidade "
                                    "CNTR.: SIM - 000001SKU Espelho.: NÃOFoto: NÃOInspeção.: NÃOEtiqueta.: SIM",
                        "load": "Datos para Contramarca – Cliente Quickfood:SIFtDescripcióntN° "
                                "RegistrotFechatVencimiento3681tCORTES DE CERDO - PERNILtI "
                                "9186/110073/1t18/8/23t17/8/243681tCORTES DE CERDO - LOMOtI "
                                "9186/110073/2t18/8/23t17/8/243681tCORTES DE CERDO - PALETAtI "
                                "9186/110073/3t18/8/23t17/8/243681tCORTES DE CERDO - PANCETAtI "
                                "9186/110073/4t18/8/23t17/8/243681tCORTES DE CERDO - BONDIOLA tI "
                                "9186/110073/5t18/8/23t17/8/243681tCORTES DE CERDO - PANCETA CON CUEROtI "
                                "9186/110073/6t18/8/23t17/8/24716tCORTES DE CERDO - JAMONtI "
                                "9186/103041/1t18/8/23t17/8/24716tCORTES DE CERDO - PALETAtI "
                                "9186/103041/2t18/8/23t17/8/24716tCORTES DE CERDO - BONDIOLA tI "
                                "9186/103041/4t18/8/23t17/8/24716tCORTES DE CERDO - LOMOtI "
                                "9186/103041/5t18/8/23t17/8/243515tCORTES DE CERDO CONG SIN HUESO - JAMONtI "
                                "9186/113681/1t5/5/23t4/5/243515tCORTES DE CERDO CONG SIN HUESO - LOMOtI "
                                "9186/113681/2t5/5/23t4/5/243515tCORTES DE CERDO CONG SIN HUESO - PALETAtI "
                                "9186/113681/3t5/5/23t4/5/24"
                                "--------------------------------------------------Carregamento "
                                "PALETIZADO===Fronteira: São Borja===Peso total do veículo (carga + tara) não "
                                "pode ultrapassar 45tons.Dúvidas contatar: "
                                "felipe.pardo@brf.comcarlos.furlan@brf.com===Carga paletizada e todos os pallets "
                                "devem ser fumigados.Os pallets da porta devem estar com o carimbo à vista ("
                                "virados para aporta);Colocar próximo a porta traseira um pallet de cada produto "
                                "(caso tenhamais de um);Esses pallets deverão estar com os números de lotes "
                                "visíveis próximos aporta do Baú.===Enviar copia dos documentos "
                                "para:marta.bucciarelli@marfrig.comdaniel.lines@marfrig.comhernan.canepa@marfrig"
                                ".commh_serviciosinternacionales@cuf.com.brnyara.mesquita@marfrig.commonica"
                                ".kombrink@marfrig.com",
                        "proforma_shipment": "",
                        "csi": "QUICKFOOD SASUIPACHA 1111, PISO 18, CABA,ARGENTINA",
                        "proforma_remarks": "",
                        "analises_requisitos": "Datos para Contramarca – Cliente Quickfood:SIFtDescripcióntN° "
                                               "RegistrotFechatVencimiento3681tCORTES DE CERDO - PERNILtI "
                                               "9186/110073/1t18/8/23t17/8/243681tCORTES DE CERDO - LOMOtI "
                                               "9186/110073/2t18/8/23t17/8/243681tCORTES DE CERDO - PALETAtI "
                                               "9186/110073/3t18/8/23t17/8/243681tCORTES DE CERDO - PANCETAtI "
                                               "9186/110073/4t18/8/23t17/8/243681tCORTES DE CERDO - BONDIOLA tI "
                                               "9186/110073/5t18/8/23t17/8/243681tCORTES DE CERDO - PANCETA CON "
                                               "CUEROtI 9186/110073/6t18/8/23t17/8/24716tCORTES DE CERDO - "
                                               "JAMONtI 9186/103041/1t18/8/23t17/8/24716tCORTES DE CERDO - "
                                               "PALETAtI 9186/103041/2t18/8/23t17/8/24716tCORTES DE CERDO - "
                                               "BONDIOLA tI 9186/103041/4t18/8/23t17/8/24716tCORTES DE CERDO - "
                                               "LOMOtI 9186/103041/5t18/8/23t17/8/243515tCORTES DE CERDO CONG SIN "
                                               "HUESO - JAMONtI 9186/113681/1t5/5/23t4/5/243515tCORTES DE CERDO "
                                               "CONG SIN HUESO - LOMOtI 9186/113681/2t5/5/23t4/5/243515tCORTES DE "
                                               "CERDO CONG SIN HUESO - PALETAtI 9186/113681/3t5/5/23t4/5/24"
                    },
                    "per_vessel": "",
                    "per_container": "",
                    "order_quantity": "1",
                    "arrival_shipment": "",
                    "composition_rules": "",
                    "incoterms": "CIP",
                    "sales_office": "4641",
                    "delivery_block": "11",
                    "billing_block": ""
                }
            }

    }

    return body_orders_mex


def create_mer_post_orders(null=None):
    order_number, fuso_horario, current_datetime, future_data = rules_body()
    body_orders_mer = {
        "order": {
            "partner": "MERCATO",
            "created_date": f"{current_datetime.strftime('%Y-%m-%dT%H:%M:%S.388Z')}",
            "delivery_date": f"{future_data.strftime('%Y-%m-%dT%H:%M:%S.388Z')}",
            "type": "YB2C",
            "channel": "OMNI",
            "sales_organization": "1705",
            "customer": {
                "document_number": "39006598852",
                "payment_method": "BP1C",
                "receiving_customer_code": "0000212026",
                "order_number": f"EMER{order_number}"
            },
            "items": [
                {
                    "sku": "000000000000767582",
                    "quantity": 4.0,
                    "fifo_category": "GREEN",
                    "price": {
                        "value": 43.60,
                        "unit": "KG",
                        "currency": "BRL"
                    },
                    "additional_info": {
                        "ean": "7891515577513",
                        "freight_cost": "14.9"
                    }
                }
            ],
            "additional_info": {
                "sales_off": "1211",
                "interface": "verum",
                "payment_status": "PAID",
                "payment_comission": "0",
                "payment_merchant": "801U60000079mvtIAA",
                "payment_voucher": "0.00",
                "payment_form": "@",
                "payment_hash": "900f406c-d1cc-4594-b48d-b9fcadbe5e28",
                "seller": "80615636",
                "origin_plant": "1705",
                "installment_value_01": "62.8600",
                "receiver_name": "RODRIGO AUGUSTO TOSIN",
                "customer_name": "RODRIGO AUGUSTO TOSIN",
                "customer_email": "rodrigotosin@uol.com.br"
            },
            "url_callback": os.environ["URL_CALLBACK_DEV"]
        }
    }

    return body_orders_mer


def create_souk_post_orders(null=None):
    order_number, fuso_horario, current_datetime, future_data = rules_body()
    body_orders_souk = {
        "order": {
            "partner": "SOUK",
            "created_date": f"{current_datetime.strftime('%Y-%m-%dT%H:%M:%S.388Z')}",
            "delivery_date": f"{future_data.strftime('%Y-%m-%dT%H:%M:%S.388Z')}",
            "type": "YB2B",
            "channel": "SOUK",
            "sales_organization": "1612",
            "customer": {
                "document_number": "58340787000110",
                "payment_method": "R007",
                "order_number": f"EMES{order_number}"
            },
            "items": [
                {
                    "sku": "000000000000763327",
                    "quantity": 10.0,
                    "fifo_category": "RED",
                    "price": {
                        "value": 19.73,
                        "unit": "KG",
                        "currency": "BRL"
                    },
                    "additional_info": {}
                }
            ],
            "additional_info": {},
            "url_callback": os.environ["URL_CALLBACK_DEV"]
        }
    }

    return body_orders_souk


def rules_body():
    fake = Faker()

    order_number = fake.random_number(digits=6)
    fuso_horario = pytz.timezone('America/Los_Angeles')
    current_datetime = datetime.now(fuso_horario)
    future_data = current_datetime + timedelta(days=3)

    return order_number, fuso_horario, current_datetime, future_data
