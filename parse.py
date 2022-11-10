def makeclash(dictin):
    badprotocols = ['vless']
    proxies = []
    for y in dictin:
        try:
            if y in proxies:
                pass
            else:
                if y['type'] in badprotocols:
                    pass
                else:
                    proxies.append(y)
        except:
            continue
    return 
