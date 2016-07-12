from app.models import *

try:
     User.create_table()
except peewee.OperationalError:
    pass

try:
     State.create_table()
except peewee.OperationalError:
    pass

try:
     City.create_table()
except peewee.OperationalError:
    pass

try:
     Place.create_table()
except peewee.OperationalError:
    pass

try:
     PlaceBook.create_table()
except peewee.OperationalError:
    pass

try:
     Amenity.create_table()
except peewee.OperationalError:
    pass

try:
     PlaceAmenities.create_table()
except peewee.OperationalError:
    pass
