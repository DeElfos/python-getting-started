import os
import json
import pymongo
import simplejson

from bson import json_util
from datetime import datetime
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.core import serializers



class intents(object):
    intents = ''
    # The class "constructor" - It's actually an initializer

    def __init__(self, intents):
        self.intents


def getObjects():
    # USER_MONGO = os.getenv("USER_MONGO")
    # PASS_MONGO = os.getenv("PASS_MONGO")
    # DATA_MONGO = os.getenv("DATA_MONGO")

    USER_MONGO = 'shawdom'
    PASS_MONGO = 'MarcosFilho'
    DATA_MONGO = 'myFirstDatabase'
    #print('users', USER_MONGO, PASS_MONGO, DATA_MONGO)

    client = pymongo.MongoClient(
        f'mongodb+srv://{USER_MONGO}:{PASS_MONGO}@cluster0.a5pjd.mongodb.net/{DATA_MONGO}?retryWrites=true&w=majority')

    db = client.myFirstDatabase
    blog_collection = db.intentsschemas

    callback = blog_collection.find({})

    docs = list(callback)  # fetch the documents
    retornar = simplejson.dumps(docs, default = json_util.default)

    # for post in callback:
    #     student = intents(post)
    #     retornar.append(student)

    return retornar