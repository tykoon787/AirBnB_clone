from models.base_model import BaseModel
from models import storage

class User(BaseModel):
    email = ""
    password = ""
    first_name = ""
    last_name = ""
    def __init__(self):
        super().__init__(self.email, self.password, self.first_name, self.last_name)
        storage.new(self)


