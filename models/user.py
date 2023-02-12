from models.base_model import BaseModel
from models import storage

class User(BaseModel):
    email = ""
    password = ""
    first_name = ""
    last_name = ""
    def __init__(self):
        super().__init__(email=self.email, password=self.password, first_name=self.first_name, last_name=self.last_name)
        storage.new(self)


