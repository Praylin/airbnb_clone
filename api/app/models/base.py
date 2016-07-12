from peewee import *
import datetime
database = peewee.MySQLDatabase('airbnb_dev')

class BaseModel(peewee.Model):
    id = peewee.PrimaryKeyField(unique = True)
    created_at = DateTimeField(default=datetime.now)
    updated_at = DateTimeField(default=datetime.now)
    def save(self, *args, **kwargs): #Overloads current date and time
        self.updated_at = datetime.datetime.now()
    class Meta:
        database = database
        order_by = ("id", )
