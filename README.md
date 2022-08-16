# Project IV Sentiment Analysis API
## API - SQL query for Disneyland Reviews

![Screenshot](https://github.com/Peter-Berna/4-Sentiment-Analysis/blob/main/images/disneyland_disney.gif
________________________________________________

## 1 - Main Endpoint page for the API query:
    http://127.0.0.1:8000/


## 2 - Endpoint route to get all the reviews:

    http://127.0.0.1:8000/all

## 3 - Endpoint route to get the Disney branchs' names:

    http://127.0.0.1:8000/branch
    
## 4 - Endpoint route to get everything from 1 disney branch:

    http://127.0.0.1:8000/branch/<name>
    
## 5 - Endpoint route to get total number of reviews:

    http://127.0.0.1:8000/total/reviews
    
## 6 - Endpoint route to get all reviewers' location:

    http://127.0.0.1:8000/all/locations
  
## 7 - Endpoint route to get total reviews from one country:

    http://127.0.0.1:8000/all/reviews/<country>
    
## 8 - Endpoint route to get summary stats from the visitors (3 dictionaries):
1. Visitors & Avg. Rating per branch
2. Visitors per Month
3. Visitors per Country

    http://127.0.0.1:8000/summary_visitors
  
## 9 - Endpoint route to get avg. rating per year and branch:

    http://127.0.0.1:8000/rating
    
## 10 - Endpoint route to get avg. polarity score specifying branch, reviewer location, year, month:

    http://127.0.0.1:8000/sentiment/<branch>/<country>/<year>/<month>")


## 11 - Endpoint route to get polarity score for one random review:
 
    http://127.0.0.1:8000/sentiment/random

## 12 - Endpoint route for posting a new review:
 
    http://127.0.0.1:8000/post