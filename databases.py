from model import *

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///lecture.db')
Base.metadata.create_all(engine)
DBSession = sessionmaker(bind=engine)
session = DBSession()

# Write your functions to interact with the database here :

def add_product(name, exp, color, use):

    product_thing = Product(
        name=name,
        exp=exp,
        color=color, 
        use=use)
    session.add(product_thing)
    session.commit()

def update_product():
    product_thing= session.query(Product).filter_by(name=name).first()
    product_object.use = use()
    session.commit()


def delete_product(id):
  pass

def get_product(id):
  pass
