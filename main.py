from flask import Flask, jsonify
import random
import tools.sqltools as sql 
import json
import pandas as pd

app = Flask(__name__)

@app.route("/")
def greeting ():
    return f"Hi! How are you doing?"

# Get everything: SQL
@app.route("/all")
def all_reviews ():
    return jsonify(sql.get_everything())

# Get everything from 1 disney branch: SQL
@app.route("/branch/<branch_name>")
def all_from_branch ():
    return jsonify(sql.get_everything_from_branch())

#this will check that the name is the meain
if __name__ == '__main__': 
    app.run(port=3306, debug=True)
    # debug= True/False, when you change something it updatescle