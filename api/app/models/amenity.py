import peewee

class Amenity(BaseModel):
    name = peewee.CharField(128, null = False)

def to_hash(self):
    return self.id + self.created_at + self.updated_at + self.name
