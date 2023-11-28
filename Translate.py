from deep_translator import GoogleTranslator
# - - Esta parte del código traduce únicamente un texto plano

async def Translate(target, text) :
    traductor = GoogleTranslator(source='en', target=target)
    resultado = traductor.translate(text)
    return resultado
