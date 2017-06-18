import bson
import pymongo
import json
from bson import ObjectId
from pymongo import MongoClient
import string


import networkx as nx



def run(officer):
    # Create an empty response object.
    response = {}

   # this method traverses the documents in the selected graph collection and builds a JSON object
   # that represents a list of all nodes in the graph

    client = MongoClient('localhost', 27017)
    db = client['aspt']
    # get a list of all collections (excluding system collections)
    namehint_coll_name = 'authors5'
    collection = db[namehint_coll_name]
     
    # loop through the records in the network and take the appropriate action for each type. Suppress
    # the ID field because it doesn't serialize in JSON
    
    nodes = collection.find({},{'_id':0, 'role':1})
    count = 0
    roles = set()
    for rec in nodes:
        roles.add(rec['role'])
        count += 1
    
    rolelist = list(roles)
    # Pack the results into the response object, and return it.
    response['result'] = {}
    response['result']['roles'] = rolelist
    client.close()

    # Return the response object.
    #tangelo.log(str(response))
    return json.dumps(response)
