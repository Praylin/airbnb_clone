import peewee

class PlaceBook(BaseModel):
    place = peewee.ForeignKeyField(Place)
    user = peewee.ForeignKeyField(User, related_name = "places_booked")
    is_validated = peewee.BooleanField(default = False)
    date_start = peewee.DateTimeField(null = False)
    number_nights = peewee.IntegerField(default = 1)

    def to_hash(self):
        return self.id + self.created_at + self.updated_at + Place.id + User.id + self.is_validated + self.date_start + self.number_nights
