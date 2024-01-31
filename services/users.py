from utils.data_handler import get_data, updata_data

USERS_FILE = "data/users.json"

def get_users() -> list:
  return get_data(USERS_FILE)["users"]

def get_user(id: int) -> dict :
  users = get_users()

  for user in users: 
    if user["id"] == id:
      return user

def delete_user(id: int):
  users = get_users()
  user_to_delete = {}

  for user in users: 
    if user["id"] == id:
      user_to_delete = user

  users.remove(user_to_delete)
  updata_data(USERS_FILE, users)

def create_user(id: int, firstname: str, lastname: str, age: int):
  user = {
    "id": id,
    "firstname": firstname,
    "lastname": lastname,
    "age": age
  }

  users= get_users()
  users.append(user)
  updata_data(USERS_FILE, users)

def edit_user(id: int, firstname: str, lastname: str, age: int):
  users= get_users()

  for user in users: 
    if user["id"] == id:
      user["firstname"] = firstname
      user["lastname"] = lastname
      user["age"] = age

  updata_data(USERS_FILE, users)