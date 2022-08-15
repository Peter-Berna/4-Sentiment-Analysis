from config.sqlconfig import engine
import pandas as pd

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
    query = (f"""SELECT DISTINCT Reviewer_Location FROM disneyland_reviews""")
    df=pd.read_sql_query(query,con=engine)
    return df.to_dict()

def get_total_one_country(country):
    country = f'"{country}"'
    query = (f"""SELECT COUNT(Review_text) as 'Total reviews from {country}' FROM disneyland_reviews WHERE Reviewer_Location = {country}""")
    df=pd.read_sql_query(query,con=engine)
    return df.to_dict(orient='records')

def get_reviews_one_country(country):
    country = f'"{country}"'
    query = (f"""SELECT Review_Text FROM disneyland_reviews WHERE Reviewer_Location = {country}""")
    df=pd.read_sql_query(query,con=engine)
    return df.to_dict()

    ## POST
def new_message (scene, character_name, dialogue):

    engine.execute(f"""
    INSERT INTO users (scene, character_name, dialogue)
    VALUES ({scene}, '{character_name}', '{dialogue}');
    """)
    
    return f"Correctly introduced: {scene} {character_name} {dialogue}"