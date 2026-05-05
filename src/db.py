from sqlalchemy import create_engine

def get_engine():
    return create_engine("postgresql://user:password@db:5432/ecommerce")