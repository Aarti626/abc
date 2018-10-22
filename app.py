import re
import json
import os
from flask import Flask, render_template, request, Response, stream_with_context, jsonify,flash,Markup
from os import listdir, rename, remove


import os
import uuid
import bottle
import pymongo
bottle.debug(True)
mongo_con=pymongo.Connection(os.environ['OPENSHIFT_NOSQL_DB_HOST'],int(os.environ['OPENSHIFT_NOSQL_DB_PORT']))
mongo_db=mongo_con['sampledb']
mongo_db.authenticate(os.environ['OPENSHIFT_NOSQL_DB_USERNAME'],(os.environ['OPENSHIFT_NOSQL_DB_PASSWORD']))


app = Flask(__name__)


x="a1037.json"

y=open(x,"r").read()
e=json.loads(y)
print(e)
#print e
#z=json.loads(e)
#print z
collection.insert(e)
print("printed")     
            
      
    
   
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8080))
    app.run(host='0.0.0.0', port=port,debug=True)
    # sentiment_anlysis()
