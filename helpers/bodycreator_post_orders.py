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
                    "validacao_sif": "!@@@@@@@@@@@@@@@@!!!!!!!!!!!!!!!!!!!!$$$$$$$$$$$$$"
                                     "%%%%%%%%%%%%%%%%%%%%%%%%%%%áááááaá´çççççççççç((())**&&¨¨¨$$@##@#@@![{[[["
                                     "´´´´´`´^^^^~~~~]]}}}];;;:::...>>,,"
                                     "<<< 343;331;335;320;322;358;377;310;364;328;316;383;380;382;321;323;367;378;381"
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
                        "packing_list": "!@@@@@@@@@@@@@@@@!!!!!!!!!!!!!!!!!!!!$$$$$$$$$$$$$"
                                        "%%%%%%%%%%%%%%%%%%%%%%%%%%%áááááaá´çççççççççç((())**&&¨¨¨$$@##@#@@![{[[["
                                        "´´´´´`´^^^^~~~~]]}}}];;;:::...>>,,"
                                        'Um jogo de documentos por '
                                        'container\n\n'
                                        '----------------------------------------------------------------\n\nTodos os '
                                        'documentos em nome de:\n\nCIRKEL DIRECT SALES N.V.\n\nWILHELMINASTRAAT '
                                        '62\n\nPARAMARIBO, '
                                        'SURINAME\n\nTel:597425254\n\n'
                                        '----------------------------------------------------------------\n\nEMITIR '
                                        'B/L TELEX RELEASE (PORÉM O MESMO SÓ PODERÁ SER LIBERADO MEDIANTE CONFIRMAÇÃO '
                                        'DE PAGAMENTO)\n\nObs: Referente a emissão do BL, notar que não é usado Zip '
                                        'Code no '
                                        'Suriname.\n\n'
                                        '----------------------------------------------------------------\n\nEnviar '
                                        'cópia dos documentos para os seguintes '
                                        'emails:\n\nsaskia@cirkelgroup.com;cds.finance@cirkelgroup.com\n\n'
                                        '----------------------------------------------------------------\n\nEnviar '
                                        'documentos originais para:\n\nCIRKEL DIRECT SALES N.V.\n\nWILHELMINASTRAAT '
                                        '62\n\nPARAMARIBO, SURINAME\n\nA/C:Saskia\n\nTel:597425254',
                        'logistic': "!@@@@@@@@@@@@@@@@!!!!!!!!!!!!!!!!!!!!$$$$$$$$$$$$$"
                                     "%%%%%%%%%%%%%%%%%%%%%%%%%%%áááááaá´çççççççççç((())**&&¨¨¨$$@##@#@@![{[[["
                                     "´´´´´`´^^^^~~~~]]}}}];;;:::...>>,,""3 shipments and make sure that the containers will not arrive at the same time at the destination.\n..\nNÃO MIXAR\n..\nPALETIZADO\n..\nNote: containeres não podem chegar na mesma data\n..\n..\nAUTORIZADO ANTECIPAR DESDE QUE RESPEITE A RESTRIÇÃO DE CHEGADA\n..\nATENÇÃO: OBRIGATÓRIO O USO DE DATALOGGER (MODELO SENSITECH COM ESPETO)\nACORDO COM REGULAMENTO DA JORDÂNIA. TEMPERATURA -22 ºC. FAZER O FEFO DOS\nDATALOGGERS (9 MESES DE VALIDADE).\n..\nSEPARAR 01 CAIXA POR ITEM / POR DATA DE PRODUÇÃO EM CADA CONTAINER; E\nESTA CAIXA DEVERÁ CONTER UMA ETIQUETA COM A DESIGNAÇÃO \"SAMPLE\".\n..\nPRODUTOS COM 12 MESES DE VALIDADE: O PRAZO DE PRODUÇÃO E DESEMBARAÇO DA\nCARGA NO DESTINO É DE 90 DIAS.\nPRODUTOS COM 09 MESES DE VALIDADE: O PRAZO DE PRODUÇÃO E DESEMBARAÇO DA\nCARGA NO DESTINO É DE 60 DIAS.\n..\nCONSIGNEE AND NOTIFY:\nCompany name: Acadian International Trade\nAcadian International Trade\nAmman-Jordan\nAl-Madina Al-Monawara St. Building No. 208 / Suite 408\nTel: 0096265819460/795526032\nEmail: info@acadian-trade.com\nTAX ID: 730001601\n..\nENVIAR SHIPPING SCHEDULE:\nInfo@acadian-trade.com\n.\nPart Lot.: NÃO\nTelex Release.: NÃO\nSea Waybill.: NÃO\nL/C(Cart. Crédito).: NÃO\nDU.: NÃO\nPIP.: NÃO\nMOZ.: NÃO\nL/C: NÃO\nTipo de Carregamento.: ZREP - Repaletizado\nAgrupamento: NÃO\nIncoterms.: NÃO\nQuantidade CNTR.: SIM - 000001\nSKU Espelho.: NÃO\nFoto: NÃO\nInspeção.: NÃO\nEtiqueta.: NÃO",
                        'load': "!@@@@@@@@@@@@@@@@!!!!!!!!!!!!!!!!!!!!$$$$$$$$$$$$$"
                                     "%%%%%%%%%%%%%%%%%%%%%%%%%%%áááááaá´çççççççççç((())**&&¨¨¨$$@##@#@@![{[[["
                                     "´´´´´`´^^^^~~~~]]}}}];;;:::...>>,," "3 shipments and make sure that the containers will not arrive at the same time at the destination.\n..\nNÃO MIXAR\n..\nORDEM PALETIZADA\n..\n..\n..\nNote: containeres não podem chegar na mesma data\n..\n..\n..\nATENÇÃO: OBRIGATÓRIO O USO DE DATALOGGER (MODELO SENSITECH COM ESPETO),\nDE\nACORDO COM REGULAMENTO DA JORDÂNIA. TEMPERATURA -22 ºC. FAZER O FEFO\nDOSDATALOGGERS (9 MESES DE VALIDADE).\n..\nSEPARAR 01 CAIXA POR ITEM / POR DATA DE PRODUÇÃO EM CADA CONTAINER; E\nESTA CAIXA DEVERÁ CONTER UMA ETIQUETA COM A DESIGNAÇÃO \"SAMPLE\"\n..\nPRODUTOS COM 12 MESES DE VALIDADE: O PRAZO DE PRODUÇÃO E DESEMBARAÇO DA\nCARGA NO DESTINO É DE 90 DIAS.\nPRODUTOS COM 09 MESES DE VALIDADE: O PRAZO DE PRODUÇÃO E DESEMBARAÇO DA\nCARGA NO DESTINO É DE 60 DIAS.",
                        'invoice': "!@@@@@@@@@@@@@@@@!!!!!!!!!!!!!!!!!!!!$$$$$$$$$$$$$"
                                     "%%%%%%%%%%%%%%%%%%%%%%%%%%%áááááaá´çççççççççç((())**&&¨¨¨$$@##@#@@![{[[["
                                     "´´´´´`´^^^^~~~~]]}}}];;;:::...>>,,"'Um jogo de documentos por '
                                   'container\n\n----------------------------------------------------------------\n'
                                   '\nTodos os documentos em nome de:\n\nCIRKEL DIRECT SALES N.V.\n\nWILHELMINASTRAAT '
                                   '62\n\nPARAMARIBO, '
                                   'SURINAME\n\nTel:597425254\n\n'
                                   '----------------------------------------------------------------\n\nEMITIR B/L '
                                   'TELEX RELEASE (PORÉM O MESMO SÓ PODERÁ SER LIBERADO MEDIANTE CONFIRMAÇÃO DE '
                                   'PAGAMENTO)\n\nObs: Referente a emissão do BL, notar que não é usado Zip Code no '
                                   'Suriname.\n\n----------------------------------------------------------------\n'
                                   '\nEnviar cópia dos documentos para os seguintes '
                                   'emails:\n\nsaskia@cirkelgroup.com;cds.finance@cirkelgroup.com\n\n'
                                   '----------------------------------------------------------------\n\nEnviar '
                                   'documentos originais para:\n\nCIRKEL DIRECT SALES N.V.\n\nWILHELMINASTRAAT '
                                   '62\n\nPARAMARIBO, SURINAME\n\nA/C:Saskia\n\nTel:597425254',
                        'documentary': "!@@@@@@@@@@@@@@@@!!!!!!!!!!!!!!!!!!!!$$$$$$$$$$$$$"
                                     "%%%%%%%%%%%%%%%%%%%%%%%%%%%áááááaá´çççççççççç((())**&&¨¨¨$$@##@#@@![{[[["
                                     "´´´´´`´^^^^~~~~]]}}}];;;:::...>>,,""** CRIAR 1 EMBARQUE PARA CADA CONTAINER**\n..\nNÃO MIXAR PIV'S DEVIDO RESTRIÇÃO DE CHEGADA\n..\n**GERAR UM JOGO DE DOCUMENTO PARA CADA CONTAINER**\n..\n**SOLICITAR TELEX RELEASE APÓS CONFIRMAÇAO DE PAGAMENTO***\n..\nAPÓS CONFIRMAÇAO DE PAGAMENTO ENVIAR DOCS (EXCETO BL) PARA:\nAcadian International Trade\nAmman-Jordan\nAl-Madina Al-Monawara St. Building No. 208 / Suite 408\nTel: 0096265819460/795526032\nEmail: info@acadian-trade.com\n..\nEMAIL: Info@acadian-trade.com\n..\nLEGALIZAÇAO: ESCRITÓRIO DA BRF VIA CERTIFICAÇÃO FACISC\n..",
                        'csi': "Acadian International Trade\nAmman-Jordan\nAl-Madina Al-Monawara St. Building No. 208 / Suite 408\nTel: 0096265819460/795526032\nEmail: info@acadian-trade.com",
                        'bill_of_lading': "!@@@@@@@@@@@@@@@@!!!!!!!!!!!!!!!!!!!!$$$$$$$$$$$$$"
                                     "%%%%%%%%%%%%%%%%%%%%%%%%%%%áááááaá´çççççççççç((())**&&¨¨¨$$@##@#@@![{[[["
                                     "´´´´´`´^^^^~~~~]]}}}];;;:::...>>,,"'Um jogo de documentos por '
                                          'container\n\n'
                                          '----------------------------------------------------------------\n\nTodos '
                                          'os documentos em nome de:\n\nCIRKEL DIRECT SALES N.V.\n\nWILHELMINASTRAAT '
                                          '62\n\nPARAMARIBO, '
                                          'SURINAME\n\nTel:597425254\n\n'
                                          '----------------------------------------------------------------\n\nEMITIR '
                                          'B/L TELEX RELEASE (PORÉM O MESMO SÓ PODERÁ SER LIBERADO MEDIANTE '
                                          'CONFIRMAÇÃO DE PAGAMENTO)\n\nObs: Referente a emissão do BL, notar que não '
                                          'é usado Zip Code no '
                                          'Suriname.\n\n'
                                          '----------------------------------------------------------------\n\nEnviar '
                                          'cópia dos documentos para os seguintes '
                                          'emails:\n\nsaskia@cirkelgroup.com;cds.finance@cirkelgroup.com\n\n'
                                          '----------------------------------------------------------------\n\nEnviar '
                                          'documentos originais para:\n\nCIRKEL DIRECT SALES N.V.\n\nWILHELMINASTRAAT '
                                          '62\n\nPARAMARIBO, SURINAME\n\nA/C:Saskia\n\nTel:597425254',
                        'analises_requisitos': "!@@@@@@@@@@@@@@@@!!!!!!!!!!!!!!!!!!!!$$$$$$$$$$$$$"
                                     "%%%%%%%%%%%%%%%%%%%%%%%%%%%áááááaá´çççççççççç((())**&&¨¨¨$$@##@#@@![{[[["
                                     "´´´´´`´^^^^~~~~]]}}}];;;:::...>>,,"'Um jogo de documentos por '
                                               'container\n\n'
                                               '----------------------------------------------------------------\n'
                                               '\nTodos os documentos em nome de:\n\nCIRKEL DIRECT SALES '
                                               'N.V.\n\nWILHELMINASTRAAT 62\n\nPARAMARIBO, '
                                               'SURINAME\n\nTel:597425254\n\n'
                                               '----------------------------------------------------------------\n'
                                               '\nEMITIR B/L TELEX RELEASE (PORÉM O MESMO SÓ PODERÁ SER LIBERADO '
                                               'MEDIANTE CONFIRMAÇÃO DE PAGAMENTO)\n\nObs: Referente a emissão do BL, '
                                               'notar que não é usado Zip Code no '
                                               'Suriname.\n\n'
                                               '----------------------------------------------------------------\n'
                                               '\nEnviar cópia dos documentos para os seguintes '
                                               'emails:\n\nsaskia@cirkelgroup.com;cds.finance@cirkelgroup.com\n\n'
                                               '----------------------------------------------------------------\n'
                                               '\nEnviar documentos originais para:\n\nCIRKEL DIRECT SALES '
                                               'N.V.\n\nWILHELMINASTRAAT 62\n\nPARAMARIBO, '
                                               'SURINAME\n\nA/C:Saskia\n\nTel:597425254',
                        "bill_of_lading": "",
                        "documentary": "!@@@@@@@@@@@@@@@@!!!!!!!!!!!!!!!!!!!!$$$$$$$$$$$$$"
                                       "%%%%%%%%%%%%%%%%%%%%%%%%%%%áááááaá´çççççççççç((())**&&¨¨¨$$@##@#@@![{[[["
                                       "´´´´´`´^^^^~~~~]]}}}];;;:::...>>,,<<< 1. Forma de Pagamento: Pagamento a 50 "
                                       "DIAS DO r o número de Pallets na"
                                       "fatura===8. Local de descarga: Não deve aparecer na fatura comercial",
                        "logistic": "!@@@@@@@@@@@@@@@@!!!!!!!!!!!!!!!!!!!!$$$$$$$$$$$$$"
                                    "%%%%%%%%%%%%%%%%%%%%%%%%%%%áááááaá´çççççççççç((())**&&¨¨¨$$@##@#@@![{[[["
                                    "´´´´´`´^^^^~~~~]]}}}];;;:::...>>,,<<< Datos para Contramarca – Cliente "
                                    "Quickfood:SIFtDescripcióntN°"
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
                        "load": "!@@@@@@@@@@@@@@@@!!!!!!!!!!!!!!!!!!!!$$$$$$$$$$$$$%%%%%%%%%%%%%%%%%%%%%%%%%%%áááááa"
                                "á´çççççççççç((())**&&¨¨¨$$@##@#@@![{[[[´´´´´`´^^^^~~~~]]}}}];;;:::...>>,,"
                                "<<< Datos para Contramarca – Cliente Quickfood:SIFtDescripcióntN°"
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
                        "analises_requisitos": "!@@@@@@@@@@@@@@@@!!!!!!!!!!!!!!!!!!!!$$$$$$$$$$$$$"
                                               "%%%%%%%%%%%%%%%%%%%%%%%%%%%áááááaá´çççççççççç((())**&&¨¨¨$$@##@#@@![{"
                                               "[[[´´´´´`´^^^^~~~~]]}}}];;;:::...>>,,<<<Lorem ipsum dolor sit amet, "
                                               "consectetur adipiscing elit. Fusce eget eros nec nulla fringilla "
                                               "malesuada. Integer posuere, neque a suscipit tincidunt, libero erat "
                                               "posuere nunc, a lacinia augue turpis a augue. Nunc efficitur nunc sit "
                                               "amet purus dictum, non ultricies dolor dapibus. Sed malesuada justo "
                                               "eu nulla cursus, ut vulputate purus luctus. Mauris convallis, "
                                               "purus et elementum dictum, ex nunc sodales leo, et facilisis purus "
                                               "justo a turpis. In a condimentum orci, ac ullamcorper magna. Praesent "
                                               "vehicula ante sit amet odio tincidunt, in efficitur justo interdum. "
                                               "Phasellus viverra lacinia lorem in ullamcorper. Nulla facilisi. "
                                               "Quisque vitae leo eros. Donec volutpat malesuada velit, eu vehicula "
                                               "ex consectetur ac. Pellentesque habitant morbi tristique senectus et "
                                               "netus et malesuada fames ac turpis egestas.\n\nSuspendisse potenti. "
                                               "Aenean ut risus vitae lorem tempus cursus in sit amet metus. Nullam "
                                               "id arcu eu sapien tincidunt sagittis. Vivamus malesuada ligula vitae "
                                               "lorem dapibus blandit. Etiam et sapien nec elit pretium accumsan. "
                                               "Nulla facilisi. Vivamus sit amet lectus at ipsum ultricies "
                                               "condimentum. Nunc vitae est malesuada, facilisis felis id, "
                                               "fermentum justo. Nullam vitae turpis at sapien ultrices aliquet. Sed "
                                               "convallis dictum magna. Suspendisse gravida risus ac interdum "
                                               "venenatis. Sed auctor quam sed erat feugiat, nec auctor nunc "
                                               "ullamcorper. Aenean a arcu quis risus venenatis pharetra.\n\nDonec "
                                               "bibendum quam id suscipit auctor. Maecenas consequat enim ac dolor "
                                               "tempor, sit amet scelerisque magna pellentesque. Donec consectetur "
                                               "arcu justo, ut vestibulum odio ultrices in. Proin tempor nisi libero, "
                                               "et luctus nunc aliquam non. Nam condimentum purus id magna blandit, "
                                               "in ullamcorper nunc cursus. Aliquam bibendum nibh nec magna "
                                               "pellentesque, vel posuere odio facilisis. Cras quis risus vitae lacus "
                                               "pharetra lobortis. Nulla facilisi. Phasellus faucibus risus non "
                                               "sapien convallis, ut facilisis eros vulputate. Aenean sit amet metus "
                                               "a dui varius dignissim. Fusce a nisl id nunc vehicula bibendum. "
                                               "Curabitur sit amet turpis quis elit euismod feugiat. Phasellus rutrum "
                                               "purus ac vehicula auctor. Sed suscipit libero eget nunc viverra, "
                                               "non vestibulum ex bibendum. Aliquam ac enim non eros cursus "
                                               "dignissim.\n\nNam in tincidunt lacus. Integer vulputate pharetra "
                                               "dolor sit amet laoreet. Aliquam erat volutpat. Vivamus sed "
                                               "scelerisque arcu, sit amet lacinia arcu. Phasellus suscipit ex sit "
                                               "amet enim egestas, at accumsan lacus facilisis. Integer sed gravida "
                                               "erat, in fermentum metus. Curabitur at diam sit amet libero vulputate "
                                               "scelerisque non non leo. Fusce vehicula neque ac felis blandit "
                                               "tristique. Quisque vel urna nec ex interdum tristique. Ut ultricies "
                                               "metus non leo pretium, sit amet tempor elit cursus. Nullam gravida "
                                               "ultricies nisi. Proin volutpat varius turpis et feugiat. Nulla "
                                               "malesuada velit in quam vestibulum, ut faucibus sapien vehicula. "
                                               "Aliquam maximus erat nec nisi elementum, at hendrerit erat "
                                               "eleifend.\n\nCurabitur auctor neque et justo dignissim, "
                                               "id scelerisque metus efficitur. Etiam dictum arcu id metus "
                                               "condimentum, sed aliquam justo feugiat. Proin accumsan tortor a velit "
                                               "vehicula, id volutpat libero ultricies. Nam mollis bibendum sapien, "
                                               "in aliquet eros vehicula ac. Nam posuere justo ac ante convallis "
                                               "feugiat. Suspendisse potenti. Duis tristique ligula ac nibh "
                                               "vulputate, quis pretium nisi fermentum. Maecenas rutrum risus vitae "
                                               "tellus gravida, vel vehicula libero feugiat. Etiam at mauris sed eros "
                                               "consequat venenatis. Nulla facilisi. Donec nec libero in felis "
                                               "fringilla bibendum. Etiam malesuada felis eget metus eleifend, "
                                               "non ultrices turpis aliquet. Proin elementum sem id purus tincidunt "
                                               "scelerisque. Donec feugiat lacus id turpis luctus, eu dapibus ex "
                                               "dapibus. Sed tempus tortor non purus tristique, sed finibus tortor "
                                               "pharetra.\n\nSed at magna vitae libero auctor iaculis. Curabitur "
                                               "malesuada purus nec facilisis vulputate. Nam vulputate, sapien sit "
                                               "amet laoreet varius, velit eros fermentum nunc, et efficitur eros "
                                               "libero a eros. Integer posuere metus felis, sed accumsan lorem "
                                               "posuere in. Fusce condimentum orci in urna ultrices, et aliquam "
                                               "lectus pharetra. Quisque vestibulum mauris ac dui finibus, "
                                               "ac tempor justo malesuada. Aliquam ut ex sed lectus vulputate "
                                               "consequat a non dolor. Aliquam erat volutpat. Fusce et leo tortor. "
                                               "Aliquam a ultricies nunc. In dignissim nisl sit amet pharetra "
                                               "consequat. Nam sagittis eros nec tincidunt dignissim. Vestibulum in "
                                               "lacinia nunc. In in nisi sem. Sed aliquet sapien nec nulla cursus, "
                                               "vel viverra metus luctus. Nulla facilisi.\n\nDuis venenatis, "
                                               "orci in dapibus gravida, nunc augue scelerisque libero, eu aliquam "
                                               "orci enim quis libero. Integer ut enim id sapien congue consequat. "
                                               "Vestibulum rhoncus nisi nec purus scelerisque laoreet. Pellentesque "
                                               "bibendum leo et tortor convallis, at venenatis orci lacinia. Maecenas "
                                               "ullamcorper quam sit amet metus luctus viverra. Sed venenatis"

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
            "sales_organization": "1694",
            "customer": {
                "document_number": "19231508806",
                "payment_method": "BP1C",
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
                "sales_off": "1694",
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
                "receiver_name": "MARCIO LOPES CARVALHAL",
                "customer_name": "MARCIO LOPES CARVALHAL",
                "customer_email": "marciocarvalhal962@gmail.com",
                "unloading_point": "B2C - 0812"
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
                    "fifo_category": "Z098",
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
