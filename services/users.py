from utils.data_handler import get_data

def get_users() -> list:
  return get_data("data/users.json")["users"]

def get_user(id: int) -> dict | None:
  users = get_users()
  real_id = id - 1

  if real_id < 0 or real_id >= len(users):
    return None
  
  return users[real_id]