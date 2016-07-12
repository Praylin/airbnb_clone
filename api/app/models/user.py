import peewee
import md5

class User(BaseModel):
    email = peewee.CharField(128, null = False, unique = True)
    password = peewee.CharField(128, null = False)
    first_name = peewee.CharField(128, null = False)
    last_name = peewee.CharField(128, null = False)
    is_admin = peewee.BooleanField(default = False)
    def set_password(self, clear_password): #Function to encrypt password using RSA's MD5 algorithm
        password = md5.new(clear_password).digest()
        
