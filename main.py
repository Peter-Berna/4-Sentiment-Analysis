from tokenize import Name
from flask import Flask, request, jsonify
import random
import tools.sqltools as sql 
import json
import pandas as pd
from os import name
import markdown.extensions.fenced_code
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from nltk.corpus import stopwords
import statistics as st


app = Flask(__name__)

@app.route("/")
def greeting ():
    return f"Hi! How are you doing?"

#SUBSTITUTE GREETING BY 
# GET: render markdown
# @app.route("/")
# def index():
    # readme_file = open("README.md", "r")
    # md_template = markdown.markdown(readme_file.read(), extensions = ["fenced_code"])
    # return md_template

# Get everything: SQL
@app.route("/all")
def all_reviews ():
    print("These are all the reviews from the database:")
    return jsonify(sql.get_everything())

# Get branches' names
@app.route("/branch")
def branches_names ():
    print("These are the three branch names:")
    return jsonify(sql.get_branch_names())

# Get everything from 1 disney branch: SQL
@app.route("/branch/<name>")
def all_from_branch (name):
    print(f"These are all the reviews from {name}")
    return jsonify(sql.get_everything_from_branch(name))

# Get total nº of reviews
@app.route("/total/reviews")
def total_reviews ():
    return jsonify(sql.get_total_reviews())

#Get all reviewers' location
@app.route("/all/locations")
def all_locations ():
    note = "These are all the reviewers' countries' of origin:"
    result = sql.get_all_reviewer_location()
    result["0"] = note
    return jsonify(result)

# Get total reviews from one country
@app.route("/total/<country>")
def total_one_country (country):
    return jsonify(sql.get_total_one_country(country))

# Get all review texts from one country
@app.route("/all/reviews/<country>")
def all_reviews_one_country(country):
    note = f"These are all the reviews of visitors from {country}"
    result = sql.get_reviews_one_country(country)
    result["0"] = note
    return jsonify(result)

# Get summary stats visitors (3 dictionaries):
## 1. Visitors & Avg. Rating per branch
## 2. Visitors per Month
## 3. Visitors per Country
@app.route("/summary_visitors")
def summary_stats_visitors():
    visitors_rating = sql.get_visitors_rating_branch()
    month = sql.get_visitors_month()
    country = sql.get_visitor_country()
    result = {
        "Visitors & Avg. Rating per branch": visitors_rating,
        "Visitors per Month": month,
        "Visitors per Country": country
    }
    return jsonify(result)

# Get avg. rating per year and branch
@app.route("/rating")
def rating():
    return jsonify(sql.get_year_branch_rating())

## SENTIMENTS HELL YEAH!
# get avg. polarity score specifying branch, reviewer location, year, month
@app.route("/sentiment/<branch>/<country>/<year>/<month>")
def get_sentiment_branch_country_year_month(branch, country, year, month):


#this will check that the name is the meain
if __name__ == '__main__': 
    app.run(port=8000, debug=True)
    # debug= True/False, when you change something it updatescle