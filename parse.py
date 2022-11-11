def makeclash(dictin):
    badprotocols = ['vless']
    proxies = []
    proxies_noname = []
    for y in dictin:
        try:
            if y in proxies_noname:
                pass
            else:
                if y['type'] in badprotocols:
                    pass
                else:
                    proxies.append(y)
                    proxies_noname.append(y[1:])
        except:
            continue
    print(len(proxies))
    return proxies
