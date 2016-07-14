
from app import app
from app.views import *
import config
# if __name__ == '__main__':
app.run(host = config.HOST, port = config.PORT, debug = config.DEBUG)
