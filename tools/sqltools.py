from config.sqlconfig import engine
import pandas as pd
import random

## GET
def get_everything():
    query = (f"""SELECT * FROM disneyland_reviews;""")
    df=pd.read_sql_query(query,con=engine)
    return df.to_dict(orient='records')

def get_branch_names():
    query = (f"""SELECT DISTINCT Branch FROM disneyland_reviews""")
    df=pd.read_sql_query(query,con=engine)
    return df.to_dict(orient='records')

def get_everything_from_branch(name):
    query = (f"""SELECT * FROM disneyland_reviews WHERE Branch = "{name}";""")
    df=pd.read_sql_query(query,con=engine)
    return df.to_dict(orient='records')

def get_total_reviews():
    query = ("""SELECT COUNT(Review_text) as 'Total reviews' FROM disneyland_reviews;""")
    df=pd.read_sql_query(query,con=engine)
    return df.to_dict(orient='records')

def get_all_reviewer_location():
    query = (f"""SELECT DISTINCT Reviewer_Location FROM disneyland_reviews;""")
    df=pd.read_sql_query(query,con=engine)
    return df.to_dict()

def get_total_one_country(country):
    country = f'"{country}"'
    query = (f"""SELECT COUNT(Review_text) as 'Total reviews from {country}' FROM disneyland_reviews WHERE Reviewer_Location = {country};""")
    df=pd.read_sql_query(query,con=engine)
    return df.to_dict(orient='records')

def get_reviews_one_country(country):
    country = f'"{country}"'
    query = (f"""SELECT Review_Text FROM disneyland_reviews WHERE Reviewer_Location = {country};""")
    df=pd.read_sql_query(query,con=engine)
    return df.to_dict()

def get_visitors_rating_branch():
    query = (f"""SELECT Branch, COUNT(Review_ID) as 'Total Visitors', AVG(Rating) as 'Avg. Rating'
    FROM disneyland_reviews
    GROUP BY Branch
    ORDER BY COUNT(Review_ID) DESC;""")
    df=pd.read_sql_query(query,con=engine)
    return df.to_dict(orient='records')

def get_visitors_month():
    query = (f"""SELECT Month, COUNT(Review_ID) AS 'Visitors'
    FROM disneyland_reviews
    WHERE Month IS NOT NULL
    GROUP BY Month
    ORDER BY STR_TO_DATE(CONCAT('0001 ', Month, ' 01'), '%%Y %%M %%d');""")
    df=pd.read_sql_query(query,con=engine)
    return df.to_dict(orient='records')

def get_visitor_country():
    query = (f"""SELECT DISTINCT Reviewer_Location as 'Country', COUNT(Review_ID) AS 'Visitors'
    FROM disneyland_reviews
    GROUP BY Reviewer_Location
    ORDER BY COUNT(Review_ID) DESC;""")
    df=pd.read_sql_query(query,con=engine)
    return df.to_dict(orient='records')

def get_year_branch_rating():
    query = (f"""SELECT DISTINCT Year, Branch, AVG(Rating) as 'Avg. Rating'
    FROM disneyland_reviews
    WHERE Year IS NOT NULL
    GROUP BY Year, Branch
    ORDER BY Year ASC;""")
    df=pd.read_sql_query(query,con=engine)
    return df.to_dict(orient='records')

# GET SENTIMENT

def get_sentiment_branch_country_year_month(branch, country, year, month):
    query = (f"""SELECT * FROM disneyland_reviews WHERE Branch = '{branch}' AND Reviewer_Location = '{country}' AND Year = '{year}' and Month = '{month}';""")
    df=pd.read_sql_query(query,con=engine)
    return df.to_dict(orient='records')

def get_random_review():
    query = (f"""SELECT Review_Text FROM disneyland_reviews""")
    df=pd.read_sql_query(query,con=engine)
    index = random.choice(range(0, 42655))
    return df.iloc[[index]]

## POST
def new_review(id, rating, year_date, country, review, Branch, Year, Month):
    engine.execute(f""" INSERT INTO disney.disneyland_reviews (Review_ID, Rating, Year_Month, Reviewer_Location, Review_Text, Branch, Year, Month)
    VALUES ({id}, '{rating}', '{year_date}', '{country}', '{review}', '{Branch}', '{Year}', '{Month}');""")
    return f"Correctly introduced: {id}, {rating}, {year_date}, {country}, {review}, {Branch}, {Year}, {Month}"