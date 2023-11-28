import aiohttp
import certifi
import ssl

async def skchecker(sklookup):
    ssl_context = ssl.create_default_context(cafile=certifi.where())
    conn = aiohttp.TCPConnector(ssl=ssl_context)
    async with aiohttp.ClientSession(connector=conn) as session:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:96.0) Gecko/20100101 Firefox/96.0',
            'Accept': 'application/json',
            'Accept-Language': 'es-ES,es;q=0.8,en-US;q=0.5,en;q=0.3',
            'Content-Type': 'application/x-www-form-urlencoded',
            'Origin': 'https://js.stripe.com',
            'Connection': 'keep-alive',
            'Referer': 'https://js.stripe.com/',
            'Authorization': f'Bearer {sklookup}',
        }

        data = 'card[number]=4508430037598024&card[cvc]=338&card[exp_month]=03&card[exp_year]=28'
        async with session.post('https://api.stripe.com/v1/tokens', headers=headers, data=data, proxy=str("http://fctmbbxo-rotate:x4zj0j8n7k82@p.webshare.io:80/")) as resp:
            resptext = await resp.text()
            respjson = await resp.json()
            
        if (resptext.find("Invalid API Key") > 0) : return "invalid_request_error"
        elif (resptext.find("address_city") > 0) : return "SK_LIVE"
        else : return respjson['error']['code']