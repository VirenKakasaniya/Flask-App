import os
import json

with open('appFlask/config.json') as config_file:
    config = json.load(config_file)


class Config:
    SECRET_KEY= config.get('SECRET_KEY')

    #FOR LOCAL MYSQL
    #app.config['MYSQL_USER'] = ''
    #app.config['MYSQL_HOST'] = 'localhost'
    #app.config['MYSQL_PASSWORD'] = config.get('MYSQL_PASSWORD')
    #app.config['MYSQL_DB'] = 'myDatabase'

    #FOR PLANETHOSTER MYSQL
    #MYSQL_USER = ''
    #MYSQL_HOST = 'localhost'
    #MYSQL_PASSWORD = config.get('MYSQL_PASSWORD')
    #MYSQL_DB = ''
