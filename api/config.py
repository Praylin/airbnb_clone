''' variables of your RestAPI application depending of the environment variable AIRBNB_ENV'''
import os
HOST = 'localhost'
name = os.environ.get('AIRBNB_ENV')
# if (name == "development"):
DEBUG = True if name == 'development' else False
HOST = 'localhost' if name == 'development' else '0.0.0.0'
PORT = 3333 if name == 'development' else 3000
DATABASE = {'host' : '158.69.89.233',
            'user' : 'airbnb_user_dev' if name == 'development' else 'airbnb_user_prod' ,
            'database' : 'airbnb_dev' if name == 'development' else 'airbnb_prod',
            'port' : '21',
            'charset' : 'utf8',
            'password' : os.environ.get('AIRBNB_DATABASE_PWD_DEV') if name == 'development' else os.environ.get('AIRBNB_DATABASE_PWD_PROD')}
