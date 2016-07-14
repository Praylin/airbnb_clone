import peewee

class State(BaseModel):
        name = peewee.CharField(128, null = False, unique = True)

        def to_hash(self):
            return self.id + self.created_at + self.updated_at + self.name
