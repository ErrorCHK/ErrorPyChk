import random
import aiohttp
import asyncio
import json
import platform
import ssl
import certifi
import aiofiles
if platform.system()=='Windows':
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

if platform.system()=='Windows':
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

async def CMDimg(palabra, proxyrand, urlgen):
    ssl_context = ssl.create_default_context(cafile=certifi.where())
    conn = aiohttp.TCPConnector(ssl=ssl_context)
    async with aiohttp.ClientSession(connector=conn) as session:
        max_retries = 3
        retry_delay = 1
        for retry in range(max_retries):
            try:
                #---------------------------------REQUEST NUMERO 1------------------------------#
                #---------------------------------REQUEST NUMERO 1------------------------------#   
                try:     
                    session.headers.update({
                        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3",
                        "Referer": "https://duckduckgo.com/",
                        "Accept-Language": "en-US,en;q=0.9",
                        "Sec-Fetch-Dest": "empty",
                        "Sec-Fetch-Mode": "cors",
                        "Sec-Fetch-Site": "same-origin",
                        "Pragma": "no-cache",
                        "Cache-Control": "no-cache",
                    })
                    async with session.get(f'https://duckduckgo.com/?q={palabra}&t=h_&iax=images&ia=images', proxy=str(proxyrand), timeout=18) as resp:        
                        response = await resp.text()
                        vqd = (response.split("iar='';vqd='")[1]).split("';safe_ddg=0")[0]
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
                try:     
                    session.headers.update({
                        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3",
                        "Referer": "https://duckduckgo.com/",
                        "Accept-Language": "en-US,en;q=0.9",
                        "Sec-Fetch-Dest": "empty",
                        "Sec-Fetch-Mode": "cors",
                        "Sec-Fetch-Site": "same-origin",
                        "Pragma": "no-cache",
                        "Cache-Control": "no-cache",
                    })
                    async with session.get(f'https://duckduckgo.com/i.js?l=us-en&o=json&q={palabra}&vqd={vqd}&f=,,,,,&p=1', proxy=str(proxyrand), timeout=18) as resp:        
                        response = await resp.text()
                        img_data = json.loads(response)['results']
                        random_img = random.choice(img_data)
                        img_url = random_img['image']
                        title = random_img['title']
                        url = random_img['url']
                        # Definimos la URL de búsqueda y enviamos la
                        # Descargamos la imagen y la guardamos en un archivo
                    async with session.get(img_url) as resp:
                        async with aiofiles.open(urlgen, 'wb') as f:
                            while True:
                                chunk = await resp.content.read(1024)
                                if not chunk:
                                    break
                                await f.write(chunk)
                        res="Imagen guardada correctamente."
                except UnboundLocalError :
                    return 'An unexpected error occurred in request 02. It was not generated correctly [UnboundLocalError]. ♻️'  
                except TypeError :
                    return 'An unexpected error occurred in request 02. It was not generated correctly [TypeError]. ♻️'
                except KeyError :
                    return 'An unexpected error occurred in request 02. It was not generated correctly [KeyError]. ♻️'
                except IndexError :
                    return 'An unexpected error occurred in request 02. It was not generated correctly [KeyError]. ♻️'
                except aiohttp.client_exceptions.ClientHttpProxyError as e:
                    print(f"Error al conectarse {retry+1}/{max_retries}: {e}")
                    if retry < max_retries-1:
                        print(f"Reintentando en {retry_delay} segundo...")
                        await asyncio.sleep(retry_delay)
                    else:
                        print(f"No se pudo conectar después de {max_retries} intentos.") 
                        return "Maximum number of retries reached: 3"
                #---------------------------------CHECCK REQUESTS------------------------------#
                if res=="Imagen guardada correctamente.":
                    return title, url
                else :
                    return
            except (aiohttp.client_exceptions.ServerDisconnectedError):
                return "An unexpected error occurred. ServerDisconnectedError. ♻️"
            except (asyncio.exceptions.TimeoutError):
                return "An unexpected error occurred. Timeout Error. ♻️"
            except (aiohttp.client_exceptions.ClientConnectorError):
                return "An unexpected error occurred. ClientConnectorError. ♻️"
            finally:
                 await session.close()