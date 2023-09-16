from bson.errors import InvalidId
from bson.objectid import ObjectId
from fastapi.exceptions import HTTPException

from app.DB import DB_CONNECT
from app.Error import Error
from app.models import Account_model
from app.schema import Account


def create_user(user:Account):
  query_filter = {"user_id":user.user_id}

  if DB_CONNECT.count(query_filter) > 0:
    raise HTTPException(detail="User with name already exist", status_code=400)

  try:

    account = Account_model(
    id = ObjectId(),
    name = user.name
  )
    DB_CONNECT.create(account)
  except Exception as e:
    print(e)
    return HTTPException(detail="failed to create account", status_code=400)
  
  return account.to_dict()


def get_all_users():
  accounts = DB_CONNECT.fetch_all()

  return accounts, None


def get_single_user(user_id:str):

  if user_id == "":
    return None, Error("user_id is required", 400)
  
  query_filter = {"user_id": user_id}
  try:
    account = DB_CONNECT.fetch_one(query_filter)
    if account:
      return account, None
    return None, Error("user not found", 404)
  except Exception as e:
    print(e)
    return None, Error("failed to get user", 500)
  

def update_user(user_id:str, account_object: Account_model = None):

  if user_id is not None:
    # check if user_id is already in use

    account, error = get_single_user(user_id)

    if account:
       return None, Error("user_id already in use", 400)
    account_object.user_id = user_id


  try:
      DB_CONNECT.update({"_id": account_object.id}, account_object.to_dict())
      return account_object, None
  except Exception:
      return None, Error("failed to update user", 500)
  

def delete_user(account: Account):
  try:

    query_filter = {"_id": account.id}
    req = DB_CONNECT.delete(query_filter)

    return req, None
  
  except Exception:
    return None, Error("failed to delete account", 500) 