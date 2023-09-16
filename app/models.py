from bson.objectid import ObjectId
from datetime import datetime


class Account_model:
  def __init__(
      self, 
      id: ObjectId,
      name: str
  ):
    self.id = id
    self.name = name

    self.used_projection = False


  def to_dict(self):
      data = {
        "_id": self.id,
        "name": self.name
      }

      return data

