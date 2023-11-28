import asyncio

async def CheckProxy() :
    import aiohttp
    try:
        #randomnum = random.randint(1,75)
        Rotate = f"http://pxu29879-0:Je9BqktsZNMNP8lIJk1O@x.botproxy.net:8080"
        session = aiohttp.ClientSession()
        async with session.get("https://ipv4.webshare.io//", proxy=str(Rotate), timeout=8) as resp:
            ResultP = await resp.text()
            if (ResultP) :
                await session.close()
                return "Live ✅", Rotate
            else:
                Tries = 0
                FinalTries = 0   
                while Tries < 3:
                    if not ResultP:
                        async with session.get("https://ipv4.webshare.io//", proxy=str(Rotate), timeout=8) as resp:
                            ResultP = await resp.text()
                            if not ResultP:
                                Tries+=1
                                FinalTries+=1
                                print(f"[Require Retrie] Tries: {Tries}")
                            else :
                                Tries+=3
                                FinalTries+=0
                    else :
                        Tries+=3
                        FinalTries = 0
                if int(FinalTries) >= 3 :
                    await session.close()
                    return None
                else :
                    print(f"Tries: {FinalTries}")
                    await session.close()
                    return "Live ✅", Rotate
    except :
        Tries = 0
        FinalTries = 0   
        while Tries < 3:
            async with session.get("https://ipv4.webshare.io//", proxy=str(Rotate), timeout=8) as resp:
                ResultP = await resp.text()
                if not ResultP:
                    Tries+=1
                    FinalTries+=1
                    print(f"[Require Retrie] Tries: {Tries}")
                else :
                    Tries+=3
                    FinalTries+=0
        if int(FinalTries) >= 3 :
            await session.close()
            return None
        else :
            print(f"Tries: {FinalTries}")
            await session.close()
            return "Live ✅", Rotate


print(asyncio.run(CheckProxy()))

