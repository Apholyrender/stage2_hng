from fastapi import APIRouter
from fastapi.responses import JSONResponse

import app.services as services
from app.schema import Account, AccountProfile
from app.services import (create_user, delete_user, get_all_users,
                          get_single_user, update_user)

router = APIRouter(prefix="/api/v1")


@router.get("/users")
def read_accounts():
  accounts, error = get_all_users()

  if error:
    return JSONResponse(status_code=500, content={"msg":"failed to get users"})
  
  if accounts is None:
    return JSONResponse(status_code=404, content={"msg":"no users found"})
  return [AccountProfile(id= str(account.id), user_id=account.user_id) for account in accounts]



@router.get("/users/{user_id}")
def read_an_account(user_id: str):
  account, error = get_single_user(user_id)
      
  if error:
    return JSONResponse(status_code=error.code, content={"msg":error.msg})
  if not account:
    return JSONResponse(status_code=404, content={"msg":"user not found"})
  return AccountProfile(id= str(account.id), user_id=account.user_id).model_dump()

@router.post("/users", response_model=AccountProfile, status_code=201)
def create_account(request: Account):
    return services.create_user(request)

    # if error:
    #     return JSONResponse(status_code=error.code, content={"msg":error.msg})

    # if not account:
    #     return JSONResponse(status_code=500, content={"msg":"failed to create user"})
    # print(account.to_dict())
    # return JSONResponse(content=AccountProfile(id= str(account.id), user_id=account.user_id).model_dump(), status_code=201)


@router.put("/users/{user_id}")
def update_account(user_id: str, request: Account):
  account, error = get_single_user(user_id)

  if error:
    return JSONResponse(status_code=error.code, content={"msg":error.msg})

  if not account:
    return JSONResponse(status_code=404, content={"msg":"user not found"})

  account, error = update_user(
    account_object=account,
    user_id=request.user_id,
    )

  if error:
    return JSONResponse(status_code=error.code, content=error.msg)

  if not account:
    return JSONResponse(status_code=500, content={"msg":"failed to update user"})

  return AccountProfile(id= str(account.id), user_id=account.user_id).model_dump()


@router.delete("/users/{user_id}")
def delete_account(user_id: str):
  account, error = get_single_user(user_id)

  if error:
    return JSONResponse(status_code=error.code, content={"msg":error.msg})

  if not account:
    return JSONResponse(status_code=404, content={"msg":"user not found"})

  account, error = delete_user(account)

  if error:
    return JSONResponse(status_code=error.code, content={"msg":error.msg})

  if not account:
    return JSONResponse(status_code=500, content={"msg":"failed to delete user"})

  return JSONResponse(status_code=204, content={})