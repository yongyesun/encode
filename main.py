import time
import yaml
from yaml.loader import BaseLoader
from parse import makeclash
from clash import push
        
proxy_list=[]

if __name__ == '__main__':
  nodes = 'input.yaml'
  with open(nodes, 'r') as reader:
                """
                reader_list = reader.readlines()                
                for i in range(reader_list.index('proxies:\n')+1,reader_list.index('proxy-groups:\n')):
                        reader_list[i] = reader_list[i].strip()
                        reader_list[i] = reader_list[i].strip("-")
                        reader_list[i] = reader_list[i].strip()
                        reader_list[i] = reader_list[i].strip("{}")
                        reader_list[i]
                        proxy_list.append(reader_list[i])
                """        
                working = yaml.load(reader, Loader=BaseLoader)
                for x in working['proxies']:
                        proxy_list.append(x)
                print("before",len(proxy_list))
                #proxy_list=list(proxy_list)
                proxies = makeclash(proxy_list)
                push(proxies)
