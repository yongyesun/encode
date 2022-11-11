import time
#import yaml
#from yaml.loader import SafeLoader
from parse import makeclash
from clash import push
        
proxy_list=[]

if __name__ == '__main__':
  nodes = 'input.yaml'
  with open(nodes, 'r') as reader:
                reader_list = reader.readlines()
                for i in range(reader_list.index('proxies:\n')+1,reader_list.index('proxy-groups:\n')):
                        reader_list[i] = reader_list[i].strip()
                        reader_list[i] = reader_list[i].strip("-")
                        reader_list[i] = reader_list[i].strip()
                        reader_list[i] = reader_list[i].strip("{}")
                        reader_list[i] = reader_list[i].split(",")
                        proxy_list.append(reader_list[i])
                #print(proxy_list)
                proxies = makeclash(proxy_list)
                push(proxies)
