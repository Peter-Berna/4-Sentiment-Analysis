from flask import Flask, jsonify
import random
from pymongo import MongoClient
import tools.mongotools as mongo 
import json

# mongo.all_sentences()
# mongo.inserting()

app = Flask(__name__)

@app.route("/")
def greeting ():
    return f"How are you doing"

@app.route("/line/<name>")
def all_from_mongo(name):
    lines = mongo.all_sentences(name)
    return jsonify(lines)

@app.route("/random-number")
def random_number ():
    return str(random.choice(range(0,11)))

@app.route("/campus/<location>")
def campus_location (location):
    if location == "bcn":
        return "Carrer Pamplona 96"
    elif location == "mad":
        return "Paseo de la chopera, 14"

if __name__ == '__main__':
    app.run(debug=True)