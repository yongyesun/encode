import time
import yaml
from yaml.loader import SafeLoader
from parse import makeclash
from clash import push
        
proxy_list=[]

if __name__ == '__main__':
  nodes = 'input.yaml'
  with open(nodes, 'r') as reader:
                working = yaml.load(reader, Loader=yaml.SafeLoader)
                for x in working['proxies']:
                        proxy_list.append(x)
                proxies = makeclash(proxy_list)
                push(proxies)
