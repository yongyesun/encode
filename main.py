import time
import yaml
from yaml.loader import SafeLoader
from parse import makeclash
from clash import push
        
proxy_list=[]

if __name__ == '__main__':
  nodes = 'input.yaml'
  with open(nodes, 'r') as reader:
                reader_list = reader.readlines()
                working = []
                for i in range(reader_list.index('proxies:\n'),reader_list.index('proxy-groups:\n')+1):
                        working.append(reader_list(i))
                print(working)
                #for x in working['proxies']:
                        #proxy_list.append(x)
                #proxies = makeclash(proxy_list)
                #push(proxies)
