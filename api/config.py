''' variables of your RestAPI application depending of the environment variable AIRBNB_ENV'''
import os
HOST = 'localhost'
name = os.environ.get('AIRBNB_ENV')
DEBUG = False
HOST = '0.0.0.0'
PORT = 3000
DATABASE = {'host' : '158.69.89.233',
            'user' : 'airbnb_user_prod',
            'database' : 'airbnb_prod',
            'port' : 3306,
            'charset' : 'utf8',
            'password' : os.environ.get('AIRBNB_DATABASE_PWD_PROD')
            }

if name == "development":
    DEBUG = True
    HOST = 'localhost'
    PORT = 3333
    DATABASE = {'host' : '158.69.89.233',
                'user' : 'airbnb_user_dev'
                'database' : 'airbnb_dev'
                'port' : 21
                'charset' : 'utf8',
                'password' : os.environ.get('AIRBNB_DATABASE_PWD_DEV')
                }

elif name == "test":
    DEBUG = False
    HOST = 'localhost'
    PORT = 5555
    DATABASE = {'host' : '158.69.89.233',
                'user' : 'airbnb_user_test'
                'database' : 'airbnb_test'
                'port' : 21
                'charset' : 'utf8',
                'password' : os.environ.get('AIRBNB_DATABASE_PWD_TEST')
                }
