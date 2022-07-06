from sqlite3 import connect
from sqlalchemy import create_engine, MetaData 

engine = create_engine("mysql+pymysql://root:marioarturo2512@localhost:3306/hearhstoneproyect")

Meta = MetaData()

conn = engine.connect()