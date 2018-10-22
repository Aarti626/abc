import re
import json
import os
from flask import Flask, render_template, request, Response, stream_with_context, jsonify,flash,Markup
from os import listdir, rename, remove


from pymongo import MongoClient
connection = MongoClient()
connection = MongoClient('localhost', 27017)
db = connection.cognisearch
collection = db.candidate

app = Flask(__name__)


x="a1037.json"
print x
y=open(x,"r").read()
e=json.loads(y)
#print e
#z=json.loads(e)
#print z
collection.insert(e)
       
            
      
    
   
