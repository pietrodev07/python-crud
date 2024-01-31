def show_users(users: list):
  for user in users:
    show_user(user)

def show_user(user: dict):
  print("***************************")
  print(f"ID: {user["id"]}")
  print(f"Firstname: {user["firstname"]}")
  print(f"Lastname:  {user["lastname"]}")
  print(f"Age: {user["age"]}")
  print("***************************")
  print()