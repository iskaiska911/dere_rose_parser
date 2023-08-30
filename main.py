from parser import max_page,items_info,item_parse
from dict_elements import headers
import time
import numpy as np
import json
import datetime
import re

max_page,product_amount=max_page('https://www.derek-rose.com/collections/all?sort_by=title-ascending&filter.p.m.custom.global_market_availability=1',headers=headers)
print(max_page,product_amount)

info=[]
for i in range(1,max_page+1):
    print(f'{i} out of {max_page}')
    time.sleep(np.random.choice([x / 10 for x in range(7, 22)]))
    info.append(items_info(f"https://www.derek-rose.com/collections/all?sort_by=title-ascending&filter.p.m.custom.global_market_availability=1&page={i}",headers=headers))

patterns = [r'\s*-\s*XS',r'\s*-\s*S',r'\s*-\s*M', r'\s*-\s*O/S', r'\s*-\s*3XL',r'\s*-\s*L',r'\s*-\s*XL',r'\s*-\s*L',r'\s*-\s*XXL']

names=[info[i]['products'][j]['variants'][0]['name'] for i in range(0,len(info)) for j in range(0,len(info[i]['products']))]
names=list(set([i[0:i.index(' - ')].replace(' ','-').replace("'",'') for i in names]))

jsonData=json.dumps(info)
filename='www.derek-rose.com'+str(datetime.datetime.now().strftime("%Y_%m_%d-%I_%M_%S_%p"))

with open(filename, 'w') as f:
    json.dump(info, f)


full_item_info=[]
for i in names:
    print(f'{names.index(i)} out of {len(names)}')
    time.sleep(np.random.choice([x / 10 for x in range(7, 22)]))
    full_item_info.append(item_parse(f'https://www.derek-rose.com/products/{i}',headers=headers))

jsonData=json.dumps(full_item_info)
filename='full_item_derek-rose.com'+str(datetime.datetime.now().strftime("%Y_%m_%d-%I_%M_%S_%p"))
with open(filename, 'w') as f:
    json.dump(full_item_info, f)

