import requests
import json
import pymongo
client= pymongo.MongoClient("mongodb://root:s123@mongo_compose:27017/")
db=client["transacciones"]
coll=db["moni"]
bulk=[]
#response=requests.get("") #aqui se pondria el link del cual sacaremos la info 
#dcc= response.json()
with open('dato.json','r') as j:
    doc=json.load(j)

print (list(doc[0].keys()))
for i in range (0, len(doc),1):
    insert_data={}
    if coll.find_one({'_id':doc[i]['reference']})== None:
        insert_data['_id']=doc[i]['reference']
        insert_data['date']=doc[i]['date']
        insert_data['amount']=doc[i]['amount']
        insert_data['type']=doc[i]['type']
        insert_data['category']=doc[i]['category']
        insert_data['user_email']=doc[i]['user_email']
        bulk.append(insert_data)
result = coll.insert_many(bulk)
print(f"¡Se ha terminado la inserción de datos!: {result.inserted_ids}")
