from Model import Model_db
from View import View_db
from Controller import Controller_db

c = Controller_db(Model_db("postgres", "qwerty", "localhost", "5434", "Library"), View_db())
c.main_menu()
print("Connection closed")
