#!/usr/bin/python3
import unittest
from models.base_model import BaseModel

class TestBaseModel(unittest.TestCase):
    my_model = BaseModel()

    def test_dict(self):
        self.assertEqual(self.my_model.to_dict, "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__))

if __name__ == '__main__':
    unittest.main()