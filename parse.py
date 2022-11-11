def makeclash(dictin):
    badprotocols = ['vless']
    proxies = []
    proxies_noname = []
    for y in dictin:
        try:
            z = y.pop('name')
            if z in proxies_noname:
                pass
            else:
                if y['type'] in badprotocols:
                    pass
                else:
                    proxies.append(y)
                    proxies_noname.append(z)
        except:
            continue
    print("makeclash",len(proxies))
    return proxies
