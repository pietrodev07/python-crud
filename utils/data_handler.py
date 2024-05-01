import json

def get_data(file_path: str) -> dict:
  with open(file_path, "r") as file:
    return json.load(file)
  
def update_data(file_path: str, users: list):
  data = { "users": users }
  with open(file_path, "w") as file:
    return json.dump(data, file, indent=2)