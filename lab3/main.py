from Model import Base, engine
from Controller import Controller_db
from sqlalchemy import MetaData

metadata = MetaData()
Base.metadata.create_all(engine)
Controller_db.main_menu()

print("Connection closed")
