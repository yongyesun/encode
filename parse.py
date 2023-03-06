def makeclash(dictin):
    badprotocols = ['vless']
    proxies = []
    proxies_noname = []
    for y in dictin:
        #try:
        z = y.copy()
        y.pop('name')
        if y in proxies_noname:
            pass
        else:
            proxies_noname.append(y)
            if z['type'] in badprotocols:
                pass
            else:
                proxies.append(z)                                                 
        #except:
        #    continue
    print("makeclash",len(proxies))
    return proxies

"""                
   https://github.com/yu-steven/openit/
""" 
