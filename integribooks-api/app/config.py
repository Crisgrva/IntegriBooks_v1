import os


class Config:
    user = os.environ['MYSQL_USER']
    password = os.environ['MYSQL_ROOT_PASSWORD']
    database = os.environ['MYSQL_DATABASE']
    host = os.environ['MYSQL_HOST']

    SQLALCHEMY_DATABASE_URI = f'mysql+pymysql://{user}:{password}@{host}:3306/{database}'
    #SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL", "sqlite:///integribooks.db")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
