import sqlalchemy as alch
import os
import dotenv 

dotenv.load_dotenv()

password = os.gentenv("sql_password")
dbName = "HP"
connectionData = f”mysql+pymysql://root:{passw}@localhost/{dbName}”
engine = alch.create_engine(connectionData)
