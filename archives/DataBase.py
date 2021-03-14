import os
import json
import pymongo
import simplejson

from bson import json_util
from datetime import datetime
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.core import serializers


USER_MONGO = os.getenv("USER_MONGO")
PASS_MONGO = os.getenv("PASS_MONGO")
DATA_MONGO = os.getenv("DATA_MONGO")

client = pymongo.MongoClient(f'mongodb+srv://{USER_MONGO}:{PASS_MONGO}@cluster0.a5pjd.mongodb.net/{DATA_MONGO}?retryWrites=true&w=majority')
db = client.myFirstDatabase




def getObjects():
    try:
        with open("archives\database.json", "r") as f:
            print('achou', f)
            return json.dump(f)
    except:
        print('Consultou em banco de dados')
        blog_collection = db.intentsschemas

        callback = blog_collection.find({})

        docs = list(callback)  # fetch the documents
        retornar = simplejson.dumps(docs, default = json_util.default)

        with open('archives\database.json', 'w') as outfile:
            json.dump(retornar, outfile)

        return retornar

def WriteHistory(msg, tag, resposta):
    blog_collection = db.conversations
    post = {
        'msg': msg,
        'tag': tag,
        'resposta': resposta,
        'post_date': datetime.now()
    }
    
    insert_post = blog_collection.insert_one(post)
    print(insert_post.inserted_id)