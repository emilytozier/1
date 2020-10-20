from urllib.request import  urlopen, urlretrieve

import json
total=366
i=0
while i<total:
    response= urlopen('https://apidata.mos.ru/v1/datasets/3288?api_key=2925bf10e3a77c895dddbcb2d32d3e7b')
    dct = response.read().decode('utf-8')
    lst=json.loads(dct)
    print(dct[27])