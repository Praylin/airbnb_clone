import peewee

class City(BaseModel):
    name = peewee.CharField(128, null = False)
    state = peewee.ForeignKeyField(State,  related_name = "cities", on_delete = "CASCADE")
    
