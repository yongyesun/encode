import time
import yaml
from yaml.loader import BaseLoader, SafeLoader
from parse import makeclash
from clash import push
        
proxy_list=[]

if __name__ == '__main__':
  nodes = 'input.yaml'
  with open(nodes, 'r') as reader:       
                working = yaml.load(reader, Loader=BaseLoader)
                for x in working['proxies']:
                        proxy_list.append(x)
                print("before",len(proxy_list))
                #proxy_list=list(proxy_list)
                proxies = makeclash(proxy_list)
                push(proxies)

"""                
   https://github.com/yu-steven/openit/
"""   
