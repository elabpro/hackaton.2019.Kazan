from elasticsearch import Elasticsearch
import datetime
import random
import time

# Connect to ElasticSearch
def getES(host = ["localhost:9200"]):
    es = Elasticsearch(host)
    result = None
    if es.ping():
        result = es
    else:
        print(host)
        print('ES is not ready!')
    return result


# Publish data to ElasticSearch
def publishToES(data, es):
    print(es.index(index='datalake', doc_type='_doc', id=data['id'], body=data))


es = getES()
if es != None:
    print("OK")
    towns = [{
        "town": "Irkutsk",
        "lat": 52.243610,
        "lon": 104.227603
        },{
        "town": "Kazan",
        "lat": 55.794006,
        "lon": 49.116671
        },{
        "town": "Moscow",
        "lat": 55.732060,
        "lon": 37.597434
        },{
        "town": "Novosibirsk",
        "lat": 54.976479,
        "lon": 82.924725
        }
    ]
    i = 0
    while (True):
        i = (i+1) % len(towns)
        lat = towns[i]["lat"]
        lon = towns[i]["lon"]
        timestamp = datetime.datetime.utcnow()
        lati = lat + float(random.random()/1)
        loni = lon + float(random.random()/1)
        sig = float(random.random()*100)-50
        eq = 'person' + str(float(random.random()*10))[:3]

        data = {'id': timestamp.timestamp(),
            'location': str(lati)+ ',' + str(loni), 
            'operator': 'Tele2',
            'type': '3G',
            'timestamp': timestamp.strftime('%Y-%m-%dT%H:%M:%S'),
            'signal': sig,
            'equipment': eq
            }
        print(data)
        publishToES(data,es)
        time.sleep(1)
#    for i in range(1,100,1):
#      lati = lat + float(i)/1000
#      loni = lon + float(i*random.random())/1000
#      data = {'id':(i+100),'location': str(lati)+ ',' + str(loni), 'route': 40, 'reg_number': 'o123oo 38', 'timestamp': timestamp.strftime('%Y-%m-%dT%H:%M:%S')}
#      publishToES(data,es)
#      print(data)
