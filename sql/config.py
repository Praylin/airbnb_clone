''' variables of your RestAPI application depending of the environment variable AIRBNB_ENV'''
import os
name = os.environ.get('AIRBNB_ENV')
if (name == "development"):
    DEBUG = True
    HOST = 'localhost'
    PORT = 3333
    DATABASE = {'host' : '158.69.89.233',
                'user' : 'airbnb_user_dev',
                'database' : 'airbnb_dev',
                'port' : '21',
                'charset' : 'utf8',
                'password' : os.environ.get('AIRBNB_DATABASE_PWD_DEV')}

elif (name == "production"):
    DEBUG = False
    HOST = '0.0.0.0'
    PORT = 3000
    DATABASE = {'host' : '158.69.89.233',
                'user' : 'airbnb_user_prod',
                'database' : 'airbnb_prod',
                'port' : '21',
                'charset' : 'utf8',
                'password' : os.environ.get('AIRBNB_DATABASE_PWD_PROD')}
