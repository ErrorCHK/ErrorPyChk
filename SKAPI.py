import json
from pdb import pm
import requests

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:96.0) Gecko/20100101 Firefox/96.0',
    'Accept': 'application/json',
    'Accept-Language': 'es-ES,es;q=0.8,en-US;q=0.5,en;q=0.3',
    'Content-Type': 'application/x-www-form-urlencoded',
    'Origin': 'https://js.stripe.com',
    'Connection': 'keep-alive',
    'Referer': 'https://js.stripe.com/',
    'Authorization': 'Bearer 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',
}

data = 'type=card&card[number]=4508430037598024&card[cvc]=338&card[exp_month]=03&card[exp_year]=28'
response = requests.post('https://api.stripe.com/v1/payment_methods', headers=headers, data=data)
if 'billing_details' in response.text :
    pmid = response.json()['id']

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:96.0) Gecko/20100101 Firefox/96.0',
    'Accept': 'application/json',
    'Accept-Language': 'es-ES,es;q=0.8,en-US;q=0.5,en;q=0.3',
    'Content-Type': 'application/x-www-form-urlencoded',
    'Origin': 'https://js.stripe.com',
    'Connection': 'keep-alive',
    'Referer': 'https://js.stripe.com/',
    'Authorization': 'Bearer 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',
}
data = 'name=Juanito+Juan&email=emailhola1234@gmail.com&description=Jam&address[line1]=1900+street&address[city]=Miami&address[state]=Florida&address[postal_code]=33130&address[country]=US'
response = requests.post('https://api.stripe.com/v1/customers', headers=headers, data=data)
if 'emailhola1234@gmail.com' in response.text :
    cus = response.json()['id']

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:96.0) Gecko/20100101 Firefox/96.0',
    'Accept': 'application/json',
    'Accept-Language': 'es-ES,es;q=0.8,en-US;q=0.5,en;q=0.3',
    'Content-Type': 'application/x-www-form-urlencoded',
    'Origin': 'https://js.stripe.com',
    'Connection': 'keep-alive',
    'Referer': 'https://js.stripe.com/',
    'Authorization': 'Bearer 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',
}

data = f'&customer={cus}'
response = requests.post(f'https://api.stripe.com/v1/payment_methods/{pmid}/attach', headers=headers, data=data)
print(response.text)