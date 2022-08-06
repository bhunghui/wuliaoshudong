# 数据库配置信息
import os

HOSTNAME = 'localhost'
PORT = '3306'
DATABASE = 'flask'
USERNAME = 'root'
PASSWORD = 'Born0128.Ydh'
DB_URI = 'mysql+pymysql://{}:{}@{}:{}/{}?charset=utf8'.format(USERNAME, PASSWORD, HOSTNAME, PORT, DATABASE)
SQLALCHEMY_DATABASE_URI = DB_URI
SECRET_KEY = os.urandom(24)
