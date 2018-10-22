import re
import json
import os
from flask import Flask, render_template, request, Response, stream_with_context, jsonify,flash,Markup
from os import listdir, rename, remove
from os.path import dirname, isfile, join

from pymongo import MongoClient
connection = MongoClient()
connection = MongoClient('localhost', 27017)
db = connection.cognisearch
collection = db.candidate

app = Flask(__name__)

directory="/home/bsutfdemo/DataBase_Updated/candidate"
for filename in os.listdir(directory):
    if filename.endswith(".json"):
        x=os.path.join(directory,filename)
        print x
        y=open(x,"r").read()
        e=json.loads(y)
	#print e
	#z=json.loads(e)
	#print z
        collection.insert(e)
       
            
      
    
   