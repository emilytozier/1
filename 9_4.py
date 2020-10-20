import urllib.request

import json

from urllib.request import urlopen, urlretrieve
import re
from collections import defaultdict
fout = open('outa12.json', 'w', encoding='utf-8')

response = urlopen('https://apidata.mos.ru/v1/datasets/1251/rows?api_key=244a3bbb4bc0e5a51cccdb571c71eabe&$')

respData = response.read().decode('utf-8')

lst = json.loads(respData)

d1 = {}


d2= {}
res = defaultdict(list)

for now in lst:
    cells = now['Cells']
    admArea = cells['AdmArea']
    distr = cells['District']
    addr = cells['Address']
    res[distr].append(addr)
    #d2[distr] = res
    d1[admArea] = res

json.dump(d1, fout, ensure_ascii=False)
fout.close()