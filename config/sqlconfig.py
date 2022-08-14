import sqlalchemy as alch
import os
#import dotenv 

#dotenv.load_dotenv()

password = "password" #os.getenv("sql_password")
dbName = "disney"
connectionData = f"mysql+pymysql://root:{password}@127.0.0.1/{dbName}"
engine = alch.create_engine(connectionData, pool_pre_ping=True)
