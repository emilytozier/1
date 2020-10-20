import urllib.request

import json

from urllib.request import urlopen, urlretrieve

response = urlopen( 'https://apidata.mos.ru/v1/datasets/1251/rows?api_key=244a3bbb4bc0e5a51cccdb571c71eabe&$')

respData = response.read().decode('utf-8')

lst = json.loads(respData)

d1 = {}

d2 = {}
mega_array=[]
for now in lst:

    cells = now['Cells']

    admArea = cells['AdmArea']

    distr = cells['District']

    addr = cells['Address']

    d2[distr] = {}
    d1[admArea] = d2

    mega_array={}
    if admArea not in mega_array:
        mega_array[admArea] = {distr: [addr]}


    else:
        if distr in mega_array[admArea]:
            mega_array[admArea][distr].append(addr)
        else:
            mega_array[admArea][distr]=[addr]
    print(mega_array)

fout = open('outage.json', 'w', encoding='utf-8')

json.dump(d1, fout, ensure_ascii=False)

fout.close()