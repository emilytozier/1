import json
a_data=[{'a':[1,2,3],'b':{'c':'Copy','d':'Data'},'e':(1,2,3),'f':3.14}]
json_data1=json.dumps(a_data)
#print(json_data1)
#print(a_data)
#b_data=json.loads(json_data1)
#print(b_data)

#json_data2=json.dumps(a_data, separators=(',',':'))
#print(json_data2)

#json_data3=json.dumps(a_data,indent=4)
#print(json_data3)

json_data4=json.dumps(a_data,sort_keys=True)
print(json_data4)