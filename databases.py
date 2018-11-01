from model import *

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///lecture.db')
Base.metadata.create_all(engine)
DBSession = sessionmaker(bind=engine)
session = DBSession()

# Write your functions to interact with the database here :

def create_product():
  #TODO: complete the functions (you will need to change the function's inputs)
  pass

def update_product():
  #TODO: complete the functions (you will need to change the function's inputs)
  pass

def delete_product(id):
  pass

def get_product(id):
  pass
