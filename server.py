from flask import Flask, request
import json
from config import db

app = Flask(__name__) #__name__ this is using the name of the folder (107)

@app.get("/")
def home():
    return "Hello from flask"

@app.get("/testing")
def test():
    return "Hello form another page"

# create 2 more API (about and blog)
@app.get("/about")
def about():
    me = {"name": "Fernanda Ugalde"}
    return json.dumps(me)

@app.get("/blog")
def blog():
    return "Hello from Blog page"

@app.get("/version")
def version():
    version = {"name": "mouse", "version": "2", "build": 123456}
    return json.dumps(version)

# this time we need to read and write into the server
products = []
@app.get("/api/products") 
def get_products():
    return json.dumps(products) #js to json

def fix_id(obj):
    obj["_id"]=str(obj["_id"])
    return obj

@app.post("/api/products") 
def save_product():
    # should save a new product
    product = request.get_json() #json to js

    print (product)
    #mock the save
    #products.append(product)
    db.products.insert_one(product)

    return json.dumps(fix_id(product))

app.run(debug=True) # apply the changes on dthe code, live


# API / Endpoints
#transform JSON / convert JSON in an object again
