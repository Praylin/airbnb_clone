import peewee

class City(BaseModel):
    name = peewee.CharField(128, null = False)
    state = peewee.ForeignKeyField(State,  related_name = "cities", on_delete = "CASCADE")

    def to_hash(self):
        return self.id + self.created_at + self.updated_at + self.name + State.id
