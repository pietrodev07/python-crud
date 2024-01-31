from services.users import get_users, get_user, delete_user, create_user, edit_user
from utils.view import show_users, show_user

while (True):
  print("Choice the operation that you would to execute")

  print("Digit <1> to view all users")
  print("Digit <2> to view a specific user (by id)")
  print("Digit <3> to delete a specific user (by id)")
  print("Digit <4> to create a user")
  print("Digit <5> to edit a user")
  print("Digit <6> to exit")

  choice = 0

  try:
    choice = int(input())
  except ValueError:
    print("Insert only numbers")

  match choice:
    case 1:
      users = get_users()
      show_users(users)
    case 2:
      id = int(input("Insert the ID of the user: "))
      user = get_user(id)

      if user is not None:
        show_user(user)
    case 3:
      id = int(input("Insert the ID of the user: "))
      delete_user(id)
    case 4:
      id = int(input("Insert the ID of the user: "))
      firstname = input("Insert the first name of the user: ")
      lastname = input("Insert the last name of the user: ")
      age = int(input("Insert the age of the user: "))

      create_user(id, firstname, lastname, age)
    case 5:
      id = int(input("Insert the ID of the user: "))
      firstname = input("Insert the first name of the user: ")
      lastname = input("Insert the last name of the user: ")
      age = int(input("Insert the age of the user: "))

      edit_user(id, firstname, lastname, age)
    case 6:
      break