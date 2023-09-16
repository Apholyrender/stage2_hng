from pydantic import BaseModel


class Account(BaseModel):
  name: str
  
class AccountProfile(Account):
  id: str


